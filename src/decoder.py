import base64
from stegano import lsb
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

from crypto_utils import unpad_data

def extract_message_from_image(image_path: str) -> bytes:
    """
    Pull the base-64 encoded payload out of the image LSB and decode to bytes
    """
    # Walks through LS bits of each pixel channel, reassemble and return B64 encoded string or None
    b64 = lsb.reveal(image_path)
    if b64 is None:
        raise ValueError("No hidden message found.")
    return base64.b64decode(b64)

def decrypt_message_aes(ciphertext: bytes, key: bytes) -> str:
    """
    Split off the IV (first 16 bytes), decrypt the rest, unpad, and return UTF-8 string
    """
    # Prefixed with 16 bit IV before, so slice it out 
    iv, ct = ciphertext[:16], ciphertext[16:]
    # Takes the same key + IV + CBC mode to decrypt 
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    # Feeds raw ciphertext in decryptor, yielding padded message bytes 
    padded_data = cipher.decryptor().update(ct) 
    padded_data += cipher.decryptor().finalize()

    # Strip off the padding 
    data = unpad_data(padded_data)

    return data.decode()
