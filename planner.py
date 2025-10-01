# planner.py
import random
from ai_client import AIClient

client = None

def get_client():
    global client
    if client is None:
        client = AIClient()
    return client

def create_flashcards(explanations, num_flashcards=5):
    """Generate simple flashcards from explanations"""
    flashcards = []
    for i, exp in enumerate(explanations[:num_flashcards]):
        flashcards.append({"q": f"What is key point {i+1}?", "a": exp})
    return flashcards

def generate_conceptual_mcq(sentence, other_sentences):
    """
    Generates a conceptual MCQ for a given sentence.
    Uses other sentences as plausible distractors.
    """
    # Take a small sample of other sentences as wrong options
    wrong_options = random.sample(other_sentences, min(3, len(other_sentences)))
    
    # Correct answer
    correct_option = sentence
    
    # Shuffle options
    options = wrong_options + [correct_option]
    random.shuffle(options)
    
    # Create a child-friendly question prompt
    question = f"What is true based on this information?\n'{sentence}'"
    
    return {
        "question": question,
        "options": options,
        "answer": correct_option
    }

def create_study_pack(content: str, num_flashcards=5, num_mcq=5):
    """
    Generates a study pack with summary, explanations, flashcards, and conceptual MCQs
    """
    client = get_client()
    
    # 1️⃣ Summarize content
    summary = client.summarize(content, max_length=200, min_length=50)
    
    # 2️⃣ Split summary into explanations
    explanations = [s.strip() for s in summary.split(".") if s.strip()]
    
    # 3️⃣ Create flashcards
    flashcards = create_flashcards(explanations, num_flashcards)
    
    # 4️⃣ Generate conceptual MCQs
    mcqs = []
    for i, sentence in enumerate(explanations[:num_mcq]):
        # Use other sentences as distractors
        other_sentences = [s for j, s in enumerate(explanations) if j != i]
        mcq = generate_conceptual_mcq(sentence, other_sentences)
        mcqs.append(mcq)
    
    # 5️⃣ Return the structured study pack
    return {
        "summary": summary,
        "explanations": explanations,
        "flashcards": flashcards,
        "quiz": mcqs,
        "further_reading": ["https://huggingface.co/models"]
    }
