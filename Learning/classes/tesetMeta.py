class Meta(type):

    def __new__(meta, cls_name, base_clses, cls_attrs):
        print ("============Meta_new==============")
        print ("meta", meta)
        print ("class name", cls_name)
        print ("base classes", base_clses)
        print ("class attrs", cls_attrs)
        instance = super(Meta, meta).__new__(meta, cls_name, base_clses, cls_attrs)
        print ("=============Meta_new============")
        return instance

    def __init__(cls_obj, cls_name, base_clses, cls_attrs):
        print("============Meta_init============")
        print(cls_obj)
        print ("class name", cls_name)
        print ("base classes", base_clses)
        print ("class attrs", cls_attrs)
        print ("============Meta_init===========")

    def __call__(cls_obj,  *args, **kwargs):
        print ("=============Meta_call==========")
        print ("class obj" , cls_obj)
        instance = super(Meta, cls_obj).__call__(*args, **kwargs)
        print ("=============Meta_call==========")
        return instance


class Foo(object,metaclass=Meta):
    # __metaclass__ = Meta

    def __new__(cls):
        print (cls)
        print ('Foo.__new__')
        return super(Foo, cls).__new__(cls)

    def __init__(self):
        print ('Foo.__init__')

if __name__ == '__main__':
    Foo()
    print (type.__call__(Foo))