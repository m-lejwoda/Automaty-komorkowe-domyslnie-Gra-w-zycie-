from vpython import *
import time
#Testy do programu
#redcells = [11,12,22,23,32,34,33]
#redcells = [10,21,2,12,22]
#redcell = [21,22,31,32]
#redcells = [12,22,32]
redcells = [11,21,31,12,23]
allcells = []  
wrong = [0,1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,19,29,39,49,59,69,79,89,99,91,92,93,94,95,96,97,98]
S = [2,3]
B = [3]
class Cell():
    def __init__(self,id,x,y,color):
        self.id = id
        self.x = x
        self.y = y
        self.color = color
        self.live = False
    def set_neighbours(self):
        try:
            self.lefttop = allcells[self.id - 11].live
        except IndexError:
            self.lefttop = False
        try:
            self.leftmid = allcells[self.id - 10].live
        except IndexError:
            self.leftmid = False
        try:
            self.leftbot = allcells[self.id - 9].live
        except IndexError:
            self.leftbot = False
        try:
            self.midtop = allcells[self.id - 1].live
        except IndexError:
            self.midtop = False
        try:
            self.midbot = allcells[self.id + 1].live
        except IndexError:
            self.midbot = False
        try: 
            self.righttop = allcells[self.id + 9].live
        except IndexError: 
            self.righttop = False
        try: 
            self.rightmid = allcells[self.id + 10].live
        except IndexError:
            self.rightmid = False
        try: 
            self.rightbot = allcells[self.id + 11].live
        except IndexError:
            self.rightbot = False
    
    def check_numbers_of_alive_neighbours(self):
        self.alive = 0
        if self.lefttop == True:
            self.alive = self.alive+1
        if self.leftmid == True:
            self.alive = self.alive+1
        if self.leftbot == True:
            self.alive = self.alive+1
        if self.midtop == True:
            self.alive = self.alive+1
        if self.midbot == True:
            self.alive = self.alive+1
        if self.righttop == True:
            self.alive = self.alive+1
        if self.rightmid == True:
            self.alive = self.alive+1
        if self.rightbot == True:
            self.alive = self.alive+1
        # sprawdzenie czy komórka jest żywa
    def change_to_alive(self):
        self.live = True
        self.color = color.red
    def change_to_dead(self):
        self.live = False
        self.color = color.white
    def check_and_change(self):
        if self.live == True:
            if self.alive == 2 or self.alive == 3:
                self.change_to_alive()
            else:
                self.change_to_dead()
        else:
            if self.alive == 3:
                self.change_to_alive()
    def check_and_change_v2(self,s,b):
        is_alive = False
        if self.live == True:
            for i in s:
                if self.alive == i:
                    self.change_to_alive()
                    is_alive = True
                    break      
        else:
            for j in b:
                if self.alive == j:
                    self.change_to_alive()
                    is_alive = True
                    break
        if is_alive == False:
            self.change_to_dead()
        
        
        

def generate_fields():   
    iteration_id = 0
    for i in range(10):
        for j in range(10):
            cell = Cell(iteration_id,i,j*(-1),color.white)
            allcells.append(cell)    
            iteration_id = iteration_id + 1

def set_red_cells():
    for el in allcells:
        if el.id in redcells:
            el.color = color.red
            el.live = True


if __name__ == '__main__':
    generate_fields()
    set_red_cells()
    for el in allcells:
        b = box(pos=vec(el.x,el.y,0),color=el.color,height=0.8,width=0.5,length=0.8) 
    while True:
        for el in allcells:
            el.set_neighbours()
            el.check_numbers_of_alive_neighbours()
        for el in allcells:
            # el.check_and_change()
            el.check_and_change_v2(S,B)
        time.sleep(2)    
        for el in allcells:
            b = box(pos=vec(el.x,el.y,0),color=el.color,height=0.8,width=0.5,length=0.8)

    

