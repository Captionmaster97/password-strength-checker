import re

print("=" * 45)
print("      PASSWORD STRENGTH CHECKER")
print("=" * 45)

password = input("Enter Password: ")

score = 0

if len(password) >= 8:
    score += 1

if re.search(r"[A-Z]", password):
    score += 1

if re.search(r"[a-z]", password):
    score += 1

if re.search(r"\d", password):
    score += 1

if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1

print("\nPassword Analysis")
print("-" * 30)

print("Length:", "✔" if len(password) >= 8 else "✘")
print("Uppercase:", "✔" if re.search(r"[A-Z]", password) else "✘")
print("Lowercase:", "✔" if re.search(r"[a-z]", password) else "✘")
print("Numbers:", "✔" if re.search(r"\d", password) else "✘")
print("Special Characters:", "✔" if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) else "✘")

print()

if score <= 2:
    print("Password Strength : Weak")
elif score == 3 or score == 4:
    print("Password Strength : Moderate")
else:
    print("Password Strength : Strong")
