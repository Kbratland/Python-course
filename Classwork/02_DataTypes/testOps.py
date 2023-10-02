old = 0
current = 1
new = 0
target = 1000000
while current < target:
     print(new,end=" ")
     old = current
     current = new
     new = current + old