class Input:
    def __init__(self,time='2023', style='', gps='', direction=[],pic =''):
        self.time = time
        self.style = style
        self.gps = gps
        self.direction = direction
        self.pic = pic
    
    def getInput(self):
        return self.time,self.gps,self.direction,self.pic