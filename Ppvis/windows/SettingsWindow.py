from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel

from windows.Window import Window

mdtf1 = """
MDTextField:
    hint_text: "E-mail"
    mode: "rectangle"
    color_mode: "custom"
    fill_color: 0.1, 1, 1, 1
    line_color_normal: 0.1, 1, 1, 1
    line_color_focus: 0.1, 1, 1, 1
    font_size: 20
    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
    size_hint: 0.5, 0.5
    halign:"center"
    icon_right_color: 0.1, 1, 1, 1
    background_color:0.53, 0.71, .53, .6
"""

mdtf2 = """
MDTextField:
    hint_text: "Номер телефона"
    mode: "rectangle"
    color_mode: "custom"
    fill_color: 0.1, 1, 1, 1
    line_color_normal: 0.1, 1, 1, 1
    line_color_focus: 0.1, 1, 1, 1
    font_size: 20
    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
    size_hint: 0.5, 0.5
    halign:"center"
    icon_right_color: 1, 1, 1, 1
    background_color:0.53, 0.71, .53, .6
"""

mdtf3 = """
MDTextField:
    hint_text: "Пароль"
    mode: "rectangle"
    color_mode: "custom"
    fill_color: 0.1, 1, 1, 1
    line_color_normal: 0.1, 1, 1, 1
    line_color_focus: 0.1, 1, 1, 1
    font_size: 20
    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
    size_hint: 0.5, 0.5
    halign:"center"
    icon_right_color: 1, 1, 1, 1
    background_color:0.53, 0.71, .53, .6
"""

mdtf4 = """
MDTextField:
    hint_text: "Карта"
    mode: "rectangle"
    color_mode: "custom"
    fill_color: 0.1, 1, 1, 1
    line_color_normal: 0.1, 1, 1, 1
    line_color_focus: 0.1, 1, 1, 1
    font_size: 20
    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
    size_hint: 0.5, 0.5
    halign:"center"
    icon_right_color: 1, 1, 1, 1
    background_color:0.53, 0.71, .53, .6
"""
class SettingsWindow(Window):

    def __init__(self, controller, **kw):
        super(SettingsWindow, self).__init__(controller, **kw)
        self.pin_code = ""

        self.title_label._set_text("Настройки")

        button_layout = GridLayout(cols=3)

        paymant_button = Button(text="Изменить", background_color=(0.53, 0.71, .53, .6),
                                size_hint_y=None, height=50, size_hint_x=None, width=150,
                                on_press=lambda x: controller.set_present_screen_name("SettingsOKWindow"))

        self.phone_number_text_filed = Builder.load_string(mdtf1)
        phone_number_text_filed_layout = AnchorLayout(anchor_x='center', anchor_y='center')


        phone_number_text_filed_layout.add_widget(self.phone_number_text_filed)
        self.controlled_layout.add_widget(phone_number_text_filed_layout)

        self.money_text_filed = Builder.load_string(mdtf2)
        money_text_filed_layout = AnchorLayout(anchor_x='center', anchor_y='center')

        money_text_filed_layout.add_widget(self.money_text_filed)
        self.controlled_layout.add_widget(money_text_filed_layout)

        self.phone_number_text_filed2 = Builder.load_string(mdtf3)
        phone_number_text_filed2_layout = AnchorLayout(anchor_x='center', anchor_y='center')


        phone_number_text_filed2_layout.add_widget(self.phone_number_text_filed2)
        self.controlled_layout.add_widget(phone_number_text_filed2_layout)

        self.phone_number_text_filed3 = Builder.load_string(mdtf4)
        phone_number_text_filed_layout3 = AnchorLayout(anchor_x='center', anchor_y='center')


        phone_number_text_filed_layout3.add_widget(self.phone_number_text_filed3)
        self.controlled_layout.add_widget(phone_number_text_filed_layout3)

        next_layout = AnchorLayout(anchor_x='right', anchor_y='center')

        next_layout.add_widget(paymant_button)
        button_layout.add_widget(next_layout)
        self.controlled_layout.add_widget(button_layout)



    def on_leave(self, *args):
        self.phone_number_text_filed.text = ""
        self.money_text_filed.text = ""