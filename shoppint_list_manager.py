
Item_list = []
while True:
   
   Item =(input("Enter Shopping item or typed done to close: "))
   if Item == "done":
      break
   else:
      Item_list.append(Item)

print(f"Shopping list:{Item_list}") 
print(f"Total Item: {len(Item_list)}")

