def solution(park, routes):
    # N, E, S, W
    vector = {'N' : (-1,0), 'E' : (0,1) , 'S' : (1,0), 'W' : (0,-1)}
    current = []
    width = len(park[0]) - 1
    height = len(park) - 1
    
    for index, row in enumerate(park) : 
        if 'S' in row :
            current = [index,row.index('S')]
            break
    
    for route in routes :
        v, n = route.split()
        n = int(n)
        enabled = True
        dx,dy = vector[v]
        nx = current[0] + dx*n
        ny = current[1] + dy*n
        temp_current = current[:]
        if nx < 0 or nx > height or ny < 0 or ny > width :
            enabled = False
        else : 
            for _ in range(n) : 
                tx = temp_current[0] + dx
                ty = temp_current[1] + dy
                temp_current = [tx,ty]
                if (park[tx][ty] == 'X') :
                    enabled = False
                    break
        
        if enabled :
            current = [nx,ny]
    return current