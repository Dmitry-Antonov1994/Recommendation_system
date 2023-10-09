import pandas as pd

from database import batch_load_sql


def load_features_users_control() -> pd.DataFrame:
    users_query_control = 'SELECT * FROM dm_antonov_user_data_transformed_lesson_22_final'

    return batch_load_sql(users_query_control)


def load_features_users_test() -> pd.DataFrame:
    users_query_test = 'SELECT * FROM dm_antonov_user_data_transformed_lesson_10_final'

    return batch_load_sql(users_query_test)


def load_features_post_control() -> pd.DataFrame:
    post_query_control = 'SELECT * FROM dm_antonov_post_transformed_lesson_22_final'

    return batch_load_sql(post_query_control)


def load_features_post_test() -> pd.DataFrame:
    post_query_test = 'SELECT * FROM dm_antonov_post_transformed_lesson_10_final'

    return batch_load_sql(post_query_test)
