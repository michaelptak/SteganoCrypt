# encoder.py
import os
import base64
from stegano import lsb
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from steganocrypt.crypto_utils import pad_data, derive_key

def encrypt_message_aes(message: str, password: bytes) -> bytes:
    """
    AES-CBC encryption. Encrypt a message in UTF-8 with provided key (must be 16/24/32 bytes)
    Returns: IV + Ciphertext
    """
    # 1. Derive key + salt from user password
    salt, key = derive_key(password)

    # 2. Pad to block size. AES works in 16-byte blocks, ensure it is extended to a multiple of 16 with PKCS#7 padding
    padded_data = pad_data(message.encode())

    # 3. Randomize the IV and encrypt 
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    ct = cipher.encryptor().update(padded_data) + cipher.encryptor().finalize()

    return salt + iv + ct

def embed_message_in_image(image_path: str, output_path: str, encrypted_message: bytes):
    """
    Base64 encode the encrypted bytes and hide in the image LSB 
    """
    # Convert bytes to an ASCII string 
    b64 = base64.b64encode(encrypted_message).decode()
    # Hide the message in the image and save it to the output path 
    secret_img = lsb.hide(image_path, b64)
    secret_img.save(output_path)
