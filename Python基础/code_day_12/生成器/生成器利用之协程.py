#coding=utf-8
def test1():
	while True:
		print("------1------");
		yield None

def test2():
	while True:
		print("-------2------");
		yield None

t1 = test1();
t2 = test2();
i = 0;
while i<10:
	t1.__next__();
	t2.__next__();
	i+=1;
