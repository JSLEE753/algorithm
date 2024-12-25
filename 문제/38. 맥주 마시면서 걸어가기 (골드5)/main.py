from collections import deque

# 데이터 입력
T = int(input())
tcs = []
for _ in range(T) : 
    conv = int(input())
    test_case = []
    for _ in range(conv+2) : 
        test_case.append(list(map(int,input().split())))

    tcs.append(test_case)


def bfs(tc, visited) :
    # 시작 지점 설정
    queue = deque([tc[0]])

    while queue : 
        cx, cy = queue.popleft()
        
        # 현재 위치에서 목표에 도달할 수 있는가?
        if abs(cx - tc[-1][0]) + abs(cy - tc[-1][1]) <= 1000 : 
            return 'happy'
        
        # 그렇지 않다면, 다음 편의점에 도착할 수 있는가?
        for i in range(len(tc) - 2) :
            if not visited[i] : 
                if abs(cx - tc[1:-1][i][0]) + abs(cy - tc[1:-1][i][1]) <= 1000 :
                    queue.append(tc[1:-1][i])
                    visited[i] = 1  

    # 위 두 경우에 모두 해당하지 않으면, sad를 return
    return 'sad'

for tc in tcs : 
    visited = [0] * (len(tc) - 2) # 편의점 개수

    print(bfs(tc, visited))