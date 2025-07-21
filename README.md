# sudoku_solver
A Python-based Sudoku Solver that uses backtracking to find the solution for any 9x9 Sudoku puzzle. Enter your puzzle and get the solved version in seconds!

📌 Features
Solves any valid 9x9 Sudoku puzzle
Uses backtracking algorithm
Easy-to-read terminal output
Simple and beginner-friendly codebase

🛠️ How It Works
The solver uses a recursive backtracking algorithm that:
Finds an empty cell
Tries all digits (1–9)
Checks if the digit is safe (no duplicates in row, column, or 3x3 box)
Fills in the digit and recursively attempts to solve the rest
If stuck, it backtracks and tries another number
