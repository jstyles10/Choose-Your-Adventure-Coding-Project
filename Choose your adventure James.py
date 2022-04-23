from PIL import Image
name = input("Type your name:")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road with a zombie apocalypse chasing you, it has come to an end and you can go left or right, which way do you go?").lower()
image1 = Image.open('zomB.jpg')
image1.show('zomB.jpg')
if answer == "left":
    answer = input("You are now near a house in the middle of a forest, do you want to enter in or walk further? house/walk")
    if answer == "house":
        print("You walk into the house, and there's zombies inside and eat you alive! You died.")
    elif answer == "walk":
        print("You walk further and are now surrounded by zombies. They eat you alive and you died.")
if answer == "right":
    print("You run faster to escape the zombies from eating you.")
    answer = input("You come to a bridge with a portal on the other side, do you walk over the bridge or turn around? back/cross")
    image1 = Image.open('bridge.jpg')
    image1.show('bridge.jpg')
if answer == "back":
        print("You turn around to see zombies who then eat you.")
elif answer == "cross":
    print("You cross the bridge safely.")
    answer = input("You now have to make the decision into entering the mysterious portal or fight the zombies? Which do you choose? enter/fight").lower()
    image1 = Image.open('portal.webp')
    image1.show('portalwebp')
    if answer ==  "fight":
        print("You fight the zombies but are quickly getting attacked back and the zombies ambush you. You died!")
if answer == "enter":
    print("You have entered the portal and now  return back to your house.")
    answer = input(" You open the curtains to see zombies trying to enter through your window, do you attack them or close the window? attack/close")
if answer == "close":
        print("You close the windows quickly with no zombies entering in time.")
elif answer == "attack":
        print("You get more zombies entering your house and they eat you alive!")
answer = input("You then go into the kitchen to encounter a zombie going to attack you. You have a glass on the side of the table, do you attack it with your bare hands or the glass? glass/hands")
if answer == "hands":
            print("The zombie has eaten you. You die.")
if answer == "glass":
    print("You have killed the zombie.")
    answer = input("You then proceed to go to the bed. You then see a rocket launcher on your bed. Do you use it to kill the zombies or try and fight all the zombies with your fists?  rocketlauncher/barehands")
if answer == "rocketlauncher":
        print("You have succesfully killed all the zombies and survive the day and go to bed! You WIN!!")
        image1 = Image.open('rocketlauncher.jpg')
        image1.show('rocketlauncher.jpg')
elif answer == "barehands":
    print("You died after being surrounded and eated by the zombies.")
    

       
else:
    print('Not a valid option.You lose.')

