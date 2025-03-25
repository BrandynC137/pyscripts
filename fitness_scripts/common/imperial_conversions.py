class ImperialConversion:
    def __init__(self, inches, pounds):
        self.pounds = float(pounds)  # Instance variable
        self.inches = float(inches)   # Instance variable

    def pounds_to_kilos(self):
        return self.pounds * 0.453592

    def inches_to_centimeters(self):
        return self.inches * 2.54