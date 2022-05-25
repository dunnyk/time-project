import smtplib


smtplib

sender = "sender_email@gmail.com"
receiver = "destination_email@gmail.com"
password = "password"
subject = "Just for trial"
body = "Hello Dan kam, I am your future keep coding I will rewward you."

# header
message = f"""
    from: {sender}
    to: {receiver}
    subject: {subject}\n
    body: {body}

"""

# connect to server
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(sender, password)
    print(7 * "==>", "logged in server")

    server.sendmail(sender, receiver, message)
    print("email has been sent to destination")
except smtplib.SMTPAuthenticationError as error:
    print(error, "unable to sign in kindly check the problem")

finally:
    print("good signed in now")
