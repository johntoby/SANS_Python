idowu_children = ["tolu", "toby", "toye", "timmy", 6.44, 55, False]
print(idowu_children[4])

idowu_children_2 = ["tolu", "toby", "toye", ["ayo", "sandra", "chicko"], 6.44, 55, False]
print(idowu_children_2[0]) 
print(idowu_children_2[3])

#to modify a list
jt_babes = ["ayomide", "clare", "isioghene", 'joan']
print(jt_babes[1])
jt_babes[0] = "Jennifer" 
print(jt_babes) 
jt_babes [2] = "okeoghene" 
print(jt_babes) 

jt_babes.sort()
print(jt_babes)
jt_babes.reverse()
print(jt_babes)  

#to ADD ITEMS TO THE END OF A LIST, USE THE append tool 

travel_bucket_list = ["vienna", 'sacramento', 'san francisco', 'joburg']
travel_bucket_list.append("banana")
print(travel_bucket_list)

#ADD ITEM INSIDE A LIST, We use the insert tool 

travel_bucket_list.insert(1, "suleja")
print(travel_bucket_list)

#to remove an item from a list, use pop ()

visited = travel_bucket_list.pop()
visited_yesterday = travel_bucket_list.pop(2) 
print(visited)
print(visited_yesterday)
print("I recently visited " + visited_yesterday)

#to remove a specific item, use remove()

print(travel_bucket_list)
travel_bucket_list.remove("suleja")
print(travel_bucket_list) 
travel_bucket_list.remove("joburg") 
print(travel_bucket_list) 
