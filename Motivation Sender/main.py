import smtplib
import datetime as dt
import random

now = dt.datetime.now()
day_of_week = now.weekday()

with open("./Motivation Sender/quotes.txt") as file:
    quotes = file.readlines()
    quote_to_send = random.choice(quotes).strip()

my_email = "mymail@example.com"
password = "mypass"

if day_of_week == 0:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="anothermail@example.com",
            msg="Subject:Monday Motivation\n"
            "To:anothermail@example.com\n"
            "From:mymail@example.com\n\n"
            f"{quote_to_send}"
        )
