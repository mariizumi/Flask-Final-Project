from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emote_detector():
    # Retrieving response from emotion_detector()
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    # Extracting specific information from response\
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dom_emotion = response["dominant_emotion"]

    return ("For the given statement, the system response is "
              f"\'anger\': {anger}, "
              f"\'disgust\': {disgust}, "
              f"\'fear\': {fear}, "
              f"\'joy\': {joy}, "
              f"\'sadness\': {sadness}. "
              f"The dominant emotion is {dom_emotion}.")

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
