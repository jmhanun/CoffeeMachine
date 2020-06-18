class Recipient:
    def __init__(self, code, name, water, milk, coffee, money):
        self.code = code
        self.name = name
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money

    def __str__(self):
        return "{} - {}".format(self.code, self.name)


class CoffeeMachine:

    def __init__(self, water=400, milk=540, coffee=120, cups=9, money=550):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money
        self.recipients = []

    def __str__(self):
        return "The coffee machine has:\n{} of water\n" \
               "{} of milk\n{} of coffee beans\n" \
               "{} of disposable cups\n${} of money\n"\
            .format(self.water, self.milk, self.coffee, self.cups, self.money)

    def add_recipient(self, code, name, water, milk, coffee, money):
        self.recipients.append(Recipient(code, name, water, milk, coffee, money))

    def get_recipient(self, code):
        for recipient in self.recipients:
            if recipient.code == code:
                return recipient
        return None

    def make_recipient(self, recipient):
        self.fill(-recipient.water, -recipient.milk, -recipient.coffee, -1, recipient.money)
        return "I have enough resources, making you a coffee!\n"

    def hay_stock(self, recipient):
        return self.water >= recipient.water and \
               self.milk >= recipient.milk and \
               self.coffee >= recipient.coffee and \
               self.cups >= 1

    def fill(self, water=0, milk=0, coffee=0, cups=0, money=0):
        self.water += water
        self.milk += milk
        self.coffee += coffee
        self.cups += cups
        self.money += money

    def take(self):
        total, self.money = self.money, 0
        return "I gave you ${}".format(total)

    def not_enough(self, recipient):
        response = ""
        if self.water < recipient.water:
            response += "Sorry, not enough water!\n"
        if self.milk < recipient.milk:
            response += "Sorry, not enough milk!\n"
        if self.coffee < recipient.coffee:
            response += "Sorry, not enough coffee beans!\n"
        if self.cups < 1:
            response += "Sorry, not enough cups!\n"
        return response


class UserInterface:
    def __init__(self, cm):
        self.coffee_machine = cm

    def buy(self):
        options = []
        for recipient in self.coffee_machine.recipients:
            options.append(str(recipient))
        print("What do you want to buy? {}:".format(", ".join(options)))
        code = input()
        if code != "back":
            code = int(code)
            recipient = self.coffee_machine.get_recipient(code)
            if self.coffee_machine.hay_stock(recipient):
                print(self.coffee_machine.make_recipient(recipient))
            else:
                print(self.coffee_machine.not_enough(recipient))

    def fill(self, water=0, milk=0, coffee=0, cups=0):
        self.coffee_machine.fill(water, milk, coffee, cups)

    def take(self):
        print(self.coffee_machine.take())
        print()

    def start(self):
        action = input("Write action (buy, fill, take, remaining, exit):\n")
        while action != "exit":
            if action == "buy":
                print()
                self.buy()
            elif action == "fill":
                print()
                print("Write how many ml of water the coffee machine has:")
                water = int(input())
                print("Write how many ml of milk the coffee machine has:")
                milk = int(input())
                print("Write how many grams of coffee beans the coffee machine has:")
                coffee = int(input())
                print("Write how many disposable cups of coffee do you want to add:")
                cups = int(input())
                print()
                self.fill(water, milk, coffee, cups)
            elif action == "take":
                print()
                self.take()
            elif action == "remaining":
                print()
                print(self.coffee_machine)
            action = input("Write action (buy, fill, take, remaining, exit):\n")


coffee_machine = CoffeeMachine()
coffee_machine.add_recipient(1, "Espresso", 250, 0, 16, 4)
coffee_machine.add_recipient(2, "Latte", 350, 75, 20, 7)
coffee_machine.add_recipient(3, "Cappuccino", 200, 100, 12, 6)

ui = UserInterface(coffee_machine)
ui.start()

