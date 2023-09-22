class Enemy(object):
    def __init__(self, name, life ):
        self.life = life
        self.name = name
        print(f'Welcome to the game {name}! You have {life} lives.')
    def attack(self):
        print('Ouch!')
        self.life = self.life- 1
    def checkLife(self):
        if self.life == 1:
            print('You can return to the start point to get +1 live.')
            inp = input('Press 5 to get +1 live or press anything to continue.')
            if inp == 5:
                self.life += 1
            else:
                print('You have 1 life left.')
        if self.life == 0:
            print('You are dead, game over.')
        else:
            print(f'{self.life} life(s) left!')
class Enemies(Enemy):
    def type(self):
        if self.name == 'Enemy 1':
            print('You are a zombie')
        elif self.name == 'Enemy 2':
            print('You are a monster')
        elif self.name == 'Enemy 3':
            print('You are a mouse')

enemy1 = Enemies('Enemy 1',4)
enemy1.type()
enemy1.attack()
enemy1.checkLife()
enemy1 = Enemies('Enemy 1', 4)
enemy1.type()
enemy2 = Enemies('Enemy 2', 3)
enemy2.type()
enemy3 = Enemies('Enemy 3', 2)
enemy3.type()
enemy1.attack()
enemy1.checkLife()
enemy1.attack()
enemy1.checkLife()
enemy2.attack()
enemy2.checkLife()
enemy3.attack()
enemy3.checkLife()
enemy1.attack()
enemy1.checkLife()