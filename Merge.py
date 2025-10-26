# Author: Shashank Shivakumar Muthkur
# If you are running it for first time, install PyPDF2 using command pip install PyPDF2, 
# Run from command prompt using python merge_pdfs.py <directory_path> <output_file_name>


import os
import PyPDF2

def merge_pdfs(directory, output_filename):
    # List to store all PDF files in the directory
    pdf_files = []

    # Loop through the directory to find all PDFs
    for file_name in os.listdir(directory):
        if file_name.endswith('.pdf'):
            pdf_files.append(os.path.join(directory, file_name))

    # Sort files alphabetically (optional, remove this if you want to keep original order)
    pdf_files.sort()

    # Create a PDF merger object
    pdf_merger = PyPDF2.PdfMerger()

    # Loop through all found PDF files and append them to the merger
    for pdf in pdf_files:
        with open(pdf, 'rb') as file:
            pdf_merger.append(file)

    # Write out the merged PDF to the specified output file
    with open(output_filename, 'wb') as output_file:
        pdf_merger.write(output_file)

    print(f"All PDFs have been merged into {output_filename}")

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print("Usage: python merge_pdfs.py <directory> <output_filename>")
    else:
        merge_pdfs(sys.argv[1], sys.argv[2])
