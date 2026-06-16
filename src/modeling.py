from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np


def evaluate_model(y_test, prediction):

    return {
        "RMSE":
        np.sqrt(
            mean_squared_error(
                y_test,
                prediction
            )
        ),

        "R2":
        r2_score(
            y_test,
            prediction
        )
    }



def train_random_forest(X_train,y_train):

    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )

    return model



def train_xgboost(X_train,y_train):

    model = XGBRegressor(
        n_estimators=200,
        learning_rate=0.05,
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )

    return model