# crypto_utils.py
import os
from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import algorithms

def pad_data(data: bytes) -> bytes:
    """
    PKCS#7–pad data to the AES block size (16 bytes)
    """
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    return padder.update(data) + padder.finalize()

def unpad_data(padded_data: bytes) -> bytes:
    """
    Remove PKCS#7 padding from padded_data
    """
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    return unpadder.update(padded_data) + unpadder.finalize()

def derive_key(password: bytes, salt: bytes = None) -> tuple[bytes, bytes]:
    """
    Derive a 32-byte key from any-length password via PBKDF2-SHA256
    Returns (salt, key). If salt is None, generates a fresh 16-byte salt
    """
    salt = salt or os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000
    )
    key = kdf.derive(password)
    return salt, key
