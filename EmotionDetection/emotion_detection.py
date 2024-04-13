import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    dict_response = formatted_response['emotionPredictions'][0]
    if response.status_code == 200:
        emotion = dict_response['emotion']
        anger = emotion['anger']
        disgust = emotion['disgust']
        fear = emotion['fear']
        joy = emotion['joy']
        sadness = emotion['sadness']
        max_key = [k for k in emotion.keys() if emotion[k] == max(emotion.values())]
    elif response.status_code == 400:
        emotion = None
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        max_key = ['None']  
    return {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness, 'dominant_emotion': max_key[0]}