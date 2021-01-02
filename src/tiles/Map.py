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
    def __init__(self):
        print("construct")
        self.case=[]

    def generateTile(self,p,x,y):
        p=random.randint(0,100)
        if (p<33):
            T=Forest([x*64, y*64])
        elif (p<66):
            T=GreyTile([x*64, y*64])
        elif (p<101):
            T=WaterTile([x*64, y*64])
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
            self.case[x1][y1]=Road([x1*64, y1*64])
        for i in range(x*y//12):
            x1=random.randint(0,x-1)
            y1=random.randint(0,y-1)
            self.case[x1][y1]=Sidewalk([x1*64, y1*64])
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
                    self.case[i][j]=Road([i*64, j*64])
                if(self.case[i][j]=="S"):
                    self.case[i][j]=Sidewalk([i*64, j*64])
        for i in range(len(b2)):
            if (b2[i]==0):
                b2[i]=1
                x2=random.randint(0,x-1)
                y2=random.randint(0,y-1)
                while ((issubclass(self.case[x2][y2].__class__,Building))):
                    print(not(issubclass(self.case[x2][y2].__class__,Building)),self.case[x2][y2].__class__)
                    x2=random.randint(0,x-1)
                    y2=random.randint(0,y-1)
                self.case[x2][y2]=T
                if (i==0):
                    T=FastFood([x2*64, y2*64])
                elif (i==1):
                    T=House([x2*64, y2*64])
                    housePos=[x2,y2]
                elif (i==2):
                    T=Library([x2*64, y2*64])
                elif (i==3):
                    T=Pub([x2*64, y2*64])
                elif (i==4):
                    T=University([x2*64, y2*64])
        return housePos

    def __str__(self):
        return "map affichage"

    def affichage(self):
        for i in range(len(self.case)):
            for j in range(len(self.case[i])):
                print(self.case[i][j]," | ",end='')
            print()

    def display(self, screen):
        for line in self.case:
            for cell in line:
                cell.display(screen)
