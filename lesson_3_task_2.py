from smartphone import Smartphone

catalog = ([
    Smartphone("Samsung", "S9", "+7987..."),
    Smartphone("Huawey", "P301", "+7985..."),
    Smartphone("Honor", "h101", "+7986..."),
    Smartphone("Nokia", "i301", "+7988..."),
    Smartphone("ZTE", "y4", "+7989...")
])

for smartphone in catalog:
    print(
        f"{smartphone.phone_brand} - {smartphone.phone_model}."
        f" {smartphone.phone_number}")
