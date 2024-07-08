import numpy as np
import pandas as pd
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Load the CSV file
qa_df = pd.read_csv('cleanfile.csv')


def get_answer(question):
    for index, row in qa_df.iterrows():
        if question.lower() in row['Questions'].lower():
            return row['Answer']
    return "Sorry, I don't have an answer for that."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_answer',methods=['POST'])
def get_answer_route():
    question = request.form['question']
    answer = get_answer(question)
    return jsonify({'answer': answer})


if __name__ == '__main__':
    app.run(debug=True)