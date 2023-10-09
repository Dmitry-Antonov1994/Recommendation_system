from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from datetime import datetime as dt

from features import load_features_users_control, load_features_users_test, load_features_post_control, \
    load_features_post_test
from models import load_models
from schema import Response, Post
from database import get_db
from groups import get_exp_group

df_users_control = load_features_users_control()
df_users_test = load_features_users_test()
df_posts_control = load_features_post_control()
df_posts_test = load_features_post_test()

model_control, model_test = load_models()

app = FastAPI()

# эндпоинт, возвращающий полученную группу для А/Б теста и список id рекомендованных постов
@app.get("/post/recommendations/", response_model=Response)
def recommended_posts(id: int, db: Session = Depends(get_db)):
    exp_group = get_exp_group(id)
    if exp_group == 'control':
        user = df_users_control.query(f'user_id == {id}')
        df = user.merge(df_posts_control, how='cross')
        post_ids = df[['post_id']]
        predict_df = df.drop(['user_id', 'post_id'], axis=1)
        predict_df['month'] = dt.now().month
        predict_df['day'] = dt.now().day
        predict_df['hour'] = dt.now().hour
        prediction = model_control.predict_proba(predict_df)[:, 1]
    elif exp_group == 'test':
        user = df_users_test.query(f'user_id == {id}')
        df = user.merge(df_posts_test, how='cross')
        post_ids = df[['post_id']]
        predict_df = df.drop(['user_id', 'post_id'], axis=1)
        predict_df['month'] = dt.now().month
        predict_df['day'] = dt.now().day
        predict_df['hour'] = dt.now().hour
        prediction = model_test.predict_proba(predict_df)[:, 1]
    else:
        raise ValueError('unknown group')
    post_ids['prob'] = prediction
    post_top_5 = post_ids.sort_values('prob', ascending=False).head(5).post_id.tolist()
    result = (db.query(Post).select_from(Post).filter(Post.id.in_(post_top_5)).all())

    return {'exp_group': exp_group, 'recommendations': result}
