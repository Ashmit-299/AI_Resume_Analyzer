import pymupdf
def extract_text_from_pdf(pdf_path):
    try:
        doc = pymupdf.open(pdf_path)
        all_text = ""
        for page in doc:
            all_text += page.get_text()
        doc.close()
        return all_text
    except Exception as e:
        print("Please provide a valid pdf.")
        return ""