import requests

def emotion_detector(text_to_analyze):
    # Defining url, json dictionary, and header
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    json_input = { "raw_document": { "text": text_to_analyze } }
    header = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }

    # Sending request to API
    response = requests.post(url, json = json_input, headers = header)

    # Returning API's response
    return response.text
