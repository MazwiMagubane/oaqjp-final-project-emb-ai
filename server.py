"""
The purpose of the web application is to predict emotion from input text.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

"""
The purpose of the script is to predict emotion from input text.
"""

@app.route("/emotionDetector")
def emo_detector():
    """
    emo_detector function predicts emotion from the text input in textToAnalyzetext.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response is not None:
        anger = response['anger']
        disgust = response['disgust']
        fear = response['fear']
        joy = response['joy']
        sadness = response['sadness']
        dominant_emotion = response['dominant_emotion']
        return (
            "For the given statement, the system response is \n"
            f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, \n"
            f"'joy': {joy}, 'sadness': {sadness}. \n"
            f"The dominant emotion is {dominant_emotion}."
        )
    return "Invalid text! Please try again!"

@app.route("/")
def render_index_page():
    """
    render_index_page displayes the index page when accessing the root route.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
