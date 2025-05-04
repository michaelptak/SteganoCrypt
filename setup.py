from setuptools import setup, find_packages

setup(
    name="steganocrypt",
    version="1.0",
    author="Michael Ptak",
    description="CLI tool for AES-encrypted steganography in images",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "cryptography",
        "Pillow",
        "stegano",
    ],
    entry_points={
        "console_scripts": [
            # defines a steganocrypt CLI command
            "steganocrypt=steganocrypt.main:main"
        ],
    },
)
