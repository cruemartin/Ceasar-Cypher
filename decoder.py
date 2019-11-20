"""Decodes a message encrypted with a Ceasar Cypher"""

class Decoder():

    def __init__(self, key, encoded_message):
        """initilize attributes do decoder"""
        self.key = key
        self.encoded_message = encoded_message
        self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                    'n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.decoded_message = []

    def decode_message(self):
        """Finds the offset by subtacting the key"""

        for letter in self.encoded_message:
            if letter == ' ':
                self.decoded_message.append(' ')
            else:
                y = 0
                for alpha in self.alphabet:
                    if letter == alpha:
                        offset = (y - self.key) % 26
                        self.decoded_message.append(self.alphabet[offset])
                        break
                    else:
                        y += 1
    

    def print_decoded_message(self):
        """Prints the decoded message to the console"""
        message = ''
        message = message.join(self.decoded_message)
        return message