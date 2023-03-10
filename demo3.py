from kivy.lang import Builder
from kivymd.app import MDApp

KV = """
MDScreen:

    MDToolbar:
        title: 'MDFloatingActionButtonSpeedDial'
        pos_hint: {'top': 1}

    MDFloatingActionButtonSpeedDial:
        data: app.data
        rotation_root_button: True
"""


class Example(MDApp):
    data = {
        "language-python2222": "Python",
        "language-php": "PHP",
        "language-cpp": "C++",
    }

    def build(self):
        return Builder.load_string(KV)


Example().run()
