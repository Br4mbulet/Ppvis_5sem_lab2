from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.label import MDLabel

from windows.Window import Window


class ShoppingCartWindow(Window):
    def __init__(self, controller, **kw):
        super(ShoppingCartWindow, self).__init__(controller, **kw)

        self.title_label._set_text("Выбор блюда")

        button_layout = GridLayout(cols=1)

        order1_button = Button(text="Убрать Блюдо из корзины", background_color=(0.53, 0.71, .53, .6), size_hint=(0.4, 0.4),
                                        )
        continue_button = Button(text="Продолжить", background_color=(0.53, 0.71, .53, .6), size_hint=(0.4, 0.4),
                             on_press=lambda x: controller.set_present_screen_name("ConfirmWindow"))
        exit_button = Button(text="Выход", background_color=(0.53, 0.71, .53, .6), size_hint=(0.4, 0.4),
                             on_press=lambda x: controller.set_present_screen_name("Menu"))

        order1_button_layout = AnchorLayout(anchor_x='center', anchor_y='center')
        order1_button_layout.add_widget(order1_button)

        continue_button_layout = AnchorLayout(anchor_x='center', anchor_y='bottom')
        continue_button_layout.add_widget(continue_button)

        exit_button_layout = AnchorLayout(anchor_x='center', anchor_y='center')
        exit_button_layout.add_widget(exit_button)

        button_layout.add_widget(order1_button_layout)
        button_layout.add_widget(continue_button_layout)
        button_layout.add_widget(exit_button_layout)

        self.controlled_layout.add_widget(button_layout)
