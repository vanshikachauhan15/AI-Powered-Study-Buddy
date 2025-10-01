from transformers import pipeline
from config import AI_PROVIDER, DEFAULT_MODEL

class AIClient:
    def __init__(self):
        if AI_PROVIDER != "huggingface":
            raise ValueError("Only HuggingFace free models are supported in this setup.")
        # Load summarization model
        self.summarizer = pipeline("summarization", model=DEFAULT_MODEL)

    def summarize(self, text, max_length=200, min_length=50):
        result = self.summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        return result[0]['summary_text']
