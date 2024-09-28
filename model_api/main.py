from flask import Flask, render_template, request, jsonify
from model_interface import HuggingFaceQAModel
from logging import warning
import os

app = Flask(__name__)

# Loading model for question answering
warning("Start model loading")
model = HuggingFaceQAModel(model_name="Megnis/bert-finetuned-sbersquad")
warning("End model loading")
warning(os.path.dirname(os.path.abspath(__file__)))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        context = request.form.get('context', '')
        question = request.form.get('question', '')

        # get answer from model
        response = model.generate(context=context, question=question)

        # return answer in JSON format
        return render_template('index.html', context=context, question=question, answer=response)
    else:
        return render_template('index.html')


@app.route('/api/get_answer', methods=['POST'])
def get_answer():
    context = request.form['context']
    question = request.form['question']

    # get answer from model
    response = model.generate(context=context, question=question)

    # return answer in JSON format
    return jsonify({'context': context, 'question': question, 'answer': response})

@app.route('/api/get_model_answer', methods=['POST'])
def get_model_answer():
    context = request.form['context']
    question = request.form['question']

    # get answer from model
    response = model._get_model_answer(context=context, question=question)

    # return answer in JSON format
    return jsonify({'context': context, 'question': question, 'model_answer': response})


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
