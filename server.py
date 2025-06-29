"""
Flask server for Emotion Detector web application.
"""

import os
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Set template and static directory paths
template_dir = os.path.abspath('oaqjp-final-project-emb-ai/templates')
static_dir = os.path.abspath('oaqjp-final-project-emb-ai/static')

# Initiate Flask application
app = Flask(
    "Emotion Detector",
    template_folder=template_dir,
    static_folder=static_dir
)

@app.route("/")
def render_index_page():
    """Render the main index page."""
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detect():
    """
    Handle GET request for emotion analysis.

    Returns:
        str: Formatted emotion analysis result.
    """
    # Retrieve text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze")

    # Pass the text to emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Check if dominant_emotion is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
