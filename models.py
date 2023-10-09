import os
from catboost import CatBoostClassifier


def get_model_path(path_control: str, path_test: str) -> tuple[str, str]:
    model_path_control = path_control
    model_path_test = path_test

    return model_path_control, model_path_test


def load_models():
    model_path = get_model_path(
        "C:/Users/User/KC/Final_poject/Recommendation_system/models_training/ml/cboost_tf-idf",
        "C:/Users/User/KC/Final_poject/Recommendation_system/models_training/dl/cboost_embeddings"
    )
    model_control = CatBoostClassifier().load_model(model_path[0], format='cbm')
    model_test = CatBoostClassifier().load_model(model_path[1], format='cbm')

    return model_control, model_test
