import matplotlib.pyplot as plt
import numpy as np


class MED:
    word1:str = None
    word2:str = None
    matrix:list = []
    path:list = []
    min_edit_distance:int = 0


    def __init__(self, word1:str, word2:str) -> None:
        self.word1 = word1
        self.word2 = word2
        self._setMatrix()
        self._setPathMatrix()


    def _setMatrix(self) -> None:
        m = len(self.word1)
        n = len(self.word2)
        self.matrix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    self.matrix[i][j] = j
                elif j == 0:
                    self.matrix[i][j] = i
                elif self.word1[i - 1] == self.word2[j - 1]:
                    self.matrix[i][j] = self.matrix[i - 1][j - 1]
                else:
                    self.matrix[i][j] = min(self.matrix[i - 1][j] + 1,
                                    self.matrix[i][j - 1] + 1,
                                    self.matrix[i - 1][j - 1] + 2)
        self.min_edit_distance = self.matrix[m][n]


    def _setPathMatrix(self) -> None:
        path_matrix = [[0] * len(self.matrix[0]) for _ in range(len(self.matrix))]
        m = len(self.matrix)
        n = len(self.matrix[0])
        i = m - 1
        j = n - 1
        while i >= 0 and j >= 0:
            path_matrix[i][j] = 1
            min_value = min(self.matrix[i - 1][j], self.matrix[i][j - 1], self.matrix[i - 1][j - 1])
            if min_value == self.matrix[i - 1][j - 1]:
                i -= 1
                j -= 1
            elif min_value == self.matrix[i - 1][j]:
                i -= 1
            else:
                j -= 1
        path_matrix[0][0] = 1
        self.path = path_matrix


    def showMatrix(self, matrix:list = None) -> None:
        """
        Display the dynamic programming matrix used to calculate the minimum edit distance.
        
        Parameters:
            matrix (list, optional): The dynamic programming matrix to display. 
                                     If not provided, defaults to self.matrix.

        Prints the matrix with values representing the minimum edit distance
        between substrings of word1 and word2.
        """
        m = len(self.word1)
        n = len(self.word2)
        print("\t#", end="")
        for j in range(n):
            print("\t" + self.word2[j], end="")
        print()
        for i in range(m + 1):
            print()
            if i == 0:
                print("#", end="")
            else:
                print(self.word1[i - 1], end="")
            for j in range(n + 1):
                print("\t" + str(matrix[i][j]), end="")
            print()


    def showEditPath(self) -> None:
        """
        Display the edit path showing the sequence of insertions, deletions, and substitutions
        required to transform word1 into word2.
        
        Prints the edit path as a series of actions (Match, Insert, Delete, Substitute).
        """
        path = []
        i, j = len(self.word1), len(self.word2)
        while i > 0 and j > 0:
            if self.word1[i - 1] == word2[j - 1]:
                path.append(('Match', self.word1[i - 1], self.word2[j - 1]))
                i -= 1
                j -= 1
            elif self.matrix[i][j] == self.matrix[i - 1][j] + 1:
                path.append(('Delete', self.word1[i - 1], '-'))
                i -= 1
            elif self.matrix[i][j] == self.matrix[i][j - 1] + 1:
                path.append(('Insert', '-', self.word2[j - 1]))
                j -= 1
            else:
                path.append(('Substitute', self.word1[i - 1], self.word2[j - 1]))
                i -= 1
                j -= 1

        while i > 0:
            path.append(('Delete', self.word1[i - 1], '-'))
            i -= 1
        while j > 0:
            path.append(('Insert', '-', self.word2[j - 1]))
            j -= 1
        for action, char1, char2 in path[::-1]:
            print(f"{action}: {char1} -> {char2}")


    def showPlot(self) -> None:
        """
        Display a graphical representation of the shortest path from the bottom-right 
        to the top-left corner of the dynamic programming matrix.
        
        Plots the shortest path as a line on a grid, with the starting point marked in red.
        """
        m = len(self.path)
        n = len(self.path[0])
        plt.figure(figsize=(8, 8))
        x = range(n)
        y = range(m)
        X, Y = np.meshgrid(x, y)
        plt.pcolormesh(X, Y, self.path, cmap='Greys', edgecolor='black')
        plt.plot([n - 1], [m - 1], marker='o', markersize=8, color="red")  # Starting point
        i = m - 1
        j = n - 1
        while i > 0 or j > 0:
            if i > 0 and self.path[i - 1][j] == 1:
                plt.plot([j, j], [i, i - 1], color="red", linewidth=2)
                i -= 1
            elif j > 0 and self.path[i][j - 1] == 1:
                plt.plot([j, j - 1], [i, i], color="red", linewidth=2)
                j -= 1
            else:
                plt.plot([j, j - 1], [i, i - 1], color="red", linewidth=2)
                i -= 1
                j -= 1

        plt.xticks(range(n))
        plt.yticks(range(m))
        plt.xlabel('Columns')
        plt.ylabel('Rows')
        plt.title('Shortest Path')
        plt.grid(True)
        plt.gca().invert_yaxis()
        plt.show()



if __name__ == '__main__':
    word1 = 'moment'
    word2 = 'government'
    myOBJ = MED(word1, word2)
    print("[+] Main Matrix :\n")
    myOBJ.showMatrix(myOBJ.matrix)
    print("\n\n[+] Path Matrix :\n")
    myOBJ.showMatrix(myOBJ.path)
    print("\n\n[+] Edit Path Steps :\n")
    myOBJ.showEditPath()
    myOBJ.showPlot()
