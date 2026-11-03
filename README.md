# Expense Tracker 💰

## Project Description

Expense Tracker is a simple GUI-based application developed using Python. It helps users manage and track their daily expenses easily.

The application allows users to add expenses, view expense records, delete selected expenses, and calculate the total amount spent.

It uses Tkinter for the graphical user interface and SQLite for storing expense records in a database.

## Features

- Add new expenses.
- Enter expense name, amount, category, and date.
- View all expense records in a table.
- Delete selected expenses.
- Calculate the total expense automatically.
- Validate user input.
- Store expense records permanently using SQLite.
- Automatically displays the current date.

## Technologies Used

- **Python** – Main programming language.
- **Tkinter** – Graphical User Interface (GUI).
- **SQLite** – Database management.
- **ttk** – Table and dropdown widgets.

## Categories

The application provides the following expense categories:

1. Food
2. Travel
3. Shopping
4. Education
5. Other

## Sample Output

**Application Window:**

```text
             EXPENSE TRACKER

Expense Name:       Food
Amount (Rs.):       200
Category:           Food
Date:               2026-11-03

[ Add Expense ] [ Delete Expense ] [ Clear Fields ]


ID    Expense Name    Amount (Rs.)    Category    Date
---------------------------------------------------------
1     Food            200.00          Food        2026-11-03
2     Bus Ticket      50.00           Travel      2026-11-03
3     Books           300.00          Education   2026-11-03


        Total Expense: Rs. 550.00
```

*Note: This is an illustrative sample output. The actual application displays a graphical window.*

## How to Run the Project

1. Install Python on your computer.
2. Open the project folder.
3. Open the terminal or command prompt.
4. Run the following command:

```bash
python expense_tracker.py
```

5. The Expense Tracker application window will open.
6. Enter expense details and click the Add Expense button.

## Database

The application uses SQLite to store expense records.

A database file named `expenses.db` is automatically created when the program runs for the first time.

## Conclusion

This project provides a simple and user-friendly way to manage daily expenses. It also demonstrates the practical use of Python GUI programming, database connectivity, and CRUD operations.

Sample Screenshoot

<img width="1065" height="787" alt="Screenshot 2026-11-03 020019" src="https://github.com/user-attachments/assets/746aa767-a086-4bd9-aba4-6cf6added6d7" />
<img width="1052" height="770" alt="Screenshot 2026-11-03 020105" src="https://github.com/user-attachments/assets/5da3aefb-07ca-462b-9d33-1d0102ec8bd3" />
