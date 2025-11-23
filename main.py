import tkinter as tk
from tkinter import messagebox
import re
import math

def calculate_entropy(password: str) -> float:
    charset = 0
    if re.search(r'[a-z]', password):
        charset += 26
    if re.search(r'[A-Z]', password):
        charset += 26
    if re.search(r'[0-9]', password):
        charset += 10
    if re.search(r'[^a-zA-Z0-9]', password):
        charset += 32

    if charset == 0:
        return 0

    return len(password) * math.log2(charset)


def check_strength(password: str) -> str:
    entropy = calculate_entropy(password)

    has_lower = bool(re.search(r'[a-z]', password))
    has_upper = bool(re.search(r'[A-Z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[^a-zA-Z0-9]', password))
    length_ok = len(password) >= 8

    score = sum([has_lower, has_upper, has_digit, has_special, length_ok, entropy >= 50])

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


def on_check():
    password = entry.get()
    strength = check_strength(password)
    entropy_value = calculate_entropy(password)

    result_label.config(text=f"Password Strength: {strength}")
    entropy_label.config(text=f"Entropy: {entropy_value:.2f} bits")


# GUI
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x250")
root.resizable(False, False)

title = tk.Label(root, text="Password Strength Checker", font=("Arial", 14))
title.pack(pady=10)

entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack(pady=10)

btn = tk.Button(root, text="Check Strength", command=on_check, width=20)
btn.pack(pady=10)

result_label = tk.Label(root, text="Password Strength:", font=("Arial", 12))
result_label.pack(pady=5)

entropy_label = tk.Label(root, text="Entropy:", font=("Arial", 12))
entropy_label.pack()

root.mainloop()
