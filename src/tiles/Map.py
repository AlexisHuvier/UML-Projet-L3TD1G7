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
        self.case=[]

    def generateTile(self,x,y):
        p=random.randint(0,100)
        if (p<40):
            T=Forest([x*64, y*64])
        elif (p<75):
            T=GreyTile([x*64, y*64])
        elif (p<101):
            T=WaterTile([x*64, y*64])
        return T

    def generateMap(self,x=10,y=10):
        self.case=[]
        b=[]
        buildingsPos={}             #position of buildings
        for i in range(x): # Génère la liste de liste
            self.case.append([])
            for j in range(y):
                self.case[i].append("V")
        for i in range (5): # Créer les cinq batiments
            x1=random.randint(0,x-1)
            y1=random.randint(0,y-1)
            while (issubclass(self.case[x1][y1].__class__,Building)):
                x1=random.randint(0,x-1)
                y1=random.randint(0,y-1)
            if (i==0):
                self.case[x1][y1]=House([x1*64, y1*64])
                buildingsPos["House"]=[x1,y1]
            elif (i==1):
                self.case[x1][y1]=Pub([x1*64, y1*64])
                buildingsPos["Pub"]=[x1,y1]
            elif (i==2):
                self.case[x1][y1]=FastFood([x1*64, y1*64])
                buildingsPos["FastFood"]=[x1,y1]
            elif (i==3):
                self.case[x1][y1]=Library([x1*64, y1*64])
                buildingsPos["Library"]=[x1,y1]
            elif (i==4):
                self.case[x1][y1]=University([x1*64, y1*64])
                buildingsPos["University"]=[x1,y1]
            b.append([x1,y1])
        for i in range (len(b)): # Prend un point aléatoire autour de chaque batiment
            x1=b[i][0]
            y1=b[i][1]
            poss=[]
            if (x1<x-1):
                poss.append([x1+1,y1])
            if (x1>0):
                poss.append([x1-1,y1])
            if (y1<y-1):
                poss.append([x1,y1+1])
            if (y1>0):
                poss.append([x1,y1-1])
            r=random.randint(0,len(poss)-1)
            b[i]=poss[r]
        for i in range (0,len(b)): # Génération Trottoir/Route entre chaque batiment
            for j in reversed(range(i+1,len(b))):
                tmp=b[i]
                save=[b[i][0],b[i][1]]
                contournement=0
                r=random.randint(0,1)
                if (r==0):
                    while (tmp!=b[j] and (contournement>=0)):
                        x1=0
                        y1=0
                        if ((b[j][0]>b[i][0]) or (contournement==1)):
                            x1=tmp[0]+1
                            y1=tmp[1]
                            if (not(issubclass(self.case[x1][y1].__class__,Building))):
                                self.case[x1][y1]=Road([x1*64, y1*64])
                            tmp[0]=tmp[0]+1
                        elif ((b[j][0]<b[i][0]) or (contournement==2)):
                            x1=tmp[0]-1
                            y1=tmp[1]
                            if (not(issubclass(self.case[x1][y1].__class__,Building))):
                                self.case[x1][y1]=Road([x1*64, y1*64])
                            tmp[0]=tmp[0]-1
                        elif ((b[j][1]>b[i][1]) or (contournement==3)):
                            x1=tmp[0]
                            y1=tmp[1]+1
                            if (not(issubclass(self.case[x1][y1].__class__,Building))):
                                self.case[x1][y1]=Road([x1*64, y1*64])
                            tmp[1]=tmp[1]+1
                        elif ((b[j][1]<b[i][1]) or (contournement==4)):
                            x1=tmp[0]
                            y1=tmp[1]-1
                            if (not(issubclass(self.case[x1][y1].__class__,Building))):
                                self.case[x1][y1]=Road([x1*64, y1*64])
                            tmp[1]=tmp[1]-1
                else :
                    while (tmp!=b[j] and (contournement>=0)):
                        x1=0
                        y1=0
                        if ((b[j][1]<b[i][1]) or (contournement==4)):
                            x1=tmp[0]
                            y1=tmp[1]-1
                            if (not(issubclass(self.case[x1][y1].__class__,Building)) and (not(issubclass(self.case[x1][y1].__class__,Road)))):
                                self.case[x1][y1]=Sidewalk([x1*64, y1*64])
                            tmp[1]=tmp[1]-1
                        elif ((b[j][1]>b[i][1]) or (contournement==3)):
                            x1=tmp[0]
                            y1=tmp[1]+1
                            if (not(issubclass(self.case[x1][y1].__class__,Building)) and (not(issubclass(self.case[x1][y1].__class__,Road)))):
                                self.case[x1][y1]=Sidewalk([x1*64, y1*64])
                            tmp[1]=tmp[1]+1
                        elif ((b[j][0]<b[i][0]) or (contournement==2)):
                            x1=tmp[0]-1
                            y1=tmp[1]
                            if (not(issubclass(self.case[x1][y1].__class__,Building)) and (not(issubclass(self.case[x1][y1].__class__,Road)))):
                                self.case[x1][y1]=Sidewalk([x1*64, y1*64])
                            tmp[0]=tmp[0]-1
                        elif ((b[j][0]>b[i][0]) or (contournement==1)):
                            x1=tmp[0]+1
                            y1=tmp[1]
                            if (not(issubclass(self.case[x1][y1].__class__,Building)) and (not(issubclass(self.case[x1][y1].__class__,Road)))):
                                self.case[x1][y1]=Sidewalk([x1*64, y1*64])
                            tmp[0]=tmp[0]+1
                b[i]=save
        t=buildingsPos.get("House")
        x1=t[0]
        y1=t[1]
        poss=[]
        if (x1<x-1):
            poss.append([x1+1,y1])
        if (x1>0):
            poss.append([x1-1,y1])
        if (y1<y-1):
            poss.append([x1,y1+1])
        if (y1>0):
            poss.append([x1,y1-1])
        r=random.randint(0,len(poss)-1)
        for j in poss: # Met des trottirs sur les cases adjacentes à la Maison si elles sont différentes d'un batiment ou d'une route
            x1=j[0]
            y1=j[1]
            if (not(issubclass(self.case[x1][y1].__class__,Building)) and (not(issubclass(self.case[x1][y1].__class__,Road)))):
                self.case[x1][y1]=Sidewalk([x1*64, y1*64])
        for i in range(x): # Remplace les cases restantes par de l'eau, des cases grises ou de la forêt
            for j in range(y):
                if (self.case[i][j]=="V"):
                    self.case[i][j]=self.generateTile(i,j)
        return buildingsPos # Retourne un dictionnaire contenant les positions des batiments

    def __str__(self):
        return "map affichage"

    def display(self, screen):
        for line in self.case:
            for cell in line:
                cell.display(screen)

    def get_case(self, position):
        return self.case[position[0]][position[1]]
