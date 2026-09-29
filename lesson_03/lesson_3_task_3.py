from address import Address
from mailing import Mailing

sender = Address("108392", "Москва", "Ленина", "3", "249")
receiver = Address("190000", "Санкт-Петербург", "Невский проспект", "1", "12")

my_mailing = Mailing(
    to_address=receiver, from_address=sender, cost=350.50, track="RU1234567RU"
)

my_mailing.print_info()
