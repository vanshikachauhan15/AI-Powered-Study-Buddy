from dotenv import load_dotenv
import os

load_dotenv()

AI_PROVIDER = os.getenv("AI_PROVIDER", "huggingface").lower()
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "sshleifer/distilbart-cnn-12-6")
