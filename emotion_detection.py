import requests
import json

def emotion_detector(text_to_analyze):
    # Defining url, json dictionary, and header
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    json_input = { "raw_document": { "text": text_to_analyze } }
    header = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }

    # Sending request to API
    response = requests.post(url, json = json_input, headers = header)

    # Formatting into JSON
    formatted_response = json.loads(response.text)

    # Extracting emotion information
    anger_score = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
    disgust_score = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
    fear_score = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
    joy_score = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
    sadness_score = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]

    # Putting all emotions into dictionary to use max() on
    emotions = {
    "anger": anger_score,
    "disgust": disgust_score,
    "fear": fear_score,
    "joy": joy_score,
    "sadness": sadness_score,
    }

    # Calculating dominant_emotion by using max()
    dominant_emotion = max(emotions, key = lambda key: emotions[key])

    # Returning API's response and dominant_emotion
    return {
    "anger": anger_score,
    "disgust": disgust_score,
    "fear": fear_score,
    "joy": joy_score,
    "sadness": sadness_score,
    "dominant_emotion": dominant_emotion,
    }
