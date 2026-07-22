import datetime as dt
import smtplib
import random
import glob
import pandas as pd
import os

now=dt.datetime.now()
day=now.day
month=now.month

df=pd.read_csv("birthdays.csv")

matches=df[(df["day"]==day) & (df["month"]==month)]
txt_files = glob.glob("letter_templates/*.txt")
my_email=os.environ.get("MY_EMAIL")
my_password=os.environ.get("MY_PASSWORD")
old_word="[NAME]"

if not matches.empty:
     birthday_people=matches.to_dict(orient='records')
     for person in birthday_people:
          # Select one file completely at random
          random_file = random.choice(txt_files)
          modified_lines=[]
          with open(random_file,"r") as file:
               letter=file.readlines()

          for line in letter:
               modified_lines.append(line.replace(old_word,person["name"]))
          result="".join(modified_lines)
          with smtplib.SMTP("smtp.gmail.com", 587) as connection:
               connection.starttls()
               connection.login(user=my_email, password=my_password)
               connection.sendmail(from_addr=my_email,
                                   to_addrs=person["email"],
                                   msg=f"Subject:Happy Birthday\n\n{result}")

else:
     print("No matching days found")



