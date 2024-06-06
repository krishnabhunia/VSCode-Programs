from pdf2docx import Converter

def convert_pdf_to_docx(pdf_file, docx_file):
    cv = Converter(pdf_file)
    cv.convert(docx_file)
    cv.close()

# Example usage
pdf_file = 'path/to/your/file.pdf'
docx_file = 'path/to/your/file.docx'
convert_pdf_to_docx(pdf_file, docx_file)