pi=0
value=-1
def calculate(c,v,d):
  for i in range(0,c):
    if i%2==0:
      v=v+2
      d=d-4/v
      print("pi with the iteration",i+1,"is/n")
      print(abs(d),"n/n")
    else:
      v=v+2
      d=d+4/v
      print("pi with the iteration",i,"is/n")
      print(abs(d),"/n/n")
task=0
while True:
  try:
    task=int(input("enter a number for n\n: "))
  except ValueError:
    print("Try Again")
    continue

  else:
    if task<1:
      continue
    else:
        calculate(task,value,pi)
        break