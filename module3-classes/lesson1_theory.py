# CLASSES, атрибуты, методы
# классы – абстракции, которые совмещают в себе атрибуты(переменные) и методы, которые явл f
# классы замыкают в себе связку атрибутов и методов => замыкание логики
class EmptyClass:
    pass
class ClassWithAttribute:
    a = 5
class ClassWithAttributeAndMethod:
    # a = 5 # задать переменную статически - аттрибут
    def __init__(self, a): # динамически
        self.a = a
    def plus_one(self):
       self.a += 1
if __name__ == '__main__':
    empty_class = EmptyClass()
    class_attribute = ClassWithAttribute()
    class_attribute_method = ClassWithAttributeAndMethod(10) # создание класса с динамическим атрибутом
    class_attribute_method.plus_one()

    print(class_attribute.a)
    print(class_attribute_method.a) # результат метода plus_one - в поле 'а' этого метода


