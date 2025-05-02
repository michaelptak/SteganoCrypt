# SteganoCrypt 

## Features
- AES-256 encryption via PBKDF2-SHA256 key derivation (any-length password)
- Salt (16 bytes) + IV (16 bytes) prepended to ciphertext
- Basic CLI: `encode` & `decode`

## Requirements
- Python 3.x 
- `venv` (activate before use)
- `cryptography`, `Pillow`, `stegano`

## 🛠️ Quick Start
```bash
git clone https://github.com/michaelptak/SteganoCrypt.git
cd SteganoCrypt
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Encode
python main.py encode \
  --image in.png \
  --output out.png \
  --key my16bytepass \
  --message "secret"

# Decode
python main.py decode \
  --image out.png \
  --key my16bytepass
