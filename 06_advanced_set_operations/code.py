friends = {"Bob", "Carter", "Annie"}
abroad = {"Bob", "Annie"}

#local_friends = {"Carter"}
local_friends = friends.difference(abroad)

print(local_friends)


friends = local_friends.union(abroad)

print(friends)