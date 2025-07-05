from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
from PIL import Image
import pytesseract
import openai
from gtts import gTTS
import speech_recognition as sr
from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.text import TextTranslationClient

# Load environment variables
load_dotenv()
app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Azure Translator setup
translator_key = os.getenv("AZURE_TRANSLATOR_KEY")
translator_region = os.getenv("AZURE_TRANSLATOR_REGION")
translator_endpoint = f"https://{translator_region}.api.cognitive.microsofttranslator.com"

translation_client = TextTranslationClient(
    endpoint=translator_endpoint,
    credential=AzureKeyCredential(translator_key)
)

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("🎙️ Speak now...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        return "Speech not recognized."

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    translated_text = ""
    if request.method == "POST":
        image = request.files["image"]
        target_lang = request.form.get("language", "hi")
        img = Image.open(image)
        text = pytesseract.image_to_string(img)

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                {"role": "user", "content": f"Summarize this: {text}"}
            ]
        )
        summary = response.choices[0].message.content

        translation = translation_client.translate(
            content=[summary],
            to=[target_lang],
            from_parameter="en"
        )
        translated_text = translation[0].translations[0].text

        tts = gTTS(translated_text, lang=target_lang)
        tts.save("static/speech.mp3")

    return render_template("index.html", summary=summary, translation=translated_text)

@app.route("/voice", methods=["GET"])
def voice():
    question = recognize_speech_from_mic()
    return render_template("index.html", summary=f"You asked: {question}")

if __name__ == "__main__":
    app.run(debug=True)