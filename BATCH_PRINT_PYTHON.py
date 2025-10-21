# Author: Shashank Shivakumar Muthkur
# ASU email: smuthkur@asu.edu

import os
import glob
import time
import re

# --- CONFIGURATION ---
# Set the delay in seconds between sending each print job.
# If your printer is still mixing up pages, try increasing this value (e.g., to 30).
DELAY_SECONDS = 15
# ---------------------

def natural_sort_key(s):
    """
    Create a sort key that handles numbers in filenames naturally.
    For example, 'paper 10.pdf' comes after 'paper 2.pdf'.
    """
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def batch_print_pdfs():
    """
    Finds all PDF files in the current directory, sorts them,
    and sends them to the default printer with a delay between each job.
    """
    print("--- PDF Batch Print Script (with Delay) ---")
    
    # Get the current directory where the script is running
    current_directory = os.getcwd()
    print(f"Scanning for PDF files in: {current_directory}\n")

    # Find all files ending with .pdf
    pdf_files = glob.glob('*.pdf')

    if not pdf_files:
        print("No PDF files found in this directory. Exiting.")
        return

    # Sort files using the natural sort key
    pdf_files.sort(key=natural_sort_key)

    total_files = len(pdf_files)
    print(f"Found {total_files} PDF files to print.")
    print(f"A delay of {DELAY_SECONDS} seconds will be added between each print job.\n")
    print("---------------------------------")

    for i, filename in enumerate(pdf_files):
        print(f"({i+1}/{total_files}) Sending to printer: {filename}")
        try:
            # This command works on Windows to print a file using its default application
            os.startfile(filename, "print")
            
            # Only wait if it's not the very last file
            if i < total_files - 1:
                print(f"  -> Waiting for {DELAY_SECONDS} seconds...")
                time.sleep(DELAY_SECONDS)

        except Exception as e:
            print(f"  -> Could not print {filename}. Error: {e}")
    
    print("---------------------------------")
    print("✅✅✅✅ All PDF files have been sent to the printing queue!")


if __name__ == '__main__':
    batch_print_pdfs()
    # Keep the window open for a few seconds to see the final message
    input("Press Enter to exit...")
