import time

from kivy.config import Config
from kivy.lang import Builder


Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '720')


from windows.Window import Window
from windows.StartWindow import StartWindow
from windows.LoginWindow import LoginWindow
from windows.Menu import Menu
from windows.OrderWindow import OrderWindow
from windows.ShoppingCartWindow import ShoppingCartWindow
from windows.ConfirmWindow import ConfirmWindow
from windows.OrderOK import OrderOKWindow
from windows.SettingsWindow import SettingsWindow
from kivy.uix.screenmanager import Screen, ScreenManager
from windows.SettingsOKWindow import SettingsOKWindow
from kivymd.app import MDApp


class View(MDApp):
    def __init__(self, model, controller, **kw):
        super(View, self).__init__()
        self.model = model
        self.controller = controller
        self.controller.set_view(self)
        self.screens = ScreenManager()
        self.screens.add_widget(Window(name="Window", controller=self.controller))
        self.screens.add_widget(StartWindow(name="StartWindow", controller=self.controller))
        self.screens.add_widget(LoginWindow(name="LoginWindow", controller=self.controller))
        self.screens.add_widget(OrderWindow(name="OrderWindow", controller=self.controller))
        self.screens.add_widget(Menu(name="Menu", controller=self.controller))
        self.screens.add_widget(ShoppingCartWindow(name="ShoppingCartWindow", controller=self.controller))
        self.screens.add_widget(ConfirmWindow(name="ConfirmWindow", controller=self.controller))
        self.screens.add_widget(OrderOKWindow(name="OrderOKWindow", controller=self.controller))
        self.screens.add_widget(SettingsWindow(name="SettingsWindow", controller=self.controller))
        self.screens.add_widget(SettingsOKWindow(name="SettingsOKWindow", controller=self.controller))

        self.screens.current = "StartWindow"

    def set_present_screen_name(self, present_screen_name):
        if present_screen_name == "Stop":
            self.stop()
        else:
            self.screens.current = present_screen_name

    def get_present_screen_name(self):
        return self.screens.current

    def build(self):
        return self.screens

    def view_work(self):
        self.run()
