#Клас стек
class Stack:
	#Инициализация стека
	def __init__(self):
		self._stack = []
	#Снять со стека элемент
	def take(self):
		a=self._stack[len(self._stack)-1]
		self._stack=self._stack[:len(self._stack)-1]
		return a
	#Поместить элемент на стек
	def put(self, x):
		self._stack.append(x)
	#Количество элементов в стеке
	def __len__(self):
		return len(self._stack)
	#Представление в виде строки
	def __str__(self):
		return " : ".join(["%s" % e for e in self._stack])
#Клас очередь	
class Queue:
	#инициализация очереди
	def __init__(self,first,second):
		self.first=first
		self.second=second
	#Поместить элемент в очередь
	def put(self,x):
		self.second.put(x)
	#Взять элемент с очереди
	def take(self):
		temp=second._stack[0]
		TEMP=first.take()
		first.put(temp)
		temp=[]
		for i in range(1,len(second._stack)):
			temp.append(second._stack[i])
		second._stack=temp
		return TEMP
	#Представление очереди в виде строки
	def __str__(self):
		temp=str(first)
		for i in range(len(second._stack)):
			temp+=':'+str(second._stack[i])
		temp=temp.replace(' ','')
		return temp
#Создание двух обьектов класа стек и дописывание им по одному значению в конец
first=Stack()
second=Stack()
first.put(1)
second.put(5)
second.put(7)
#Взятие значения с конца стека
second.take()


#Создание очереди
queue=Queue(first,second)
#Вывод очереди на экран
print(queue)
#Дописывание в конец очереди значения
queue.put(10)
#Вывод очереди на экран
print(queue)
#Взятие значения с начала очереди
print(queue.take())
#Вывод очереди
print(queue)


		