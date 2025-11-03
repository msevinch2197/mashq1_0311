class Telefon:
    def __init__(self, brend, model, batareya):
        self.brend = brend
        self.model = model
        self.batareya = batareya

    def batareya_korsat(self):
        return f"Batareya darajasi: {self.batareya}%"

    def zaryadla(self, miqdor):
        self.batareya = min(self.batareya + miqdor, 100)
        return f"Batareya zaryadlandi: {self.batareya}%"

# Misol
telefon = Telefon("Samsung", "Galaxy S23", 45)
print(telefon.batareya_korsat())
print(telefon.zaryadla(30))
