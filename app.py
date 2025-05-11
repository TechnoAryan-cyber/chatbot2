
import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Configure Gemini API
GOOGLE_API_KEY = "AIzaSyA7wri1ps-zrW4mlCEfh0Ap0XV-3a4Ffc0 "  # Replace with your API key
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    try:
        # Send user input to Gemini API
        response = model.generate_content(user_input)
        bot_response = response.text
    except Exception as e:
        bot_response = f"Error: {str(e)}"
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True , port=5002)
