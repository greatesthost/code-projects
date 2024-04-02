import concept
import random
class monsterInfo():
    class bodyMonster():
        name = "The Brute Orc"
        gate = concept.GateClass.gateDict["bodyGate"]
        moveList = ["Savage Slash", "Undaunting Defense"]
        moveList = gate

    class mindMonster():
        name = "The Mindbender"
        gate = concept.GateClass.gateDict["mindGate"]
        moveList = ["Brain Melt", "Meditation"]
        moveList = gate





whichMonster = random.randint(1,2)
currentMonster = None
class monsterGenerator():
    def __init__(self):
    
     if whichMonster == 1:
        self.currentMonster = monsterInfo.bodyMonster()
     elif whichMonster == 2:
        self.currentMonster = monsterInfo.mindMonster()

        self.randomHp = random.randint(50,100)
        self.health = self.randomHp

activeMonster = monsterGenerator()


def monsterStats():
    return activeMonster.currentMonster.name, activeMonster.health