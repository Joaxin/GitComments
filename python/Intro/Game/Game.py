#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

times = 1

class people:
    name = ''
    hp = 10
    ruby = 10
    wounded = False

    def __init__(self, n, h, r, w):
        self.name = n
        self.hp = h
        self.ruby = r
        self.wounded = w

    def show(self):
        print("%s has  %d rubies and %d hp." %
              (self.name, self.ruby, self.hp))
        if self.wounded:
            print("\n wounded... so everytime you destroy an enemy \n \
                you will loose %d health" % int(self.hp / 20))


class NPC(people):

    vials = 1000
    __ruby = 20

    def set_ruby(self, ruby):
        if 0 <= ruby <= 1000:
            self.__ruby = ruby
        else:
            raise ValueError('Not properly ruby')

    def __init__(self, n, h, r, v):
        super().__init__(n, h, r, False)
        # people.__init__(self,n,h,r,False)
        self.vials = v
        self.__ruby = r

    def show(self):
        print("%s has  %d rubies , %d vials and %d hp." %
              (self.name, self.__ruby, self.vials, self.hp))


c = NPC('Luna', 10, 30, 2000)
c.show()


elf_hp = 10
wasp_hp = 20


def wandering():
    monster = random.choice(["goblin", "elf", "wasp"])
    print("you encoutered a %s" % monster)
    return monster


def say(noun):
    return 'You said "{}"'.format(noun)


def get_input():
    try:
        command = input(": ").split()
        verb_word = command[0]
    except IndexError:
        print("error detected, plz input again")
        return get_input()
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    elif verb_word == "wandering":
        return wandering()
    else:
        print("Unknown verb {}". format(verb_word))
        return

    if len(command) >= 2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb("nothing"))


class GameObject:
    class_name = ""
    desc = ""
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self

    def get_desc(self):
        return self.class_name + "\n" + self.desc


def examine(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
    else:
        return "There is no {} here.".format(noun)


def show(noun):
    return you.show()


class Goblin(GameObject):

    def __init__(self, name):
        self.class_name = "goblin"
        self.health = 3
        self._desc = " A foul creature"
        super().__init__(name)

    @property
    def desc(self):
        if self.health >= 3:
            return self._desc
        elif self.health == 2:
            health_line = "It has a wound on its knee."
        elif self.health == 1:
            health_line = "Its left arm has been cut off!"
        elif self.health <= 0:
            health_line = "It is dead."
        return self._desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value


def hit(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Goblin:
            thing.health = thing.health - 1
            if thing.health <= 0:
                msg = "You killed the goblin!"
            else:
                msg = "You hit the {}".format(thing.class_name)
                thing.desc = "pitiful wounded {}".format(thing.class_name)
    else:
        msg = "There is no {} here.".format(noun)
    return msg

verb_dict = {
    "say": say,
    "examine": examine,
    "hit": hit,
    "check": show
}

goblin = Goblin("Gobbly")


def monster(monster):
    global times
    times = times + 1.01
    global elf_hp
    global wasp_hp
    elf = elf_hp
    wasp = wasp_hp
    if monster == "elf":
        while elf > 0:
            damage = random.randint(-1, 3)
            print("You HP:", you.hp)
            print("Her HP:", elf)
            status = input('Want to hit elf?(Y or N)\n')
            if status == "Y":
                elf = elf - damage
                if damage > 0:
                    if damage == 3:
                        print('rampage hit')
                    else:
                        print('normal hit')
                elif damage == 0:
                    print('The elf dodged')
                else:
                    print('You are beated back by elf')
                    elf = elf + damage
                    you.hp = you.hp - 1
                    if people.hp <= 0:
                        print('You are dead')
                        return
                if elf <= 0:
                    print('Elf dead')
                    you.ruby = you.ruby + 1
            else:
                print("you escaped")
                times = times - 1
                return
    if monster == "wasp":
        while wasp > 0:
            damage = random.randint(-2, 3)
            print("You hp:", you.hp)
            print("Her HP:", wasp)
            status = input('Want to hit wasp?(Y or N)\n')
            if status == "N":
                print("you escaped")
                times = times - 1
                return
            else:
                wasp = wasp - damage
                if damage > 0:
                    if damage == 3:
                        print('rampage hit')
                    else:
                        print('normal hit')
                elif damage == 0:
                    print('The wasp dodged')
                else:
                    print('You are beated back by wasp')
                    you.hp = you.hp - 1
                    wasp = wasp + damage
                    if you.hp <= 0:
                        print('You are dead')
                        return
        else:
            print('The wasp dead')
            you.ruby = you.ruby + 2

while True:
    if times <= 1:
        name = input("your name plz:")
        you = people(name, 10, 30, False)
        you.show()
    while (times == 50):
        print("pass")
    monster(monster=get_input())
