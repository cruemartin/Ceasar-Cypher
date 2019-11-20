"""This class encodes a message using a Ceaser Cypher and a key"""


class Encoder():

    def __init__(self, key, unencoded_message):
        """initilizes attributes to encode the users message"""
        self.key = key
        self.unencoded_message = unencoded_message
        self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                    'n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.encoded_message = []

    def encode_message(self):
        """Encodes the message by calculating an offset based on the key"""
        for letter in self.unencoded_message:
            if letter == ' ':
                self.encoded_message.append(' ')
            else:
                y = 0
                for alpha in self.alphabet:
            
                    if letter == alpha:
              
                        offset = (y + self.key) % 26
                   
                        self.encoded_message.append(self.alphabet[offset])
                        break
                    else:
                        y +=1

    def print_encoded_message(self):
        """Prints the encoded message """
        message = ''
        message = message.join(self.encoded_message)
        return message

    def get_encoded_message(self):
        return self.encoded_message