from kivy.uix.screenmanager import Screen
from datetime import datetime
from kivy.properties import StringProperty

class TutorialTwo(Screen):
    
    current_date = StringProperty()
    
    def __init__(self, **kwargs):
        super(TutorialTwo, self).__init__(**kwargs)
        self.current_date = self.current_date_method_two()
    
    def current_date_method_one(self):
        current_date = datetime.now()
        formated_date = current_date.strftime("%A, %B %d %Y - %H:%M")
        return formated_date
    
    def current_date_method_two(self):
        current_date = datetime.now()
        formated_date = current_date.strftime("%A, %B %d %Y - %H:%M")
        return formated_date