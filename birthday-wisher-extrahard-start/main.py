##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import pandas as pd
import datetime as dt
import random
from configparser import ConfigParser

df = pd.read_csv("birthdays.csv")
time_now = dt.datetime.now()
month = time_now.month
day = time_now.day

configparser = ConfigParser()
configparser.read("../smtp-email/email.config")
sender = configparser["info"]["user"]
password = configparser["info"]["password"]


for index, row in df.iterrows():
    birth_month = int(row["month"])
    birth_day = int(row["day"])
    if birth_day == day and birth_month == month:
        template_letter_id = random.randint(1, 3)
        with open(f"letter_templates/letter_{template_letter_id}.txt") as letter_template:
            letter_text = letter_template.read()
            letter_text = letter_text.replace("[NAME]", row["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(sender, password)
            connection.sendmail(
                from_addr=sender,
                to_addrs=row["email"],
                msg="Subject:Happy Birthday!\n\n" + letter_text
            )


