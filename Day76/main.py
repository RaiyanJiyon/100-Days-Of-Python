import PyPDF2
a = PyPDF2.PdfFileReader("Algorithm book.pdf")
print(a.documentInfo)
print(a.getNumPages)
print("Hello")