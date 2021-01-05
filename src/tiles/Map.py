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
        for i in range(x):
            self.case.append([])
            for j in range(y):
                self.case[i].append("V")
        for i in range (5):
            x1=random.randint(0,x-1)
            y1=random.randint(0,y-1)
            while (issubclass(self.case[x1][y1].__class__,Building)):
                print("!",self.case[x1][y1])
                x1=random.randint(0,x-1)
                y1=random.randint(0,y-1)
            print("<>",self.case[x1][y1])
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
        #for i in buildingsPos:
        #    print(i," : ",buildingsPos.get(i))
        for i in range (len(b)):
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
        #print(b)
        for i in range (0,len(b)):
            #print(b[i])
            for j in reversed(range(i+1,len(b))):
                #print(j)
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
                                #contournement=0
                            #else :
                                #contournement=3
                            #if (b[j][0]==x1 and b[j][1]==y1):
                                #tmp=b[j]
                        elif ((b[j][0]<b[i][0]) or (contournement==2)):
                            x1=tmp[0]-1
                            y1=tmp[1]
                            if (not(issubclass(self.case[x1][y1].__class__,Building))):
                                self.case[x1][y1]=Road([x1*64, y1*64])
                            tmp[0]=tmp[0]-1
                                #contournement=0
                            #else :
                                #contournement=4
                            #if (b[j][0]==x1 and b[j][1]==y1):
                                #tmp=b[j]
                        elif ((b[j][1]>b[i][1]) or (contournement==3)):
                            x1=tmp[0]
                            y1=tmp[1]+1
                            if (not(issubclass(self.case[x1][y1].__class__,Building))):
                                self.case[x1][y1]=Road([x1*64, y1*64])
                            tmp[1]=tmp[1]+1
                                #contournement=0
                            #else :
                                #contournement=1
                            #if (b[j][0]==x1 and b[j][1]==y1):
                                #tmp=b[j]
                        elif ((b[j][1]<b[i][1]) or (contournement==4)):
                            x1=tmp[0]
                            y1=tmp[1]-1
                            if (not(issubclass(self.case[x1][y1].__class__,Building))):
                                self.case[x1][y1]=Road([x1*64, y1*64])
                            tmp[1]=tmp[1]-1
                                #contournement=0
                            #else :
                                #contournement=2
                            #if (b[j][0]==x1 and b[j][1]==y1):
                                #tmp=b[j]
                        #if (contournement>0):
                            #break
                        #print(self.case[x1][y1])
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
                                #contournement=0
                            #else :
                                #contournement=2
                            #if (b[j][0]==x1 and b[j][1]==y1):
                                #tmp=b[j]
                        elif ((b[j][1]>b[i][1]) or (contournement==3)):
                            x1=tmp[0]
                            y1=tmp[1]+1
                            if (not(issubclass(self.case[x1][y1].__class__,Building)) and (not(issubclass(self.case[x1][y1].__class__,Road)))):
                                self.case[x1][y1]=Sidewalk([x1*64, y1*64])
                            tmp[1]=tmp[1]+1
                                #contournement=0
                            #else :
                                #contournement=1
                            #if (b[j][0]==x1 and b[j][1]==y1):
                                #tmp=b[j]
                        elif ((b[j][0]<b[i][0]) or (contournement==2)):
                            x1=tmp[0]-1
                            y1=tmp[1]
                            if (not(issubclass(self.case[x1][y1].__class__,Building)) and (not(issubclass(self.case[x1][y1].__class__,Road)))):
                                self.case[x1][y1]=Sidewalk([x1*64, y1*64])
                            tmp[0]=tmp[0]-1
                                #contournement=0
                            #else :
                                #contournement=4
                            #if (b[j][0]==x1 and b[j][1]==y1):
                                #tmp=b[j]
                        elif ((b[j][0]>b[i][0]) or (contournement==1)):
                            x1=tmp[0]+1
                            y1=tmp[1]
                            if (not(issubclass(self.case[x1][y1].__class__,Building)) and (not(issubclass(self.case[x1][y1].__class__,Road)))):
                                self.case[x1][y1]=Sidewalk([x1*64, y1*64])
                            tmp[0]=tmp[0]+1
                                #contournement=0
                            #else :
                                #contournement=3
                            #if (b[j][0]==x1 and b[j][1]==y1):
                                #tmp=b[j]



                        #if (contournement>0):
                            #break
                        #print(self.case[x1][y1])
                b[i]=save
                #print("ROUTE FINI entre :", i," ",b[i]," et ",j, " ",b[j])
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
        for j in poss:
            x1=j[0]
            y1=j[1]
            if (not(issubclass(self.case[x1][y1].__class__,Building)) and (not(issubclass(self.case[x1][y1].__class__,Road)))):
                self.case[x1][y1]=Sidewalk([x1*64, y1*64])
        self.case[x1][y1]
        for i in range(x):
            for j in range(y):
                if (self.case[i][j]=="V"):
                    self.case[i][j]=self.generateTile(i,j)
        #for i in buildingsPos:
        #    print(i," : ",buildingsPos.get(i))
        return buildingsPos



    def generateMap2(self,x=10,y=10):
        self.case=[]
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
                T=self.generateTile(i,j)
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
        for i in range(len(b2)): ## not generation be sure that building have spawn
            if (b2[i]==0):
                b2[i]=1
                x2=random.randint(0,x-1)
                y2=random.randint(0,y-1)
                while ((issubclass(self.case[x2][y2].__class__,Building))):
                    print(not(issubclass(self.case[x2][y2].__class__,Building)),self.case[x2][y2].__class__)
                    x2=random.randint(0,x-1)
                    y2=random.randint(0,y-1)
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
                self.case[x2][y2]=T
        buildingsPos={}     #position of buildings
        for i in range(x):
            for j in range(y):
                if (isinstance(self.case[i][j],House)):
                    buildingsPos["House"]=[i,j]
                elif  (isinstance(self.case[i][j],Pub)):
                    buildingsPos["Pub"]=[i,j]
                elif  (isinstance(self.case[i][j],FastFood)):
                    buildingsPos["FastFood"]=[i,j]
                elif  (isinstance(self.case[i][j],Library)):
                    buildingsPos["Library"]=[i,j]
                elif  (isinstance(self.case[i][j],University)):
                    buildingsPos["University"]=[i,j]
        for i in buildingsPos:
            print(i," : ",buildingsPos.get(i))
        return buildingsPos

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

    def get_case(self, position):
        return self.case[position[0]][position[1]]
