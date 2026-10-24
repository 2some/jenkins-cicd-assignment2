def greet(name):
    """Return a greeting for the supplied name."""
    if not name or not name.strip():
        raise ValueError("Name cannot be empty")

    return f"Hello, {name.strip()}!"


def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b


if __name__ == "__main__":
    print(greet("DevOps Learner"))
    print(f"Build check: 2 + 3 = {add_numbers(2, 3)}")