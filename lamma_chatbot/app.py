from flask import Flask, render_template, request, jsonify
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

def get_response(user_input):
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        groq_api_key=os.getenv["api_key"]
    )
    res = llm.invoke(user_input)  
    return str(res.content.strip())  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = get_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
