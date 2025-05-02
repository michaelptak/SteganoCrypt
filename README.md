# SteganoCrypt 

## Features
- AES-CBC encryption (16/24/32-byte keys)
- LSB steganography on PNGs
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
