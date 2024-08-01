from requests import post
from json import loads
from operator import itemgetter

BASE_URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1"

def emotion_detector(text_to_analyze):
    url = f'{BASE_URL}/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
        }
    payload = {"raw_document": {"text": text_to_analyze}}  

    r = post(url, headers=headers, json=payload)
    if r.status_code == 400:
        return dict(
            anger=None,
            disgust=None,
            fear=None,
            joy=None,
            sadness=None,
            dominant_emotion=None
        )
    emotions = loads(r.text)["emotionPredictions"][0]["emotion"]
    anger_score = emotions["anger"]
    disgust_score = emotions["disgust"]
    fear_score = emotions["fear"]
    joy_score = emotions["joy"]
    sadness_score = emotions["sadness"]
    dominant = max(
        *zip(
            [anger_score, disgust_score, fear_score, joy_score, sadness_score],
            ["anger", "disgust", "fear", "joy", "sadness"],
            ),
        key=itemgetter(0),
        )
    return dict(
        anger=anger_score,
        disgust=disgust_score,
        fear=fear_score,
        joy=joy_score,
        sadness=sadness_score,
        dominant_emotion=dominant[1]
    )