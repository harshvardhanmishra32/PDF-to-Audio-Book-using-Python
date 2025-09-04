import pyttsx3
from PyPDF2 import PdfReader
from tkinter.filedialog import askopenfilename

# Ask the user to select a PDF file
file_path = askopenfilename(
    title="Select a PDF file",
    filetypes=[("PDF files", "*.pdf")]
)

if file_path:  # If a file is selected
    # Read the PDF file
    pdf = PdfReader(file_path)
    num_pages = len(pdf.pages)

    # Start the text-to-speech engine
    speaker = pyttsx3.init()
    speaker.setProperty("rate", 150)   # Speed of reading
    speaker.setProperty("volume", 1.0) # Volume (0.0 to 1.0)

    # Go through each page and read the text
    text_content = ""
    for i in range(num_pages):
        page = pdf.pages[i]
        text = page.extract_text()
        if text:  # Add text only if page has text
            text_content += text + "\n"

    # Speak the text if found
    if text_content.strip():
        speaker.say(text_content)
        speaker.runAndWait()
    else:
        print("⚠️ No readable text found. This PDF may be scanned or image-based.")

else:
    print("❌ No file selected.")

