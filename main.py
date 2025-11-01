"""Simple Task Manager CLI (Step 1)

This file demonstrates a minimal command-line menu for a Task Manager.
It uses an in-memory list to store tasks and implements three simple
options: Add Task, View Tasks, and Exit.

The purpose is educational: each key line has an inline comment that
explains what it does (for example, the `while True:` loop and how
`input()` controls program flow).
"""

# In-memory storage for tasks (list lives only while program runs)
tasks = []


def print_menu() -> None:
    """Print the menu options to the console."""
    print("\n=== Task Manager ===")
    print("1) Add Task")
    print("2) View Tasks")
    print("3) Exit")


if __name__ == "__main__":
    # `while True:` creates an infinite loop. We use `break` to exit it.
    # This pattern is common for CLI menus because it keeps showing the
    # menu until the user explicitly chooses to quit.
    while True:
        print_menu()

        # `input()` waits for the user to type something and press Enter.
        # We call `.strip()` to remove accidental leading/trailing spaces.
        choice = input("Enter your choice (1-3): ").strip()

        # The menu options are controlled by checking the user's input.
        # Each branch handles one option; an invalid input falls through
        # to the `else` message and the loop repeats.
        if choice == "1":
            # Add Task: ask the user for a description and append it.
            task = input("Enter task description: ").strip()
            if task:
                tasks.append(task)  # `.append()` adds the item to the list
                print(f"Task added: {task}")
            else:
                print("No text entered. Task not added.")

        elif choice == "2":
            # View Tasks: show tasks stored in the `tasks` list.
            if not tasks:
                print("No tasks yet. Use option 1 to add a task.")
            else:
                print("\nYour tasks:")
                # enumerate(..., 1) shows a 1-based index for readability
                for idx, t in enumerate(tasks, 1):
                    print(f"{idx}. {t}")

        elif choice == "3":
            # Exit: break out of the loop which ends the program.
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            # Invalid input handling keeps the loop robust.
            # Show the raw value received so it's clear why the choice
            # was rejected (useful for debugging when special chars
            # like '/' are entered).
            print(f"Invalid choice: {choice!r}. Please enter 1, 2, or 3.")
