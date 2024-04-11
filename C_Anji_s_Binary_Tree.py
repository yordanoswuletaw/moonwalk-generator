from collections import defaultdict

def main():
    for _ in range(int(input())):
        n = int(input())
        ltrs = input()
        graph = defaultdict(list)
        visited = set()
        for v in range(n):
            l, r = map(int, input().split())
            graph[v].append(max(0, l - 1))
            graph[v].append(max(0, r - 1))
      
        def dfs(v):
            if v in visited:
                return 0
            visited.add(v)
            left = graph[v][0]
            right = graph[v][1]
            if not left and not right:
                return 0
            res = float('inf')
            if left:
                res = min(res, int(ltrs[v] != 'L') + dfs(left))
            if right:
                res = min(res, int(ltrs[v] != 'R') + dfs(right))

            return res


        print(dfs(0))
        



if __name__ == '__main__':
    main()