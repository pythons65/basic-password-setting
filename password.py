i = 1
fun = True
while i<5:
  a = input("code:")
  if (a == "admin"):
    print("code accessed")
    fun = True
    i = 5
    break
  elif(a == ""):
    print("empty")
    fun = False
    i+=1
  else:
    print("deneid code")
    i+=1
    fun = False
if (i==5):

  if (fun==True):
    print("you can access")
  else:
    print("you cannot access any more")  


