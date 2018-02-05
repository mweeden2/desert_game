# Matt Weeden
# 2/4/18
#
# The Person class for the "Dessert" game

class Person(LivingThing):

def __init__(self, mainp, name, weight, health, stamina, xp):

    LivingThing.__init__(self, name, 'person', weight, health, False)
    self.mainp = mainp
    self.xp_a = xp
    self.stamina_a = stamina

    # update player attributes based on s string
    def update(self, s, n=0):

        # action updates
        if s == "walk":
            i = self.r.randint(0, 9)
            if i > 7:
                print 'ye'
                self.update("stamina", -2)
            elif i > 2:
                print 'yep'
                self.update("stamina", -1)

        # attribute updates
        if s == "health":
            self.health_a += n
            if self.health_a < 1:
                self.die()

        if s == "stamina":
            self.stamina_a += n
            if self.stamina_a < 1:
                self.die()
