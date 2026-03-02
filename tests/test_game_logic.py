from logic_utils import check_guess


def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    # This specifically ensures the bug is fixed:
    # Too High must tell user to go LOWER.
    assert "LOWER" in message


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    # Too Low must tell user to go HIGHER.
    assert "HIGHER" in message


# 🔎 NEW TEST — directly targets the original reversed hint bug
def test_hint_direction_is_correct():
    """
    Regression test for the original bug where:
    - Too High incorrectly said 'Go HIGHER'
    - Too Low incorrectly said 'Go LOWER'
    """

    high_outcome, high_message = check_guess(80, 50)
    low_outcome, low_message = check_guess(20, 50)

    assert high_outcome == "Too High"
    assert "LOWER" in high_message
    assert "HIGHER" not in high_message

    assert low_outcome == "Too Low"
    assert "HIGHER" in low_message
    assert "LOWER" not in low_message