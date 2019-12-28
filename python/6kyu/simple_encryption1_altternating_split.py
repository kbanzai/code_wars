# https://www.codewars.com/kata/57814d79a56c88e3e0000786

def decrypt(encrypted_text, n):
    if n > 0:
        return decrypt(''.join(encrypted_text[i//2] if i % 2 else encrypted_text[i//2+len(encrypted_text)//2] for i in range(len(encrypted_text))), n-1)
    else:
        return encrypted_text


def encrypt(text, n):
    for i in range(n):
        text = text[1::2]+text[::2]
    return text