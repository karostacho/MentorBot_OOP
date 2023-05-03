from displayer import Displayer
import datetime

class Logger:
    def __init__(self):
        self.displayer = Displayer()
        self.errors = []

    def display_error_message(self,  message = "Something went wrong"):
        self.displayer.display(message)

    def log_error(self, error, message):
        self.log(error)
        self.displayer.display(message)

    def log_message(self, message):
        self.log(message)

    def log(self, log):
        file = open("log.txt", "a")
        self.errors.append(log)
        for log in self.errors:
            file.write(str(f'\n{datetime.datetime.now()} {log}'))
        file.close()
