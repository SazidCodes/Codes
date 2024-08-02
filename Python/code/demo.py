class robot:
   def __init__(self, name , color , weight):
      self.n = name
      self.c = color
      self.w = weight

   def selfintroduce(self):
      print(f'my name is {self.n}')
   
   def comp(self):
      if(self.w > 100):
         print("Heavy")
      else:
         print("Light")


r1 = robot('chitti', 'white', 110)
r2 = robot('sofia', 'white', 90)
print(r1.n)
print(r2.n)

r1.selfintroduce()
r1.comp()