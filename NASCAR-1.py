##################################
##
##   James Hudspeth
##   CSC102
##   Week13 Assignmnet
##   12/01/16
##   NASCAR
##
##################################

from random import randint

name = ['Mark','James','Steve','Lovecraft','Cthulhu','Dresden','Murphy','Steven','Bob','Meliodas','Arthur','Merlin','Booker','Andrew Ryan','John','Larry','Simone','Nathan','Dave','Raiden']
sponsor = ['UAT','Miskatonic U','Apple','Weird Tales',"R'lyeh",'Paranet','CPD','Universe','Burgers','Britannia','Camelot','WC','Columbia','Rapture','Coca Cola','Dr Pepper','Epica','Dethklok','Megadeth','Mortal Kombat']



class Car():
    """ This class simulates a NASCAR race with 20 cars racing 500 miles
    This class will contain the following attributes:
    Total Odometer Miles
    Speed in mph
    Driver Name
    Sponsor"""

    def __init__(self,name,sponsor,number):
        self.name = name
        self.sponsor = sponsor
        self.miles = 0
        self.speed = 0
        self.number = number

    def __str__(self):
        output = '\nCar#{}\n\tName: {}\n\tSponsor: {}\n\tMiles: {:.2f}\n\tSpeed: {:.2f}' \
                 .format(self.number,self.name,self.sponsor,self.miles,self.speed)
        return output

    def update(self):
        ## Cheat speeds
        if self.name == 'Mark':
            self.speed = randint(2,125)
        ## Speed
        else: self.speed = randint(1,120)
        ## Odometer tracking
        self.miles += self.speed/60


## Program Run
while True:

    place = 0
    cars = []

    print('====================================================')
    print()

    ## Build cars
    for x in range(len(name)):
        cars += [Car(name[x],sponsor[x],x+1)]
        ##print(cars[x])

    ## Race cars
    while cars[0].miles < 500:
        for x in range(len(cars)):
            cars[x].update()
        cars.sort(key = lambda x: x.miles, reverse = True)

    ## Results
    for x in range(len(cars)):
        place += 1
        print()
        print(place,' place goes to:')
        print(cars[x])
    print('====================================================')
    input('Press <Enter> to race again')
    
