from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.label import MDLabel

from windows.Window import Window


class Menu(Window):
    def __init__(self, controller, **kw):
        super(Menu, self).__init__(controller, **kw)

        self.title_label._set_text("Меню")

        button_layout = GridLayout(cols=2)

        place_order_button = Button(text="Выбор заказа", background_color=(0.53, 0.71, .53, .6), size_hint=(0.9, 0.3),
                                        on_press=lambda x: controller.set_present_screen_name("OrderWindow"))
        settings_button = Button(text="Настройки", background_color=(0.53, 0.71, .53, .6), size_hint=(0.9, 0.3),
                                on_press=lambda x: controller.set_present_screen_name("SettingsWindow"))
        support_button = Button(text="Поддержка", background_color=(0.53, 0.71, .53, .6), size_hint=(0.9, 0.3),
                                      )
        history_button = Button(text="История заказов", background_color=(0.53, 0.71, .53, .6), size_hint=(0.9, 0.3),
                                      )

        place_order_button_layout = AnchorLayout(anchor_x='center', anchor_y='center')
        place_order_button_layout.add_widget(place_order_button)

        settings_button_layout = AnchorLayout(anchor_x='center', anchor_y='center')
        settings_button_layout.add_widget(settings_button)

        support_button_layout = AnchorLayout(anchor_x='center', anchor_y='center')
        support_button_layout.add_widget(support_button)

        history_button_layout = AnchorLayout(anchor_x='center', anchor_y='center')
        history_button_layout.add_widget(history_button)

        button_layout.add_widget(place_order_button_layout)
        button_layout.add_widget(settings_button_layout)
        button_layout.add_widget(support_button_layout)
        button_layout.add_widget(history_button_layout)

        self.controlled_layout.add_widget(button_layout)
