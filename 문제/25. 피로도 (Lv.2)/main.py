def dfs(k,dungeons ,visited, cnt) :
    maxCnt = 0
    for idx, dungeon in enumerate(dungeons) : 
        n_k = k
        n_visited = visited[:]
        if k >= dungeon[0] and not n_visited[idx]: 
            n_k -= dungeon[1]
            n_visited[idx] = 1
            dcnt = dfs(n_k, dungeons, n_visited, cnt+1)
            maxCnt = max(maxCnt, dcnt)    

    return max(maxCnt, cnt)

def solution(k, dungeons):
    visited = [0] * len(dungeons)
    
    return dfs(k, dungeons, visited,0)