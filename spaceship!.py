PLANET='earth'
NAME=''
WEIGHT=''

def startup():
    global NAME
    print(" Are you ready to travel throuhg space? (km/s)")
    NAME=input('What is your name? ')
    start_menu()

def start_menu():
    global NAME
    global PLANET
    print("Hi "+NAME)
    print('1. Start Game\n2. Load Planet')
    choice=input('Choice: ')
    if choice=='1' or 'start game': 
        weight=input(" What is your ship weight? ")
        location() 
    elif choice=='2':def take_off():
        
    global PLANET
    dest = input("What planet do you want to go to? ").lower()
    spd=float(input("What speed do you want to go? (in km/s) "))
    if PLANET=='Jupiter':
        esc=20
        check(esc,spd,dest)
    else:
        print('Where are you?!')
        start_menu()

def check(esc,spd,dest):
    global PLANET
    if spd < esc:
        print('NOT FAST ENOUGH!!! BOOOOM!')
        start_menu()
    elif spd <= (esc * 1.1):
        print('YAY! You made it to %s' % dest)
        PLANET = dest
        location()
    elif spd > (esc * 1.1):
        print('BOOM! YOU BURNED UP GOING TOO FAST!')
        start_menu()
    else:
        print(" Your in Surious Trouble!!!!")
        take_off()

def location():
    global PLANET
    print('''You are currently on the planet %s''' %PLANET.title())
    take_off()
        print("loading") 
        start_menu()
    else:
        print('INVALID ENTRY') 
        start_menu()

def take_off(): 
    global PLANET
    dest = input("What planet do you want to go to? ").lower()
    spd=float(input("What speed do you want to go? (in km/s) "))
    if PLANET=='Mars':
        esc=15
        check(esc,spd,dest)
    else:
        print(" You made it to Mars!! ")
        start_menu()

def check(esc,spd,dest):
    global PLANET
    if spd < esc:
        print('NOT FAST ENOUGH!!! BOOOOM!')
        start_menu()
    elif spd <= (esc * 1.1):
        print('YAY! You made it to %s' % dest)
        PLANET = dest
        location()
    elif spd > (esc * 1.1):
        print('BOOM! YOU BURNED UP GOING TOO FAST!')
        start_menu()
    else:
        print(" Your in Surious Trouble!!!!")
        take_off()

def location():
    global PLANET
    print('''You are currently on the planet %s''' %PLANET.title())
    take_off()
def take_off(): 
    global PLANET
    dest = input("What planet do you want to go to? ").lower()
    spd=float(input("What speed do you want to go? (in km/s) "))
    if PLANET=='Jupiter':
        esc=25
        check(esc,spd,dest)
    else:
        print('Where are you?!')
        start_menu()

def check(esc,spd,dest):
    global PLANET
    if spd < esc:
        print('NOT FAST ENOUGH!!! BOOOOM!')
        start_menu()
    elif spd <= (esc * 1.1):
        print('YAY! You made it to %s' % dest)
        PLANET = dest
        location()
    elif spd > (esc * 1.1):
        print('BOOM! YOU BURNED UP GOING TOO FAST!')
        start_menu()
    else:
        print(" Your in Surious Trouble!!!!")
        take_off()

def location():
    global PLANET
    print('''You are currently on the planet %s''' %PLANET.title())
    take_off()

def take_off(): 
    global PLANET
    dest = input("What planet do you want to go to? ").lower()
    spd=float(input("What speed do you want to go? (in km/s) "))
    if PLANET=='Saturn':
        esc=35
        check(esc,spd,dest)
    else:
        print('Where are you?!')
        start_menu()

def check(esc,spd,dest):
    global PLANET
    if spd < esc:
        print('NOT FAST ENOUGH!!! BOOOOM!')
        start_menu()
    elif spd <= (esc * 1.1):
        print('YAY! You made it to %s' % dest)
        PLANET = dest
        location()
        
    elif spd > (esc * 1.1):
        print('BOOM! YOU BURNED UP GOING TOO FAST!')
        start_menu()
    else:
        print(" Your in Surious Trouble!!!!")
        take_off()

def location():
    global PLANET
    print('''You are currently on the planet %s''' %PLANET.title())
    take_off()

def take_off(): 
    global PLANET
    dest = input("What planet do you want to go to? ").lower()
    spd=float(input("What speed do you want to go? (in km/s) "))
    if PLANET=='Uranus':
        esc=50
        check(esc,spd,dest)
    else:
        print('Where are you?!')
        start_menu()

def check(esc,spd,dest):
    global PLANET
    if spd < esc:
        print('NOT FAST ENOUGH!!! BOOOOM!')
        start_menu()
    elif spd <= (esc * 1.1):
        print('YAY! You made it to %s' % dest)
        PLANET = dest
        location()
    elif spd > (esc * 1.1):
        print('BOOM! YOU BURNED UP GOING TOO FAST!')
        start_menu()
    else:
        print(" Your in Surious Trouble!!!!")
        take_off()

def location():
    global PLANET
    print('''You are currently on the planet %s''' %PLANET.title())
    take_off()

def take_off(): 
    global PLANET
    dest = input("What planet do you want to go to? ").lower()
    spd=float(input("What speed do you want to go? (in km/s) "))
    if PLANET=='Neptune':
        esc=65
        check(esc,spd,dest)
    else:
        print('Where are you?!')
        start_menu()

def check(esc,spd,dest):
    global PLANET
    if spd < esc:
        print('NOT FAST ENOUGH!!! BOOOOM!')
        start_menu()
    elif spd <= (esc * 1.1):
        print('YAY! You made it to %s' % dest)
        PLANET = dest
        location()
    elif spd > (esc * 1.1):
        print('BOOM! YOU BURNED UP GOING TOO FAST!')
        start_menu()
    else:
        print(" Your in Surious Trouble!!!!")
        take_off()

def location():
    global PLANET
    print('''You are currently on the planet %s''' %PLANET.title())
    take_off()

def take_off(): 
    global PLANET
    dest = input("What planet do you want to go to? ").lower()
    spd=float(input("What speed do you want to go? (in km/s) "))
    if PLANET=='Venus':
        esc=15
        check(esc,spd,dest)
    else:
        print('Where are you?!')
        start_menu()

def check(esc,spd,dest):
    global PLANET
    if spd < esc:
        print('NOT FAST ENOUGH!!! BOOOOM!')
        start_menu()
    elif spd <= (esc * 1.1):
        print('YAY! You made it to %s' % dest)
        PLANET = dest
        location()
    elif spd > (esc * 1.1):
        print('BOOM! YOU BURNED UP GOING TOO FAST!')
        start_menu()
    else:
        print(" Your in Surious Trouble!!!!")
        take_off()

def location():
    global PLANET
    print('''You are currently on the planet %s''' %PLANET.title())
    take_off()

def take_off(): 
    global PLANET
    dest = input("What planet do you want to go to? ").lower()
    spd=float(input("What speed do you want to go? (in km/s) "))
    if PLANET=='Mercury':
        esc=2
        check(esc,spd,dest)
    else:
        print('Where are you?!')
        start_menu()

def check(esc,spd,dest):
    global PLANET
    if spd < esc:
        print('NOT FAST ENOUGH!!! BOOOOM!')
        start_menu()
    elif spd <= (esc * 1.1):
        print('YAY! You made it to %s' % dest)
        PLANET = dest
        location()
    elif spd > (esc * 1.1):
        print('BOOM! YOU BURNED UP GOING TOO FAST!')
        start_menu()
    else:
        print(" Your in Surious Trouble!!!!")
        take_off()

def location():
    global PLANET
    print('''You are currently on the planet %s''' %PLANET.title())
    take_off()


startup()
