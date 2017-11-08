#coding=utf-8
class Foo(object):
    '''foo class'''

    def __init__(self):
        pass;

    def __str__(self):
        return ""

    def __getattr__(self, item):
        print(item,)
        return self

foo = Foo();
print(foo.think.different.foo);

