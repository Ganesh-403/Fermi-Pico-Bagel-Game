# Fermi Pico Bagel - Number Guessing Game

A fun and interactive number guessing game based on logic clues: **Fermi**, **Pico**, and **Bagel**. Play in **VS Code terminal or Google Colab**.

# How to Play  
- The program selects a **random 3-digit number** with **no duplicate digits**.  
- Your goal is to **guess the secret number** using the hints provided.  
- Enter a **3-digit number** as your guess.  
- The game will respond with clues:  
  - **"Fermi"** → A digit is correct and in the right position.  
  - **"Pico"** → A digit is correct but in the wrong position.  
  - **"Bagel"** → No digits are correct.  
- Keep guessing until you find the correct number!  
- Type **'q'** to **quit the game** at any time.  

# Requirements  
- Python 3.x  
- Works in **VS Code terminal & Google Colab**  

# How to Run  
1. Copy the Python script into a file (e.g., `fermi_pico_bagel.py`).  
2. Open a terminal and navigate to the file location.  
3. Run the game:  
   ```
   python fermi_pico_bagel.py
   ```
4. Follow the on-screen instructions to play!  


# Example Gameplay  
```
Welcome to Fermi Pico Bagel!
Try to guess the secret number. Type 'q' to quit at any time.
Enter your 3-digit guess (or 'q' to quit): 123
Pico Fermi
Enter your 3-digit guess (or 'q' to quit): 345
Bagel
Enter your 3-digit guess (or 'q' to quit): 567
Bagel
Enter your 3-digit guess (or 'q' to quit): 432
Fermi Pico
Enter your 3-digit guess (or 'q' to quit): 241
Fermi Fermi Fermi
You win!!
```

# Features  
- **Random Secret Number** – No two games are the same!  
- **User Input Validation** – Ensures correct length & no duplicate digits  
- **Clue System** – Get hints after each guess  
- **Quit Anytime** – Type `'q'` to exit the game  
- **Works in VS Code & Google Colab**  

# License  
This project is free to use for learning and personal projects.  

---
Enjoy playing **Fermi Pico Bagel**! 

