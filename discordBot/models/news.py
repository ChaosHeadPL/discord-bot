from datetime import datetime
# from pydantic import BaseModel


class dailyNews():
    def __init__(self):
        self.day: str = str(datetime.now().strftime("%d-%m-%y"))
        self.welcome_message = "Siema Ziomeczku!"
        self.todays_birthdays = get_todays_birthdays()
        self.upcoming_borthdays = get_upcoming_birthdays(days=7)
        

    def render_message(self):
        message = []
        message.append(self.welcome_message)
        message.append(f"Dziś mamy: {self.day}")

        return "\n".join(message)
