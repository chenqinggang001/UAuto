

class BaseFiled(object):
    pass


class CharFiled(BaseFiled):
    def __init__(self, max_lenght=20):
        self.max_lenght = max_lenght

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        # 类型限制
        if isinstance(value,str):
            if len(value) <= self.max_lenght:
                self.value = value
            else:
                raise ValueError('长度应该在%s以内'%self.max_lenght)
        else:
            raise TypeError('need a str')

    def __delete__(self, instance):
        # del self.value
        self.value = None

class IntFiled(BaseFiled):
    def __init__(self, max_lenght=20):
        self.max_lenght = max_lenght

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        # 类型限制
        if isinstance(value,int):
            if len(value) <= self.max_lenght:
                self.value = value
            else:
                raise ValueError('长度应该在%s以内'%self.max_lenght)
        else:
            raise TypeError('need a int')

    def __delete__(self, instance):
        # del self.value
        self.value = None

class BoolFiled(BaseFiled):

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        # 类型限制
        if isinstance(value,bool):
            self.value = value
        else:
            raise TypeError('need a bool')

    def __delete__(self, instance):
        # del self.value
        self.value = None



# class UserModel(object):
#     # 模型类
#     name = CharFiled(max_lenght=2)   # 假设只能赋值字符串
#     pwd = CharFiled()

# m = UserModel()

# m.name = '999'
# type()
# print(m.name)