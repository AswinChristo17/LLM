from flask import Flask, request, jsonify, render_template, Response
import ollama
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_etiquette', methods=['POST'])
def get_etiquette():
    country = request.form.get('country', '').strip()

    if not country:
        return jsonify({'error': 'Please enter a valid country name.'}), 400

    try:
        prompt = (
            f"You are a Cultural Etiquette Expert. "
            f"Provide a detailed guide for {country}. "
            f"Include: \n"
            f"1. Greetings \n"
            f"2. Dining Manners \n"
            f"3. Gift-Giving Customs \n"
            f"4. Major Taboos \n"
            f"5. Special Traditions or Festivals\n\n"
            f"Format the response clearly with headings for each section."
        )

        # Stream the response from Ollama
        def generate():
            stream = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": prompt}], stream=True)
            for chunk in stream:
                yield chunk['message']['content']

        return Response(generate(), mimetype='text/plain')

    except Exception as e:
        logger.error(f"Error fetching etiquette: {str(e)}")
        return jsonify({'error': f"Failed to fetch response: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)