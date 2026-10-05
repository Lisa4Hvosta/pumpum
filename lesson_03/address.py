class Address:
    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment
        print(
            f"{self.index} {self.city} "
            f"ул. {self.street} д. {self.house} кв. {self.apartment}"
        )

    def get_address_string(self):
        return (
            f"{self.index}, {self.city}, "
            f" ул. {self.street}, д. {self.house}, кв. {self.apartment}"
        )


Address1 = Address("108392", "Москва", "Ленина", "3", "249")
Address2 = Address("190000", "Санкт-Петербург", "Невский проспект", "1", "12")
