# lists in python
# start with a regular variable name
#  i e name = [3, True, "strings"]

enemy_positions = [5, 10, 15]
enemy_positions = [5, 10, 15, 25]
#  you can access a specific element
# print(enemy_positions[0])

# if yoo are not sure abou the  length of the list use len
print (len(enemy_positions))
# can also change value
enemy_positions[0] = 6
print(enemy_positions)

#  can also get  a range between index o and 2

print(enemy_positions[0:2])


# methos
# append fxn takes an element to the end of a list
enemy_positions.append(30)
print(enemy_positions)

# can as well insert an element at a specific index

enemy_positions.insert(1,11)
print(enemy_positions)

#  can as well remove elements from their attached positions in the list as shown

enemy_positions.remove(30)
print(enemy_positions)

# can as well delete from a specific element
del(enemy_positions[2])
print(enemy_positions)