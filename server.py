'''
Run server
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_route():
    '''
    Takes text and runs it through the emotion_detector
    Returns formatted response from detector
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    return (f"For the given statement, the system response is "
            f"'anger':{response['anger']}, 'disgust': {response['disgust']}, "
            f"'fear': {response['fear']}, 'joy': {response['joy']} "
            f"and 'sadness': {response['sadness']}. The dominant emotion is "
            f"{response['dominant_emotion']}.\n")

@app.route("/")
def render_index_page():
    '''
    Render homepage
    '''
    return render_template('./index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
