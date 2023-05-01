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
