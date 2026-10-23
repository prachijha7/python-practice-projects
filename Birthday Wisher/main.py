import pandas, datetime as dt, smtplib, random

my_email = "yourmail@example.com"
password = "yourpass"

data = pandas.read_csv("./Birthday Wisher/birthdays.csv")
now = dt.datetime.now()
today = (now.month, now.day)

birthdays_dict = {(row["month"], row["day"]):row for (index, row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    birthday_person_name = birthday_person["name"]
    birthday_person_email = birthday_person["email"]
    number = random.randint(1,3)

    with open(f"./Birthday Wisher/letter_templates/letter_{number}.txt") as letter:
        letter_data = letter.read()
        letter_data = letter_data.replace("[NAME]", birthday_person_name)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person_email,
            msg=f"Subject:Happy Birthday {birthday_person_name}!\n"
                f"To:{birthday_person_email}\n"
                f"From:{my_email}\n\n"
                f"{letter_data}"
            )

