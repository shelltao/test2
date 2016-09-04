import sys
import time
from collections import deque
#fancy_loading = deque('>--------------------')
fancy_loading = deque('123456')
while True:
    print '\r%s' % ''.join(fancy_loading),
    fancy_loading.rotate(1)
    sys.stdout.flush()
    time.sleep(1)