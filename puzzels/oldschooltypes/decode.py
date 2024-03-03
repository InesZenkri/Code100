'''
If 44-33-555-555-666 is hello and 9-666-777-555-3 is world, what is:
9-33-0-2-777-33-0-3-33-888-33-555-666-7-33-777-7777
Can you do an encoder/decoder for this way of writing?
'''
def encode(message):
    keypad = {
        'a': '2', 'b': '22', 'c': '222',
        'd': '3', 'e': '33', 'f': '333',
        'g': '4', 'h': '44', 'i': '444',
        'j': '5', 'k': '55', 'l': '555',
        'm': '6', 'n': '66', 'o': '666',
        'p': '7', 'q': '77', 'r': '777', 's': '7777',
        't': '8', 'u': '88', 'v': '888',
        'w': '9', 'x': '99', 'y': '999', 'z': '9999',
        ' ': '0'
    }

    encoded_message = ''
    for char in message.lower():
        if char in keypad:
            encoded_message += keypad[char] + '-'

    return encoded_message[:-1] 


def decode(encoded_message):
    keypad_reverse = {
        '2': 'a', '22': 'b', '222': 'c',
        '3': 'd', '33': 'e', '333': 'f',
        '4': 'g', '44': 'h', '444': 'i',
        '5': 'j', '55': 'k', '555': 'l',
        '6': 'm', '66': 'n', '666': 'o',
        '7': 'p', '77': 'q', '777': 'r', '7777': 's',
        '8': 't', '88': 'u', '888': 'v',
        '9': 'w', '99': 'x', '999': 'y', '9999': 'z',
        '0': ' '
    }

    decoded_message = ''
    encoded_parts = encoded_message.split('-')
    for part in encoded_parts:
        if part in keypad_reverse:
            decoded_message += keypad_reverse[part]

    return decoded_message



encoded = "9-33-0-2-777-33-0-3-33-888-33-555-666-7-33-777-7777"
print("Decoding '9-33-0-2-777-33-0-3-33-888-33-555-666-7-33-777-7777':", decode(encoded))


message_to_encode = "hello world"
encoded_message = encode(message_to_encode)
print("Encoded message:", encoded_message)
print("Decoding encoded message:", decode(encoded_message))
