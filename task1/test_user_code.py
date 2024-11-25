import pytest
import user_code  # Импортируем модуль с пользовательским кодом


@pytest.mark.parametrize("input_data, expected_output", [
    ((14, 5), 19),
    ((4, 6), 10)
])
def test_add_function(input_data, expected_output):
    result = user_code.add(*input_data)
    assert result == expected_output, f"Ожидалось {expected_output}, но получили {result}"
