class Computer:
    def __init__(self, cpu: str, ram: int):
        self.cpu = cpu
        self.ram = ram
        self.disk = 10*2**32
    
    @staticmethod
    def start():
        print('запуск компьютера')
    
    def __call__(self):
        print('вызов экземпляра')
        return self.start()


pc = Computer('i7-3970x', 16*2*30)

# >>> pc()
# вызов экземпляра
# запуск компьютера
