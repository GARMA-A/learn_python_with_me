import datetime as dt

now  = dt.datetime.now()
print(now)

print(now.year)
print(now.month)

# i dont realy know the hour and minute 😅
date_of_birth = dt.datetime(year=2004 , month=4 , day=21 , hour=4 , minute=12)
print(date_of_birth) # 2004-04-21 04:12:00
# --------------------------------------------
# Send email 
# import smtplib 
# import random

# now = dt.datetime.now()
# with open('quotes.txt') as quote_file:
#        all_quotes = quote_file.readlines()
#        quote = random.choice(all_quotes)
# print(quote)

# connection = smtplib.SMTP("")


#To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


# from datetime import datetime
# import pandas
import random
# import smtplib

# MY_EMAIL = "gitgisemad74@gmail.com"
# MY_PASSWORD = "girgis2004"

# # today = datetime.now()
# # today_tuple = (today.month, today.day)

# # data = pandas.read_csv("birthdays.csv")
# # birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# # if today_tuple in birthdays_dict:
# #     birthday_person = birthdays_dict[today_tuple]
# #     file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
# #     with open(file_path) as letter_file:
# #         contents = letter_file.read()
# #         contents = contents.replace("[NAME]", birthday_person["name"])

with open("quotes.txt") as quote_file:
       content = quote_file.readlines()

# with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs="gemad9663@gmail.com",
#             msg=f"MSg From Python\n\n{random.choice(content)}"
#         )
        
        
        
 # Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage


msg = EmailMessage()
msg.set_content(random.choice(content))

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = random.choice(content)
msg['From'] = "girgisemad74@gmail.com"
msg['To'] = "gemad9663@gmail.com"

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()


       







