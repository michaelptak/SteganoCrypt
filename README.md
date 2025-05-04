# SteganoCrypt

A CLI tool for AES-256 encrypted steganography in images, created as the final project for my computer security class.

## Features
- AES-256-CBC via PBKDF2-SHA256 key derivation (any-length password)  
- 16-byte salt + 16-byte IV prepended to ciphertext  
- LSB steganography on PNGs  
- Basic commands: `encode`, `decode`, `convert`  

## Requirements
- Python 3.x  
- `venv` (activate before use)  
- `cryptography`, `Pillow`, `stegano`  

## Installation
```bash
git clone https://github.com/michaelptak/SteganoCrypt.git
cd SteganoCrypt
python3 -m venv venv
source venv/bin/activate
pip install -e .
```
## Usage
```bash
# Encode a message into an image
steganocrypt encode \
  --image in.png \
  --output out.png \
  --key "your password" \
  --message "secret stuff"

# Decode a message from an image
steganocrypt decode \
  --image out.png \
  --key "your password"

# (Optional) Convert any image to PNG
steganocrypt convert \
  --image photo.jpg \
  --output photo.png
```

## Project Layout
```css
SteganoCrypt/
├── setup.py
├── README.md
├── requirements.txt
└── src/
    └── steganocrypt/
        ├── __init__.py
        ├── main.py
        ├── encoder.py
        ├── decoder.py
        ├── crypto_utils.py
        └── image_utils.py
```
