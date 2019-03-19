class Player:
    team = ''
    role = ''
    status = 'Alive'
    saved = False

    def __init__(self, name):
       self.name = name

    def setTeam(self, t):
        if t == "Town":
            return Town(self.name)
        if t == "Mafia":
            return Mafia(self.name)

    def displayPlayer(self):
        print("Name: " + self.name)
        print("Role: "+ self.role)
        print("Team: "+ self.team)
        print("Status: "+ self.status)

    def setDead(self):
        if (self.saved == False):
            self.status = 'Dead'


    def describe(self):
        print("I am a " + self.role + "!")


class Town(Player):                     #Town inherits from player
    team = 'Town'
    role = 'Innocent'

    def setRole(self, r):
        if r == "Doctor":
            return Doctor(self.name)

class Mafia(Player):                    #Mafia inherits from player
    team = 'Mafia'
    role = 'Mafioso'

    def killPlayer(self, Player):
        print("Mafia attacked " + Player.name + " last night!")
        Player.setDead()



class Doctor(Town, Player):
    role = 'Doctor'

    def savePlayer(self, Player):
        print("The doctor saved " + Player.name)
        Player.saved = True

def main():
    player1 = Player("Wyatt").setTeam("Town").setRole("Doctor")
    player2 = Player("Talon").setTeam("Mafia")

    player1.displayPlayer()

    player2.describe()

    player1.savePlayer(player1)

    player2.killPlayer(player1)

    player1.displayPlayer()




main()