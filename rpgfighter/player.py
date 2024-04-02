import concept


class PlayerClass():
    health = 100
    moveList = ["Stab", "Introspection", "Dragon Strike"]
    moveList[0] = concept.GateClass().gateDict["bodyGate"]
    moveList[1] = concept.GateClass().gateDict["mindGate"]
    moveList[2] = concept.GateClass().gateDict["mindGate"]

    def playerStats(self):
        return self.health, self.moveList
