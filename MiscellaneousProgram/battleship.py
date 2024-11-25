def isValid(p1,p2,p3):
    points = [p1,p2,p3]
    points.sort()
    r1, c1 = int(points[0][0]), int(points[0][1])
    r2, c2 = int(points[1][0]), int(points[1][1])
    r3, c3 = int(points[2][0]), int(points[2][1])
    
    horizontal = r1 == r2 == r3 and c1+1 == c2 and c2+1 == c3 
    vertical = c1 == c2 == c3 and r1+1 == r2 and r2+1 ==r3
    diagonal = r1+1 == r2 and r2+1 == r3 and c1+1 == c2 and c2+1 ==c3

    return horizontal or vertical or diagonal

def play():
    p1a,p2a,p3a = input(), input(), input()
    if not isValid(p1a,p2a,p3a):
        print("incorrect")
        return
    
    p1b,p2b,p3b = input(), input(), input()
    if not isValid(p1b,p2b,p3b):
        print("incorrect")
        return

    shipA = [p1a,p2a,p3a]
    shipB = [p1b,p2b,p3b]
    scoreA,scoreB = 0,0

    for  i in range(3):
        if input() in shipB:
            scoreA += 1
        if input() in shipA:
            scoreB += 1
    
    if scoreA > scoreB:
        print("A wins by",scoreA-scoreB,"points")
    elif scoreB > scoreA:
        print("B wins by",scoreB-scoreA,"points")
    else:
        print("A and B ties by",scoreA,"points")

play()