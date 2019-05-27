def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for k,v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of item: ' + str(item_total))

def addToInventory(inventory, addedItems):
    for idx,item in enumerate(addedItems):
        inventory.setdefault(item, 0)
        inventory[item] += 1

    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
display_inventory(inv)
