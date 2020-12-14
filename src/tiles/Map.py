import random
from src.tiles.Forest import Forest
from src.tiles.GreyTile import GreyTile
from src.tiles.Road import Road
from src.tiles.WaterTile import WaterTile
from src.tiles.Sidewalk import Sidewalk

from src.tiles.buildings.Building import Building
from src.tiles.buildings.FastFood import FastFood
from src.tiles.buildings.House import House
from src.tiles.buildings.Library import Library
from src.tiles.buildings.Pub import Pub
from src.tiles.buildings.University import University

class Map:
    """
    classe Map
    """
    case=[]

    def generateTile(self,p):
        if (p==1):
            T=Forest()
        elif (p==2):
            T=GreyTile()
        elif (p==3):
            T=Road()
        elif (p==4):
            T=WaterTile()
        elif (p==5):
            T=Sidewalk()
        return T


    def generateMap(self,x=10,y=10):
        
        b2=[0,0,0,0,0]
        housePos=[]
        for i in range(x):
            self.case.append([])
            for j in range(y):
                p=random.randint(1,6)
                if (p==6):
                    p=random.randint(0,4)
                    if (b2[p]==0):
                        b2[p]=1
                        if (p==0): 
                            T=FastFood()
                        elif (p==1):
                            T=House()
                            housePos=[i,j]
                        elif (p==2):
                            T=Library()
                        elif (p==3):
                            T=Pub()
                        elif (p==4):
                            T=University()
                    else :
                        p=random.randint(1,5)
                        T=self.generateTile(p)
                else :
                    T=self.generateTile(p)  
                self.case[i].append(T)
        for i in range(len(b2)):
            if (b2[i]==0):
                b2[i]=1
                if (p==0): 
                    T=FastFood()
                elif (p==1):
                    T=House()
                    housePos=[i,j]
                elif (p==2):
                    T=Library()
                elif (p==3):
                    T=Pub()
                elif (p==4):
                    T=University()
                x1=random.randint(0,x-1)
                y2=random.randint(0,y-1)
                if (not(issubclass(self.case[x1][y2].__class__,Building))):
                    print(not(issubclass(self.case[x1][y2].__class__,Building)))
                    self.case[x1][y2]=T
                else :
                    print("not spawn")
        return housePos
    
    def __init__(self):
        print("map")
        
    def __str__(self):
        return "map affichage"

    def affichage(self):
        for i in range(len(self.case)): 
            for j in range(len(self.case[i])):
                print(self.case[i][j]," | ",end='')
            print()
            
    def display(self):
        print("lol")

