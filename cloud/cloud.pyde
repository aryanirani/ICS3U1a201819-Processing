def setup():
    size(800, 600)
    background(51)
    noStroke()
    noLoop()
     
def draw():
    drawCloud("#0dc620", 100, 300)
    drawCloud("#0dc620", 200, 200)
    drawCloud("#ff0000", width/2, height/1.5)
    
        
def drawCloud(colour, xloc, yloc):
    # right target
    for i in range(5): 
        ellipse(xloc +70, yloc, 100, 100)
        ellipse(xloc, yloc, 100, 100)
        ellipse(xloc +60, yloc +50, 100, 100)
