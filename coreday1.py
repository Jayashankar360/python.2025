

item=["tomato","onion","potato","carrot","cabbage","spinach","broccoli","cauliflower","bell pepper","cucumber","green beans"]
storage= input("Enter the items you have in your storage: ")
storage_items = storage.split(",")
missing_items = []
for i in item:
    if i not in storage_items:
        missing_items.append(i)
print("You need to buy the following items:", missing_items)
