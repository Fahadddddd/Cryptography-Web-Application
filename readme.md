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

### 3. JavaScript Functionality
The JavaScript code handles the encryption and decryption logic, as well as the user interactions with the form elements.

- **Encryption Function**: The `encrypt()` function takes the plaintext input from the user and encrypts it using the AES-256 encryption algorithm. The encrypted text is then displayed in the output field.
- **Decryption Function**: The `decrypt()` function takes the encrypted text from the user and decrypts it using the AES-256 decryption algorithm. The decrypted plaintext is then displayed in the output field.

<!-- ### 4. PHP Server-Side Script
The PHP script is used to handle the encryption and decryption requests from the client-side JavaScript code.

- **Encryption Request**: When the user clicks the "Encrypt" button, the JavaScript code sends an AJAX request to the PHP script with the plaintext input. The PHP script then encrypts the plaintext using the AES-256 encryption algorithm and returns the encrypted text to the client-side JavaScript code.
- **Decryption Request**: When the user clicks the "Decrypt" button, the JavaScript code sends an AJAX request to the PHP script with the encrypted text input. The PHP -->

