# 📈 Stock Price Alert Bot (AI Agent with Email Notifications)

This is a lightweight Python-based AI agent that automatically monitors selected stock prices (e.g., NVIDIA, Tesla, Apple) and sends you an **email alert** when they drop below your defined thresholds.

It runs **fully in the cloud using GitHub Actions**, so you don’t need to keep your laptop on. No paid APIs, no server hosting, no nonsense — just free and reliable automation.

---

## 💡 Features

- 🔔 Sends **email alerts** when a stock drops below your target price
- 📈 Monitors any stock available on **Yahoo Finance**
- ☁️ Runs every 5 hours using **GitHub Actions** (no manual effort!)
- 🔐 Stores Gmail credentials safely via **GitHub Secrets**
- 🧩 Easily customizable: add more stocks, change thresholds, tweak logic

---

## 📦 Requirements

No need to install anything locally! But if you want to run the bot manually:

```bash
pip install yfinance
