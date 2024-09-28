from transformers import pipeline


class HuggingFaceQAModel:
    def __init__(self, model_name: str) -> None:
        # Load model from huggingface
        self.model = pipeline(model=model_name)

    def generate(self, context: str, question: str) -> str:
        '''get context and question and return model answer'''
        # Generate answer
        answer = self.model(question=question, context=context)
        return answer["answer"]

    def _get_model_answer(self, context: str, question: str) -> dict:
        '''get context and question and return model answer with score, start index and end index of answer'''
        # Generate answer
        return self.model(question=question, context=context)
