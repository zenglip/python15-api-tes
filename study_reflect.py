class People:
    number_eye = 2

    def __init__(self,name,age):
        self.name = name
        self.age = age

if __name__ == '__main__':
    p = People('moo',18)
    print(hasattr(People,'number_leg'))
    print(hasattr(People, 'number_eye'))

    print(getattr(People,'number_eye'))
    print(getattr(p,'number_eye'))
    print(getattr(p,'age'))

    setattr(p,'dance',True)
    print('新加对象属性：',p.dance)