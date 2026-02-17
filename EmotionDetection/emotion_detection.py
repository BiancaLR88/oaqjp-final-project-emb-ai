import requests
import json

def emotion_detector(text_to_analyse):
    # URL for the Watson NLP Emotion Predict function
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Input JSON format expected by the API
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # sending the POST request to the API
    response = requests.post(url, json = myobj, headers=header)
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    
    # Extracting the required emotions dictionary
    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        
        # Finding the dominant emotion (the one with the highest score)
        dominant_emotion = max(emotions, key=emotions.get)
        
        # Adding the dominant emotion to the dictionary
        emotions['dominant_emotion'] = dominant_emotion
        
        return emotions
    elif response.status_code == 400:
        # If the text is blank/invalid, return None for everything
        return {
            'anger': None, 
            'disgust': None, 
            'fear': None, 
            'joy': None, 
            'sadness': None, 
            'dominant_emotion': None
        }