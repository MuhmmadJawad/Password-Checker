# 🔐 Password Strength Checker

A beginner-level cybersecurity project built in Python.  
Analyzes passwords in real time using a rules engine, entropy calculation, and a common-password blacklist — all from the standard library, no pip installs required.

---

## Project Structure

```
password_checker/
├── password_checker.py     ← Main CLI tool
├── common_passwords.txt    ← Blacklist of 10,000 common passwords
├── generator.py            ← Secure password generator
└── test_checker.py         ← Unit tests (20+ cases)
```

---

## Features

- ✔/✘ checklist for 8 security rules
- Colored progress bar showing overall strength
- Entropy calculation in bits (`log2(charset) × length`)
- Specific improvement tips for each failed rule
- Hidden input via `getpass` (like a real password prompt)
- Common password blacklist loaded from file at runtime
- Cryptographically secure password generator using `secrets`
- Full unit test suite runnable without external tools

---

## Requirements

- Python 3.6 or higher
- No external libraries — standard library only
s
## Usage

### Check a password

```bash
python password_checker.py
```

You will be prompted to enter a password (input is hidden).  
Type `quit` or press `Ctrl+C` to exit.

**Example output:**

```
  🔐 Password Strength Checker

  Enter password (hidden):

  Password Analysis
  ────────────────────────────────────
  ✔  At least 8 characters
  ✔  At least 12 characters (recommended)
  ✔  Contains an uppercase letter
  ✔  Contains a lowercase letter
  ✔  Contains a digit (0–9)
  ✔  Contains a symbol (!@#$…)
  ✔  Not a commonly used password
  ✘  No character repeated 3+ times in a row

  Strength : Good
  Score    : [████████████████░░░░] 7/8
  Entropy  : ~72 bits  (higher = harder to crack)

  💡 Tips to improve:
    → Avoid patterns like 'aaa' or '111'.
```

---

### Generate a secure password

```bash
python generator.py
```

**With options:**

```bash
python generator.py --length 20
python generator.py --length 16 --no-symbols
python generator.py --count 5
python generator.py --length 24 --no-digits --no-symbols
```

| Flag | Description | Default |
|---|---|---|
| `--length` | Password length | 16 |
| `--no-upper` | Exclude uppercase letters | off |
| `--no-lower` | Exclude lowercase letters | off |
| `--no-digits` | Exclude digits | off |
| `--no-symbols` | Exclude symbols | off |
| `--count` | Number of passwords to generate | 1 |

---

### Run tests

```bash
# Using unittest directly
python test_checker.py

# Using pytest (if installed)
python -m pytest test_checker.py -v
```

---

## Security Rules

| Rule | Description |
|---|---|
| Minimum length | At least 8 characters |
| Recommended length | At least 12 characters |
| Uppercase | Contains A–Z |
| Lowercase | Contains a–z |
| Digit | Contains 0–9 |
| Symbol | Contains `!@#$` etc. |
| Not common | Not in the top 10,000 common passwords |
| No repeats | No character repeated 3+ times in a row |

Strength is scored as passed rules / total rules:

| Score | Label |
|---|---|
| ≤ 30% | Very Weak |
| ≤ 50% | Weak |
| ≤ 70% | Fair |
| ≤ 87% | Good |
| > 87% | Strong |

---

## Entropy

Entropy is calculated as:

```
bits = log2(charset_size) × password_length
```

Where `charset_size` is the number of unique character types used:

| Characters used | Charset size |
|---|---|
| Lowercase only | 26 |
| + Uppercase | 52 |
| + Digits | 62 |
| + Symbols | 94 |

A password with 60+ bits of entropy is generally considered strong.

---

## Phase 5 Extensions (ideas to build next)

- **Have I Been Pwned API** — check if the password appeared in a real data breach using the `requests` library and SHA-1 k-anonymity
- **GUI version** — rebuild the tool with `tkinter` for a graphical interface
- **Save results to file** — log checked passwords (not the actual password, just the score) using Python file I/O
- **argparse CLI flags** — add `--json` output mode, `--verbose`, and `--quiet` flags to `password_checker.py`
- **Extended blacklist** — download the full rockyou.txt wordlist and load it as the blacklist

---

## Concepts Covered

- Regular expressions (`re` module)
- ANSI terminal colors (escape codes)
- Password entropy and information theory
- Cryptographic randomness (`secrets` module)
- Blacklist/set lookups for O(1) performance
- Unit testing with `unittest`
- CLI argument parsing with `argparse`

---

## License

MIT — free to use, modify, and share.