import openai
from flask import Flask, request, render_template

app = Flask(__name__)

# OpenAI API key
api_key="AIzaSyBzumjD3ZMsobIL_GeuNscmhIBu-HWM3N4"
openai.api_key = api_key

# Define a dictionary to store the mappings of commands to HTML pages
page_mappings = {
    "home": "home.html",
    "buy": "buy.html",
    # Add more mappings as needed
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/command", methods=["POST"])
def process_command():
    command = request.form.get("command")
    if command in page_mappings:
        page = page_mappings[command]
        return render_template(page)
    else:
        # Use OpenAI API to generate a response for unknown commands
        response = generate_response(command)
        return response

def generate_response(command):
    # Use the OpenAI API to generate a response based on the input command
    prompt = f"Command: {command}\nResponse:"
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can experiment with different engines
        prompt=prompt,
        temperature=0.7,
        max_tokens=100
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    app.run(debug=True)
