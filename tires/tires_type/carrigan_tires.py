from tires import Tires

class CarriganTires(Tires):

    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
        self.tire_need_to_service = 0.9

    def needs_service(self):
        wear = [tire>= tire_need_to_service for tire in tire_wear]
        return any(wear)