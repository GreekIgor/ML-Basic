class File:
    def __init__(self, name, size, date_create, owner):
        self.name = name
        self.size = size
        self.date_create = date_create
        self.owner = owner

    def save(self):
        print('сохранение')

    def convert(self, type):
        print(f'конвертация фаила в ${type}')
        

class Media(File):
    def play(self):
        print(f'Проигрывание фаила - {self.name}')

    def stop(self):
        print(f'остановка проигрывания фаила {self.name}')

class FTPServer(File):
    
    def __init__(self, name, size, date_create, owner, ip, login, pwd):
        super().__init__(name, size, date_create, owner)
        self.ip = ip
        self.login = login
        self.pwd = pwd

    def connect(self):
        print(f'соединение по ip {self.ip}')

    def download(self):
        print(f'скачивание фаила {self.name} ip {self.ip}')


mp3 = Media('Преступление.mp3', 300, '2025-02-01', 'volodya')
mp3.play()

ftp = FTPServer('Преступление.mp3', 300, '2025-02-01', 'volodya', '76.112.41.7', 'test', '123qaz')
ftp.connect()
ftp.convert('mp4')

