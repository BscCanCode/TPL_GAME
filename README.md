# PyQuestEvolution - TPL Game (Beginner Edition) - April 2025

> "Not production-ready. Just me learning to code a fun game!"  
> — Sid.py

---

## 📌 About This Project
A Tambe Premiere League (TPL) game script, built in April 2025. It simulates a cricket-like match where the user selects a number (1-6), and an automated opponent chooses randomly, playing up to 6 rounds until the user is “out” (matching numbers) or the rounds are complete.

---

## Why I Built This
- To develop an interactive game to learn more about the working and functions of Python programming language.  
- To practice using loops, conditionals, and random number generation in Python.  
- To expand on skills from my password generator and OTP validator.

---

## 🚀 What It Does
- Takes user input: “play” or “exit” to start or quit the game.  
- In “play” mode:  
  - User enters a number between 1-6.  
  - Opponent’s number (1-6) is chosen randomly and displayed.  
  - If numbers match, the user is “out,” and the game ends.  
  - Otherwise, scores add the chosen numbers (e.g., user picks 4, opponent picks 2 → user +4, opponent +2).  
  - Runs for up to 6 rounds, showing scores and declaring a winner.  
- Validates inputs and handles non-integer errors.

---

## 🧠 What I Learned
- Implementing a `while` loop to limit the game to 6 rounds.  
- Using `random.choice()` to automate the opponent’s input.  
- Applying `try-except` to manage invalid input errors.

---

## 🔄 Updates
- ✅ Initial version with automated opponent and basic game mechanics.  

## Issues
-I know TPL is not perfect, but I am unaware of any issues. I'm open to any feedback.

---

## Author
- [Sid.py] ([https://github.com/BscCanCode](https://github.com/BscCanCode))

---

## Development Notes
- Built on 25 April 2025, inspired by a micro-internship idea for a game.  
- Uses Python’s `sys` and `random` modules (note: `string` is imported but unused, done by mistake).

---

## NOTE
- README with AI chatbot help.  
- Raw to show my learning journey—plan to refine.

---

### Copy-Paste Instructions
1. Copy the entire text above (from `# PyQuestEvolution - TPL Game` to the final `---`).
2. Go to `https://github.com/BscCanCode`, click "New" (or navigate to `PyQuestEvolution`).
3. Name the repo `tpl-game`, uncheck "Add README."
4. Upload `tpl_game.py`.
5. Create a new file named `README.md`, paste the text, and save.
6. Commit with:  
   `Add TPL Game Script - 25 April 2025`  
   Description: `Interactive game simulating a cricket-like match.

## Fact
- TPL (TAMBE Premier League) is inspired by ZPL (Zomato Premier League).
