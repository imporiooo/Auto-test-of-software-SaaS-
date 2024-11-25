import pytest
import user_code  # Импортируем модуль с пользовательским кодом


@pytest.mark.parametrize("input_data, expected_output", [
    (49, 7 ),
    (1, 1 ),
    (5, 1 ),
    (10, 1 ),
    (25, 1 ),
    (2111, 86 ),
    (4, 4 ),
    (100, 4 ),
    (499, 25 ),
    (9, 5 )

    
])
def test_fibonacci_num(input_data, expected_output):
    result = user_code.min_coin_amount(input_data)
    assert result == expected_output, f"{result}"
