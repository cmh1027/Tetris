cellSize, columns, rows, trial = 20, 11, 21, 12
initScore, initLines, initY, lvlStep, white = 0, 0, 0, 9, 255
colourfav = (228, 204, 200)
pauseMsg = "Paused. Hit P to Resume"
lvlDebuggerMsg = "Debug level"
tetrisFact = []
colours = []
for i in range(72, 230, 18):
	for k in range(72, 230, 18):
		for j in range(72, 230, 18):
			colours.append([i, k, j])
tetrisShapes = []
oddtetrisShapes = []
oddtetrisShapes2 = []
bombShape = [[[2]], [[3]]]
tetrisShapes.append([[1, 1, 1, 1]])
tetrisShapes.append([[1, 0, 0], [1, 1, 1]])
tetrisShapes.append([[0, 0, 1], [1, 1, 1]])
tetrisShapes.append([[1, 1], [1, 1]])
tetrisShapes.append([[0, 1, 1], [1, 1, 0]])
tetrisShapes.append([[1, 1, 0], [0, 1, 1]])
tetrisShapes.append([[0, 1, 0], [1, 1, 1]])
tetrisShapes.append([[1, 1, 1, 1]])
tetrisShapes.append([[1, 0, 0], [1, 1, 1]])
tetrisShapes.append([[0, 0, 1], [1, 1, 1]])
tetrisShapes.append([[1, 1], [1, 1]])
tetrisShapes.append([[0, 1, 1], [1, 1, 0]])
tetrisShapes.append([[1, 1, 1, 1]])
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
oddtetrisShapes.append([[1, 0, 0], [1, 0, 0], [1, 1, 1]])
oddtetrisShapes.append([[0, 0, 1], [0, 0, 1], [1, 1, 1]])
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