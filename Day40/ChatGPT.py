import random
import string

def encode_message(msg):
    if len(msg) >= 3:
        first_character = msg[0]
        new_msg = msg[1:] + first_character
        random_chars = ''.join(random.choice(string.ascii_letters) for _ in range(3))
        encoded_msg = random_chars + new_msg + random_chars
    else:
        encoded_msg = msg[::-1]
    return encoded_msg

def decode_message(encoded_msg):
    if len(encoded_msg) >= 7:
        random_chars = encoded_msg[:3]
        new_msg = encoded_msg[3:-3]
        last_character = encoded_msg[-3]
        decoded_msg = last_character + new_msg
    else:
        decoded_msg = encoded_msg[::-1]
    return decoded_msg

while True:
    choice = input("Do you want to code or decode a message? (Enter 'code' or 'decode' or 'quit' to exit): ")
    
    if choice == 'quit':
        print("Program End. Thank you.")
        break
    elif choice == 'code':
        msg = input("Enter the message (at least 3 characters) for Encoding: ")
        if len(msg) < 3:
            print("You have to enter at least 3 characters!")
        else:
            encoded_msg = encode_message(msg)
            print("Your encoded message is: " + encoded_msg)
    elif choice == 'decode':
        encoded_msg = input("Enter the encoded message for Decoding: ")
        decoded_msg = decode_message(encoded_msg)
        print("Your decoded message is: " + decoded_msg)
    else:
        print("Invalid choice. Please enter 'code', 'decode', or 'quit'.")
