class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        orig = image[sr][sc]
        if orig == color:
            return image
        q = [(sr, sc)]
        while len(q) > 0:
            i, j = q.pop(0)
            if i < 0 or i > R-1 or j < 0 or j > C-1:
                continue
            if image[i][j] == orig:
                image[i][j] = color
                q.append((i-1, j))
                q.append((i+1, j))
                q.append((i, j-1))
                q.append((i, j+1))
        return image