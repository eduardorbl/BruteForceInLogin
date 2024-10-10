# 🛠️ Simple Brute Force Attack Simulation on a Vulnerable Login System

Welcome to my small project! 🙌 This repository demonstrates a basic brute force attack on a vulnerable login system using Python and Flask. The goal here is to showcase the basics of cybersecurity, specifically how brute force attacks work, while also focusing on learning and improving defenses.

## 🔍 What is this about?

This project is a learning exercise where I created a fictional login page vulnerable to brute force attacks. The purpose is to simulate how an attacker could exploit this type of vulnerability, and how we, as developers, can learn from it to build better security measures. 

**Note**: This project is purely for educational purposes and should only be used in a controlled environment.

## ⚙️ How does it work?

The application is built with:
- **Flask** to create a simple web server with a vulnerable login page.
- **SQLite** for a small user database.
- **Python** to perform the brute force attack by trying different password combinations until the correct one is found.

I’ve also written a script that simulates the brute force attack by systematically attempting to guess the password. It's a basic approach but effective for educational purposes.

## 🚀 How to run it?

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask server:
    ```bash
    python app.py
    ```

4. In a separate terminal, run the brute force script:
    ```bash
    python brute_force.py
    ```

5. Watch the script attempt to crack the password (don't worry, it's all for learning! 😉).

## 🛡️ What can we learn from this?

While this project demonstrates a brute force attack, the real takeaway is understanding **why brute force attacks work** and **how to protect against them**. Here are a few ways to strengthen login security:
- Limit the number of login attempts.
- Use CAPTCHA to prevent bots from repeatedly trying passwords.
- Implement strong password hashing (e.g., bcrypt, Argon2).
- Encourage users to use strong, complex passwords.

## 🌱 What's next?

This is just a starting point for my learning in cybersecurity and web development. I plan to:
- Add more layers of defense to the login system.
- Explore other attack types like SQL injection and XSS.
- Implement proper logging and monitoring of login attempts.

## 🤗 A humble note

I’m still learning and growing as a developer, and I welcome any feedback, suggestions, or ideas you might have! If you find any issues or areas where I can improve, feel free to open an issue or send a pull request.

Thank you for taking the time to check out my project! 🙏

---

### Let's connect!
[LinkedIn](https://www.linkedin.com/in/jos%C3%A9-eduardo-santos-rabelo-296239234/)
