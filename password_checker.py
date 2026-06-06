"""
Password Strength Checker — Beginner Cybersecurity Project
Run: python password_checker.py
"""

import re
import getpass

COMMON_PASSWORDS = [
    "password", "123456", "qwerty", "abc123", "letmein", "monkey",
    "dragon", "master", "iloveyou", "sunshine", "princess", "welcome",
    "shadow", "superman", "michael", "football", "baseball", "soccer",
    "hockey", "batman", "trustno1", "hello", "admin", "login", "pass",
    "test", "guest", "1234", "12345", "123456789", "000000"
]

def check_length(password):
    return len(password) >= 8, "At least 8 characters"

def check_long(password):
    return len(password) >= 12, "At least 12 characters (recommended)"

def check_uppercase(password):
    return bool(re.search(r"[A-Z]", password)), "Contains an uppercase letter"

def check_lowercase(password):
    return bool(re.search(r"[a-z]", password)), "Contains a lowercase letter"

def check_digit(password):
    return bool(re.search(r"\d", password)), "Contains a digit (0–9)"

def check_symbol(password):
    return bool(re.search(r"[^A-Za-z0-9]", password)), "Contains a symbol (!@#$…)"

def check_not_common(password):
    return password.lower() not in COMMON_PASSWORDS, "Not a commonly used password"

def check_no_repeats(password):
    return not bool(re.search(r"(.)\1{2,}", password)), "No character repeated 3+ times in a row"

RULES = [
    check_length,
    check_long,
    check_uppercase,
    check_lowercase,
    check_digit,
    check_symbol,
    check_not_common,
    check_no_repeats,
]

RESET  = "\033[0m"
BOLD   = "\033[1m"
RED    = "\033[91m"
YELLOW = "\033[93m"
GREEN  = "\033[92m"
CYAN   = "\033[96m"
GRAY   = "\033[90m"

def color_bar(score, total):
    filled = round((score / total) * 20)
    empty  = 20 - filled

    if score <= total * 0.3:
        col = RED
    elif score <= total * 0.6:
        col = YELLOW
    else:
        col = GREEN

    bar = col + "█" * filled + GRAY + "░" * empty + RESET
    return f"[{bar}] {score}/{total}"

def strength_label(score, total):
    ratio = score / total
    if ratio <= 0.3:
        return RED + "Very Weak" + RESET
    elif ratio <= 0.5:
        return RED + "Weak" + RESET
    elif ratio <= 0.7:
        return YELLOW + "Fair" + RESET
    elif ratio <= 0.87:
        return GREEN + "Good" + RESET
    else:
        return GREEN + BOLD + "Strong" + RESET

def analyze(password):
    results = [(fn(password)) for fn in RULES]
    passed  = [(ok, label) for ok, label in results if ok]
    failed  = [(ok, label) for ok, label in results if not ok]
    score   = len(passed)
    return score, len(RULES), results, failed

def print_results(password, score, total, results, failed):
    print()
    print(BOLD + "  Password Analysis" + RESET)
    print("  " + "─" * 36)

    # Checklist
    for ok, label in results:
        icon  = GREEN + "✔" + RESET if ok else RED + "✘" + RESET
        style = RESET if ok else GRAY
        print(f"  {icon}  {style}{label}{RESET}")

    print()

    # Bar + label
    print(f"  Strength : {strength_label(score, total)}")
    print(f"  Score    : {color_bar(score, total)}")

    charset = 0
    if re.search(r"[a-z]", password): charset += 26
    if re.search(r"[A-Z]", password): charset += 26
    if re.search(r"\d",    password): charset += 10
    if re.search(r"[^A-Za-z0-9]", password): charset += 32
    if charset > 0:
        import math
        bits = math.log2(charset) * len(password)
        print(f"  Entropy  : ~{bits:.0f} bits  {GRAY}(higher = harder to crack){RESET}")

    # Tips
    if failed:
        print()
        print(CYAN + "  💡 Tips to improve:" + RESET)
        tip_map = {
            "At least 8 characters":                   "Use at least 8 characters.",
            "At least 12 characters (recommended)":    "Aim for 12+ characters — length is the single biggest factor.",
            "Contains an uppercase letter":            "Add at least one uppercase letter (A–Z).",
            "Contains a lowercase letter":             "Add at least one lowercase letter (a–z).",
            "Contains a digit (0–9)":                  "Include at least one number.",
            "Contains a symbol (!@#$…)":               "Add a symbol like !, @, #, or $.",
            "Not a commonly used password":            "Avoid dictionary words — attackers test common passwords first.",
            "No character repeated 3+ times in a row": "Avoid patterns like 'aaa' or '111'.",
        }
        for _, label in failed:
            print(f"    {GRAY}→{RESET} {tip_map.get(label, label)}")

    print()
def main():
    print()
    print(BOLD + CYAN + "  🔐 Password Strength Checker" + RESET)
    print(GRAY + "  Beginner Cybersecurity Project\n" + RESET)
    print(GRAY + "  Type 'quit' to exit.\n" + RESET)

    while True:
        try:
            # Use getpass to hide input (like a real password prompt)
            password = getpass.getpass("  Enter password (hidden): ")
        except (KeyboardInterrupt, EOFError):
            print("\n\n  Goodbye!\n")
            break

        if password.lower() == "quit":
            print("\n  Goodbye!\n")
            break

        if not password:
            print(GRAY + "  (no input — try again)\n" + RESET)
            continue

        score, total, results, failed = analyze(password)
        print_results(password, score, total, results, failed)

        again = input("  Check another? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Goodbye!\n")
            break
        print()

if __name__ == "__main__":
    main()