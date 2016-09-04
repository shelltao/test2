# coding:utf-8


class Human(object):
    def speak

    def eat

    def xxx


class Base(object):
    def get_context(self):
        #  操作底层model拿到数据
        news_list = []
        result = {
            'news': news_list,
            'pages': pages,
            'user': self.user
        }
        return result


class IPLocationMixin(object):
    pass

class Page(IPLocationMixin, Base):
    def get_context(self):
        result = super(Page, self).get_context()
        result.update({
            'user': self.user,
            'location': iptools.locat(self.ip),
        })
        return result

    def render(self):
        context = self.get_context()

        # 渲染页面


class API(Base):
    def get_context(self):
        result = super(API, self).get_context()
        news_list = result['news_list']
        # 进行计算
        has_next = True
        result.update({
            'has_next': has_next
        })


class AP(object):
    def say(self):
        print 'ap'


class A(AP):
    name = 'A'

    def say(self):
        super(A, self).say()
        t = 1 + 1
        print 'A say hi'
        return t


class D(A):
    def say(self):
        result = super(D, self).say()
        print 'D say hi'
        result = result * 10
        return result

d = D()
d.say()
