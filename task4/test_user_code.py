import pytest
import user_code  # Импортируем модуль с пользовательским кодом


@pytest.mark.parametrize("input_data, expected_output", [
    ((1, 2, 1), -1.0 ),
    ((1, -7.5, 3), (0.4239663260874824, 7.076033673912518) ),
    ((-4, 12, -9), 1.5 ),
    ((1, 0, 0), 0 ),
    ((0.1, -1.5, 10), "No roots" ),
    ((0.1, -2, 0.999), (0.5126399878575283, 19.48736001214247) ),
    ((-5.64671390542564, 7.90460919676605, -2.10960556210672), (0.35889742396881147, 1.0409626236902196)),
    ((-7.10198466858238, 1.68832342688049, 9.61165416968306), (-1.050540545337323, 1.2882661256739383)),
])
def test_fibonacci_num(input_data, expected_output):
    result = user_code.quadratic_equation(*input_data)
    assert result == expected_output, f"{result}"
