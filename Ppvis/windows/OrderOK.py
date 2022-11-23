import time

from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivymd.uix.label import MDLabel

from windows.Window import Window


class OrderOKWindow(Window):
    def __init__(self, controller, **kw):
        super(OrderOKWindow, self).__init__(controller, **kw)

        completed_label = MDLabel(text="Заказано Успешно", font_size=200, halign="center")
        self.controlled_layout.add_widget(completed_label)

    def on_enter(self, *args):
        time.sleep(2)
        self.controller.set_present_screen_name("Menu")