import library , random

if __name__ == "__main__":
   #Создаём два экземлпяра воина
   Warior1 = library.Warrior()
   Warior2 = library.Warrior()
   
   #print(Warior1.health ) 

   #цикл идёт: Если здоровье одного из игроков достигнет нуля или меньше, то игра закончится.
   while Warior1.health > 0 and Warior2.health > 0:
    #Случайно выбираем атакующего игрока
    attacker = random.choice([warrior1, warrior2]) 
    #Если атакующий игрок - это warrior1, то защищаться будет warrior2, и наоборот
    defense = warrior2 if attacker == warrior1 else warrior1
    #Атакующий атакует защищающего 
    attacker.attack(defense)

    # Определяем победителя
   if warrior1.health > 0:
       print("Воин 1 - победил")
   else:
       print("Воин -  2 победил!")