import os
import requests
from typing import List

# Load Hugging Face token from env
HF_TOKEN = os.getenv("HF_TOKEN")
if not HF_TOKEN:
    raise ValueError("❌ Hugging Face token not found. Please set HF_TOKEN environment variable.")

# Hugging Face Inference API endpoint for llama
API_URL = "https://router.huggingface.co/v1/chat/completions"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}


def chat_with_llama(prompt: str, max_new_tokens: int = 200) -> str:
    """
    Send a prompt to Hugging Face Inference API and return generated text.
    """
    payload = {
    "messages": [
        {
            "role": "user",
            "content": prompt
        }
    ],
    "model": "meta-llama/Llama-3.1-8B-Instruct:fireworks-ai"
    }
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        # HF returns a list of dicts with "generated_text"
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        return f"An error occurred: {str(e)}"


def interact_with_llama(system_message: str, user_message: str) -> str:
    """
    Simulate chat by combining system + user message into a single prompt.
    """
    prompt = f"{system_message}\nUser: {user_message}\nAI:"
    return chat_with_llama(prompt)


def extract_prescription_info(prescription_text: str) -> str:
    return interact_with_llama(
        "You are an AI that helps pharmacists analyze prescriptions.",
        f"Analyze the prescription and list essential details in concise bullet points without any conversational elements: {prescription_text}"
    )


def get_drug_information(drug_name: str) -> str:
    return interact_with_llama(
        "You are an AI that provides drug information.",
        f"Provide concise bullet points about the drug, focusing on factual information without conversational elements: {drug_name}"
    )


def validate_prescription(prescription_text: str) -> str:
    return interact_with_llama(
        "You are an AI that validates prescriptions for errors.",
        f"Review the prescription for errors and list them in factual bullet points, avoiding conversational language: {prescription_text}"
    )


def check_drug_interactions(drug_list: List[str]) -> str:
    drug_list_str = ", ".join(drug_list)
    return interact_with_llama(
        "You are an AI that checks for drug interactions.",
        f"Identify interactions between the following drugs and summarize in concise bullet points, omitting conversational language: {drug_list_str}"
    )


def search_drug_or_condition(query: str) -> str:
    return interact_with_llama(
        "You are an AI that helps pharmacists search for drug information and conditions.",
        f"Search for factual information about the given query and present in concise bullet points, avoiding conversational elements: {query}"
    )


def preprocess_prescription_text(ocr_text: str) -> str:
    system_message = (
        "The following text is a raw OCR output of a prescription, which may contain unclear or garbled text. "
        "Use contextual understanding to interpret the text correctly. "
        "Extract and list only the medications and their details such as dosage, frequency, and quantity. "
        "Correct any unclear text and ignore any non-medication information like doctor's name, patient's name, etc."
    )
    return interact_with_llama(system_message, ocr_text)
