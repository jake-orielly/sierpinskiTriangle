import random

def getAverage (q0,q1,pc0,pc1):
    return [((pc0+q0)/2),((pc1+q1)/2)]

def main():
    w = 1000
    h = 1000
    canvas = makeEmptyPicture(w,h)
    show(canvas)
    
    p0 = [w / 2, 0]
    
    p1 = [0, h - 1]
    
    p2 = [w - 1, h - 1]
    
    pc = [p0[0],p0[1]]
    
    counter = 0
    
    points = [p0,p1,p2]
    
    while True:
        n = random.randrange(3)
        pc = getAverage(points[n][0],points[n][1],pc[0],pc[1])
            
        px = getPixel(canvas,pc[0],pc[1])

        setRed(px,((float(pc[0])/w)*256))
        setGreen(px,(256-(float(pc[0])/w)*256))
        setBlue(px,(256-(float(pc[1])/w)*256))
        
        counter = counter + 1
        if counter > 1000:
            repaint(canvas)
            counter = 0
            
    return