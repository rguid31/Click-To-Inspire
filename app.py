import os
from flask import Flask, jsonify
from openai import OpenAI  # Import the updated client
from flask_cors import CORS, cross_origin  # Import CORS to allow cross-origin requests

# Initialize the OpenAI client
client = OpenAI()
client.api_key = os.getenv('OPENAI_API_KEY')  # Fetch API key

app = Flask(__name__)
CORS(app)  # Allow CORS for all routes globally

@app.route('/generate-idea', methods=['GET'])
@cross_origin()  # Allow CORS for this specific route
def generate_idea():
    try:
        # Using the new format to interact with GPT models
        completion = client.chat.completions.create(
            model="gpt-4o",  # Assuming gpt-4o is a valid model name (please verify)
            messages=[
                {"role": "user", "content": "Give me a creative web app idea that a beginner could build."}
            ]
        )
        # Extract the generated response
        idea = completion.choices[0].message.content.strip()
        return jsonify({'idea': idea})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
 ##   app.run(debug=True)
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)