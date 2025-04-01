from flask import Flask, render_template, request, jsonify
import hashlib
import zlib
import uuid
import boto3
from Crypto.Hash import MD4, MD2, RIPEMD160  # pycryptodome for additional hashing
from langchain.llms.bedrock import Bedrock
from threading import Thread
import logging
import os

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# AWS Bedrock Client for Claude
bedrock = boto3.client(service_name="bedrock-runtime")

# In-memory task store to handle chatbot responses
tasks = {}

# Claude LLM setup
def get_claude_llm():
    return Bedrock(model_id="anthropic.claude-v2", client=bedrock)

# Claude prompt template
prompt_template = """Human: Please answer the following question regarding to Hash Algorithms Generation with clarity and accuracy.
Question: {question}
Assistant:"""

def generate_prompt(question):
    return prompt_template.format(question=question)

# Function to get response from Claude
def get_response_from_claude(llm, question):
    prompt = generate_prompt(question)
    response = llm.generate([prompt])

    if response.generations and len(response.generations) > 0:
        return response.generations[0][0].text
    else:
        return "Sorry, I couldn't generate an answer."

# Background thread for processing chatbot tasks
def process_task(task_id, question):
    try:
        logger.info(f"Processing task ID: {task_id} with question: {question}")
        llm = get_claude_llm()
        answer = get_response_from_claude(llm, question)
        tasks[task_id] = {"status": "completed", "result": answer}
    except Exception as e:
        logger.error(f"Error processing task ID: {task_id}", exc_info=True)
        tasks[task_id] = {"status": "error", "result": str(e)}

# Hashing function mapping
hash_algorithms = {
    'md5': hashlib.md5,
    'md2': MD2.new,
    'md4': MD4.new,
    'sha1': hashlib.sha1,
    'sha256': hashlib.sha256,
    'sha384': hashlib.sha384,
    'sha512': hashlib.sha512,
    'ripemd160': RIPEMD160.new,
    'adler32': zlib.adler32,
    'crc32': zlib.crc32,
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-hash', methods=['POST'])
def generate_hash():
    data = request.json
    text = data.get('text', '').strip()
    algorithm = data.get('algorithm', 'sha1').lower()

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    hash_func = hash_algorithms.get(algorithm)

    if not hash_func:
        return jsonify({'error': f'Unsupported algorithm {algorithm}'}), 400

    if algorithm in ['adler32', 'crc32']:
        hash_value = hash_func(text.encode('utf-8'))
        return jsonify({'hash': format(hash_value, '08x')})

    hash_object = hash_func(text.encode('utf-8'))
    hash_value = hash_object.hexdigest() if hasattr(hash_object, 'hexdigest') else hash_object

    return jsonify({'hash': hash_value})

# Route for chatbot page
@app.route('/ask-doubt')
def ask_doubt():
    return render_template('chat.html')

# API to handle chatbot questions
@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    user_question = data.get('question')

    if not user_question:
        return jsonify({"status": "error", "result": "Question is required"}), 400

    task_id = str(uuid.uuid4())
    tasks[task_id] = {"status": "pending", "result": None}

    thread = Thread(target=process_task, args=(task_id, user_question))
    thread.start()

    return jsonify({"task_id": task_id})

# API to get chatbot response
@app.route('/result/<task_id>', methods=['GET'])
def get_result(task_id):
    task = tasks.get(task_id)
    if not task:
        return jsonify({"status": "error", "result": "Invalid task ID"}), 404

    return jsonify(task)

if os.getenv("VERCEL"):
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
else:
    app.run(debug=True)