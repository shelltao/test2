def say():
    print 1
    print 2
    t = 11
    n = 0

    import pdb;pdb.set_trace()

    r = t / n

    print t
    return 'hello'


def hi():
    print 'hi'
    say()
    print 'dddd'


hi()
