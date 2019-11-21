#Create a simple Ceaser Cypher

import encoder
import decoder

print("Welcome to the message encypter!")
key = int(input("\nPlease enter an offset: "))

x = input("Enter a phrase to be encoded: ").lower()

unencoded_message = list(x)

message = encoder.Encoder(key, unencoded_message)

message.encode_message()

encoded_message = message.print_encoded_message()

print("\nYour encoded message is:\n\t" + encoded_message)

print("\nNow we will decode you message...")

de_encode_message = decoder.Decoder(key, message.get_encoded_message())

de_encode_message.decode_message()

decoded_message = de_encode_message.print_decoded_message()

print("\nThe decoded message is :\n\t" + decoded_message)
