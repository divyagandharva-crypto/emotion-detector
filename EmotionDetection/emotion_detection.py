"""Detect emotions in text using the Watson NLP Emotion API."""

import requests


def empty_emotion_result():
    """Return empty emotion values."""

    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }


def emotion_detector(text_to_analyze):
    """Return emotion scores and the dominant emotion."""

    if not isinstance(text_to_analyze, str):
        return empty_emotion_result()

    if not text_to_analyze.strip():
        return empty_emotion_result()

    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(
        url,
        headers=headers,
        json=input_json,
        timeout=30
    )

    if response.status_code == 400:
        return empty_emotion_result()

    response_dictionary = response.json()

    if "emotionPredictions" not in response_dictionary:
        return empty_emotion_result()

    emotion_scores = (
        response_dictionary["emotionPredictions"][0]["emotion"]
    )

    dominant_emotion = max(
        emotion_scores,
        key=emotion_scores.get
    )

    return {
        "anger": emotion_scores["anger"],
        "disgust": emotion_scores["disgust"],
        "fear": emotion_scores["fear"],
        "joy": emotion_scores["joy"],
        "sadness": emotion_scores["sadness"],
        "dominant_emotion": dominant_emotion
    }
