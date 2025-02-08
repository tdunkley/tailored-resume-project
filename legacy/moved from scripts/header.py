import logging

# ...existing code...

def create_header(document, text):
    """Create a header for the document."""
    header = document.sections[0].header
    paragraph = header.paragraphs[0]
    paragraph.text = text
    paragraph.style = document.styles['Header']
    logging.info(f"Header created with text: {text}")

# ...existing code...
