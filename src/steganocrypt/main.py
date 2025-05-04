# main.py
import os
import sys
import argparse
from steganocrypt.encoder import encrypt_message_aes, embed_message_in_image
from steganocrypt.decoder import extract_message_from_image, decrypt_message_aes
from steganocrypt.image_utils import convert_image_to_png

def file_exists(path: str):
    if not os.path.isfile(path):
        print(f"[-] File not found: {path}")
        sys.exit(1)

def main(): 
    parser = argparse.ArgumentParser(description="SteganoCrypt - Hide encrypted messages inside images.")
    subparsers = parser.add_subparsers(dest='command', required=True, help='Commands')

    # Encoder parser 
    encode_parser = subparsers.add_parser('encode', help='Encrypt and embed a message into an image.')
    encode_parser.add_argument('--image', required=True, help='Path to input image (PNG)')
    encode_parser.add_argument('--output', required=True, help='Path to output image with hidden message')
    encode_parser.add_argument('--key', required=True, help='Encryption key (A string)')
    encode_parser.add_argument('--message', required=True, help='Message to encrypt and embed')

    # Decoder parser
    decode_parser = subparsers.add_parser('decode', help='Extract and decrypt a message from an image.')
    decode_parser.add_argument('--image', required=True, help='Path to stego image (PNG)')
    decode_parser.add_argument('--key', required=True, help='Encryption key used for decryption')

    # Converting image util for convenience if using a lossy format
    convert_parser = subparsers.add_parser('convert', help='Convert any image to PNG')
    convert_parser.add_argument('--image', required=True, help='Path to source image')
    convert_parser.add_argument('--output', required=True, help='Path to output PNG')

    args = parser.parse_args()

    if args.command == 'encode':
        file_exists(args.image)
        try:
            encrypted = encrypt_message_aes(args.message, args.key.encode())
            embed_message_in_image(args.image, args.output, encrypted)
            print("[+] Message encrypted and embedded successfully.")
        except Exception as e:
            print(f"[-] Encoding failed: {e}")
            sys.exit(1)    

    elif args.command == 'decode':
        file_exists(args.image)
        try:
            blob = extract_message_from_image(args.image)
        except ValueError as e:
            print(f"[-] Extraction failed: {e}")
            sys.exit(1)
        except Exception:
            print(f"[-] Could not read image: {args.image}")
            sys.exit(1)

        try:
            plaintext = decrypt_message_aes(blob, args.key.encode())
            print("[+] Decrypted message:")
            print(plaintext)
        except Exception:
            print("[-] Decryption failed: Incorrect key or corrupted image.")
            sys.exit(1)

    elif args.command == 'convert':
        file_exists(args.image)
        try:
            convert_image_to_png(args.image, args.output)
            print(f"[+] Converted {args.image} → {args.output} (PNG)")
        except Exception as e:
            print(f"[-] Conversion failed: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()
