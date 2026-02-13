# Advance Python Leap Year Calculator

A robust Python-based utility designed to determine leap years using precise Gregorian calendar logic. This tool doesn't just check the date; it also calculates the century and provides the Roman numeral conversion for the input year.

**Repository:** [https://github.com/muazify/practice_leap_year_calculator.git](https://github.com/muazify/practice_leap_year_calculator.git)

---

## 📜 Description

This project serves as a practical implementation of conditional logic and external library integration in Python. It provides a continuous loop interface where users can input any year to receive instant astronomical and historical data. By leveraging the `roman` library, it bridges the gap between modern computing and classical notation.

## ✨ Features

* **Leap Year Validation:** Uses the standard leap year algorithm to ensure 100% accuracy.
* **Century Identification:** Automatically calculates the ordinal century (e.g., 2024 → 21st Century).
* **Roman Numeral Conversion:** Integrates the `roman` package to transform integers into Roman numerals.
* **Error Handling:** Robust `try-except` blocks to manage non-integer inputs gracefully.
* **Continuous Loop:** Stay in the program to check multiple years without restarting; exit anytime by typing "exit".

## 🚀 How to Use

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/muazify/practice_leap_year_calculator.git
    cd practice_leap_year_calculator
    ```

2.  **Install Dependencies:**
    This tool requires the `roman` library.
    ```bash
    pip install roman
    ```

3.  **Run the Script:**
    ```bash
    python leap_year_calculator.py
    ```

4.  **Input:**
    Enter a year (e.g., `2024`) or type `exit` to close the program.

---

## 🧪 Logic & Math

The tool determines a leap year based on the following mathematical criteria:

1.  The year must be evenly divisible by 4.
2.  If the year is divisible by 100, it must also be divisible by 400 to be a leap year.

The logic is expressed in the code as:

$$Year \pmod{400} = 0 \lor (Year \pmod{4} = 0 \land Year \pmod{100} \neq 0)$$

To calculate the century (Here used 'Right Floor' which means taking the intiger part only):

$$\text{Century} = \lfloor \frac{Year + 99}{100} \rfloor$$

---

## 🤝 Contributing

As an aspiring developer and **SSC '27** candidate, I welcome all feedback! If you have suggestions for new features (like adding the Chinese Zodiac or Day of the Week), feel free to:

* Fork the repo.
* Submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
