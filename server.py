'''
Flask server to get emotions from text via Watson API
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detection")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detect():
    '''
    Route to call by JS
    '''
    text = request.args["textToAnalyze"]
    processed_text = emotion_detector(text)
    if processed_text['dominant_emotion'] is None:
        return "<b>Invalid text! Please try again!</b>"

    return f"For the given statement, the system response is \
    'anger': {processed_text['anger']}, \
    'disgust': {processed_text['disgust']}, \
    'fear': {processed_text['fear']}, \
    'joy': {processed_text['joy']} and \
    'sadness': {processed_text['sadness']}. \
    The dominant emotion is <b>{processed_text['dominant_emotion']}</b>.", 200


@app.route("/")
def index():
    '''
    Basic route
    '''
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
