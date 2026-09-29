from address import Address


class Mailing:
    def __init__(
        self, to_address: Address, from_address: Address,
            cost: float, track: str
    ):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def print_info(self):
        print(f"Отправление из: {self.from_address.get_address_string()}")
        print(f"Отправление в:  {self.to_address.get_address_string()}")
        print(f"Трек-номер:     {self.track}")
        print(f"Стоимость:      {self.cost} руб.")
        print("-" * 40)
