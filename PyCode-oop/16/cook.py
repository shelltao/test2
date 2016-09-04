# coding:utf-8


class Human(object):
    def __init__(self, name):
        self.name = name

    def speak(self, words):
        print self.name, 'say:', words


class Boy(Human):
    def buy_food(self, food):
        print self.name, 'go to buy:', food


class Girl(Human):
    def cook_food(self, food):
        print self.name, 'start cook food:', food
        return food


class SalesPerson(Human):
    price_sheet = None

    def check(self, good_name):
        price = self.price_sheet.get(good_name)
        if not price:
            self.speak('抱歉，没有%s' % good_name)
            return

        self.speak('%s 卖 %s$钱' % (good_name, price))
        return price

    def sale(self, good_name, money):
        Food = self.good_sheet.get(good_name)
        food = Food(good_name, money)
        self.speak('给你%s' % food)
        return food


class Food(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return '%s/价格:%s' % (self.name, self.price)


class Vegetable(Food):
    pass


class Meat(Food):
    pass


def main():
    dabai = Boy('dabai')
    dahong = Girl('dahong')

    dabai.speak('我饿了,想吃饭不会做,大红可以帮我吗？')

    dahong.speak('可以，你去买菜吧')
    dahong.speak('一颗白菜，一斤肉')

    check_list = ['白菜', '五花肉']

    sales = SalesPerson('卖菜的')
    sales.price_sheet = {
        '白菜': 3,
        '五花肉': 15,
    }
    sales.good_sheet = {
        '白菜': Vegetable,
        '五花肉': Meat,
    }

    food_list = []
    for food_name in check_list:
        dabai.buy_food(food_name)

        price = sales.check(food_name)
        if price:
            food = sales.sale(food_name, price)
            food_list.append(food)

    for food in food_list:
        dahong.cook_food(food)


if __name__ == '__main__':
    main()
