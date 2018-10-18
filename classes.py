# created by Matt Weeden
# 7/8/16
#
# This script defines classes for a text-based game

import sys
import random

#TODO: expand status (prettyPrint) into status and info commands

class Thing(object):

    # Note: "..._a" means a user-visible attribute of a Thing
    def __init__(self, name, kind, weight, health, is_edible):
        self.name_a = name
        self.kind_a = kind
        self.weight_a = weight
        self.is_edible_a = is_edible
        self.health_a = health
        self.r = random.Random()

    def getName(self):
        return self.name_a

    def getKind(self):
        return self.kind_a

    def getWeight(self):
        return self.weight_a

    def isEdible(self):
        return self.is_edible_a

    def getHealth(self):
        return self.health_a

    def prettyPrint(self):
        print
        attributes = [a[:-2] for a in dir(self) if not a.startswith("__") and a.endswith("_a")]
        for a in attributes:
            if len(a) > 5:
                print a + ":", "\t", getattr(self, a + "_a")
            else:
                print a + ":", "\t\t", getattr(self, a + "_a")

    def __str__(self):
        return "%s is a %s" % (self.name_a, self.kind_a)

class LivingThing(Thing):

    def __init__(self, name, kind, weight, health, is_edible):
        Thing.__init__(self, name, 'living thing', weight, health, is_edible)
        self.sub_kind_a = kind

    def die(self):
        if self.mainp:
            print '\n\tI...I.......there\'s more about this than I thought.\n'
            sys.exit()

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
                self.update("stamina", -2)
            elif i > 2:
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


class Paper(Thing):

    def __init__(self, name, weight, health, message):
        Thing.__init__(self, name, 'paper', weight, False, health)
        self.message_a = message

    def getMessage(self):
        return self.message_a

class Food(Thing):

    def __init__(self, name, weight, health, nutrition_val):
        Thing.__init__(self, name, 'food', weight, True, health)
        self.nutrition_val = nutrition_val

    def getNutritionVal(self):
        return self.nutrition_val
