from flask import Flask, render_template, request

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
    text = request.form['floatingTextarea2']
    key = request.form['key']
    
    # Convert input to bytes
    data = text.encode('utf-8')
    key_bytes = key.encode('utf-8')

    # Encrypt
    encrypted_data = xor_encrypt_decrypt(data, key_bytes)
    encrypted_text = encrypted_data.decode('utf-8')
    
    return render_template('layout.html', encrypted_text=encrypted_text)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_text = request.form['encrypted_text']
    key = request.form['key']
    
    # Convert input to bytes
    encrypted_data = encrypted_text.encode('utf-8')
    key_bytes = key.encode('utf-8')

    # Decrypt
    decrypted_data = xor_encrypt_decrypt(encrypted_data, key_bytes)
    decrypted_text = decrypted_data.decode('utf-8')

    return render_template('layout.html', decrypted_text=decrypted_text)

if __name__ == '__main__':
    app.run(debug=True)
