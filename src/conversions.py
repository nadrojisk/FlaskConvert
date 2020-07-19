import codecs
import base64


def ascii_conversion(text):
    # helper function to convert hex to ascii
    text = text.split(' ')
    output = ''.join([chr(int(x, 16)) for x in text])
    return output.strip()


def bin_conversion(text):
    # helper function to convert hex to bin
    text = text.split(' ')
    output = ''.join(["0b" + bin(int(x, 16))[2:].zfill(8) + " " for x in text])
    return output.strip()


def dec_conversion(text):
    # helper function to convert hex to dec
    text = text.split(' ')
    output = ''.join([str(int(x, 16)) + " " for x in text])
    return output.strip()


def hex_conversion(text):
    # helper function to convert hex to hex
    text = text.split(' ')
    output = ''.join(["0x" + hex(int(x, 16))[2:].zfill(2) + " " for x in text])
    return output.strip()


def oct_conversion(text):
    # helper function to convert hex to octal
    text = text.split(' ')
    output = ''.join(['0o' + oct(int(x, 16))[2:].zfill(3) + " " for x in text])
    return output.strip()


def base64_conversion(text):
    # helper function to convert hex to base64
    text = ascii_conversion(text)
    output = base64.b64encode(text.encode()).decode().replace('\n', '')
    return output.strip()


def base32_conversion(text):
    # helper function to convert hex to base32
    text = ascii_conversion(text)
    output = base64.b32encode(text.encode()).decode().replace('\n', '')
    return output.strip()


def hex_to_hex(input_text):
    # function to convert from hex to hex
    # this is mainly here to ensure the input is hex
    text = input_text.split(' ')
    for x in text:
        try:
            int(x, 16)
        except ValueError:
            # input is not hex
            return 0
    output = input_text
    return output


def bin_to_hex(input_text):
    # function to convert from binary to hex
    text = input_text.split(' ')
    output = ''
    for x in text:
        try:
            output += hex(int(x, 2)) + " "
        except ValueError:
            # input is not bin
            return 0
    return output


def dec_to_hex(input_text):
    # function to convert from decimal to hex
    text = input_text.split(' ')
    output = ''
    for x in text:
        try:
            # crash on negative numbers
            if int(x) < 0:
                return 0
            output += hex(int(x)) + " "
        except ValueError:
            # input is not dec
            return 0
    return output


def oct_to_hex(input_text):
    # function to convert from octal to hex
    text = input_text.split(' ')
    output = ''
    for x in text:
        try:
            output += hex(int(x, 8)) + " "
        except ValueError:
            # input is not oct
            return 0
    return output


def ascii_to_hex(input_text):
    # function to convert from ascii to hex
    output = ''.join([hex(ord(x)) + " " for x in input_text])
    return output


def base64_to_hex(input_text):
    # function to convert from base64 to hex

    # add in code to handle improperly padded input
    rem = len(input_text) % 4
    if rem:
        padding = (4 - rem)*"="
        input_text += padding
    try:
        input_text = base64.b64decode(input_text).decode()
    except:
        return 0
    output = ''.join([hex(ord(x)) + " " for x in input_text])
    return output


def base32_to_hex(input_text):
    # function to convert from base32 to hex

    # add in code to handle improperly padded input
    rem = len(input_text) % 8
    if rem:
        padding = (8 - rem)*"="
        input_text += padding
    try:
        input_text = base64.b32decode(input_text).decode()
    except:
        return 0
    output = ''.join([hex(ord(x)) + " " for x in input_text])
    return output
