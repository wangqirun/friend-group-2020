
import json
my_group = {'Jill':{'Age':26,'Job':'biologist','Relationship':{'Zalika':'friend','John':'partner'}},
'Zalika':{'Age':28,'Job':'artist','Relationship':{'Jill':'friend'}},
'John':{'Age':27,'Job':'writer','Relationship':{'Jill':'partner'}},
'Nash':{'Age':34,'Job':'chef','Relationship':{'John':'cousin','Zalika':'landlord'}}}

json.dumps(my_group)
print(my_group.items())
print(json.dumps(my_group, indent=4))


with open('my_group.json', 'r') as json_file:
    print(json.dump(my_group, json_file, indent=4))

#Loading data
with open('my_group.json', 'r') as json_file:
    my_group_as_string = json_file.read()
    print(my_group_as_string)

    mygroup = json.loads(my_group_as_string)
    print(mygroup)


 



