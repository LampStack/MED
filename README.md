# Minimum Edit Distance (MED) Calculator


## Overview
The Minimum Edit Distance (MED) Calculator is a Python class designed to calculate the minimum number of single-character edits required to transform one word into another. This project implements dynamic programming techniques to efficiently compute the minimum edit distance between two words.


## Features
- **Minimum Edit Distance Calculation**: Compute the minimum edit distance between two input words.
- **Edit Path Visualization**: Visualize the edit path, showing the sequence of insertions, deletions, and substitutions required to transform one word into another.
- **Graphical Representation**: Graphically display the shortest path from the bottom-right corner to the top-left corner of the dynamic programming matrix.


## Requirements
* Python 3.x
* Matplotlib
* NumPy


## Usage
To use the MED Calculator, simply instantiate the `MED` class with two input words, and then call the appropriate methods to display the results.
Example usage:
```python
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
```

## Contribution

If you would like to contribute to the enhancement and improvement of this project, please send a pull request. You can also report issues through the issue tracker.

## Contact

<a href="https://t.me/LampStack">Telegram</a><br>
<a href="mailto:xialop@outlook.com">Email</a>

## License

This project is released under the [MIT License](LICENSE).
