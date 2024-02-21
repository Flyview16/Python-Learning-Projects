alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift
        new_text = alphabet[new_position]
        cipher_text += new_text
    
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        old_position = position - shift
        plain_text += alphabet[old_position]
    
    print(f"The decoded text is {plain_text}")


if direction == "encode":
    encrypt(plain_text = text, shift = shift)
elif direction == "decode":
    decrypt(encoded_message = text, shift = shift)
else:
    print("Invalid instruction.")


