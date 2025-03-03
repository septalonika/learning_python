def min_protection_levels(n, p1, p2, portals):
    results = []
    
    all_portals = portals + [p1, p2]
    
    for i in range(n):
        target = portals[i]
        
        min_protection = min(abs(target - p1), abs(target - p2))
        
        for intermediate in all_portals:
            if intermediate == target:  
                continue
                
            protection1 = max(abs(p1 - intermediate), abs(intermediate - target))
            
            protection2 = max(abs(p2 - intermediate), abs(intermediate - target))
            
            min_protection = min(min_protection, protection1, protection2)
            
            for second_intermediate in all_portals:
                if second_intermediate == target or second_intermediate == intermediate:
                    continue
                    
                protection3 = max(abs(p1 - intermediate), 
                                 abs(intermediate - second_intermediate),
                                 abs(second_intermediate - target))
                                 
                protection4 = max(abs(p2 - intermediate), 
                                 abs(intermediate - second_intermediate),
                                 abs(second_intermediate - target))
                                 
                min_protection = min(min_protection, protection3, protection4)
        
        results.append(min_protection)
    
    return results

def main():
    t = int(input().strip())
    
    for _ in range(t):
        line = input().strip().split()
        n, p1, p2 = int(line[0]), int(line[1]), int(line[2])
        
        portals = list(map(int, input().strip().split()))
        
        result = min_protection_levels(n, p1, p2, portals)
        print(' '.join(map(str, result)))

if __name__ == '__main__':
    main()
    
    
    import heapq

def solve():
    t = int(input().strip())
    
    for _ in range(t):
        n, p1, p2 = map(int, input().strip().split())
        portal_powers = list(map(int, input().strip().split()))
        
        results = [min(abs(power - p1), abs(power - p2)) for power in portal_powers]
        
        unique_powers = {} 
        for i, power in enumerate(portal_powers):
            if power not in unique_powers:
                unique_powers[power] = []
            unique_powers[power].append(i)
        
        pq = [(0, p1), (0, p2)]
        heapq.heapify(pq)
        
        min_protection = {p1: 0, p2: 0}
        
        while pq:
            protection, current = heapq.heappop(pq)
            
            if protection > min_protection.get(current, 0):
                continue
            
            for power, indices in unique_powers.items():
                new_protection = max(protection, abs(current - power))
                
                if power not in min_protection or new_protection < min_protection[power]:
                    min_protection[power] = new_protection
                    heapq.heappush(pq, (new_protection, power))
                    
                    for idx in indices:
                        if new_protection < results[idx]:
                            results[idx] = new_protection
        
        print(" ".join(map(str, results)))

if __name__ == "__main__":
    solve()