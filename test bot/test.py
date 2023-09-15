from itertools import repeat
import pyautogui as auto
from time import sleep
import keyboard

def CheckForBattle():
    
    book = auto.locateOnScreen("img/book.png", confidence=0.7, grayscale=True)
    if (book):
        print("not in battle, waiting...")
        sleep(2)
        return False
    else:
        return True
        
def SelectSpell():
    spell = auto.locateOnScreen("img/unenchanted.png", confidence= 0.7, grayscale=True)

    if (spell):
        button = auto.center(spell)
        auto.click(button)
        sleep(0.1)
        auto.click(button)
        auto.move(0,200)
        CastSpell()



def SelectEnchant():
    enchant = auto.locateOnScreen("img/enchant.png", confidence= 0.7, grayscale=True)
    if (enchant):
        auto.move(0,300, duration=1)
        sleep(0.5)
    if (enchant):
        button = auto.center(enchant)
        auto.click(button)
        auto.click(button)
        sleep(0.3)
        auto.move(0,200)
        SelectSpell()

    CheckForBattle()
    sleep(3)

def CastSpell():
    enchanted = auto.locateOnScreen("img/enchanted.png", confidence= 0.7, grayscale=True)
    passss = auto.locateOnScreen("img/passss.png", confidence= 0.7, grayscale=True)
    repeat (2)
    if (enchanted):
        button = auto.center(enchanted)
        auto.click(button)
        sleep(0.2)
        auto.click(button)
        print("casting")
    else:
        passss
        button = auto.center(passss)
        auto.click(button)
        sleep(0.2)
        auto.click(button)

def Wander():
    with auto.hold("D"):
        auto.sleep(2)

def CheckMana():
    
        sleep(2)
        mana = auto.locateOnScreen("img/mana.png", confidence=0.7, grayscale=True)
        potion = auto.locateOnScreen("img/potion.png", confidence=0.7, grayscale=True)
        button = auto.center(potion)

        if (mana):
            auto.click(button)
            sleep(0.2)
            auto.click(button)
            
def main():

    while True:
        window = auto.locateOnScreen("img/window.png", confidence=0.7, grayscale=True)
        if (window == False):
            break
        else:
            battle = CheckForBattle()
            if (battle):
                SelectEnchant()
                
            else:
                Wander()
                CheckForBattle()
                
main()



