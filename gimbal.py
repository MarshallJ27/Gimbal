from math import radians, sin, cos, sqrt, asin
def haversine(latgim: object, longim: object, latdrn: object, londrn: object) -> object:
    #gim is for gimbal drn is for drone

    R = 6372.8

    dlat = radians(latdrn - latgim)
    dlon = radians(londrn - longim)
    latgim = radians(latgim)
    latdrn = radians(latdrn)

    a = sin(dlat/2)**2 + cos(latgim)*cos(latdrn)*sin(dlon/2)**2
    c = 2*asin(sqrt(a))
    print(R * c)
    return R * c
haversine( 30.15, 43.27, 36.21, 74.93)
#gives around 3000

#Convert lat, long into x,y to get a coordinate plane


# Retrieve x coordinate
def find_x_coordinate(latgim: object, longim: object, latdrn: object) -> object:

    xcord = haversine(latgim, longim,latdrn, longim)
    #print (xcord)

    return (xcord)

find_x_coordinate(30.15, 36.21, 43.27)


#Retrieve y Coordinate

def find_y_coordinate(latgim,longim, longdrn):
    ycord = haversine(latgim, longim, latgim, longdrn)
    #print(ycord)
    return(ycord)
find_y_coordinate(30.15, 43.27, 74.93)


#Find the distance between the point and the plane

def opposite_side_distance(latgim, longim, latdrn, londrn, prevlatgim, prevlongim, prevlatdrn, prevlondrn):
    xprev = find_x_coordinate(prevlatgim, prevlongim, prevlatdrn)
    yprev = find_y_coordinate(prevlatgim, prevlongim, prevlondrn)
    xnext = find_x_coordinate(latgim, longim, latdrn)
    ynext = find_y_coordinate(latgim,longim, londrn)

    a = ynext - yprev

    b = xnext - xprev

    c = xprev * xnext-yprev*ynext

    d = math.fabs((a*xprev + b*yprev + c )*(a*xprev + b*yprev + c ))/ sqrt(a*a+b*b)

    print(d)
    return (d)
opposite_side_distance()



























 #Retrieve y coordinate









