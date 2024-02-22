from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(start_text, shift, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift *= -1
    for char in start_text:
        #Preserve numbers,symbols and space and encrypt only letters
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"The {cipher_direction}d text is {end_text}")

#Output code
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #Control shift number to always fit in the size of alphabet
    shift = shift % 26

    caesar(start_text=text, shift= shift, cipher_direction= direction)

    result = input("Type 'yes' if you want to go again. Otherwise 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye")

