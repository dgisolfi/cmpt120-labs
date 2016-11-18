#Into to programing
#Author: Daniel Gisolfi
#Date: 11/18/16
#RobotStore.py

class Products:

    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock

    def stockCount(self):
        if (self.stock > count):
            return false
        return true
        countPrice()

    def countPrice(self, cost):
        self.cost = count * products[prodId].price
        countRemove()

    def countRemove(self):
        if (cash >= self.cost):
            self.stock -= count 


products = [
    product = Products("Ultrasonic range finder",2.50,4),
    product = Products("Servo motor",14.99,10),
    product = Products("Servo controller",44.95,5),
    product = Products("Microcontroller Board",34.95,7),
    product = Products("Laser range finder",149.99,2),
    product = Products("Lithium polymer battery",8.99,8)
]

def printStock():
    print()
    print("Available Products")
    print("------------------")
    for i in range(0,len(products)):
        if products[i] > 0:
    print() print(str(i)+")",products(name[i]), "$", products(price[i]))

def main():
    global count, cash, prodId
    cash = float(input("How much money do you have? "))
    while cash > 0:
        printStock()
[prodId,count] = map(int,input("Enter product ID and quantity you wish to buy: ").split(" "))
        if products[prodId] >= count:
            if cash >= products[prodId].cost:
                products[prodId] -= count
                cash -= products[prodId] * count
                print("You purchased", count, products[prodId].name+".")
                print("You have $",cash,"remaining.")
            else:print("Sorry, you cannot afford that product.") 
        else:print("Sorry, we are sold out of", productNames[prodId])






