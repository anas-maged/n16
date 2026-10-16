import random
words = ["ugly", 'bad', 'doin']
agine = 6
list1 = []
hang_list = 0
hang =  ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
random_word = random.choice(words)
show = ["_"for _ in random_word]
print("Welcom to the hangman!" )
print("\nYou have 6 tries")
print(f"\n{" ".join(show)}\n\n{hang[0]}\n")
while " ".join(show) != random_word and agine!= 0:
    us = input("Plese guese a letter: ").lower()
    if len(us) == 1:
        print("")
    else:
        print("Sorry enter the one letter!")
        continue
    for i in list1:
        if us == i:
            print("you already guessed That, try agine")
            continue
    list1.append(us)
    found = False
    for th in random_word:
        if th == us :
            for loc in range(len(random_word)):
                if us == random_word[loc]:
                    show[loc] = us
                    found = True
    if found == False:
            agine -= 1
            hang_list += 1
    print(hang[hang_list])
    print(" ".join(show))
    print(f"\nyou have {agine} tries")
if agine == 0 :
    print(f"""you lost
    \n\n{hang[hang_list]}""")
else:
    print("""********Good you win********""")
