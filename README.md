# SQL Injection Vulnerability Lab 🚀

## 📌 Overview
This project demonstrates **SQL Injection vulnerabilities** and how to **fix them** using secure coding practices. It is meant for **educational purposes only** to help ethical hackers and developers understand security risks.

## 📂 Project Structure
- `vulnerable-version/` → An **insecure** PHP login page vulnerable to SQL Injection.
- `secure-version/` → The **fixed** version using **prepared statements**.
- `db.sql` → MySQL database script for easy setup.

## 🚀 Getting Started

### 1️⃣ Install Apache, PHP, and MySQL (on Kali Linux)
```bash
sudo apt update && sudo apt install apache2 php mariadb-server libapache2-mod-php -y
