from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_guess_too_high_message():
    # Bug fix: when guess is too high, hint message should say Go LOWER (not Go HIGHER)
    _, message = check_guess(60, 50)
    assert "LOWER" in message, f"Expected hint to say LOWER, got: {message}"

def test_guess_too_low_message():
    # Bug fix: when guess is too low, hint message should say Go HIGHER (not Go LOWER)
    _, message = check_guess(40, 50)
    assert "HIGHER" in message, f"Expected hint to say HIGHER, got: {message}"
