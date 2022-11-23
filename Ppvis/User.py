class User:

    def __init__(self):
        self.login = None
        self.password = None
        self.phone = None
        self.registration_date = None
        self.cart_info = None

    def accept(self, visitor):
        pass

    def edit_info(self, **kwargs):
        pass

    def check_card(self):
        pass

    def check_support(self):
        pass

    def make_order(self):
        pass
