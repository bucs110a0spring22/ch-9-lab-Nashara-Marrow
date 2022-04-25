class Rectangle : 
  def __init__(self , x , y, h=0 , w=0): 
    self.x = x 
    self.y = y 
    self.height = h 
    self.width = w
  def __str__(self):
    string = "x : " , self.x , "y : " , self.y , "width : " , self.width , "height : "  , self.height
    return string 
    
  