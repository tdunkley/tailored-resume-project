import logging

# ...existing code...

def finalize_document_v2(document):
    """Finalize the document (version 2)."""
    document.save('final_document_v2.docx')
    logging.info("Document finalized and saved as final_document_v2.docx")

# ...existing code...
