from Appl import App
from Controller import Controller
from Model import Model
from View import View
from User import User
from Login import Login
from Meal import Meal
from Order import Order
from Order_processing import OrderProcessing
from Registration import Registration
from Restaurant import Restaurant
from Support import Support

if __name__ == '__main__':
    user = User()
    model = Model()
    controller = Controller(model)
    view = View(model, controller)
    controller.set_view(view)
    app = App(model, controller, view)
    app.work()
