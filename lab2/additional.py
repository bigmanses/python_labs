def create_dictionary(keys, values):
    abc_key = {}
    for i in range(len(keys)):
        abc_key[key[i]] = values[i]
    return abc_key


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def ciphering(abc_key, text):
    new_text = []
    for i in range(len(text)):
        new_text.append(get_key(abc_key, text[i]))
    print("".join(new_text))


def decoding(abc_key, text):
    new_text = []
    for i in range(len(text)):
        new_text.append(abc_key.get(text[i]))
    print("".join(new_text))


abc = input()
key = input()

abc_key = create_dictionary(key, abc)

original = input()
cipher = input()

ciphering(abc_key, original)
decoding(abc_key, cipher)