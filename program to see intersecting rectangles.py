#Ismail Ali
import math

 
class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'



#Part 2
# 13 methods
class Rectangle:

    def __init__(self, p ,q,color="colour"):
        ''' (Rectangle, Point, Point) -> None
        initialize rectangle using two point coordinates to form a rectangle '''         
        self.p=p
        self.q=q
        self.color=color
        
    def get_bottom_left(self):
        ''' (Rectangle) -> None
        returns the bottom left coordinate of the rectangle'''
 
        return self.p
        

    def get_top_right(self):
        ''' (Rectangle) -> None
        returns the top right coordinate of the rectangle'''
        

        return self.q

    def get_color(self):
        ''' (Rectangle) -> str
        returns the color of the rectangle'''
        return self.color
        
    def get_perimeter(self):
        ''' (Rectangle) -> Number 
        returns the perimeter of the rectangle'''
        xaxis = abs((self.p).x - (self.q).x)*2
        yaxis = abs((self.p).y - (self.q).y)*2
        perimeter=  xaxis + yaxis 
        
        return perimeter
        
    def get_area(self):
        ''' (Rectangle) -> Number
        returns the perimeter of the rectangle'''
        xaxis = abs((self.p).x - (self.q).x)
        yaxis = abs((self.p).y - (self.q).y)
        area = xaxis * yaxis
        
        return area
        
    def __repr__(self):
        '''(Rectangle)->str
        Returns canonical string representation Rectangle(Point, Point, color)'''
 
        return 'Rectangle('+str(self.p)+','+str(self.q)+',' +"'" + str(self.color) + "'" +')'

    def __str__(self):
        '''(Rectangle)->str
        Returns nice string representation Rectangle(x, y).'''
 
        return "I am a " +str(self.color)+ " rectangle with bottom left corner at " + str( "("+ str(self.p.x) + "," + str(self.p.y) + ")" )+" and top right corner "  + str( "("+ str(self.q.x) + "," + str(self.q.y) + ")" )
    
    def reset_color(self, color):
        '''(Rectangle)-> None
        resets the color of the rectangle'''
        self.color=color

    def __eq__(self, other):
        '''(Rectangle,Rectangle)->bool
        Returns True if self and other have the two same rectangle coordinates'''
        
        return self.p== other.p and self.q== other.q
    
    
    def contains(self, x, y):
        '''(Rectangle, Point X coordinate, Point Y coordinate )->bool
        Returns True if the rectangle contains the two coordinates'''

        return (self.p).x== x or (self.p).y== y or (self.q).x== x or (self.q).y== y
    
    def intersects(self, other):
        '''(Rectangle, other )->bool
        Returns True if Rectangle intersects with other Rectangle'''
        
        if  other.get_top_right().y >= self.get_bottom_left().y  and other.get_top_right().x>= self.get_bottom_left().x :
            if  other.get_bottom_left().x - self.get_top_right().x <= 0:
                if  other.get_bottom_left().y - self.get_top_right().y <= 0:
                    
                    return True

        
        if self.get_top_right().x>= other.get_bottom_left().x   and self.get_top_right().y >= other.get_bottom_left().y:
            if  self.get_bottom_left().x - other.get_top_right().x <= 0:
                
                if  self.get_bottom_left().y - other.get_top_right().y <= 0: 
                    
                    return True
        
                
        
        
        return False


    def move(self, dx , dy):
        '''(Rectangle, dx, dy )-> None
        Moves the Rectangle two points by zx and zy units'''


        (self.p).x += dx
        (self.p).y += dy

        (self.q).x += dx
        (self.q).y += dy
            
                   




#Class canvas
# 8 methods 
class Canvas:
   
  

    def __init__(self):
        ''' (Canvas) -> None
        Initializes this Canvas
        '''
        self.rectangle = []

    def __len__(self):
        ''' (Canvas) -> int
        Returns the amount of Rectangles in this canvas
        '''
        return len(self.rectangle)

    def add_one_rectangle(self, r1):
        ''' (Canvas, Rectangle) -> None
        Adds the passed rectangle to this Canvas
        '''
        self.rectangle.append(r1)

    def __repr__(self):
        ''' (Canvas) -> None
        Returns canonical string representation Canvas(Rectangles)
        '''
        return "Canvas({})".format(self.rectangle)

    def count_same_color(self, color):
        ''' (Canvas, string) -> int
        Returns the amount of rectangles with the passed color in this Canvas
        '''
        count=0
        for i in self.rectangle:
            if(i.get_color()==color): count+=1
        return count

    def total_perimeter(self):
        ''' (Canvas) -> String
        Returns the sum of perimeters of all Rectangles in this Canvas
        '''
        sum=0
        for i in self.rectangle:
            sum += i.get_perimeter()
        return sum

    
    def min_enclosing_rectangle(self):
        '''(Canvas)-> Rectangle
        Returns the mininum enclosing Rectangle '''

        
        
        
        minimumx= self.rectangle[0].p.x
        minimumy= self.rectangle[0].p.y
        maximumx= self.rectangle[0].q.x
        maximumy= self.rectangle[0].q.y
        
        if len(self.rectangle)>1:
            
            for i in range(len(self.rectangle)):
                #First Point
                
                if maximumx < self.rectangle[i].p.x:
                    maximumx= self.rectangle[i].p.x
                if maximumy < self.rectangle[i].p.y:
                    maximumy= self.rectangle[i].p.y
                if minimumx > self.rectangle[i].p.x:
                    minimumx= self.rectangle[i].p.x
                if minimumy > self.rectangle[i].p.y:
                    minimumy= self.rectangle[i].p.y
                #Second Point
                if maximumx < self.rectangle[i].q.x:
                    maximumx= self.rectangle[i].q.x
                if maximumy < self.rectangle[i].q.y:
                    maximumy= self.rectangle[i].q.y
                
                if minimumx > self.rectangle[i].q.x:
                    minimumx= self.rectangle[i].q.x
                if minimumy > self.rectangle[i].q.y:
                    minimumy= self.rectangle[i].q.y
                
        Point_max=Point(maximumx, maximumy)               
        Point_min=Point(minimumx, minimumy)
        
        Rectangle2=Rectangle(Point_min,Point_max, "red") #any colour user would choose
        return  Rectangle2
            
        
        
    def common_point(self):
        '''(self)->bool
        Returns True if canvas have a common point (all rectangles intersects with each other)'''
        
        for x in range(len(self.rectangle)):
            for y in range(len(self.rectangle)):
                                           
                if x!=y and self.rectangle[x].intersects(self.rectangle[y])==False:
                    
                    return False
        return True




















                
