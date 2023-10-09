import library , random

if __name__ == "__main__":
   #Создаём два экземлпяра воина
   Warrior1 = library.Warrior()
   Warrior2 = library.Warrior()
   
   #print(Warior1.health ) 

   #цикл идёт: Если здоровье одного из игроков достигнет нуля или меньше, то игра закончится.
   while Warrior1.health > 0 and Warrior2.health > 0:
    #Случайно выбираем атакующего игрока
    attacker = random.choice([Warrior1, Warrior2]) 
    #Если атакующий игрок - это warrior1, то защищаться будет warrior2, и наоборот
    if attacker == Warrior1:
         defense = Warrior2
         print("Атакует Воин 1!")
    else:
         defense = Warrior1
         print("Атакует Воин 2!")
    #Атакующий атакует защищающего 
    attacker.attack(defense)

    # Определяем победителя
   if Warrior1.health > 0:
       print("Воин 1 - победил")
   else:
       print("Воин -  2 победил!")