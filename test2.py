# Kingdom Corp has just built  new teleportation portals with power level A1,A2,.....,An. For monitoring purposes, Kingdom Corp research center plans to send one scientist to each portal. The N scientists will depart from the research center to their assigned portal, by teleporting through one or more portals.

# A person must use a teleportation suit to survive the teleportation process. Suit with protection level K can be used to teleport from portal with power level X to any other portal with power level ranging from  X-K to X + K, inclusive. For example, a level 2 suit can be used to teleport from a power level 5 portal to another portal with power level 3,4,5,6 or 7 .

# At Kingdom Corp research center, there are two existing portals which the scientists can choose to depart from, each with power level  P1 and P2. To maximize cost efficiency, Kingdom Corp asked you to determine minimum required protection level of the suit for each scientist.

# Input Format

# The first line contains a single integer  T - The number of test cases.

# The first line of each test case contains a three integers  N, P1, and P2 - The number of newly built teleporation portals and the power level of portals in at Kingdom Corp research center.

# The second line of each test case contains N integers A1, A2,.....,An -  The power level of each newly built teleportation portals.

# Constraints 

# 1<= T <= 20 

# 1 <= N <= 100000 

# 0 <= Ai <= 1.000000000 

# 0 <= P1 && P2 <= 1000000000

# Output Format

# For each test case, print N  integers  The minimum required protection level of the suit for each scientist if they visit portal with power level Ai.

# Sample Input 0
# 2
# 5 2 11
# 8 4 14 1 13
# 12 5 15
# 16 18 4 9 5 10 6 13 1 0 19 1

# Sample Output 0
# 3 2 2 1 2
# 1 2 1 3 0 3 1 2 3 3 2 3

# Explanation 0

# On the first test case, to visit portal number three with power level 14, the scientist could teleport from the second portal at research center with power level 11, then teleport to portal number five with power level 13, then to portal number three with power level 14. The minimum required protection level to make that journey is max(|11 - 13|,|13 - 14|) = 2.

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