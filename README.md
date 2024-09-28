# QA-russian-system

## Description
This is a russian question answer system using neural network. This system use BERT multilingual base model that fine-tuned on sbersquad dataset.
It has interface and api to interact with model.
## Installation and running
#### 1. Clone repository
'''git clone https://github.com/MrMegnis/QA-russian-system'''
#### 2. Start Docker Compose
In cmd at the root of the project write:
'''docker-compose up'''
#### 3. Wait until docker building complete
You have to wait until all requirements are downloaded and model is ready to use. You will get log message about finishing model loading and server start.
#### 4. Use browser
After docker build finish you have to go on http://127.0.0.1:5000 on your browser. You will see the main page.
You can test model on main page manually or send POST request to:
/api/get_answer - for string model answer
/api/get_model_answer - for json with model answer, score of this answer, start and end indexes of answer in context.
## Resourses
BERT model on huggingface: https://huggingface.co/google-bert/bert-base-multilingual-cased
Fine-tuned model on huggingface: https://huggingface.co/Megnis/bert-finetuned-sbersquad
Dataset: https://huggingface.co/datasets/kuznetsoffandrey/sberquad

model fine-tuning code you can find in model-qa-tuning.ipynb file