import smtplib
import datetime as dt
import random
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

# Debug: confirm whether the env vars were actually picked up
print("EMAIL:", MY_EMAIL)
print("PASSWORD SET:", MY_PASSWORD is not None)

# 0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday,
# 4 = Friday, 5 = Saturday, 6 = Sunday
TARGET_DAY = 5

now = dt.datetime.now()
weekday = now.weekday()
if weekday == TARGET_DAY:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Monday Motivation\n\n{quote}".encode("utf-8")
        )
