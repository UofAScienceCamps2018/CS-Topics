#!/usr/bin/env python3

"""
File: caesar_template.py
Name:

Description:
Sources:
"""


# WARNING: Aside from the line where the shift variable is initialized, don't touch this function.
def main():
    shift = None  # How the shift is calculated is up to you. This is the only line you should be changing.

    original = input("Enter word or phrase to encrypt: ")
    ciphertext = encrypt(original, shift)
    plaintext = decrypt(ciphertext, shift)

    print("Original text: ", original)
    print("Encrypted text:", ciphertext)
    print("Decrypted text:", plaintext)


def encrypt(text, shift):
    # Code here


def decrypt(text, shift):
    # Code here


if __name__ == "__main__":
    main()
