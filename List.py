#
# Food = ["Ramen", "Pizza", "Burger"]
# # print(Food.pop())
# # Food[1] = "Burrito"
# # print(Food[0:2])
# # Food.append("Taco")
# # print(Food)
# # print("Ramen" in Food)
# Food.sort()
# print(Food)
#
#
# info = ["Dave", 15, {"coding": True}, True]
# print(info[2])
# print(info.copy())
# print(info.count("Dave"))
# info.insert(4,"Laptop Hinge")
# print(info)
# info.reverse()
# print(info)
# info.extend(["3: 38 is the time rn "])
# print(info)
# info[2:1] = ["time is 3:55", "hungry me"]
# print(info)
# info.clear()
# print(info)

# List Compressions
numb =  [1, 2, 3, 4, 5, 6]
updated_numb = [n**2 for n in numb]
print(updated_numb)