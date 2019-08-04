class sample:
  y = 90
  def __init__(self):
    self.x=10
  def showx(self):
    print(self.x)
import time
dic =time.__dict__
for x,y in dic.items():
	print(x,"\t\t\t",y)
