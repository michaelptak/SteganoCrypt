from cryptography.hazmat.primitives import padding
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
