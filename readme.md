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

## 📌 **Available Hashing Algorithms and Their Explanations**  

### 🔹 **MD5 (Message-Digest Algorithm 5)**  
MD5 is a widely used cryptographic hash function that produces a **128-bit (32-character hexadecimal)** hash value. While it was once considered secure, it is now vulnerable to collision attacks and is not recommended for cryptographic security.  

### 🔹 **MD2 (Message-Digest Algorithm 2)**  
MD2 is an older cryptographic hash function designed for **8-bit processors**. It produces a **128-bit hash** but is slower compared to newer hashing algorithms. It is now considered obsolete and insecure.  

### 🔹 **MD4 (Message-Digest Algorithm 4)**  
MD4 is a **fast but insecure** cryptographic hash function that generates a **128-bit hash**. It was the predecessor of MD5 but is highly susceptible to attacks and should not be used for security-sensitive applications.  

### 🔹 **SHA-1 (Secure Hash Algorithm 1)**  
SHA-1 produces a **160-bit (40-character hexadecimal)** hash and was once widely used in SSL certificates and cryptographic applications. However, due to vulnerabilities discovered in 2017, it is now considered **insecure for cryptographic purposes**.  

### 🔹 **SHA-256 (Secure Hash Algorithm 256-bit)**  
SHA-256 is part of the SHA-2 family and generates a **256-bit (64-character hexadecimal)** hash. It is commonly used in **blockchain technologies, SSL certificates, and password hashing** due to its strong security properties.  

### 🔹 **SHA-384 (Secure Hash Algorithm 384-bit)**  
SHA-384 is a variant of SHA-2 that produces a **384-bit (96-character hexadecimal)** hash. It offers higher security and is used in digital signatures and data integrity verification.  

### 🔹 **SHA-512 (Secure Hash Algorithm 512-bit)**  
SHA-512 is another variant of SHA-2, producing a **512-bit (128-character hexadecimal)** hash. It is used in applications requiring **high security and resistance to brute-force attacks**, such as file integrity checks and cryptographic protocols.  

### 🔹 **RIPEMD-160 (RACE Integrity Primitives Evaluation Message Digest 160-bit)**  
RIPEMD-160 is a cryptographic hash function that produces a **160-bit hash**. It was developed as an alternative to SHA-1 and MD5 and is used in some blockchain applications.  

### 🔹 **Adler-32**  
Adler-32 is a **fast, lightweight checksum algorithm** used for error detection in data transmission and storage. It produces a **32-bit hash** but is **not suitable for cryptographic security**.  

### 🔹 **CRC-32 (Cyclic Redundancy Check 32-bit)**  
CRC-32 is an error-checking algorithm that generates a **32-bit checksum**. It is used to detect accidental changes in data but **is not a cryptographic hash function** and should not be used for security-related applications.  

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/online-hash-generator.git
cd online-hash-generator
