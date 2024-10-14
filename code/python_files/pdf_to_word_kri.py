from pdf2docx import Converter


def convert_pdf_to_docx(pdf_file, docx_file):
    cv = Converter(pdf_file)
    cv.convert(docx_file)
    cv.close()


# Example usage
pdf_file = r'/Users/krishna/Documents/convert to docx/Rahul Kendre for conversion.pdf'
docx_file = r'/Users/krishna/Documents/convert to docx/Rahul Kendre for conversion.docx'
convert_pdf_to_docx(pdf_file, docx_file)
