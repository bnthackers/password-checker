# 🔐 Secure Password Checker (Command-Line Tool)

![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A simple, fast, and secure command-line tool to check password strength and detect if a password has been exposed in a data breach.

---

## 📖 Description

This project provides a script to analyze password security directly from your terminal. It helps users make informed decisions about their credentials by providing two key pieces of information:

1.  **Password Strength:** Analyzes the password based on common complexity criteria (length, character types).
2.  **Data Breach Check:** Securely checks the password against the 'Have I Been Pwned' database using the **k-Anonymity** model. This ensures the user's password is never sent to any external server.

---

## ✨ Features

- **Instant Feedback:** Get immediate analysis of password strength and leak status.
- **Secure by Design:** Uses the k-Anonymity model to protect user privacy during the breach check.
- **Lightweight & Fast:** Runs directly in your terminal with no GUI overhead.
- **Informative Reports:** Clear and concise output for both strong and weak passwords.

---

## 🛠️ Technology Stack

- **Language:** Python
- **Core Libraries:** `requests`, `hashlib`

---

## ⚙️ Setup and Installation

To get a local copy up and running, follow these simple steps.

### Prerequisites
- Python 3.9+
- Git

### Installation

1. **Clone the repository:**
   ```sh
   git clone [https://github.com/](https://github.com/)
   cd password_checker
