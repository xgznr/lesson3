from adress import Address
from mailing import Mailing

to_address = Address("665700", "Bratsk", "Lenina", "5", "45")
from_address = Address("101000", "Moscow", "Kurchatova", "10", "46")

shipment = Mailing(to_address, from_address, 123, "TRC5874IRC")

print(
    f"Отправление {shipment.track} из {shipment.from_address.postal_code},"
    f"{shipment.from_address.city}, {shipment.from_address.street},"
    f"{shipment.from_address.house} - {shipment.from_address.flat}"
    f"в {shipment.to_address.postal_code},"
    f"{shipment.to_address.city}, {shipment.to_address.street},"
    f"{shipment.to_address.house} - {shipment.to_address.flat}."
    f"Стоимость {shipment.cost} рублей. ") #
