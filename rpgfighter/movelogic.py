import concept
import monster
import player

class actionInteraction():
    # body beats soul, soul beats mind, mind beats body
    neutral = False
    effective = False
    weak = False

    def effectiveness(self):
            if player.PlayerClass().moveList[0] and \
        monster.activeMonster.currentMonster.gate == "bodyC":
                self.neutral = True

            elif player.PlayerClass().moveList[0] and \
            monster.activeMonster.currentMonster.gate == "mindC":
                self.weak = True

            elif player.PlayerClass().moveList[0] and \
            monster.activeMonster.currentMonster.gate == "soulC":
                self.effective = True

    # TODO: finish all of the gate interactions :(
