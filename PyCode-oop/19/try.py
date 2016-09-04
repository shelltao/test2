# coding:utf-8

try:
    t = 1 / a
    t = t + 1000
except ZeroDivisionError as e:
    print e, 'zero error'

except (StandardError, Exception) as e:
    f.close()
    print e, 'exception'

else:
    print 'nothing exception'

finally:
    print 'finally'
