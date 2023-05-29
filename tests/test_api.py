import pytest
import api


@pytest.mark.parametrize("text_input,expected", [("MORSE", "-- --- .-. ... ."), ("morse", "-- --- .-. ... ."),
                                                 ("mOrSe", "-- --- .-. ... ."), ("JE SUIS UN MORSE", ".--- . / ... "
                                                                                                     "..- .. ... / "
                                                                                                     "..- -. / -- --- "
                                                                                                     ".-. ... .")])
def test_text_to_morse(text_input, expected):
    morse = api.text_to_morse(text_input)
    assert morse == expected


@pytest.mark.parametrize("morse_input,expected", [("-- --- .-. ... .", "MORSE"), (".. / .- -- / .- / -- --- .-. ... .",
                                                                                  "I AM A MORSE")])
def test_morse_to_text(morse_input, expected):
    paragraph = api.morse_to_text(morse_input)
    assert paragraph == expected


@pytest.mark.parametrize("split_input,expected", [("MORSE", ['--', '---', '.-.', '...', '.']),
                                                  ("morse", ['--', '---', '.-.', '...', '.']),
                                                  ("I AM A MORSE", ["..", "/", ".-", "--", "/", ".-", "/", "--", "---",
                                                                    ".-.", "...", "."])])
def test_split_morse(split_input, expected):
    """
    Cette fonction ne sert strictement à rien.
    :return: an assert
    """
    splited = api.split_morse("MORSE")
    assert splited == ['--', '---', '.-.', '...', '.']


@pytest.mark.parametrize("time_input,expected_time", [(0.2, 0.2), (0.3, 0.3), (-0.2, 0.2)])
def test_morse_time(time_input, expected_time):
    morse_time = api.MorseTime(time_input)
    assert morse_time.court == expected_time
    assert morse_time.long == expected_time * 3
    assert morse_time.space == expected_time * 7
    assert morse_time.very_short == expected_time / 2


@pytest.mark.parametrize("time, expected_symbol", [([], ""), ([400000000, 200000000, 2600001000, 436589984, 965485201], ".. / .-"), ([2600001000], " / ")])
def test_convert_button_time(time, expected_symbol):
    converter = api.convert_button_time(time)
    assert converter == expected_symbol


@pytest.mark.parametrize("time_error_values, expected", [(["a", "b", "c"], TypeError), ([1000000, "a"], TypeError), ([1000000, 1, 9000000], ValueError)])
def test_convert_button_time_with_error(time_error_values, expected):
    with pytest.raises(expected):
        api.convert_button_time(time_error_values)


def test_is_morse():
    is_morse = api.is_morse("-- ... / // //// / à adf -")
    assert is_morse is False
