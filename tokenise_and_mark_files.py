import nltk
import os
import re

# Download necessary NLTK data (punkt tokenizer)
try:
    nltk.data.find('tokenizers/punkt')
    print("NLTK 'punkt' tokenizer already found.")
except LookupError:
    print("NLTK 'punkt' tokenizer not found. Downloading...")
    nltk.download('punkt', quiet=False)
    print("'punkt' tokenizer downloaded.")

nltk.download('punkt_tab')

from nltk.tokenize import sent_tokenize

# --- Define File Paths (Keep these as they are for reading) ---
source_files_info = [
    {
        "original_name": r"C:\Users\61429\OneDrive - UTS\CurrentSubjects\41043 NLP\A3\Project\Paraphraser-Detector-\Source_Photosynthesis.txt",
        "prefix": "PHOTO"
    },
    {
        "original_name": r"C:\Users\61429\OneDrive - UTS\CurrentSubjects\41043 NLP\A3\Project\Paraphraser-Detector-\Source_MachineLearning.txt",
        "prefix": "ML"
    },
    {
        "original_name": r"C:\Users\61429\OneDrive - UTS\CurrentSubjects\41043 NLP\A3\Project\Paraphraser-Detector-\Source_WorldWar2.txt",
        "prefix": "WWII"
    }
]

submission_original_path = r"C:\Users\61429\OneDrive - UTS\CurrentSubjects\41043 NLP\A3\Project\Paraphraser-Detector-\Submission1.txt"
submission_prefix = "SUB"


def process_and_print_marked_content(original_filepath, prefix_tag):
    """
    Reads an original text file, tokenizes it into sentences,
    adds a unique ID to each sentence, and PRINTS the marked content.
    """
    print(f"\n--- Processing: {original_filepath} (Prefix: {prefix_tag}) ---")
    all_marked_lines_for_file = [] # To store lines for this specific file

    try:
        print(f"  Attempting to open for reading: {original_filepath}")
        with open(original_filepath, 'r', encoding='utf-8') as f_orig:
            text_content = f_orig.read()
        print(f"  Successfully read {len(text_content)} characters.")

        sentences = sent_tokenize(text_content)
        print(f"  Tokenized into {len(sentences)} raw sentences.")
        min_sentence_length = 15
        
        sentence_counter = 1
        for sentence_idx, sentence in enumerate(sentences):
            clean_sentence = re.sub(r'\s+', ' ', sentence).strip()
            if len(clean_sentence) >= min_sentence_length:
                marked_line = f"({prefix_tag}-S{sentence_counter}) {clean_sentence}"
                all_marked_lines_for_file.append(marked_line) # Add to list
                sentence_counter += 1
        print(f"  Prepared {len(all_marked_lines_for_file)} sentences for output.")

        # --- Print the marked content for this file ---
        print(f"\n--- Marked Content for: {os.path.basename(original_filepath)} ---")
        if all_marked_lines_for_file:
            for line in all_marked_lines_for_file:
                print(line)
        else:
            print("  (No sentences met the minimum length criteria)")
        print(f"--- End of Marked Content for: {os.path.basename(original_filepath)} ---\n")
        
        return all_marked_lines_for_file # Optionally return the list if needed elsewhere

    except FileNotFoundError:
        print(f"  ERROR: Original file not found at {original_filepath}")
        return []
    except Exception as e:
        print(f"  An unexpected error occurred while processing {original_filepath}: {e}")
        print(f"  Type of error: {type(e)}")
        return []

# --- Process Source Files and Print ---
print("=== PROCESSING SOURCE FILES ===")
for file_info in source_files_info:
    original_path = file_info["original_name"]
    process_and_print_marked_content(original_path, file_info["prefix"])

# --- Process Submission File and Print ---
print("\n=== PROCESSING SUBMISSION FILE ===")
process_and_print_marked_content(submission_original_path, submission_prefix)

print("\n\nScript finished. Check the console output above for the marked sentences.")
print("You can now copy the relevant sections from the console to create your ground truth map.")