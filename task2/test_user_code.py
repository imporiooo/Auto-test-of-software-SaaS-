import pytest
import user_code  # Импортируем модуль с пользовательским кодом


@pytest.mark.parametrize("input_data, expected_output", [
    (5321, "YES"),
    (9876543210, "YES"),
    (987654329, "NO"),
    (12345, "NO"),
    (54332222221111, "YES"),
    (111111111, "YES"),
    (7820, "NO")
])
def test_ordered_num(input_data, expected_output):
    result = user_code.ordered_num(input_data)
    assert result == expected_output, f"{result}"
