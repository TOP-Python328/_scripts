class Test:
    
    def hello():
        print('привет!')
    
    def print_arg(arg=None):
        print(arg)


instance = Test()


# >>> Test.hello
# <function Test.hello at 0x000002C085592CA0>

# >>> Test.hello()
# привет!


# >>> instance.hello
# <bound method Test.hello of <__main__.Test object at 0x000002C085588090>>

# >>> instance.hello()
# ... 
# TypeError: Test.hello() takes 0 positional arguments but 1 was given


# при вызове связанного метода от экземпляра происходит подмена вызова
# instance.hello() --> Test.hello(instance)


# >>> Test.print_arg()
# None

# >>> instance.print_arg()
# <__main__.Test object at 0x0000025003F309D0>

