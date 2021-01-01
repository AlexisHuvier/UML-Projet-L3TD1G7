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

    def generateTile(self,p,x,y):
        p=random.randint(0,100)
        if (p<33):
            T=Forest()
        elif (p<66):
            T=GreyTile()
        elif (p<101):
            T=WaterTile()
        return T


    def generateMap(self,x=10,y=10):

        b2=[0,0,0,0,0]
        housePos=[]
        for i in range(x):
            self.case.append([])
            for j in range(y):
                p=random.randint(1,5)
##                if (p==6):
##                    p=random.randint(0,4)
##                    if (b2[p]==0):
##                        b2[p]=1
##                        if (p==0):
##                            T=FastFood()
##                        elif (p==1):
##                            T=House()
##                            housePos=[i,j]
##                        elif (p==2):
##                            T=Library()
##                        elif (p==3):
##                            T=Pub()
##                        elif (p==4):
##                            T=University()
##                    else :
##                        p=random.randint(1,5)
##                        T=self.generateTile(p,i,j)
##                else :
                T=self.generateTile(p,i,j)
                self.case[i].append(T)
        for i in range(x*y//12):
            x1=random.randint(0,x-1)
            y1=random.randint(0,y-1)
            self.case[x1][y1]=Road()
        for i in range(x*y//12):
            x1=random.randint(0,x-1)
            y1=random.randint(0,y-1)
            self.case[x1][y1]=Sidewalk()
        for i in range(x):
            for j in range(y):
                if (issubclass(self.case[i][j].__class__,Road)):
                    x2=i
                    y2=j
                    r=random.randint(0,1)
                    if (r==0):
                        r=random.randint(0,1)
                        if (r==0):
                            while (x2>=0):
                                x2=x2-1
                                self.case[x2][y2]="R"
                        else :
                            while (x2<x-1):
                                x2=x2+1
                                self.case[x2][y2]="R"
                    else :
                        r=random.randint(0,1)
                        if (r==0):
                            while (y2>=0):
                                y2=y2-1
                                self.case[x2][y2]="R"
                        else :
                            while (y2<y-1):
                                y2=y2+1
                                self.case[x2][y2]="R"
                elif (issubclass(self.case[i][j].__class__,Sidewalk)):
                    x2=i
                    y2=j
                    r=random.randint(0,1)
                    if (r==0):
                        r=random.randint(0,1)
                        if (r==0):
                            while (x2>=0):
                                x2=x2-1
                                self.case[x2][y2]="S"
                        else :
                            while (x2<x-1):
                                x2=x2+1
                                self.case[x2][y2]="S"
                    else :
                        r=random.randint(0,1)
                        if (r==0):
                            while (y2>=0):
                                y2=y2-1
                                self.case[x2][y2]="S"
                        else :
                            while (y2<y-1):
                                y2=y2+1
                                self.case[x2][y2]="S"
        for i in range(x):
            for j in range(y):
                if(self.case[i][j]=="R"):
                    self.case[i][j]=Road()
                if(self.case[i][j]=="S"):
                    self.case[i][j]=Sidewalk()
        for i in range(len(b2)):
            if (b2[i]==0):
                b2[i]=1
                if (i==0):
                    T=FastFood()
                elif (i==1):
                    T=House()
                    housePos=[i,j]
                elif (i==2):
                    T=Library()
                elif (i==3):
                    T=Pub()
                elif (i==4):
                    T=University()
                x2=random.randint(0,x-1)
                y2=random.randint(0,y-1)
                while ((issubclass(self.case[x2][y2].__class__,Building))):
                    print(not(issubclass(self.case[x2][y2].__class__,Building)),self.case[x2][y2].__class__)
                    x2=random.randint(0,x-1)
                    y2=random.randint(0,y-1)
                self.case[x2][y2]=T
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
        print("display")
