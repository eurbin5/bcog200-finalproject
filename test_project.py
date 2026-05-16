import sys
import os


sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from analysis import (
    clean_response,
    get_sounds,
    get_sound_class
)


def test_clean_response():
    """Test response cleaning."""

    response = "  Ki-Ki  "

    cleaned = clean_response(response)

    assert cleaned == "kiki"


def test_get_sounds():
    """Test sound extraction."""

    response = "chiki"

    sounds = get_sounds(response)

    assert sounds == ["ch", "i", "k", "i"]


def test_get_sound_class():
    """Test sound classification."""

    sound = "k"

    sound_class = get_sound_class(sound)

    assert sound_class == "voiceless_stop"


test_clean_response()
test_get_sounds()
test_get_sound_class()

print("All tests passed!")