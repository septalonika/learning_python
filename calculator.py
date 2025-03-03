class Calculator:
    def __init__(self, number1, number2, operation):
        self.operation = operation
        self.number1 = number1
        self.number2 = number2
        self.operation = operation
        
    def calculate(self): 
        match self.operation:
            case '+' | '1': 
                self.operation = ' + '
                result = self.number1 + self.number2
            case '-' | '2':
                self.operation = ' - '
                result = self.number1 - self.number2
            case '*' | '3':
                self.operation = ' x '
                result = self.number1 - self.number2
            case '/' | '4':
                self.operation = ' : '
                result = self.number1 - self.number2
        return f"{self.number1} {self.operation} {self.number2} adalah {result}"
    
if __name__ == '__main__':    

    is_continue = True
    choice = True
    
    while is_continue:
        try:
            number1 = float(input("please input number1 : "))
            number2= float(input("please input number2 : "))
        except ValueError:
            print("Invalid input! Please input numbers only.")
            continue
        
        print("1. Penjumlahan (+)")
        print("2. Pengurangan (-)")
        print("3. Perkalian   (*)")
        print("4. Pembagian   (/)")

        operation = input("please input operation : ")

        while operation not in ['+', '-', '*', '/', '1', '2', '3', '4']:
            print("Invalid operation!")
            operation = str(input("please input operation : "))
            
        print(Calculator(number1, number2, operation).calculate())

        while choice:
            choice = input("Do you want to continue? (yes/no) ").lower()
            if choice not in ['yes', 'no']:
                print("Invalid choice!")
            elif choice == 'no':
                print("Exiting...")
                is_continue = False
                break