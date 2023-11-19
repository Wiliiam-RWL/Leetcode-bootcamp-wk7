class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: (x[0], x[1]))
        print(points)
        N = len(points)
        i = 0
        num = 0
        while i < N:
            # record the range that we can shoot the arrow
            start, end = points[i][0], points[i][1]
            while True:
                # keep finding overlaps, cutting the range
                if i + 1 < N and points[i + 1][1] >= start and points[i + 1][0] <= end:
                    i += 1
                    # adjust the overlap area
                    start = max(start, points[i][0])
                    end = min(end, points[i][1])
                    print(start, end)
                else:
                    break
            i += 1
            num += 1
        return num
