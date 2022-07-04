from time import sleep
import os, random

def lang_ver():
    clear()
    print("Choose your language \ Wybierz język:\n\t1. English\n\t2. Polski")
    lang = input("Write \ Wpisz: 1 or \ lub 2\n\t")
    if not (lang == '1' or lang == '2'):
        print("Error - type 1 or 2! \ Błąd - wpisz 2 lub 1!")
        sleep(1)
        line()
        lang_ver()
    lvl_ver(int(lang)-1)

def lvl_ver(lang):
    print(['Pick the difficulty level:\n\t1. Easy - 10 attempts + 6 last letters,\n\t2. Medium - 8 attempts + 3 last letters,\n\t3. Hard - 6 attempts.\nChoose 1, 2 or 3', 'Wybierz poziom trudności:\n\t1. Łatwy - 10 prób + 6 ostatnich liter,\n\t2. Średni - 8 prób + 3 ostatnie litery,\n\t3. Trudny - 6 prób.\nWybierz 1, 2 lub 3'][lang])
    lvl = input("\t")
    if  not (lvl == "1" or lvl == "2" or lvl == "3"):
        print(["Error - type 1, 2 or 3!", "Błąd - wpisz 1, 2 lub 3!"][lang])
        sleep(1)
        line()
        lvl_ver(lang)
    hangman(lang, int(lvl)-1)

def line():
    print("\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ \n")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_out(lang, lives, last, hit):
    hang =[
    """

        
        
        
        
        
        
    ________________""",
    """

        |
        | 
        |  
        |  
        |  
        |
    ____|____________""",
    """

        |/    
        |     
        |      
        |      
        |     
        |
    ____|____________""",
    """
         _______
        |/    
        |    
        |    
        |     
        |    
        |
    ____|____________""",
    """
         _______
        |/      
        |      
        |      
        |       
        |     
        |
    ____|____________""",
    """
         _______
        |/      |
        |      
        |      
        |       
        |      
        |
    ____|____________""",
    """
         _______
        |/      |
        |      (_)
        |      
        |       
        |      
        |
    ____|____________""",
    """
         _______
        |/      |
        |      (_)
        |       |
        |       |
        |      
        |
    ____|____________""",
    """
         _______
        |/      |
        |      (_)
        |       |/
        |       |
        |     
        |
    ____|____________""",
    """
         _______
        |/      |
        |      (_)
        |      \|/
        |       |
        |      
        |
    ____|____________""",
    """
         _______
        |/      |
        |      (_)
        |      \|/
        |       |
        |      / 
        |
    ____|____________""",
    """
         _______
        |/      |
        |      (_)
        |      \|/
        |       |
        |      / \\
        |
    ____|___________"""
        ]
    intro = [
    """

    ██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
    ██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
    ███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
    ██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
    ██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
    ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝""",
    """
        
    ░██╗░░░░░░░██╗██╗░██████╗██╗███████╗██╗░░░░░███████╗░█████╗░
    ░██║░░██╗░░██║██║██╔════╝██║██╔════╝██║░░░░░██╔════╝██╔══██╗
    ░╚██╗████╗██╔╝██║╚█████╗░██║█████╗░░██║░░░░░█████╗░░██║░░╚═╝
    ░░████╔═████║░██║░╚═══██╗██║██╔══╝░░██║░░░░░██╔══╝░░██║░░██╗
    ░░╚██╔╝░╚██╔╝░██║██████╔╝██║███████╗███████╗███████╗╚█████╔╝
    ░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝╚══════╝╚══════╝╚══════╝░╚════╝░"""
    ]
    clear()
    print(intro[lang])
    hit = " ".join(hit)
    print([f"\nWORD: {hit}", f"\nHASŁO: {hit}"][lang])
    print(hang[11-lives])
    if lives != 0:
        print([f"\nYou have {lives} lives left!", f"\nPozostało jeszcze {lives} prób!"][lang])
    if last != []:
        last = " ".join(last)
        print([f"Last used letters: \t\t{last}\n", f"Ostatnio użyte litery: \t\t{last}\n"][lang])

def vocabulary(lang):
    f = open('pl.txt' if lang == 1 else 'en.txt')
    fhand = list()
    for i, line in enumerate(f):
        fhand.append(line)
    return list(fhand[random.randint(0,i)].rstrip())

def another_game(lang):
    ans = input([f"Do you want to play again? (Y / N)\n\t", f"Chcesz zagrać jeszcze raz? (T/N)\n\t"][lang])
    if ans.upper() == "T" or ans.upper() == "Y":
        clear()
        lvl_ver(lang)
    elif ans.upper() == "N":
        quit()
    else:
        print([f"Type Y for yes or N for no.\n", f"Wpisz T dla tak lub N dla nie.\n"][lang])
        line()
        another_game(lang) 


def get_letter(lang):
    letter = ""
    while True:
        letter = input(["Guess a letter!\n\t", f"Jaki jest twój strzał?\n\t"][lang])
        if (letter.isalpha() and len(letter) == 1):
            return letter.upper()
        else:
            print([f"\"{letter}\" is not a single letter. Try one more time!\n", f"\"{letter}\" nie jest pojedyńczą literą. Spróbuj jeszcze raz!\n"][lang])


def hangman(lang, lvl):
    word = vocabulary(lang)
    hit = ["_"] * len(word)
    if lvl == 0:
        lives = 10
        last = [" "] * 6
    elif lvl == 1:
        lives = 8
        last = [" "] * 3
    elif lvl == 2:
        lives = 6
        last = []
    while True:
        print_out(lang, lives, last, hit)
        letter = get_letter(lang)
        last.append(letter)
        last.pop(0)
        if letter in word:
            print([f"Good job! The letter {letter} is in the word you are looking for!", f"Udało się! Litera {letter} jest w szukanym słowie!"][lang])
            for i in enumerate(word):
                if i[1] == letter:
                    hit[i[0]] = letter
                    word[i[0]] = " "
            if not "_" in hit:
                line()
                print(["YOU WIN! The search word is " + "".join(hit), "WYGRAŁEŚ! Szukane słowo to " + "".join(hit)][lang])
                line()
                sleep(1)
                another_game(lang)    
        elif letter in hit:
            print([f"{letter} is already in the word you are searching for, you miss the try.", f"{letter} jest już w szukanym słowie, tracisz próbę."][lang])
            lives -= 1
        else:
            print([f"The letter {letter} is not in the word you are looking for, you miss the try.", f"Litery {letter} nie ma w szukanym słowie, tracisz próbę."][lang])
            lives -= 1
        if lives == 0:
            print_out(lang, lives, last, hit)
            line()
            for i in enumerate(hit):
                if i[1] == "_":
                    hit[i[0]] = word[i[0]]
            
            print(["You failed! The word you are looking for is " + "".join(hit), "Nie udało ci się! Szukane słowo to " + "".join(hit)][lang])
            line()
            another_game(lang)
      
lang_ver()