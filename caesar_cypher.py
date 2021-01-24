


def encrypt(text, s):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text

        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

def decrypt(result, s):
    text = ""
    # transverse the encrypted text
    for i in range(len(result)):
        char = result[i]
        # Decrypt uppercase characters in result

        if (char.isupper()):
            text += chr((ord(char) - s - 65) % 26 + 65)
        # Decrypt lowercase characters in result
        else:
            text += chr((ord(char) - s - 97) % 26 + 97)
    return result


# check the above function
plain_text = input("Enter The Text You Want Encrypted:")
s = int(input("Enter desired shift:"))

print("Plain Text : " + plain_text)
print("Shift pattern : " + str(s))
print("Cipher: " + encrypt(plain_text, s))
print("Decipher: " + decrypt(plain_text, s))
