# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12, 'dota':12}

def show_inventory(inventory):
    print("Inventory:")
    # FILL THIS PART IN
    total_items = 0
    for tool, quantity in inventory.items():
        print(str(quantity) + ' ' + tool)
        total_items+=quantity
    print('Total number of tools : '+str(total_items))

show_inventory(stuff)
'''
def addToInventory(inventory, new_item)
for item in new_item:
    inventory.setdefault(item, 0)  #this adds a (defaulted to zero value) key to the inventory dict if it's not already there
    inventory[item]+=1 #and this increases that value by one, each time that item appears in the loot list
return inventory'''

def addToInventory(inventory, addedItems):
    # your code goes here
    for item in addedItems:
        inventory.setdefault(item, 0) #this adds a (defaulted to zero value) key to the inventory dict if it's not already there
        inventory[item] += 1 #and this increases that value by one, each time that item appears in the loot list
    return inventory
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
show_inventory(inv)