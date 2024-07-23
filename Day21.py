class Animal:
       def __init__(self):
              self.num_eyes = 2
              
       def breathe(self):
              print("Inable , exhale")
              
class Fish(Animal):
       def __init__(self):
              super().__init__()
       def swim(self):
              print("moving in water")
       def breathe(self):
              super().breathe()
              print("doing this ander water")
              
                     
memo= Fish()
memo.swim()
memo.breathe()