import argparse
from steganocrypt.encoder import encrypt_message_aes, embed_message_in_image
from steganocrypt.decoder import extract_message_from_image, decrypt_message_aes
from steganocrypt.image_utils import convert_image_to_png

def main(): 
    parser = argparse.ArgumentParser(description="SteganoCrypt - Hide encrypted messages inside images.")
    subparsers = parser.add_subparsers(dest='command', required=True, help='Commands')

    # Encoder parser 
    encode_parser = subparsers.add_parser('encode', help='Encrypt and embed a message into an image.')
    encode_parser.add_argument('--image', required=True, help='Path to input image (PNG)')
    encode_parser.add_argument('--output', required=True, help='Path to output image with hidden message')
    encode_parser.add_argument('--key', required=True, help='Encryption key (in hex or string form)')
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
        encrypted_message = encrypt_message_aes(args.message, args.key.encode())
        embed_message_in_image(args.image, args.output, encrypted_message)
        print("[+] Message encrypted and embedded successfully.")

    elif args.command == 'decode':
        extracted_message = extract_message_from_image(args.image)
        # print(f"[DEBUG] Extracted ciphertext: {extracted_message}")

        try:
            decrypted_message = decrypt_message_aes(extracted_message, args.key.encode())                  
            print("[+] Decrypted message:")
            print(decrypted_message)
        except Exception as e:
            print("[-] Decryption failed: Incorrect key or corrupted image.")

    elif args.command == 'convert':
        convert_image_to_png(args.image, args.output)
        print(f"[+] Converted {args.image} → {args.output} (PNG)")
        return

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
