import library , random

if __name__ == "__main__":
   Warior1 = library.Warrior()
   Warior2 = library.Warrior()
   
   print(Warior1.health ) 

   while Warior1.health > 0 and Warior2.health > 0:
    attacker = random.choice([warrior1, warrior2])
    defender = warrior2 if attacker == warrior1 else warrior1
    attacker.attack(defender)