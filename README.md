# Paraphrased Plagiarism Detector

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Made with Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)

A Natural Language Processing (NLP) system designed to detect potential paraphrased plagiarism in student essays by comparing them against provided source documents. This tool leverages Sentence-BERT embeddings for semantic understanding, combined with Cosine and Jaccard similarity metrics.

## Table of Contents
- [Motivation](#motivation)
- [Use Case](#use-case)
- [Features](#features)
- [Methodology](#methodology)
- [Tech Stack](#tech-stack)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Evaluation & Results](#evaluation--results)
- [Future Work](#future-work)
- [License](#license)

## Motivation
As an NLP engineer and educator, the primary motivation for developing this paraphrase detector stemmed from the practical challenge of identifying instances of paraphrased plagiarism in student essays. Traditional plagiarism detectors often struggle with sophisticated paraphrasing, and this tool aims to address that gap.

## Use Case
The system is designed to:
1. Take a student's essay as the "submission file."
2. Compare it against a set of "source files" (e.g., excerpts from the student's reference list).
3. Identify sentence pairs between the submission and sources that are semantically similar but lexically different, indicating potential paraphrasing.

*For demonstration purposes, the current implementation uses excerpts from source documents.*

## Features
- Segments submission and source texts into sentences.
- Utilizes the `all-MiniLM-L6-v2` Sentence-BERT model for generating sentence embeddings.
- Calculates **Cosine Similarity** to measure semantic relatedness between sentences.
- Calculates **Jaccard Similarity** to measure lexical (word) overlap.
- Flags potential paraphrases based on high Cosine Similarity and low Jaccard Similarity, using tunable thresholds.
- Distinguishes between paraphrased content and direct quotations (which would have high Jaccard similarity).

## Methodology
1.  **Data Loading:** Reads the submission text and source document texts.
2.  **Preprocessing:** Segments texts into sentences and filters out very short ones.
3.  **Sentence Embedding:** Uses Sentence-BERT to convert sentences into numerical embeddings.
4.  **Similarity Calculation:**
    *   **Cosine Similarity:** Between all submission and source sentence embeddings.
    *   **Jaccard Similarity:** For pairs that exceed the Cosine Similarity threshold.
5.  **Filtering Candidates:** Flags pairs with Cosine Similarity > `COSINE_THRESHOLD` AND Jaccard Similarity < `JACCARD_THRESHOLD`.
6.  **Evaluation:** Performance is assessed against a ground truth using Precision, Recall, and F1-Score.

*For detailed methodology and code, please refer to the Jupyter Notebook: `NLP_A3(Paraphrase_Detection) (3).ipynb`.*

## Tech Stack
- Python 3.x
- `sentence-transformers`
- `nltk`
- `numpy`
- Google Colab (recommended for GPU acceleration)

## Setup & Installation

1.  **Clone the repository:**
    ```bash
    git clone [URL_OF_YOUR_GITHUB_REPOSITORY]
    cd [REPOSITORY_NAME]
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    Create a `requirements.txt` file with the following content:
    ```
    sentence-transformers
    nltk
    numpy
    ```
    Then install:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Download NLTK data:**
    Run the following in a Python interpreter or add to your script:
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('word_tokenize') # Though 'punkt' usually includes this
    ```
    (Note: The notebook uses `nltk.download('punkt', quiet=True)` and `nltk.download('punkt_tab', quiet=True)`. `punkt_tab` is less common; `punkt` is usually sufficient for `sent_tokenize` and `word_tokenize`.)


5.  **Data:**
    - Place your submission file (e.g., `Submission1.txt`) and source files (e.g., `Source_Photosynthesis.txt`, etc.) in the appropriate directories.
    - If using Google Colab, ensure your Google Drive is mounted and file paths in the notebook (`NLP_A3(Paraphrase_Detection) (3).ipynb`) point to the correct locations on your Drive. The notebook currently uses paths like:
      ```
      /content/drive/MyDrive/NLP/Paraphrasing Detector/A3/Synethetic-Dataset/Sources/Source_Photosynthesis.txt
      /content/drive/MyDrive/NLP/Paraphrasing Detector/A3/Synethetic-Dataset/Submission/Submission1.txt
      ```
      **You will need to update these paths.**

## Usage

1.  **Prepare your data:** Ensure your submission and source text files are accessible.
2.  **Configure Paths:** Open the `NLP_A3(Paraphrase_Detection) (3).ipynb` notebook and update the file paths in "Section 2. Load Data" to match your file locations.
3.  **Set Thresholds (Optional):** In "Section 7," you can adjust `COSINE_THRESHOLD` and `JACCARD_THRESHOLD` if you wish to experiment. The notebook defaults to:
    ```python
    COSINE_THRESHOLD = 0.70
    JACCARD_THRESHOLD = 0.36 # (Improved model)
    ```
4.  **Run the Notebook:** Execute the cells in the Jupyter Notebook sequentially.
5.  **View Results:** The "Section 8. Results" and "Section 10. Data Driven Improvements (Improved Model)" will display the potential paraphrased pairs found, along with their similarity scores.

## Evaluation & Results

The system was evaluated on a synthetic dataset with known paraphrased and identical sentences.

**Baseline Model (Cosine > 0.70, Jaccard < 0.35):**
- Precision: 0.375
- Recall: 0.75
- F1-Score: 0.50

**Improved Model (Cosine > 0.70, Jaccard < 0.36):**
- Precision: 0.444
- Recall: 1.0
- F1-Score: 0.615

The improved model, with a slightly adjusted Jaccard threshold, successfully identified all true paraphrases in the test set. False positives remain an area for further improvement.

*Detailed evaluation and analysis are available in the Jupyter Notebook.*

## Future Work
- Extensive threshold tuning on a larger, more diverse dataset.
- Experimentation with other Sentence-BERT models or fine-tuning existing ones.
- Implementing advanced techniques to reduce false positives (e.g., analyzing longer text sequences, using named entity recognition, incorporating synonym-aware lexical similarity).
- Development of a user-friendly interface.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.