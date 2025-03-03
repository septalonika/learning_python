class PengaturSuhu:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit.upper()  
    def convert(self):
        if self.unit == "C":
            return round((self.value * 9/5) + 32, 2)
        elif self.unit == "F":
            return round((self.value - 32) * 5/9, 2)
        else:
            return "Unit tidak didukung"
    def display_result(self):
        result = self.convert()
        if isinstance(result, float):
            converted_unit = 'Fahrenheit' if self.unit == 'C' else 'Celsius'
            print(f"{self.value}°{self.unit} dikonversi menjadi {result}°{converted_unit[0]}")
        else:
            print(result) 


try:
    value = float(input("Masukkan nilai suhu: "))  
    unit = input("Masukkan satuan suhu (C/F): ").strip().upper()
    converter = PengaturSuhu(value, unit)
    converter.display_result()
except ValueError:
    print("Error: Masukkan angka yang valid untuk suhu!")