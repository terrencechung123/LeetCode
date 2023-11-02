class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        if len(sorted_score) >= 1:
            gold = max(sorted_score)
            score[score.index(gold)] = 'Gold Medal'
        if len(sorted_score) >= 2:
            silver = sorted_score[1]
            score[score.index(silver)] = 'Silver Medal'
        if len(sorted_score)>=3:
            bronze = sorted_score[2]
            score[score.index(bronze)] = 'Bronze Medal'
        for num in score:
            if isinstance(num,int):
                score[score.index(num)] = str(sorted_score.index(num)+1)

        return score