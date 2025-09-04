# 🗣️ PDF to Speech (Python)

Turn any text-based PDF into speech using offline Text‑to‑Speech (TTS).
This simple Python tool lets you pick a PDF via a file dialog and reads it aloud using `pyttsx3`.

> ✅ Works offline • 🖥️ Windows/macOS/Linux • 🐍 Python 3.8+

---

## ✨ Features

* Select a PDF via a native **file picker** (Tkinter)
* Extract text with **PyPDF2**
* Read aloud using **pyttsx3** (offline TTS)
* Adjustable speech **rate** and **volume**
* Skips empty pages automatically

---

## 🧰 Tech Stack

* **Python**: 3.8+
* **Libraries**: `pyttsx3`, `PyPDF2`, `tkinter`

---

## 📦 Installation

### 1) Clone the repository

```bash
https://github.com/harshvardhanmishra32/PDF-to-Audio-Book-using-Python.git
```

### 2) (Recommended) Create & activate a virtual environment

**Windows (PowerShell):**

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Install dependencies

Option A — via `pip`:

```bash
pip install pyttsx3 PyPDF2 tk
```

> **Note (Linux):** If `tkinter` isn’t found, install it via your package manager, e.g. on Ubuntu/Debian:
>
> ```bash
> sudo apt-get update && sudo apt-get install -y python3-tk
> ```

Option B — via `requirements.txt` (if you add one):

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

Assuming your script file is named **`pdf_to_speech.py`** (rename if needed):

**Windows:**

```bash
python pdf_to_speech.py
```

**macOS/Linux:**

```bash
python3 pdf_to_speech.py
```

A file dialog will open. Choose a **text-based** PDF and the app will read it aloud.

---

## 🧑‍💻 Code (reference)

```python
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
```

---

## 💾 (Optional) Save Audio to File

You can save the narration to a **WAV** file (offline) using `pyttsx3`:

```python
speaker.save_to_file(text_content, "output.wav")
speaker.runAndWait()
```

> For MP3 output, consider using `gTTS` (requires internet) or convert the WAV to MP3 using `pydub` + `ffmpeg`.

---

## 🛠️ Troubleshooting

* **No sound?** Test TTS:

  ```python
  import pyttsx3; e=pyttsx3.init(); e.say("TTS test"); e.runAndWait()
  ```
* **Nothing is read:** The PDF might be **scanned** (image-only). Use OCR (e.g., `pytesseract` + Tesseract) to convert it to text first.

  ```bash
  pip install pytesseract pillow
  # Also install the Tesseract binary from your OS package manager/installer
  ```
* **`tkinter` not found:** Install `python3-tk` (Linux) or ensure Python was installed with Tk support (Windows/macOS).

---

## 📁 Suggested Project Structure

```
.
├─ pdf_to_speech.py
├─ README.md
└─ requirements.txt   # optional
```

Example `requirements.txt`:

```
pyttsx3
PyPDF2
tk
```

---

## 📜 License

This project is licensed under the **MIT License** (you can change this). See the `LICENSE` file for details.

---

## 🙌 Acknowledgements

* `pyttsx3` for offline TTS
* `PyPDF2` for PDF text extraction
* `tkinter` for the native file dialog

---

## 📣 Notes

* Works best on **text-based PDFs**. For scanned PDFs, run OCR first.
* Adjust `rate` and `volume` to your preference.

Happy listening! 🎧
