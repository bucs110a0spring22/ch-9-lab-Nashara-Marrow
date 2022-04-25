from Rectangle import Rectangle

class Surface : 
  def __init__(self ,filename , x , y , h , w ): 
    self.image = filename 
    self.rect = Rectangle( x ,y,h,w)
  def getrect(self): 
    return self.rect
   
    
  