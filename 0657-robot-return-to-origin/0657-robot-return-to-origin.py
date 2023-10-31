class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x=0
        y=0
        
        for i in range(len(moves)):
            if moves[i] == 'U':
                y+=1
            elif moves[i] == 'D':
                y-=1
            elif moves[i] == 'L':
                x-=1
            elif moves[i]== 'R':
                x+=1
        total = [x,y]
        target = [0,0]
        return total == target