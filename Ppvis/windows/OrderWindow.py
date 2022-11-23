from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.label import MDLabel

from windows.Window import Window


class OrderWindow(Window):
    def __init__(self, controller, **kw):
        super(OrderWindow, self).__init__(controller, **kw)

        self.title_label._set_text("Выбор блюда")

        button_layout = GridLayout(cols=2)

        order1_button = Button(text="Блюдо1", background_color=(0.53, 0.71, .53, .6), size_hint=(0.9, 0.4),
                                        on_press=lambda x: controller.set_present_screen_name("ShoppingCartWindow"))
        order2_button = Button(text="Блюдо2", background_color=(0.53, 0.71, .53, .6), size_hint=(0.9, 0.4),
                                on_press=lambda x: controller.set_present_screen_name("ShoppingCartWindow"))
        order3_button = Button(text="Блюдо5", background_color=(0.53, 0.71, .53, .6), size_hint=(0.9, 0.4),
                                      on_press=lambda x: controller.set_present_screen_name("ShoppingCartWindow"))
        order4_button = Button(text="Блюдо4", background_color=(0.53, 0.71, .53, .6), size_hint=(0.9, 0.4),
                                      on_press=lambda x: controller.set_present_screen_name("ShoppingCartWindow"))
        order5_button = Button(text="Блюдо5", background_color=(0.53, 0.71, .53, .6), size_hint=(0.9, 0.4),
                                      on_press=lambda x: controller.set_present_screen_name("ShoppingCartWindow"))
        order6_button = Button(text="Блюдо6", background_color=(0.53, 0.71, .53, .6), size_hint=(0.9, 0.4),
                             on_press=lambda x: controller.set_present_screen_name("ShoppingCartWindow"))
        exit_button = Button(text="Выход", background_color=(0.53, 0.71, .53, .6), size_hint=(0.9, 0.4),
                             on_press=lambda x: controller.set_present_screen_name("Menu"))

        order1_button_layout = AnchorLayout(anchor_x='left', anchor_y='center')
        order1_button_layout.add_widget(order1_button)

        order2_button_layout = AnchorLayout(anchor_x='right', anchor_y='center')
        order2_button_layout.add_widget(order2_button)

        order3_button_layout = AnchorLayout(anchor_x='left', anchor_y='center')
        order3_button_layout.add_widget(order3_button)

        order4_button_layout = AnchorLayout(anchor_x='right', anchor_y='center')
        order4_button_layout.add_widget(order4_button)

        order5_button_layout = AnchorLayout(anchor_x='left', anchor_y='center')
        order5_button_layout.add_widget(order5_button)

        order6_button_layout = AnchorLayout(anchor_x='right', anchor_y='center')
        order6_button_layout.add_widget(order6_button)

        exit_button_layout = AnchorLayout(anchor_x='center', anchor_y='bottom')
        exit_button_layout.add_widget(exit_button)

        button_layout.add_widget(order1_button_layout)
        button_layout.add_widget(order2_button_layout)
        button_layout.add_widget(order3_button_layout)
        button_layout.add_widget(order4_button_layout)
        button_layout.add_widget(order5_button_layout)
        button_layout.add_widget(order6_button_layout)
        button_layout.add_widget(exit_button_layout)
        self.controlled_layout.add_widget(button_layout)
