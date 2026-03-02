# logic_utils.py
from __future__ import annotations


def get_range_for_difficulty(difficulty: str) -> tuple[int, int]:
    # FIX: Refactored from app.py into logic_utils.py using Copilot Agent mode
    # to separate UI from game logic and make it testable.
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    # FIX: Moved parsing logic out of Streamlit UI layer with Copilot assistance
    # so input validation can be tested independently.
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    # FIX: Copilot originally preserved reversed hint logic.
    # After reviewing the diff, we corrected direction:
    # guess > secret -> Too High -> tell user to go LOWER
    # guess < secret -> Too Low  -> tell user to go HIGHER
    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        # FIX: Normalized types instead of relying on string comparison
        # (improves robustness discovered during review of Agent changes).
        try:
            g = int(guess)
            s = int(secret)
        except Exception:
            g = str(guess)
            s = str(secret)

        if g == s:
            return "Win", "🎉 Correct!"
        if g > s:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int) -> int:
    # FIX: Moved scoring logic into logic_utils.py using Copilot Agent
    # to isolate business rules from UI state.
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score