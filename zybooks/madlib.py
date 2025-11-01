"""Zybooks Mad Lib exercise (interactive only).

This version uses only interactive prompts (four separate calls to
`input()`) and does not read or parse piped input or multi-token stdin.
That keeps the exercise focused on `input()` and simple validation.

Prompts (in order): first name, whole number, plural noun, generic location.
"""



def main() -> None:
    # Interactive prompts only (one per input). This makes the exercise
    # straightforward for learners who are just practicing `input()`.
    first_name = input("Enter a first name: ")

    # Prompt for whole number and validate immediately. If invalid,
    # reprompt until the user provides an integer.
    while True:
        whole_number_s = input("Enter a whole number: ")
        try:
            whole_number = int(whole_number_s)
            break
        except ValueError:
            # Show exactly what the user entered (including whitespace)
            print(f"Invalid input: you entered {whole_number_s!r}. Please try again.")

    plural_noun = input("Enter a plural noun: ")
    generic_location = input("Enter a generic location: ")

    print(
        first_name,
        "buys",
        whole_number,
        "different types of",
        plural_noun,
        "at",
        generic_location,
    )


if __name__ == "__main__":
    main()
