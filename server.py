from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This enables the Flutter app to talk to this server

# --- CONFIGURATION ---
# PASTE YOUR API KEY INSIDE THE QUOTES BELOW
MY_API_KEY = "AIzaSyBA1aes6VFJlW-aaLBomOlghQrR1Uut1NQ" 

genai.configure(api_key=MY_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

@app.route('/')
def home():
    return "Server is running! The Chef is ready."

@app.route('/review', methods=['POST'])
def review_code():
    try:
        # 1. Get the code from the request
        data = request.get_json()
        user_code = data.get('code')

        if not user_code:
            return jsonify({"error": "No code provided"}), 400

        # 2. Create a prompt for the AI
        prompt = f"""
        Act as a Senior Software Engineer. Review the following code.
        1. Identify any bugs or errors.
        2. Provide the corrected code.
        3. Explain what was wrong in simple terms.
        
        Code to review:
        {user_code}
        """

        # 3. Ask Gemini
        response = model.generate_content(prompt)

        # 4. Send the answer back to the user
        return jsonify({"review": response.text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the server on port 5000
    app.run(debug=True, host='0.0.0.0', port=5001)