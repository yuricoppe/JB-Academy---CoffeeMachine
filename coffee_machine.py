class CoffeeMachine:
    def __init__(self):
        self.money = 550
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        # 0 = water, 1 = milk, 2 = coffee_beans, 3 = cups, 4 = money
        self.espresso = [250, 0, 16, 1, 4]
        self.latte = [350, 75, 20, 1, 7]
        self.cappuccino = [200, 100, 12, 1, 6]

        self.state = ''
        self.change_state(self.state)

    def change_state(self, state):
        self.state = state
        if self.state == '':
            print("Write action (buy, fill, take, remaining, exit):")
            self.change_state(input())

        if self.state == "buy":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            self.state = input()
            type_of_coffee = []

            if self.state == '1':
                type_of_coffee = self.espresso
                if self.compare(type_of_coffee) is False:
                    self.state = 'buy'
                else:
                    self.buy(type_of_coffee)

            elif self.state == '2':
                type_of_coffee = self.latte
                if self.compare(type_of_coffee) is False:
                    self.state = 'buy'
                else:
                    self.buy(type_of_coffee)

            elif self.state == '3':
                type_of_coffee = self.cappuccino
                if self.compare(type_of_coffee) is False:
                    self.state = 'buy'
                else:
                    self.buy(type_of_coffee)

            elif self.state == 'back':
                self.change_state('buy')
        elif self.state == "fill":
            self.fill()
        elif self.state == "take":
            self.take()
        elif self.state == 'remaining':
            self.print_supplies()
        elif self.state == 'exit':
            exit()

    # Compare to see if machine has enough supplies
    def compare(self, t):
        if self.water - t[0] <= 0:
            print('Sorry, not enough water!')
            return False
        elif self.milk - t[1] <= 0:
            print('Sorry, not enough milk!')
            return False
        elif self.coffee_beans - t[2] <= 0:
            print('Sorry, not enough coffee beans!')
            return False
        elif self.disposable_cups - t[3] <= 0:
            print('Sorry, not enough cups!')
            return False
        else:
            return True

    def buy(self, t):
        # global water, milk, coffee_beans, disposable_cups, money

        print('I have enough resources, making you a coffee!')

        # Subtracts supplies according to type
        self.water = self.water - t[0]
        self.milk = self.milk - t[1]
        self.coffee_beans = self.coffee_beans - t[2]
        self.disposable_cups = self.disposable_cups - t[3]
        self.money = self.money + t[4]
        self.change_state('')

    def fill(self):
        # global water, milk, coffee_beans, disposable_cups
        print("Write how many ml of water do you want to add:")
        self.water = int(input()) + self.water
        print("Write how many ml of milk do you want to add:")
        self.milk = int(input()) + self.milk
        print("Write how many grams of coffee beans do you want to add:")
        self.coffee_beans = int(input()) + self.coffee_beans
        print("Write how many disposable cups of coffee do you want to add:")
        self.disposable_cups = int(input()) + self.disposable_cups
        self.change_state('')

    def take(self):
        # global money
        print("I gave you $" + str(self.money))
        self.money = 0
        self.change_state('')

    def print_supplies(self):
        print("The coffee machine has:")
        print(str(self.water) + " of water")
        print(str(self.milk) + " of milk")
        print(str(self.coffee_beans) + " of coffee beans")
        print(str(self.disposable_cups) + " of disposable cups")
        print(str(self.money) + " of money")
        print("")
        self.change_state('')


coffee_machine = CoffeeMachine()


# # Program loop
# while True:
#     print("Write action (buy, fill, take, remaining, exit):")
#     action = input()



