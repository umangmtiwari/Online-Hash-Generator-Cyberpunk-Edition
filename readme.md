# Online Hash Generator

[![Live Demo](https://img.shields.io/badge/Live-Demo-green)](https://online-hash-generator.vercel.app/)

This is a Flask-based web application that allows users to generate hashes using various algorithms and interact with an AI-powered chatbot for questions related to hash algorithms.

## 🚀 Features
- **Generate Hashes** using multiple algorithms like MD5, SHA-256, CRC32, and more.
- **AI Chatbot** powered by Amazon Bedrock's Claude model to answer questions about hashing algorithms.
- **Asynchronous Processing** for chatbot responses using background threads.
- **AWS Bedrock Integration** to leverage large language models.

## 🛠️ Technologies Used
- **Flask** - Python web framework
- **Boto3** - AWS SDK for Python
- **LangChain** - AI model integration
- **PyCryptodome** - Additional hashing support
- **Vercel** - Deployment

## 📌 Available Hashing Algorithms
- MD5
- MD2
- MD4
- SHA-1
- SHA-256
- SHA-384
- SHA-512
- RIPEMD-160
- Adler-32
- CRC-32

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/online-hash-generator.git
cd online-hash-generator
