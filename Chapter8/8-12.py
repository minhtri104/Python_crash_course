def make_sandwich(*items):
    """Summarize the sandwich being ordered."""
    for item in items:
        print("- " + item)


print("\nMaking a sandwich with:")
make_sandwich("thịt")
make_sandwich("thịt", "phô mai")
make_sandwich("thịt", "phô mai", "rau")
