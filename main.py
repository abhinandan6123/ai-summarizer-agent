from flask import Flask, request, jsonify
import vertexai
from vertexai.generative_models import GenerativeModel

app = Flask(__name__)

# Initialize Gemini
vertexai.init(project="gen-lang-client-0980949201", location="us-central1")
model = GenerativeModel("gemini-1.5-flash")

@app.route("/")
def home():
    return "AI Summarizer Agent is running 🚀"

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    text = data.get("text", "")

    prompt = f"Summarize this text in short:\n{text}"

    response = model.generate_content(prompt)

    return jsonify({
        "summary": response.text
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

