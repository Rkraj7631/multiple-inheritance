class Product:
    def __init__(self):
        self.__title=input("Enter title : ")
        self.__price=input("Enter price : ")


    def show(self):
        print(self.__title,self.__price)

class Sales:
    def __init__(self):
        self.__sales=[int(x) for x in input("Enter Sales Fig : ").split()]

    def show(self):
        print(self.__sales)

class Hardware(Product,Sales):
    def __init__(self):
        #Product.__init__(self)
        #Sales.__init__(self)
        super().__init__()
        super().__init__()  
        self.__category=input("Enter catogery : ")
        self.__oem=input("Enter oem : ")

    def show(self):
        Product.show(self)
        Sales.show(self)
        print(self.__category, self.__oem)
        
h=Hardware()
h.show()
