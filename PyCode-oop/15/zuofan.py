# coding:utf-8


class Human:
    guo = 'pingbiguo'

    def __init__(self, name):
        self.name = name

    def say(self, words):
        print self.name, 'say', words


class Dog:
    def __init__(self, name):
        self.name = name

    def cook_food(self, food):
        print self.name, 'cook', food


class Boy(Human):
    def buy_food(self, food_name):
        print self.name, 'buy', food_name
        return food_name


class Girl(Human):

    def cook_food(self, food_name):
        print self
        print self.name, 'shiyong', self.guo, 'cook', food_name
        return food_name


if __name__ == '__main__':

    dabai = Boy('dabai')
    dahong = Girl('dahong')

    Girl.cook_food(dahong, 'baicai')

    dahong.cook_food('baicai')

    print type(dahong)
