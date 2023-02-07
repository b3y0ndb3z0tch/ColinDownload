from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import MDScreen

# Declare both screens
class ScreenOne(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create the button to go to the next screen
        self.next_button = MDRectangleFlatButton(text='Next', on_release=self.go_to_next)
        self.add_widget(self.next_button)

    def go_to_next(self, *args):
        self.manager.current = 'screen_two'

class ScreenTwo(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create the button to go back to the previous screen
        self.prev_button = MDRectangleFlatButton(text='Prev', on_release=self.go_to_prev)
        self.add_widget(self.prev_button)

    def go_to_prev(self, *args):
        self.manager.current = 'screen_one'

# Create the screen manager
sm = ScreenManager()
sm.add_widget(ScreenOne(name='screen_one'))
sm.add_widget(ScreenTwo(name='screen_two'))

# Create the KivyMD app
class KivyMDApp(MDApp):
    def build(self):
        return sm

# Run the app
KivyMDApp().run()
