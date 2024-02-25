from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
continue_game = True


def caesar_cipher(cipher_direction, text_input, shift_amount):
    if not cipher_direction == "encode" and not cipher_direction == "decode":
        print("You have entered a wrong direction.")
    else:
        output_text = ""
        if cipher_direction == "decode":
            shift_amount *= -1
        for letter in text_input:
            if letter not in alphabet:
                output_text += letter
            else:
                position = alphabet.index(letter)
                new_position = position + shift_amount
                new_alphabet = alphabet[new_position]
                output_text += new_alphabet
        print(f"Here's your {cipher_direction}ed result: {output_text}")


while continue_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    if " " in text:
        text = text.translate({ord(" "): None})
    shift = int(input("Type the shift number:\n"))
    if shift > len(alphabet):
        shift %= len(alphabet)
    caesar_cipher(cipher_direction=direction, text_input=text, shift_amount=shift)
    game_on = input("Do you want to go again? Type 'yes' to continue or 'no' to exit the Caesar Cipher: ").lower()
    if game_on == 'no':
        continue_game = False
        print("Goodbye")




