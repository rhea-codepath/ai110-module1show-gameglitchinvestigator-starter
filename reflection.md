# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

Hints were backwards.
I expected the game to tell me to guess lower when I was too high and higher when I was too low. Instead, it flipped the directions (e.g., “Too High” but “Go HIGHER!”), which made it impossible to logically narrow down the number.

Difficulty didn’t match the range shown.
I expected the number range to change consistently based on Easy/Normal/Hard. But the main UI always said “Guess a number between 1 and 100,” even when the difficulty range was different.

New Game didn’t fully reset correctly.
I expected “New Game” to reset everything and generate a number within the selected difficulty. Instead, it always picked 1–100 and didn’t fully reset attempts and state consistently.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used GitHub Copilot (including Agent mode) to help refactor logic and identify bugs in the game.

One example of a correct AI suggestion was when Copilot helped refactor the game logic (check_guess, parse_guess, etc.) out of app.py into logic_utils.py. It preserved the function structure and made the logic independently testable, which aligned with the project goal of separating UI from business logic. I verified this by running pytest after the refactor and confirming that the logic worked without relying on Streamlit state.

One example of an incorrect or misleading AI suggestion was when Copilot initially preserved the reversed hint logic in check_guess. The code still returned "Go HIGHER!" when the guess was too high. After reviewing the diff manually and running targeted pytest cases, I realized the direction was still wrong and corrected it so that "Too High" now tells the user to go lower (and vice versa). This reinforced that even when AI refactors code correctly structurally, the logic still needs careful human review.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was truly fixed only after verifying both behavior in the UI and behavior in isolated logic tests. For example, after fixing the reversed hint bug, I didn’t just rely on the game “feeling right” — I confirmed that the output of check_guess matched the expected outcome and message.

One test I ran using pytest specifically targeted the reversed hint bug. I wrote a regression test that checked that when the guess is higher than the secret, the outcome is "Too High" and the message contains "LOWER" (and not "HIGHER"). Before the fix, this test would have failed because the message directions were flipped. After correcting the logic, the test passed, which confirmed that the bug was actually resolved at the logic level.

AI helped me design the regression test by suggesting that I assert on both the outcome and the message content, not just the outcome string. That pushed me to think about testing behavior more precisely. However, I still had to review and adjust the tests to match the actual return type of check_guess (a tuple), which reinforced that tests also need human verification.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
