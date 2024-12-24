def solution(rows, columns, queries):
    ini = 0
    arr = []
    result = []
    # E S W N
    vectors = ((0,1), (1,0), (0,-1), (-1,0))
    
    # 초기 배열 생성
    for i in range(rows) : 
        arr.append([])
        for j in range(columns) :
            ini += 1
            arr[i].append(ini)
            
    for query in queries : 
        max_x = query[2] - query[0] # 세로축 최대 이동횟수
        max_y = query[3] - query[1] # 가로축 최대 이동횟수
        cx = query[0] - 1 # 현재 세로 좌표
        cy = query[1] - 1 # 현재 가로 좌표
        prev_v = arr[cx][cy] # 다음 좌표의 바뀔 값
        min_v = prev_v # result에 들어갈 최솟값
        
        for idx, vector in enumerate(vectors) : 
            isHorizontal = idx % 2 == 0
            
            # 좌, 우 이동
            if isHorizontal : 
                for _ in range(max_y) :
                    ny = cy + vector[1]
                    _prev = arr[cx][ny]
                    arr[cx][ny] = prev_v
                    prev_v = _prev
                    cy = ny
                    min_v = min(min_v, prev_v)
                    
            # 상, 하 이동
            else : 
                for _ in range(max_x) : 
                    nx = cx + vector[0]
                    _prev = arr[nx][cy]
                    arr[nx][cy] = prev_v
                    prev_v = _prev
                    cx = nx
                    min_v = min(min_v, prev_v)
                    
        result.append(min_v)
    
    return result