import base64
from stegano import lsb 
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from crypto_utils import unpad_data, derive_key

def extract_message_from_image(image_path: str) -> bytes:
    """
    Pull the base-64 encoded payload out of the image LSB and decode to bytes
    """
    # Walks through LS bits of each pixel channel, reassemble and return B64 encoded string or None
    b64 = lsb.reveal(image_path)
    if b64 is None:
        raise ValueError("No hidden message found.")
    return base64.b64decode(b64)

def decrypt_message_aes(payload: bytes, password: bytes) -> str:
    """
    Parse salt+iv+ciphertext, re-derive key, decrypt, unpad, return plaintext.
    """
    # 1. Split off salt, IV, and ciphertext
    salt, iv, ct = payload[:16], payload[16:32], payload[32:]

    # 2. re-derive the same key 
    _, key = derive_key(password, salt=salt)

    # 3. Decrypt padded data 
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    padded_data = cipher.decryptor().update(ct) 
    padded_data += cipher.decryptor().finalize()

    # 4. Strip off the padding 
    data = unpad_data(padded_data)

    return data.decode()
