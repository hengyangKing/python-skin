#coding=utf-8
#1.类也是对象，在大多数语言中类就是一组用来描述如何生成一个对象的代码段，在python中同样成立
#但是在python中类同样也是一种对象，
class ObjectCreator(object):
	pass
#将在内存中船舰一个对象，名字就是ObjectCreator，这个对象（类对象ObjectCreator）拥有创建对象（实例对象）的能力，但是他的本质仍然十一个对象，于是你可以对他进行如下操作：
#将他赋值给一个变量
#copy
#增加属性，（类属性）
#将他作为参数传递

obj = ObjectCreator();
print(type(obj));


#同样的你可以利用type（）创建出一个类，
Cat = type("Cat",(ObjectCreator,),{"name":""});
katty = Cat();
print(Cat.__class__);
print(katty.name);


#type实际上十一个元类，type就是python在备用用来创建所有类的元类，str是用来创建字符串对象的类，而int是用来创建整数对象的类，type就是创建类对象的类，可以通过__class__属性来观察到这一点，python中所有的东西都是对象，而他们都是从一个类创建而来，这个类就是type
