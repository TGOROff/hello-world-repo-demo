def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def encrypt(text, s):
    result = ""
    if is_ascii(text):

    # transverse the plain text
        for i in range(len(text)):
            char = text[i]
            resultvalue = ord(char) + s
            # Encrypt uppercase characters in plain text

            if resultvalue > 128:
                resultvalue -= 128

            result += chr(resultvalue)

        return result
    else:
        return "Not a valid ascii string"

def decrypt(result, s):
    text = ""
    if is_ascii(result):

    # transverse the encrypted text
        for i in range(len(result)):
            char = result[i]
            resultvalue = ord(char) - s
            # Decrypt uppercase characters in result

            if resultvalue < 0:
                resultvalue += 128
                # There is an issue with repetition, must debug

            text += chr(resultvalue)
        return result
    else:
        return "Not a valid ascii string"


# check the above function
plain_text = input("Enter The Text You Want Encrypted:")
s = int(input("Enter desired shift:"))

print("Plain Text : " + plain_text)
print("Shift pattern : " + str(s))
print("Cipher: " + encrypt(plain_text, s))
print("Decipher: " + decrypt(plain_text, s))
