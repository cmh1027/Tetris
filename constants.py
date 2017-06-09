cellSize, columns, rows, trial = 20, 11, 21, 12
initScore, initLines, initY, lvlStep, white = 0, 0, 0, 5, 255
colourfav = (228, 204, 200)
pauseMsg = "Paused. Hit P to Resume"
lvlDebuggerMsg = "Debug level"
tetrisFact = []
colours = [
[86, 108, 48],
[0, 240, 240],
[149, 160, 217],
[0, 0, 240],
[36, 34, 37],
[240, 160, 2],
[254, 86, 85],
[240, 240, 0],
[55, 69, 79],
[0, 240, 0],
[121, 107, 244],
[160, 0, 240],
[149, 160, 217],
[36, 34, 36]
]
tetrisShapes = []
oddtetrisShapes = []
oddtetrisShapes2 = []
bombShape = [[[2]]]
tetrisShapes.append([[1, 1, 1, 1]])
tetrisShapes.append([[1, 0, 0], [1, 1, 1]])
tetrisShapes.append([[0, 0, 1], [1, 1, 1]])
tetrisShapes.append([[1, 1], [1, 1]])
tetrisShapes.append([[0, 1, 1], [1, 1, 0]])
tetrisShapes.append([[1, 1, 0], [0, 1, 1]])
tetrisShapes.append([[0, 1, 0], [1, 1, 1]])
oddtetrisShapes.append([[1, 1, 1, 1], [0, 0, 0, 1]])
oddtetrisShapes.append([[1, 1, 1, 1], [1, 0, 0, 1]])
oddtetrisShapes.append([[1, 1, 1, 1], [0, 0, 1, 0]])
oddtetrisShapes.append([[1, 1, 1, 1], [0, 1, 0, 0]])
oddtetrisShapes.append([[1, 1, 0, 0], [1, 1, 1, 0]])
oddtetrisShapes.append([[1, 1, 0, 0], [0, 1, 1, 1]])
oddtetrisShapes.append([[1, 1, 1, 1, 1]])
oddtetrisShapes.append([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
oddtetrisShapes.append([[1, 0, 1], [1, 1, 1]])
oddtetrisShapes.append([[1, 1, 0], [0, 1, 1], [0, 0, 1]])
oddtetrisShapes.append([[0, 1, 1], [1, 1, 0], [1, 0, 0]])
oddtetrisShapes.append([[0, 1, 0], [0, 1, 0], [1, 1, 1]])
oddtetrisShapes.append([[1, 0, 0], [1, 1, 1], [0, 0, 1]])
oddtetrisShapes2.append([[1, 1, 1, 1], [1, 0, 0, 1]])
oddtetrisShapes2.append([[1, 1, 1, 1], [1, 0, 1, 0]])
oddtetrisShapes2.append([[1, 1, 1, 1], [0, 1, 1, 0]])
oddtetrisShapes2.append([[1, 1, 1, 1], [1, 1, 0, 0]])
oddtetrisShapes2.append([[1, 1], [1, 1], [1, 1]])
oddtetrisShapes2.append([[1, 1, 1], [0, 1, 1], [0, 0, 1]])
oddtetrisShapes2.append([[1, 0, 0], [1, 1, 1], [0, 1, 0]])
oddtetrisShapes2.append([[1, 0, 0], [1, 1, 1], [0, 1, 1]])
oddtetrisShapes2.append([[1, 0, 1], [1, 1, 1], [0, 1, 0]])
oddtetrisShapes2.append([[1, 0, 1], [1, 1, 1], [0, 0, 1]])
oddtetrisShapes2.append([[1, 0, 1], [1, 1, 1], [1, 0, 0]])
oddtetrisShapes2.append([[1, 0, 0, 0, 0], [1, 1, 1, 1, 1]])
oddtetrisShapes2.append([[0, 0, 0, 0, 1], [1, 1, 1, 1, 1]])
oddtetrisShapes2.append([[0, 0, 1, 1, 1], [1, 1, 1, 0, 0]])
oddtetrisShapes2.append([[1, 1, 1, 0, 0], [0, 0, 1, 1, 1]])