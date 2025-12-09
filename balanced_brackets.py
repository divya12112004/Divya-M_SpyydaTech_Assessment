# Balanced Brackets Validator Program

def is_balanced(brackets):
    stack = []

    # Dictionary to store matching pairs
    pairs = {')': '(', '}': '{', ']': '['}

    for char in brackets:
        # If it's an opening bracket, push to stack
        if char in "({[":
            stack.append(char)

        # If it's a closing bracket, check stack
        elif char in ")}]":
            if not stack:  # Empty stack → no match
                return False

            top = stack.pop()

            if pairs[char] != top:  # Mismatch
                return False

    # If stack empty → fully matched
    return len(stack) == 0


def main():
    text = input("Enter a bracket string: ")

    if is_balanced(text):
        print("Balanced : True")
    else:
        print("Balanced : False")


if __name__ == "__main__":
    main()
