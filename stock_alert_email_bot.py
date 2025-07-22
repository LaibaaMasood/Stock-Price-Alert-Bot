import yfinance as yf
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ======= CONFIGURATION =======

# Stocks to monitor and their price thresholds
STOCKS = {
    "NVDA": 170,   # Notify if NVIDIA drops below $110
    "TSLA": 334,
    "AAPL": 215
}

# Email credentials and recipient
import os

SENDER_EMAIL = os.getenv("EMAIL_USER")          # Replace with your Gmail
SENDER_PASSWORD = os.getenv("EMAIL_PASS")        # Use app password if 2FA is enabled
RECEIVER_EMAIL = os.getenv("EMAIL_TO")            # Can be the same or different



# ======= FUNCTIONS =======

def get_price(ticker):
    """Fetches the latest stock price from Yahoo Finance."""
    stock = yf.Ticker(ticker)
    price = stock.history(period="1d")["Close"].iloc[-1]
    return round(price, 2)

def send_email_alert(stock, price, threshold):
    """Sends an email alert when the stock price drops."""
    subject = f"🔔 Stock Alert: {stock} dropped to ${price}"
    body = f"{stock} has dropped to ${price}, below your threshold of ${threshold}."

    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        print(f"Email sent for {stock} at ${price}")
    except Exception as e:
        print(f"Failed to send email for {stock}. Error: {e}")

def check_stocks():
    """Checks all stocks and triggers alerts if needed."""
    for stock, threshold in STOCKS.items():
        try:
            price = get_price(stock)
            print(f"{stock} current price: ${price}")
            if price <= threshold:
                send_email_alert(stock, price, threshold)
        except Exception as e:
            print(f"Error checking {stock}: {e}")

# ======= ENTRY POINT =======

if __name__ == "__main__":
    check_stocks()
