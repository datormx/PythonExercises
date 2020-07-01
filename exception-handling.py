"""Keyboard Interrupt Error"""

try:
    inp = input()
    print('Press Ctrl+C or Interrupt the Kernel: ')
except KeyboardInterrupt:
    print('Caught KeyboardInterrupt')
else: 
    print('No exception occurred')


"""Zero Division Error"""

try:
    a = 100 / 10
    print(a)
except ZeroDivisionError:
    print("Zero Division Exception Raised.")
else:
    print('Success, no error!')


"""OverFlow Error"""

try:
    import math
    print(math.exp(1000))
except OverflowError:
    print('OverFlow Exception Raised')
else:
    print('Success, no error!')


"""Assertion Error"""

try:
    a = 100
    b = 'Python'
    assert a == b
except AssertionError:
    print('Assertion Exception Raised.')
else:
    print('Success, no error!')


"""Atribute Error"""

class Attributes(object):
    a = 2
    print(a)

try:
    object = Attributes()
    print(object.attribute)
except AttributeError:
    print('Attribute Exception Raised.')


"""Import Error"""

import nibabel


"""Key Error (LookupError)"""

try:
    a = {1:'a', 2:'b', 3:'c'}
    print(a[4])
except LookupError:
    print('Key Error Exception Raised')
else:
    print('Success, no error!')


"""Index Error (LookupError)"""

try:
    a = ['a', 'b', 'c']
    print(a[4])
except LookupError:
    print('Index Error Exception Raised, list index out of range')
else: 
    print('Success, no error!')


"""Name Error"""

try:
    print(ans)
except NameError:
    print("NameError: name 'ans' is not defined")
else: 
    print('Success, no error!')


"""Type Error"""

try:
    a = 'Python'
    b = 5
    c = a + b
    print(c)
except TypeError:
    print('TyperError Exception Raised')
else:
    print('Sucess, no error!')


"""Value Error"""

try:
    print(float('DataCamp'))
except ValueError:
    print('ValueError: could not convert string to float: \'DataCamp\'')
else:
    print('Sucess, no error!')


"""Python Custom Exception"""

class UnAcceptedValueError(Exception):
    def __init__(self, data):
        self.data = data
    
    
    def __str__(self):
        return repr(self.data)

    
total_marks = int(input('Enter Total Marks Scored: '))

try:
    num_of_sections = int(input('Enter num of sections: '))
    if(num_of_sections < 1):
        raise UnAcceptedValueError("Number of sections can\'t be less than 1")
except UnAcceptedValueError as e:
    print("Received error:", e.data)


"""Asserts AFIRMACIONES"""

a = 4

assert type(a) == str, 'No es str'

print(a)

