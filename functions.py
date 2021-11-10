import math

def getPoints(points):
    xmedia = (points[0][0]+points[1][0]+points[2][0]+points[3][0])/4
    ymedia = (points[0][1]+points[1][1]+points[2][1]+points[3][1])/4

    for point in points:
        if point[0]<xmedia:
            if point[1]<ymedia:
                p1=point
            else:
                p4=point
        elif point[1]<ymedia:
            p2=point
        else:
            p3=point
    p=[p1,p2,p3,p4]
    return p, xmedia, ymedia

def getSize(qrobject, totalpixels):

    ###Calculate the area of the qr to know if it is close to the camera or no
    qrw = qrobject.rect.width
    qrh = qrobject.rect.height
    qarea = qrw*qrh
    qrsize = (qarea*100)/totalpixels

    # print('% QR size: ', qrsize)

    if (2<qrsize<4.5):
        distance = 2
        dist=1.01
    elif qrsize<=2:
        distance = 3
        dist=1.05
    else:
        distance = 1
        dist=1
    
    print("----qrsize px: ", str(qarea))
    print("----qrsize %: ", str(qrsize))
    
    return distance, dist, qrsize


def getOrientation(p, dist):
    #CALCULATE THE ORIENTATION 
    dist14 = math.sqrt( (p[3][0] - p[0][0])**2 + (p[3][1] - p[0][1])**2 )
    dist23 = math.sqrt( (p[2][0] - p[1][0])**2 + (p[2][1] - p[1][1])**2 )
    # print(dist14, dist23)

    if dist14<0.94*dist23*dist:
        if dist14>0.90*dist23*dist:
            state='right1'
        else:
            state='right2'
    elif dist23<0.94*dist14*dist:
        if dist23>0.90*dist14*dist:  
            state='left1'
        else:
            state='left2'
    else:
        state='center'

    return state
