'''import welcome
welcome.welcome_message('CS')

import welcome as obj
obj.welcome_message('eng')'''

'''import random
print('wtf', random.randint(1,10))
'''
'''
import random as rand
for i in range(3):
    print('randon n ',rand.random())'''

'''import random as rand
rand.seed(10)
for i in range(3):
    print('randon n ',rand.random())'''

import random as rand
import time as t

rand.seed(t.time())
for i in range(3):
    print('randon n ',rand.random())