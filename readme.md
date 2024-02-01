 # Project: Online Encryption and Decryption Tool

## Overview
This project aims to create a user-friendly online tool that allows users to encrypt and decrypt text using a random key or a custom secret key. The tool provides a secure and convenient way to protect sensitive information.

## Key Features
- **Encryption and Decryption**: The tool offers both encryption and decryption functionalities, allowing users to securely encode and decode text messages.
- **Random Key Generation**: By default, the tool generates a random key for encryption and decryption, ensuring utmost security.
- **Custom Key Option**: Users can also choose to use their own custom secret key for added security.
- **User-Friendly Interface**: The tool features a simple and intuitive user interface, making it easy for users to encrypt and decrypt text without any technical expertise.

## Implementation Details
The online encryption and decryption tool is implemented using HTML, CSS, JavaScript, and PHP. Here's a step-by-step explanation of the code:

### 1. HTML Structure
The HTML code defines the overall structure of the web page, including the header, banner, form, and footer sections.

### 2. CSS Styling
The CSS code provides the visual styling for the web page, including colors, fonts, and layout.


 # XOR Encryption and Decryption Web App

This repository contains the code for a simple web application that allows users to encrypt and decrypt text using the XOR encryption algorithm. The app is built using Flask, a lightweight Python web framework.

## How to Use

To use the app, follow these steps:

1. Clone the repository to your local machine.
2. Install the required Python packages by running `pip install Flask`.
3. Start the app by running `python app.py`.
4. Open your web browser and navigate to `localhost:5000`.
5. Enter the text you want to encrypt or decrypt in the "Text" field.
6. Enter the key to use for encryption or decryption in the "Key" field.
7. Click the "Encrypt" or "Decrypt" button to perform the desired operation.
8. The encrypted or decrypted text will be displayed in the "Encrypted Text" or "Decrypted Text" field, respectively.

## Code Overview

The app consists of the following files:

* `app.py`: The main Flask app file.
* `layout.html`: The HTML template for the app's layout.
* `static`: This Folder Contains Cascading Style Sheets And Images Used in the UI of the Web App.

<!-- The `app.py` file contains the following code:

```python
from flask import Flask, render_template, request
import base64

app = Flask(__name__)

def xor_encrypt_decrypt(data, key):
    encrypted_data = bytearray()
    key_length = len(key)

    for i in range(len(data)):
        encrypted_data.append(data[i] ^ key[i % key_length])

    return encrypted_data


@app.route('/')
def layout():
    return render_template('layout.html')


@app.route('/encrypt', methods=['POST'])
def encrypt():
    text = request.form.get('floatingTextarea2', '')
    key = request.form.get('key', '')
    action = request.form.get('action', '')

    data = text.encode('utf-8')
    key_bytes = key.encode('utf-8')

    if action == 'encrypt':
        encrypted_data = xor_encrypt_decrypt

Generated by [BlackboxAI](https://www.blackbox.ai) -->
