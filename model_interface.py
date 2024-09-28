from transformers import pipeline


class HuggingFaceQAModel:
    def __init__(self, model_name: str) -> None:
        self.model = pipeline(model=model_name)

    def generate(self, context: str, question: str) -> str:
        answer = self.model(question=question, context=context)
        return answer["answer"]

    def _get_model_answer(self, context: str, question: str) -> dict:
        return self.model(question=question, context=context)
