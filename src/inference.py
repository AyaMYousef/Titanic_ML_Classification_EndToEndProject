import pandas as pd
#import typing as List
from .utils.request import PassengerData
from .utils.response import PassengerPrediction, PredictionResponse
from .utils.config import model, preprocessor

def predict_survival(passengers: list[PassengerData]):
    base_model=[p.model_dump() for p in passengers]

    for i,p in enumerate(passengers):
        base_model[i]["family_size"] = p.family_size
        base_model[i]["is_alone"] = p.is_alone
        base_model[i]["is_child"] =p.is_child

    df = pd.DataFrame(base_model)
    df_processed = preprocessor.transform(df)
    prediction = (model.predict(df_processed) >0.5).astype("int32")

    pred_response = PredictionResponse(prediction=[
        PassengerPrediction(
            passenger_id= passenger.passenger_id,
            predicted = "survived" if pred==1 else "not survived"
        )
        for passenger, pred in zip(passengers, prediction.flatten())
    ])

    return pred_response