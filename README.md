# Python Assignment #3

## Hangman.py Code Enhancements

### ✅ **Adding Levels of Easiness**

The game allows for **8 trials (eight lives)** before the user loses. Initially, there was only one set of secret words (animals: ant, baboon, badger, bat, bear, beaver, camel, cat, clam, cobra). This project adds **three more sets**:

- **Shapes:** square, triangle, rectangle, circle, ellipse, rhombus, trapezoid  
- **Places:** Cairo, London, Paris, Baghdad, Istanbul, Riyadh

#### **Levels:**

- **Easy:** User selects the set (Animal, Shape, Place). Lives: **8**.
- **Moderate:** User selects the set (Animal, Shape, Place). Lives: **6**. Last two graphics not displayed.
- **Hard:** Random set and word chosen. No clue shown. Lives: **6**.

---

### ✅ **Adding Tracking of Winners and Records**

Uses **SQLite** to track the highest record (number of remaining lives) for each level. Database stores:

- **Player Name** (input by user)
- **Level** (Easy, Moderate, Hard)
- **Remaining Lives**

Hall of Fame updates when a new record is achieved.

#### **Sample Hall of Fame**

| Level    | Winner Name | Remaining Lives |
|----------|-------------|-----------------|
| Easy     | John        | 6               |
| Moderate | Nancy       | 5               |
| Hard     | Ahmed       | 3               |

---

### ✅ **Menus**

On running the code:

1. Asks for **player name**
2. Displays **introductory menu**:

Hi “player name”.
Welcome to HANGMAN

Play Easy Level

Play Moderate Level

Play Hard Level

View Hall of Fame

About the Game

Exit

 If Easy or Moderate level is chosen, prompts:

Choose a set of secret words:

Animal

Shape

Place


4. **About the Game:** Explains instructions, levels, and Hall of Fame details.

---

### 📌 **Note**

Menus are formatted using **Table libraries** for clarity and professional presentation.

---

> **Submission by:** Devraj Bavan  
> **Course:** Python Programming Assignment #3  
> **Topic:** Advanced Hangman Game with Levels, Database Tracking, and Structured Menus

