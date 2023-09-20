from caeser_cipher_art import logo
print(logo)

should_continue = True
while should_continue:

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Enter what you want to do encode or decode:")
    text = input("enter the text:").lower()
    shift = int(input("enter how much shift you want:"))

    if shift >26:
        mod = shift%26
        shift = mod

    # def encode(plain_text, shift_right):
    #     cipher_text =""
    #     for letter in plain_text:
    #         if letter in alphabet:
    #             position = alphabet.index(letter)
    #             new_position = position + shift_right         #First method
    #             new_letter = alphabet[new_position]
    #             cipher_text += new_letter
    #         else:
    #             cipher_text += letter
    #     print("your encoded text is:", cipher_text)
    #
    #
    #
    #
    #
    # def decode(cipher_text, shift_left):
    #     real_text = ""
    #     for letter in cipher_text:
    #         if letter in alphabet:
    #             position = alphabet.index(letter)
    #             new_position = position - shift_left
    #             new_letter = alphabet[new_position]
    #             real_text += new_letter
    #         else:
    #             real_text += letter
    #     print("your decoded text is:", real_text)
    #
    #
    # 
    # if direction == "encode":
    #     encode(text,shift)
    #
    # else:
    #     decode(text,shift)
    #****************************************************************************************************************
    def ceaser(new_text, shift_rl, spec_direction):
        ed_text = ""
        if spec_direction == "decode":
                shift_rl *= -1
        for letter in new_text:
            if letter in alphabet:                        #Second method
                position = alphabet.index(letter)
                new_position = position + shift_rl
                ed_text += alphabet[new_position]
            else:
                ed_text += letter 
        print("your ciphered text is:",ed_text)


    ceaser(text, shift, direction)
    ask = input("if you want to continue type yes or else no to discontinue: ")

    if ask == "no":
        should_continue = False
        print("goodbye")