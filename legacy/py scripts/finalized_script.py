import logging

# ...existing code...

def finalize_document(document):
    """Finalize the document."""
    document.save('final_document.docx')
    logging.info("Document finalized and saved as final_document.docx")

# ...existing code...
