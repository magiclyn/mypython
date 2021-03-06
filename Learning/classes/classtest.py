Foo = type('Foo',(),{'bar':True})

# print(Foo)

def echo_bar(self):
	# pass
	# print('111')
	print(self.tr)

FooChild = type('FooChild',(Foo,),{'echo_bar':echo_bar,'tr':True})


# print(FooChild)
my_foo = FooChild()

# print(my_foo.bar)
# print(my_foo.tr)

# print('222222222')
my_foo.echo_bar()

# print('222')

age = 35
print(age.__class__)

print(age.__class__.__class__)

print(age.__class__.__class__.__class__)


# 请记住，'type'实际上是一个类，就像'str'和'int'一样
# 所以，你可以从type继承
class UpperAttrMetaClass1(type):
    # __new__ 是在__init__之前被调用的特殊方法
    # __new__是用来创建对象并返回之的方法
    # 而__init__只是用来将传入的参数初始化给对象
    # 你很少用到__new__，除非你希望能够控制对象的创建
    # 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__
    # 如果你希望的话，你也可以在__init__中做些事情
    # 还有一些高级的用法会涉及到改写__call__特殊方法，但是我们这里不用
    def __new__(upperattr_metaclass, future_class_name, future_class_parents, future_class_attr):
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return type(future_class_name, future_class_parents, uppercase_attr)


class UpperAttrMetaclass2(type):
    def __new__(upperattr_metaclass, future_class_name, future_class_parents, future_class_attr):
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)

        # 复用type.__new__方法
        # 这就是基本的OOP编程，没什么魔法
        return type.__new__(upperattr_metaclass, future_class_name, future_class_parents, uppercase_attr)

class UpperAttrMetaclass3(type):
    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return type.__new__(cls, name, bases, uppercase_attr)


class UpperAttrMetaclass4(type):
    def __new__(cls, name, bases, dct):
        print("UpperAttrMetaclass4")
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return super(UpperAttrMetaclass4, cls).__new__(cls, name, bases, uppercase_attr)


class  Boss(object,metaclass=UpperAttrMetaclass4):
	# __metaclass__  = UpperAttrMetaclass4
	a = 1
	b = 3

boss = Boss()
# print(boss.a)
print(hasattr(Boss,'a'))

print(hasattr(Boss,'A'))
print(type(boss).__class__)
