print("Welcome to Burger Castle. Give us one moment while we download our menu...")
import os
bag=[]
os.system("wget -q ")
import subprocess as sp
menu=sp.getoutput("cat menu.acr")
print("Here's one we have to offer:")
print(menu)
print("Can I get anything started for you?")
def similar(a, b):
    result=SequenceMatcher(None, a, b).ratio()
selection=(input(""))
for x in menu:
  similar(x,selection)
  if result < 0.7:
    print("Did you mean?")
if exit in selection:
  print("thank you!! Your order will arive at the speed of 56kp/s!") 
  print("Your bag")
  print(bag)
if not result in menu:
  print("Sorry, I didn't get that.")
else:
  print("Ofc! Good choice")
  bag.append(selection)
  
