def dirReduc(arr):
    route = []
    for d in arr:
        if route:
            last2 = {route[-1], d}    
            if last2 == {"NORTH", "SOUTH"} or last2 == {"EAST", "WEST"}:
                route.pop()
                continue
        route.append(d)
    return route

u=["NORTH", "WEST", "SOUTH", "EAST"]
print(dirReduc(u))