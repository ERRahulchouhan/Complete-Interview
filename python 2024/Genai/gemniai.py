from flask import Flask, request, jsonify
import google.generativeai as genai

# Set up Gemini AI configuration (replace with your API key)
app = Flask(__name__)
api_key="AIzaSyBzumjD3ZMsobIL_GeuNscmhIBu-HWM3N4"
genai.configure(api_key=api_key)

@app.route("/", methods=["GET"])  # Root route
def index():
    return "Welcome to your Gemini AI Flask application!"

@app.route("/generate", methods=["POST"])  # Route for text generation
def generate_text():
    if request.method == "POST":
        prompt = request.json.get("prompt")  # Get prompt from request body
        if prompt:
            # Send the prompt to Gemini AI for text generation
            response = genai.generate(prompt=prompt)
            return jsonify({"generated_text": response})
        else:
            return jsonify({"error": "Missing 'prompt' in request body"}), 400
    else:
        return jsonify({"error": "Invalid request method"}), 405

# Other routes for different functionalities (e.g., image generation, translation, etc.)

if __name__ == "__main__":
    app.run(debug=True)