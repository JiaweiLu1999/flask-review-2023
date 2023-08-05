from configparser import ConfigParser
import smtplib

configs = ConfigParser()
configs.read("email.config")

sender = configs["info"]["user"]
password = configs["info"]["password"]
receiver = "jl5999@columbia.edu"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(sender, password)
    connection.sendmail(from_addr=sender,
                        to_addrs=receiver,
                        msg="Subject:Hello!\n\nThis is the smtp test message.")


