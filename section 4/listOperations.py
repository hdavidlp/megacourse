temperatures = [10.2, 11.3, 13.5, 16.7]

temperatures.append(19.2)

print (temperatures)
print (temperatures.index(11.3))     # Lookfor a value
print (temperatures.index(16.7, 2))  # Skip the first 2 items
temperatures.remove(16.7)            # Remove the specific item
print (temperatures.__getitem__(2))  # To get the value of an index
print (temperatures[2])              # Something like a previus line
print(temperatures[0:2])             # TO access portion of the list
print(temperatures[:2])              # Everything from the begining to index 2
print(temperatures[-1])              # To get the item 1, from the end of the list


temperatures.clear()
print ("Listado final", temperatures)


