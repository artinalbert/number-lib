from number_lib.conversions import binary_to_octal


def test_binary_to_octal():
    assert binary_to_octal("111") == "7"
    assert binary_to_octal("1111") == "17"
