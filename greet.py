# The boss is the person who creates the room.
# If the boss was last to enter, greet them with "Hello, {boss}"
# Otherwise, greet them with "Welcome, {name}"
#
# Only greet the last person who entered.
#
# If no one new has entered, further calls to greet() will return 'None'

class Greeter:

    def __init__(self, name):
        self.bossname = name
        self.people = []
        self.num_people = None

    def enter(self, name):
        self.people.append(name)

    def greet(self):
        if len(self.people) == 0 or len(self.people) == self.num_people:
            return None

        self.num_people = len(self.people)

        name = self.people[-1]

        if name == self.bossname:
            print("Hello, {}".format(name))
        else:
            print("Welcome, {}".format(name))


Greeter = Greeter('Chuck')
Greeter.enter('Larry')
Greeter.greet()
Greeter.enter('Chuck')
Greeter.greet()
Greeter.greet()
Greeter.greet()
Greeter.enter('Larry')
Greeter.enter('Dave')
Greeter.greet()
Greeter.greet()

