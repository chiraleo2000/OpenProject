
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/get_question', methods=['GET'])
def get_question():
    question = {
        "question_text": "What are the primary causes of global warming?",
        "type": "open-ended",
        "options": None
    }
    return jsonify(question)

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    player_answer = request.json.get('answer', '')
    if "emissions" in player_answer.lower() or "greenhouse" in player_answer.lower():
        feedback = "Correct! Greenhouse gas emissions are a primary cause of global warming."
        score = 10
    else:
        feedback = "Not quite. One of the primary causes of global warming is greenhouse gas emissions."
        score = 0
    return jsonify({"feedback": feedback, "score": score})

if __name__ == '__main__':
    app.run(port=8080)
    