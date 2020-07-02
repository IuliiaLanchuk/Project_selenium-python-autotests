class BasePage():
	def __init__(self, browser, url):
		self.browser = browser
		self.url = url
	
	def open(self):
		self.browser.get(self.url)

#Теперь в наш класс нужно добавить методы. Первым делом добавим конструктор — метод, который вызывается, когда мы создаем объект. Конструктор объявляется ключевым словом __init__. 
#В него в качестве параметров мы передаем экземпляр драйвера и url адрес. 
#Внутри конструктора сохраняем эти данные как аттрибуты нашего класса.