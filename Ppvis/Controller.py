from Meal import Meal
from Order import Order

class Controller:
    def __init__(self, model):
        self.model = model
        self.view = None

    def set_view(self, view):
        self.view = view

    def log_in_profile(self, login, password):
        pass

    def register_profile(self, login, password):
        pass
    
    def edit_information(self, **kwargs):
        pass
    
    def select_meal(self):
        return Meal

    def set_present_screen_name(self, present_screen_name):
        self.view.set_present_screen_name(present_screen_name)
        
    def get_order_info(self, order):
        pass
    
    def confirm_order(self, meal):
        return Order
    def support_report(self, user):
        message = ""
        return message

