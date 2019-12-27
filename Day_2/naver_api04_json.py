json = {"name":"kYEOGROK",
        "age":"32",
        "address":"은평구",
        "phone":"010=0000-0000",
        "friends":[{"name":"saun","age":"30"},{"name":"ROK","age":"31"}]}
# print(json)
# print(json.keys())
# print(json['name']),print(json['age']),print(json['address']),print(json['phone'])
# print(json['friends'])

friends = json['friends']
for friend in friends:
    print(friend)