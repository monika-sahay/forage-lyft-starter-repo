from tires import Tires


class OctoprimeTires(Tires):

    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
        self.tire_need_to_service = 3

    def needs_service(self):
        return sum(tire_wear) > tire_need_to_service 