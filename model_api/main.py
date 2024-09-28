from flask import Flask, render_template, request, jsonify
from model_interface import HuggingFaceQAModel
from logging import warning
import os

app = Flask(__name__)

# Загружаем модель для генерации текста
warning("Start model loading")
model = HuggingFaceQAModel(model_name="Megnis/bert-finetuned-sbersquad")
warning("End model loading")
warning(os.path.dirname(os.path.abspath(__file__)))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        context = request.form.get('context', '')
        question = request.form.get('question', '')

        # Передаем контекст и вопрос модели
        response = model.generate(context=context, question=question)

        # Возвращаем ответ модели в формате JSON
        answer = response
        return render_template('index.html', context=context, question=question, answer=answer)
    else:
        return render_template('index.html')


@app.route('/api/get_answer', methods=['POST'])
def get_answer():
    context = request.form['context']
    question = request.form['question']

    # Передаем контекст и вопрос модели
    response = model.generate(context=context, question=question)

    # Возвращаем ответ модели в формате JSON
    return jsonify({'context': context, 'question': question, 'answer': response})


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
