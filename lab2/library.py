class Warrior:
    # конструктор класса, задаем начальные значения здоровья и урона
    def __init__(self):
        self.health = 100
        self.damage = 20
        

# метод атаки, уменьшает здоровье противника на значение урона текущего воина
    def attack(self, enemy):
        enemy.health -= self.damage #enemy.health = enemy.health - self.damage 
        print(f"Warrior attacked! Enemy health: {enemy.health}")
    