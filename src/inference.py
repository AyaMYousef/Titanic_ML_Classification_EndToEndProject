import pandas as pd
#import typing as List
from .utils.request import PassengerData
from .utils.response import PassengerPrediction, PredictionResponse
from .utils.config import model, preprocessor

def predict_survival(passengers: list[PassengerData]):
    base_model=[p.model_dump() for p in passengers]

    for i,p in enumerate(passengers):
        """
        Feature Engineering Params
        """

    df = pd.DataFrame(base_model)
    df_processed = preprocessor.transform(df)
    prediction = (model.predict(df_processed) >0.5).astype("int32")

    pred_response = PredictionResponse(prediction=[
       """"
       """"
    ])

    return pred_response
