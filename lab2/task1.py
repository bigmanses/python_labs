from itertools import cycle


def xor_string(message, key):
    cyphered = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(message, cycle(key)))
    return cyphered


text = input()
key = input()
result = xor_string(text, key)
print(result)
print(xor_string(result, key))