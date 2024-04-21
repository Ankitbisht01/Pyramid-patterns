n = int(input("enter number of rows: "))
print("simple pyramid pattern")
for i in range(n):
  print("x "*(i+1), end=" \n")

print()
#inverted pyramid
for i in range(n):
  print(" "*(n-i-1), " x"*(i+1), end ="\n")

for i in range(1, n+1):
  for j in range(i):
    print(i, end = " ")
  print()


  