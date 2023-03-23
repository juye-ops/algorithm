import sys
input = sys.stdin.readline

def solution(M):
    s = set()
    func = {
        "add": lambda x: s.add(x),
        "remove": lambda x: s.discard(x),
        "check": lambda x: print(1 if x in s else 0),
        "toggle": lambda x: s.remove(x) if x in s else s.add(x),
    }
    ret_func = {
        "all": lambda: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20},
        "empty": lambda: set(),
    }
    
    for i in range(M):
        query = input().strip()
        if query in ["all", "empty"]:
            s = ret_func[query]()
        else:
            cmd, x = query.split()
            x = int(x)
            func[cmd](x)
        
        
    
    
M = int(input())

solution(M)