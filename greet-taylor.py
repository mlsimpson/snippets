class Greeter:

    def __init__(self, boss):
        self.boss = boss;
        self.lastEntered = boss;

    def enters(self, visitor):
        self.lastEntered = visitor;

    def greet(self):
        if self.lastEntered is None:
            return None;
        print("Hello, " + self.lastEntered if self.lastEntered == self.boss else "Welcome, " + self.lastEntered);
        self.lastEntered = None;

if __name__ == "__main__":
    g = Greeter('Chuck')
    g.enters('John')
    print(g.greet())

