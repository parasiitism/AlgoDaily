class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if len(image) == 0 or len(image[0]) == 0:
            return []

        for i in range(len(image)):
            for j in range(len(image[0])):
                if sr == i and sc == j and image[i][j] != newColor:
                    self.bfs(image, i, j, newColor)
        return image

    def bfs(self, image, x, y, newColor):
        origColor = image[x][y]
        q = [(x, y)]
        while len(q) > 0:
            i, j = q.pop(0)
            if i < 0 or i+1 > len(image) or j < 0 or j+1 > len(image[0]):
                continue
            if image[i][j] == origColor:
                image[i][j] = newColor
                q.append((i-1, j))
                q.append((i+1, j))
                q.append((i, j-1))
                q.append((i, j+1))
