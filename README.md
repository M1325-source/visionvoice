# 🧠 VisionVoice – AI-Powered Accessibility Assistant

**VisionVoice** is an intelligent web-based assistant built to empower **visually impaired users** by transforming printed text in images into **spoken, summarized, and translated content** — all with the power of **AI and cloud services**.

Built using **Flask, OpenAI GPT-4, Azure Translator, OCR (Tesseract)**, and **gTTS**, this project showcases the use of **modern AI tools** to solve real-world accessibility challenges.

---

## 🌟 Features

| Feature | Description |
|--------|-------------|
| 🖼️ Image Upload | Upload any image containing text |
| 🔍 OCR | Extracts readable text from the image using `pytesseract` |
| 🧠 GPT-4 Summarization | Summarizes the extracted text using OpenAI GPT-4 |
| 🌍 Translation | Translates the summary into multiple languages (Hindi, French, Spanish, etc.) via **Azure Translator** |
| 🔊 Text-to-Speech | Speaks out the translated summary using `gTTS` |
| 🎙️ Voice Input | Allows asking questions using microphone (speech-to-text) |
| 💻 Clean Flask UI | Simple, accessible user interface made with Flask & HTML |
| ☁️ Azure Ready | Designed to be deployed on **Azure App Service** |

---

## 🧪 Tech Stack

- **Frontend:** HTML, CSS (via Flask templates)
- **Backend:** Python, Flask
- **AI/ML APIs:** OpenAI GPT-4
- **Cloud Services:** Azure Translator API
- **Audio:** gTTS (Text-to-Speech), SpeechRecognition (Voice input)
- **OCR:** Tesseract OCR via `pytesseract`

  
                                                      📸 Screenshots
  
  <img width="1545" height="829" alt="image" src="https://github.com/user-attachments/assets/b1674f1f-c125-4780-b660-d54289cd26e9" />

  <img width="1570" height="684" alt="image" src="https://github.com/user-attachments/assets/007228ad-481f-4fa2-ae06-f110b7dd8f28" />



---

## 📂 Project Structure

visionvoice/
├── app.py # Main Flask App
├── templates/
│ └── index.html # Web UI Template
├── static/
│ └── speech.mp3 # Audio Output File
├── requirements.txt # Python Dependencies
├── .gitignore # Prevents committing secrets
├── env_template # Sample .env file
└── README.md # You're here!


🔑 3. Setup .env with Your API Keys
OPENAI_API_KEY=your_openai_api_key
AZURE_TRANSLATOR_KEY=your_azure_translator_key
AZURE_TRANSLATOR_REGION=your_azure_region

