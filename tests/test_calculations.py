from number_lib.calculations import product_of_even_numbers


def test_product_of_even_numbers():
    assert product_of_even_numbers(6) == 48
    assert product_of_even_numbers(5) == 8