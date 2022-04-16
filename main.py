import pyae


def printAuthor():
    print("Fellia Ayu SA - 1197050043")
    print("Sabili Haq RS - 1197050123")

def dotBorder():
    print("...........................................")

def printHeader():
    print("____________ARITHMETIC ENCODING____________")

frequency_table = {"a": 2, "b": 3, "c": 1, "d": 4, "e": 3, "f": 6, "g": 2, "h": 1, "i": 5, "j": 2, "k": 8, "l": 2,
                   "m": 1, "n": 4, "o": 2, "p": 1, "q": 4, "r": 3, "s": 1, "t": 2, "u": 4, "v": 2, "w": 1, "x": 1, "y": 2, "z": 4}

AE = pyae.ArithmeticEncoding(frequency_table)

print("Input message :")
original_msg = input()

dotBorder()
printHeader()
dotBorder()
printAuthor()
dotBorder()

AE = pyae.ArithmeticEncoding(frequency_table=frequency_table,
                             save_stages=False)

original_msg = "abc"
print("Original Message: {msg}".format(msg=original_msg))

# encode message
encoded_msg, encoder, interval_min_value, interval_max_value = AE.encode(msg=original_msg,
                                                                         probability_table=AE.probability_table)
print("Encoded Message  : {msg}".format(msg=encoded_msg))

# get binary code
binary_code, encoder_binary = AE.encode_binary(float_interval_min=interval_min_value,
                                               float_interval_max=interval_max_value)
print("The Binary Code  : {binary_code}".format(binary_code=binary_code))

# decode the message
decoded_msg, decoder = AE.decode(encoded_msg=encoded_msg,
                                 msg_length=len(original_msg),
                                 probability_table=AE.probability_table)
decoded_msg = "".join(decoded_msg)
print("Decoded Message  : {msg}".format(msg=decoded_msg))

dotBorder()

print("Message Decoded Successfully? {result}".format(
    result=original_msg == decoded_msg))

dotBorder()