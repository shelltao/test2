# coding:utf-8


class Car(object):
    color = 'red'

    def __init__(self, logo):
        self.logo = logo


benz = Car('benz')
benz.color = 'white'
