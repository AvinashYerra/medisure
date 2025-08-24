# MediSure 🚑💊

**MediSure** is a Flask-based web service designed to assist pharmacists and healthcare professionals.  
It provides an easy-to-use interface for analyzing prescriptions, retrieving drug information, validating prescriptions, checking drug interactions, and searching for drugs or conditions.  

This implementation leverages **Hugging Face’s LLaMA model** for natural language understanding, enabling flexible, local AI processing without reliance on OpenAI.

---

## ✨ Features

- **Analyze Prescriptions** → Extract key information from prescription texts  
- **Prescription Upload** → Upload an image of a prescription and process it with OCR + LLaMA  
- **Drug Information** → Retrieve detailed information about drugs  
- **Prescription Validation** → Check prescriptions for potential errors  
- **Drug Interaction Check** → Identify interactions between multiple drugs  
- **Drug or Condition Search** → Search for drugs or medical conditions  

---

## ⚙️ Installation

### 1. Clone the repository
To set up medisure on your local machine, follow these steps:

1. Clone this repository to your local machine.
2. Ensure you have Python 3.x installed.
3. Install the required Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

4. Authenticate with Hugging Face

    Login via CLI:
    ```bash
    huggingface-cli login
    ``
5. Run the Flask application:

    ```bash
    flask run
    ```

## Usage

The web interface provides easy access to upload prescriptions and input text for analysis. The API also provides several endpoints:

- `POST /upload_and_process_image`: Uploads a prescription image for text extraction and processing.
- `POST /analyze_prescription`: Analyzes the given prescription text.
- `POST /get_drug_information`: Retrieves information for a specified drug.
- `POST /validate_prescription`: Validates the given prescription text.
- `POST /check_drug_interactions`: Checks for interactions between a list of drugs.
- `POST /search_drug_or_condition`: Searches for information on a drug or medical condition.

When uploading a prescription image, the service uses OCR technology to extract the text and then leverages AI to preprocess this text, ensuring that it is clear and structured, ready for further analysis.

## Development

To contribute to Medisure or to build on top of it, clone the repository and make sure to follow the best practices for Flask and RESTful API development. Feel free to submit pull requests.
