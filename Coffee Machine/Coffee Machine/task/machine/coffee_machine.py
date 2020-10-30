# Write your code here
# Write your code here
class CoffeeMachine:
    buy = "buy"
    fill = "fill"
    take = "take"
    remaining = "remaining"
    exit_ = "exit"

    def __init__(self):
        self.ingre = {"water": 400, "milk": 540, "coffee_beans": 120, "cups": 9, "money": 550}

    def print_state(self):
        print(f'''The coffee machine has:
{self.ingre["water"]} of water
{self.ingre["milk"]} of milk
{self.ingre["coffee_beans"]} of coffee beans
{self.ingre["cups"]} of disposable cups
${self.ingre["money"]} of money
    ''')

    def to_do(self, action):
        if action == self.buy:
            self.action_buy()
        elif action == self.fill:
            self.action_fill()
        elif action == self.take:
            self.action_take()
        elif action == self.remaining:
            self.print_state()
        elif action == self.exit_:
            exit(0)
        else:
            print("Invalid action.")

    def change_state(self, action, water, milk, coffee_beans, cups, money):
        if action == self.buy:
            self.ingre["water"] -= water
            self.ingre["milk"] -= milk
            self.ingre["coffee_beans"] -= coffee_beans
            self.ingre["cups"] -= 1
            self.ingre["money"] += money
        elif action == self.fill:
            self.ingre["water"] += water
            self.ingre["milk"] += milk
            self.ingre["coffee_beans"] += coffee_beans
            self.ingre["cups"] += cups
        else:
            print("Invalid action")

    def action_buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        choice = input()
        if choice == "back":
            return
        else:
            choice = int(choice)
        if self.check_availabilty(choice):
            if choice == 1:
                self.change_state(self.buy, 250, 0, 16, 1, 4)
            elif choice == 2:
                self.change_state(self.buy, 350, 75, 20, 1, 7)
            elif choice == 3:
                self.change_state(self.buy, 200, 100, 12, 1, 6)
            else:
                print("Invalid choice")
            print("I have enough resources, making you a coffee!")

    def action_fill(self):
        print("Write how many ml of water do you want to add:")
        fill_water = int(input())
        print("Write how many ml of milk do you want to add:")
        fill_milk = int(input())
        print("Write how many grams of coffee beans do you want to add:")
        fill_coffee_beans = int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        fill_cups = int(input())
        self.change_state(self.fill, fill_water, fill_milk, fill_coffee_beans, fill_cups, 0)

    def action_take(self):
        print(f'I gave you ${self.ingre["money"]}')
        self.ingre["money"] = 0

    def ingredients_required(self, choice):
        if choice == 1:
            return [250, 0, 16, 1]
        elif choice == 2:
            return [350, 75, 20, 1]
        elif choice == 3:
            return [200, 100, 12, 1]
        else:
            return [0, 0, 0, 0]

    def check_availabilty(self, choice):
        current_ingredients = [self.ingre["water"], self.ingre["milk"], self.ingre["coffee_beans"], self.ingre["cups"]]
        ingredients_name = ("water", "milk", "coffee_beans", "cups")
        required_ingredients = self.ingredients_required(choice)
        difference = []
        zip_object = zip(current_ingredients, required_ingredients)
        for list1, list2 in zip_object:
            difference.append(list1 - list2)
        for items in difference:
            if items < 0:
                index = difference.index(items)
                print(f'Sorry, not enough {ingredients_name[index]}!')
                return False
            else:
                return True


coffee_machine = CoffeeMachine()
while True:
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    coffee_machine.to_do(action)





