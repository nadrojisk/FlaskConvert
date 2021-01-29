import conversions


def helper(prefix=True, width=8):
    return conversions.Conversions(prefix, width)


def test_ascii_conversion_normal():
    text = "0x30 0x31 0x32 0x33 0x34 0x35 0x41 0x42"
    conv = helper()
    actual = conv.ascii_conversion(text)
    expected = "012345AB"

    assert expected == actual


def test_ascii_conversion_unicode():
    text = "0x3010"
    conv = helper()
    actual = conv.ascii_conversion(text)
    expected = "【"

    assert expected == actual


def test_bin_conversion_normal():
    text = "0x30 0x31 0x32 0x33 0x34 0x35 0x41 0x42"
    conv = helper(True, 8)
    actual = conv.bin_conversion(text)
    expected = [
        "0b00110000",
        "0b00110001",
        "0b00110010",
        "0b00110011",
        "0b00110100",
        "0b00110101",
        "0b01000001",
        "0b01000010",
    ]

    assert " ".join(expected) == actual


def test_bin_conversion_muti_byte():
    text = "0x3031"
    conv = helper(True, 8)
    actual = conv.bin_conversion(text)
    expected = "0b11000000110001"

    assert expected == actual


def test_dec_conversion_normal():
    text = "0x30 0x31 0x32 0x33 0x34 0x35 0x41 0x42"
    conv = helper()
    actual = conv.dec_conversion(text)
    expected = "48 49 50 51 52 53 65 66"

    assert expected == actual


def test_dec_conversion_multi_byte():
    text = "0x3031"
    conv = helper()
    actual = conv.dec_conversion(text)
    expected = "12337"

    assert expected == actual


def test_hex_conversion_normal():
    text = "0x30 0x31 0x32 0x33 0x34 0x35 0x41 0x42"
    conv = helper(True, 8)
    actual = conv.hex_conversion(text)
    expected = "0x30 0x31 0x32 0x33 0x34 0x35 0x41 0x42"

    assert expected == actual


def test_hex_conversion_multi_byte():
    text = "0x3031"
    conv = helper(True, 8)
    actual = conv.hex_conversion(text)
    expected = "0x3031"

    assert expected == actual


def test_oct_conversion_normal():
    text = "0x30 0x31 0x32 0x33 0x34 0x35 0x41 0x42"
    conv = helper(True, 3)
    actual = conv.oct_conversion(text)
    expected = "0o060 0o061 0o062 0o063 0o064 0o065 0o101 0o102"

    assert expected == actual


def test_oct_conversion_multi_byte():
    text = "0x3031"
    conv = helper(True, 5)
    actual = conv.oct_conversion(text)
    expected = "0o30061"

    assert expected == actual


def test_base64_conversion_normal():
    text = "0x30 0x31 0x32 0x33 0x34 0x35 0x41 0x42"
    conv = helper()
    actual = conv.base64_conversion(text)
    expected = "MDEyMzQ1QUI="

    assert expected == actual


def test_base32_conversion_normal():
    text = "0x30 0x31 0x32 0x33 0x34 0x35 0x41 0x42"
    conv = helper()
    actual = conv.base32_conversion(text)
    expected = "GAYTEMZUGVAUE==="

    assert expected == actual


def test_hex_to_hex():
    text = "0x30 0x31 0x32 0x33 0x34 0x35 0x41 0x42"
    conv = helper()
    actual = conv.hex_to_hex(text)
    expected = "0x30 0x31 0x32 0x33 0x34 0x35 0x41 0x42"

    assert expected == actual


def test_hex_to_hex_multi_byte():
    text = "0x3031"
    conv = helper()
    actual = conv.hex_to_hex(text)
    expected = "0x3031"

    assert expected == actual


def test_bin_to_hex():
    text = [
        "0b00110000",
        "0b00110001",
        "0b00110010",
        "0b00110011",
        "0b00110100",
        "0b00110101",
        "0b01000001",
        "0b01000010",
    ]
    conv = helper()
    actual = conv.bin_to_hex(" ".join(text)).strip()
    expected = "0x30 0x31 0x32 0x33 0x34 0x35 0x41 0x42"

    assert expected == actual


def test_bin_to_hex_multi_byte():
    text = "0b11000000110001"

    conv = helper()
    actual = conv.bin_to_hex(text).strip()
    expected = "0x3031"

    assert expected == actual


def test_dec_to_hex():
    text = "48 49 50 51 52 53 65 66"
    conv = helper()
    actual = conv.dec_to_hex(text).strip()
    expected = "0x30 0x31 0x32 0x33 0x34 0x35 0x41 0x42"

    assert expected == actual


def test_dec_to_hex_multi_byte():
    text = "12337"
    conv = helper()
    actual = conv.dec_to_hex(text).strip()
    expected = "0x3031"

    assert expected == actual


def test_oct_to_hex():
    text = "0o060 0o061 0o062 0o063 0o064 0o065 0o101 0o102"
    conv = helper()
    actual = conv.oct_to_hex(text).strip()
    expected = "0x30 0x31 0x32 0x33 0x34 0x35 0x41 0x42"

    assert expected == actual


def test_oct_to_hex_multi_byte():
    text = "0o30061"
    conv = helper()
    actual = conv.oct_to_hex(text).strip()
    expected = "0x3031"

    assert expected == actual


def test_base64_to_hex():
    text = "MDEyMzQ1QUI="
    conv = helper()
    actual = conv.base64_to_hex(text).strip()
    expected = "0x30 0x31 0x32 0x33 0x34 0x35 0x41 0x42"

    assert expected == actual


def test_base64_to_hex_bad_short():
    text = "a"
    conv = helper()
    actual = conv.base64_to_hex(text)
    expected = conversions.ERROR_INVALID

    assert expected == actual


def test_base32_to_hex_bad_short():
    text = "a"
    conv = helper()
    actual = conv.base32_to_hex(text)
    expected = conversions.ERROR_INVALID

    assert expected == actual


def test_base32_to_hex():
    text = "GAYTEMZUGVAUE==="
    conv = helper()
    actual = conv.base32_to_hex(text).strip()
    expected = "0x30 0x31 0x32 0x33 0x34 0x35 0x41 0x42"

    assert expected == actual


def test_input_to_hex_hex():
    text = "0x30 0x31 0x32 0x33 0x34 0x35 0x41 0x42"
    conv = helper()
    actual = conv.input_to_hex(text, conversions.HEX)
    expected = "0x30 0x31 0x32 0x33 0x34 0x35 0x41 0x42"

    assert expected == actual


def test_input_to_hex_hex_bad():
    text = "ZZ"
    conv = helper()
    actual = conv.input_to_hex(text, conversions.HEX)
    expected = conversions.ERROR_INVALID

    assert expected == actual


def test_input_to_hex_hex_bad_neg():
    text = "-0x1"
    conv = helper()
    actual = conv.input_to_hex(text, conversions.HEX)
    expected = conversions.ERROR_NEG

    assert expected == actual


def test_input_to_hex_bin():
    text = [
        "0b00110000",
        "0b00110001",
        "0b00110010",
        "0b00110011",
        "0b00110100",
        "0b00110101",
        "0b01000001",
        "0b01000010",
    ]
    conv = helper()
    actual = conv.input_to_hex(" ".join(text), conversions.BIN)
    expected = "0x30 0x31 0x32 0x33 0x34 0x35 0x41 0x42"

    assert expected == actual


def test_input_to_hex_bin_bad():
    text = "2"
    conv = helper()
    actual = conv.input_to_hex(text, conversions.BIN)
    expected = conversions.ERROR_INVALID

    assert expected == actual


def test_input_to_hex_bin_bad_neg():
    text = "-0b1"
    conv = helper()
    actual = conv.input_to_hex(text, conversions.BIN)
    expected = conversions.ERROR_NEG

    assert expected == actual


def test_input_to_hex_dec():
    text = "48 49 50 51 52 53 65 66"
    conv = helper()
    actual = conv.input_to_hex(text, conversions.DEC)
    expected = "0x30 0x31 0x32 0x33 0x34 0x35 0x41 0x42"

    assert expected == actual


def test_input_to_hex_dec_bad():
    text = "a"
    conv = helper()
    actual = conv.input_to_hex(text, conversions.DEC)
    expected = conversions.ERROR_INVALID

    assert expected == actual


def test_input_to_hex_dec_bad_neg():
    text = "-1"
    conv = helper()
    actual = conv.input_to_hex(text, conversions.DEC)
    expected = conversions.ERROR_NEG

    assert expected == actual


def test_input_to_hex_oct():
    text = "0o060 0o061 0o062 0o063 0o064 0o065 0o101 0o102"
    conv = helper()
    actual = conv.input_to_hex(text, conversions.OCT)
    expected = "0x30 0x31 0x32 0x33 0x34 0x35 0x41 0x42"

    assert expected == actual


def test_input_to_hex_oct_bad():
    text = "8"
    conv = helper()
    actual = conv.input_to_hex(text, conversions.OCT)
    expected = conversions.ERROR_INVALID

    assert expected == actual


def test_input_to_hex_oct_bad_neg():
    text = "-0o1"
    conv = helper()
    actual = conv.input_to_hex(text, conversions.OCT)
    expected = conversions.ERROR_NEG

    assert expected == actual


def test_input_to_hex_ascii():
    text = "012345AB"
    conv = helper()
    actual = conv.input_to_hex(text, conversions.ASCII)
    expected = "0x30 0x31 0x32 0x33 0x34 0x35 0x41 0x42"

    assert expected == actual


def test_input_to_hex_base64():
    text = "MDEyMzQ1QUI="
    conv = helper()
    expected = "0x30 0x31 0x32 0x33 0x34 0x35 0x41 0x42"
    actual = conv.input_to_hex(text, conversions.BASE64)

    assert expected == actual


def test_input_to_hex_base64_bad():
    text = "$$"
    conv = helper()
    actual = conv.input_to_hex(text, conversions.BASE64)
    expected = conversions.ERROR_INVALID

    assert expected == actual


def test_input_to_hex_base32():
    text = "GAYTEMZUGVAUE==="
    conv = helper()
    actual = conv.input_to_hex(text, conversions.BASE32)
    expected = "0x30 0x31 0x32 0x33 0x34 0x35 0x41 0x42"

    assert expected == actual


def test_input_to_hex_base32_bad():
    text = "a"
    conv = helper()
    actual = conv.input_to_hex(text, conversions.BASE32)
    expected = 0

    assert expected == actual
