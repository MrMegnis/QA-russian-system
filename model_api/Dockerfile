FROM python:3.11-bookworm

COPY ../requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ../model_api/ .
COPY ../model_interface.py/ .

CMD ["python", "main.py"]