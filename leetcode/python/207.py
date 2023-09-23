# 207. Course Schedule

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dict for prereqs
        course_map = {i: [] for i in range(numCourses)}
        # set to detect loops
        visited = set()

        # init prereq info
        for c, p in prerequisites:
            course_map[c].append(p)

        def dfs(course: int) -> bool:
            # are we in a loop?
            if course in visited:
                return False

            # if empty list, means no prereqs, reachable
            if not course_map[course]:
                return True

            visited.add(course)

            # recursively check prereqs
            for prereq in course_map[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            course_map[course] = []
            return True

        # check each course
        for c in course_map:
            if not dfs(c):
                return False

        # true if everything above went well
        return True


def test():
    solver = Solution()

    assert solver.canFinish(2, [[1, 0]]) == True
    assert solver.canFinish(2, [[1, 0], [0, 1]]) == False
    assert solver.canFinish(5, [[1, 4], [2, 4], [3, 1], [3, 2]]) == True

    print("All tests passed!")
