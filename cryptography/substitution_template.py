#!/usr/bin/env python3

"""
File:
Name:

Description:
Sources:
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"

# WARNING: Aside from the line where the key variable is initialized, don't touch this function.
def main():
    key = None  # How the key is calculated is up to you. This is the only line you should be changing.
    
    original = input("Enter word or phrase to encrypt: ").lower()
    ciphertext = encrypt(original, key)
    plaintext = decrypt(ciphertext, key)

    print("Original text: ", original)
    print("Encrypted text:", ciphertext)
    print("Decrypted text:", plaintext)


def encrypt(text, key):
    # Code here


def decrypt(text, key):
    # Code here


if __name__ == "__main__":
    main()