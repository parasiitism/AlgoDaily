"""
    hashset, sort

    Time    O(NlogN) <- or O(NlogK) if we use a maxheap
    Space   O(N)
"""


class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive_set = set(positive_feedback)
        negative_set = set(negative_feedback)
        n = len(report)
        students_score = []
        for i in range(n):
            r = report[i]
            sid = student_id[i]
            score = 0
            for c in r.split(" "):
                if c in positive_set:
                    score += 3
                elif c in negative_set:
                    score -= 1
            students_score.append([score, sid])
        students_score.sort(key=lambda x: (-x[0], x))
        return [b for _a, b in students_score[:k]]
