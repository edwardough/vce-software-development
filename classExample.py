class MyPlayer():
    def __init__( self, name, height ):
        self.name = name
        self.height = str(height) + "cm"
        # add a breakpoint to a line in the __init__ function

    def __str__( self ):
        return self.name + ', ' + self.height

    def changeName( self, newName ):
        self.name = newName

    def reset( self, newName, newHeight ):
        self.name = newName
        self.height = str(newHeight) + "cm"

    def printGreeting( self ):
        print("Hello, my name is",self.name,"and my height is",self.height)

# add players to a watchlist using the debugger
players = [ MyPlayer("Cameron",180), MyPlayer("James",72), MyPlayer("Matthew",175) ]

for player in players:
    player.printGreeting()
    print(str(player))


