'''Write a program to manipulate pdf files using pyPDF. Your programs should be able to merge multiple pdf files into a single pdf. You are welcome to add more functionalities


pypdf is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. It can also add custom data, viewing options, and passwords to PDF files. pypdf can retrieve text and metadata from PDFs as well.
'''

from PyPDF2 import PdfMerger
import os

# Create a PdfMerger object
merger = PdfMerger()

# List PDF files in the current directory
pdf_files = [file for file in os.listdir() if file.endswith(".pdf")]

# Sort the PDF files if needed
pdf_files.sort()

# Append each PDF to the merger
for pdf in pdf_files:
    merger.append(pdf)

# Write the merged PDF to a file
merger.write("merged-pdf.pdf")

# Close the merger
merger.close()
