mylist = [1, 2, 3, 4, 5]
print(mylist)
print(mylist[0])

mylist2 = [{'name': 'John', 'age': 45}, {'name': 'Mary', 'age': 35}, {'name': 'Bob', 'age': 55}]
print(mylist2)
print(mylist2[0])
print(mylist2[0]['name'])

mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(mylist)
print(mylist[0])
print(mylist[1][1])


# car -> book -> park -> book -> park
# {init_time: "2020-01-01 00:00:00", final_time: "-1" }
# {init_time: "2020-01-01 00:00:00", final_time: "2020-01-01 00:30:00" }
# {init_time: "2020-01-01 10:00:00", final_time: "-1" }
# # active_parking
# {init_time: "2020-01-01 00:30:00", final_time: "-1" }
# {init_time: "2020-01-01 00:30:00", final_time: "2020-01-01 01:00:00" }