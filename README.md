# Physician Notetaker AI

This project implements an AI system for medical transcription, NLP-based summarization, sentiment analysis, and SOAP note generation. It's designed to assist physicians by automating the process of extracting key medical details from patient conversations and analyzing patient sentiment and intent.

## Overview

The application is built using Python and leverages several powerful NLP libraries, including:

-   **Streamlit:** For creating an interactive web interface.
-   **spaCy:** For Named Entity Recognition (NER) and general text processing.
-   **Transformers (Hugging Face):** For sentiment analysis and intent detection.

The system provides the following functionalities:

1.  **Medical NLP Summarization:**
    -      Extracts key medical details from patient conversations (Symptoms, Diagnosis, Treatment, Prognosis).
    -      Generates a structured medical report in JSON format.
    -      Identifies important medical phrases.
2.  **Sentiment & Intent Analysis:**
    -      Classifies patient sentiment as Anxious, Neutral, or Reassured.
    -      Identifies patient intent (e.g., Seeking reassurance, Reporting symptoms).
3.  **SOAP Note Generation (Bonus):**
    -      Converts transcribed text into a structured SOAP note format (Subjective, Objective, Assessment, Plan).

## Getting Started

Follow these steps to set up and run the application:

### Prerequisites

-      Python 3.11.0
-      pip (Python package installer)

## Live Application

You can access the live application here: [https://physiciannotetaker-bcyjd3aiekdczfkvp4uavy.streamlit.app/]

### Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/HemanthSanju/Physician_Notetaker.git]
    cd Physician_Notetaker
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv env
    ```

    -   On Windows:

        ```bash
        env\Scripts\activate
        ```

3.  **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

    Note: I have created a sample requirements.txt file below, you can create one by running `pip freeze > requirements.txt` after installing all dependencies.

    ```
    streamlit
    spacy
    transformers
    torch # transformers require torch
    ```

4.  **Download the spaCy English model:**

    ```bash
    python -m spacy download en_core_web_sm
    ```

### Running the Application

1.  **Start the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

2.  **Open your web browser and navigate to the URL displayed in the terminal (usually `http://localhost:8501`).**

### Usage

1.  **Chat Interface:**
    -      Use the chat interface to simulate a conversation between a physician and a patient.
    -      Select the role (Doctor or Patient) and enter the message.
    -      Click "Send" to add the message to the chat history.
2.  **NLP Processing:**
    -      Click the "Extract Medical Details" button to generate a structured medical summary.
    -   Click "Analyze Sentiment & Intent" button to get sentiment and intent analysis.
    -   Click "Generate SOAP Note" to create a SOAP note from the patient's transcript.
3.  **View Results:**
    -      The results of the NLP processing will be displayed in JSON format below the respective buttons.

## Code Structure

-   `app.py`: Contains the Streamlit application code, including the chat interface and button handlers.
-   `nlp_pipeline.py`: Implements the NLP pipeline for extracting medical details and performing sentiment/intent analysis.
-   `soap_note_generator.py`: Generates SOAP notes from the transcript.
-   `requirements.txt`: Lists the Python packages required to run the application.

## NLP Pipeline Details

-   **Medical NLP Summarization:**
    -      Uses spaCy for basic text processing and keyword matching to extract medical entities.
    -      Extracts patient names, symptoms, diagnosis, treatment, and prognosis.
-   **Sentiment & Intent Analysis:**
    -      Uses the DistilBERT model from Hugging Face for sentiment classification.
    -      Implements rule-based intent detection based on keywords.
-   **SOAP Note Generation:**
    -   Uses rule-based extraction to put the information into the correct sections of the SOAP note.

## Future Improvements

-      Integrate a more advanced Named Entity Recognition model for medical entities (e.g., SciSpacy).
-      Fine-tune a BERT model on medical datasets for improved sentiment and intent analysis.
-      Implement more sophisticated techniques for SOAP note generation, such as sequence-to-sequence models.
-   Add error handling and improve the robustness of the application.
-   Incorporate a better method of patient name extraction.
-   Use a better summarization model.

## Dependencies

* streamlit
* spacy
* scispacy
* keybert
* transformers
* pydantic
* (List other dependencies from `requirements.txt`)

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Author

HemanthSanju
hemanthsanju127@gmail.com