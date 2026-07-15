import datetime as dt
import smtplib
import random
import glob
import pandas as pd


##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now=dt.datetime.now()
day=now.day
month=now.month

df=pd.read_csv("birthdays.csv")

matches=df[(df["day"]==day) & (df["month"]==month)]
txt_files = glob.glob("letter_templates/*.txt")
my_email="davidgonroj2000@gmail.com"


old_word="[NAME]"

# with open("birthdays.csv") as file:
#     todays_bithday=[user for user,birthday in csv.reader(file) if birthday==current_day]
#


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if not matches.empty:
     emails=matches.to_dict(orient='records')
     for person in emails:
          # print(person["email"])
          # Find all text files in the current directory

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
               connection.login(user=my_email, password="mmmo tvxi gksw gclo")
               connection.sendmail(from_addr=my_email,
                                   to_addrs=person["email"],
                                   msg=f"Subject:Happy Birthday\n\n{result}")

else:
     print("No matching days found")
# 4. Send the letter generated in step 3 to that person's email address.


