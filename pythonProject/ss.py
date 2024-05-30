import smtplib
import ssl
import json
from datetime import datetime


sender_email = "sendtestmsg@gmail.com"
password = "lqhw ejll hwsn bzoq"

with open("test.json", "r") as file:
    email_data_list = json.load(file)

current_date = datetime.now().strftime("%Y-%m-%d")

context = ssl.create_default_context()

for email_data in email_data_list:
    email_date = email_data.get("date")
    email_text = email_data.get("text")
    receiver_email = email_data.get("email")

    if email_date == current_date:
        subject = "Automatic Email"
        message = f"Subject: {subject}\n\n{email_text}"

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls(context=context)  # Secure the connection
                server.login(sender_email, password)  # Log in to the server
                server.sendmail(sender_email, receiver_email, message)  # Send the email
                print(f"Email sent to {receiver_email}")
        except smtplib.SMTPAuthenticationError:
            print("Failed to authenticate. Please check your email and password.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"The date in the JSON file ({email_date}) does not match today's date ({current_date}).")
