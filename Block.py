from random import randrange as rand
import random
import os
import pygame
import math
import sys
from constants import *

class Block(object):

	def joinMatrices(self, mat1, mat2, mat2Off):
		offX = mat2Off[0]
		offY = mat2Off[1]
		for countY, row in enumerate(mat2):
			for countX, val in enumerate(row):
				mat1[countY + offY + trial - 13][countX + offX] += val
		return mat1

	def moveLeft(self):
		if(self.gameover == False and self.paused == False):
			newX = self.blockX - 1
			if newX < 0:
				newX = 0
			if not self.checkCollision(self.board, self.block, (newX, self.blockY)):
				self.blockX = newX

	def moveRight(self):
		if(self.gameover == False and self.paused == False):
			newX = self.blockX + 1
			if newX > columns - len(self.block[0]):
				newX = columns - len(self.block[0])
			if not self.checkCollision(self.board, self.block, (newX, self.blockY)):
				self.blockX = newX

	def rotate(self):
		if(self.gameover == False and self.paused == False):
			newBlock = [[self.block[x][y] for x in range(len(self.block))] for y in range(len(self.block[0]) - 1, -1, -1)]
			if not self.checkCollision(self.board, newBlock, (self.blockX, self.blockY)):
				self.block = newBlock

	def fallBottom(self):
		if(self.gameover == False and self.paused == False):
			self.score += trial - 2
			while(not self.drop()):
				pass
	def hold(self):
		if self.holdBlock==None:
			self.holdBlock = self.block
			self.newBlock()
		else:
			if not self.checkCollision(self.board, self.holdBlock, (self.blockX, self.blockY)):
				self.block, self.holdBlock = self.holdBlock, self.block
	def hold2(self):
		if self.holdBlock2==None:
			self.holdBlock2 = self.block
			self.newBlock()
		else:
			if not self.checkCollision(self.board, self.holdBlock2, (self.blockX, self.blockY)):
				self.block, self.holdBlock2 = self.holdBlock2, self.block
	def drop(self):
		if(self.gameover == False and self.paused == False):
			self.blockY += 1
			if self.checkCollision(self.board, self.block, (self.blockX, self.blockY)):
				self.board = self.joinMatrices(self.board, self.block, (self.blockX, self.blockY))
				self.newBlock()
				clearedRows = 0
				clearedRows = self.checkRowFull(clearedRows)
				self.addClearedLines(clearedRows)
				return True
		return False

	def newBlock(self):
		self.block = self.nextBlock
		ran = random.randrange(1000)
		if self.level<10:
			if 100-self.level*3<=ran<=150+self.level*3:
				self.nextBlock = oddtetrisShapes2[rand(len(oddtetrisShapes))]
			elif 400-self.level*15<=ran<600+self.level*15:
				self.nextBlock = oddtetrisShapes[rand(len(oddtetrisShapes))]
			else:
				self.nextBlock = tetrisShapes[rand(len(tetrisShapes))]
		else:
			if 400-self.level*15<=ran<600+self.level*15:
				self.nextBlock = oddtetrisShapes[rand(len(oddtetrisShapes))]
			elif 800-self.level*(self.level-10)*6<=ran<900+self.level*(self.level-10)*6:
				self.nextBlock = oddtetrisShapes2[rand(len(oddtetrisShapes))]
			else:
				self.nextBlock = tetrisShapes[rand(len(tetrisShapes))]			
		self.blockX = int(columns / 3 - len(self.block[0]) / 2 + trial - 7)
		self.blockY = initY
		if self.checkCollision(self.board, self.block, (self.blockX, self.blockY)):
			self.gameover = True
		else:
			False

	def renderMatrix(self, matrix, offset, flag=True):
		if matrix!=None:
			for y, row in enumerate(matrix):
				for x, val in enumerate(row):
					if flag:
						if val:
							if(self.score >= 0 and self.level >= 0):
									pygame.draw.rect(self.screen, colours[6], pygame.Rect((offset[0] +x) * cellSize, (offset[1] + y) * cellSize, cellSize, cellSize), 0)
									pygame.draw.rect(self.screen, colours[7], pygame.Rect(((offset[0] +x) * cellSize)+1, ((offset[1] + y) * cellSize)+1, cellSize-2, cellSize-2), 0)
					else:
						if(self.score>=0 and self.level>=0):
							pygame.draw.rect(self.screen, [35,35,35], pygame.Rect((offset[0] +x) * cellSize, (offset[1] + y) * cellSize, cellSize, cellSize), 0)
							pygame.draw.rect(self.screen, [75,75,75], pygame.Rect(((offset[0] +x) * cellSize)+1, ((offset[1] + y) * cellSize)+1, cellSize-2, cellSize-2), 0)
							

	def checkRowFull(self, clearedRows):
		while 1:
			for i, row in enumerate(self.board[:-1]):
				if 0 not in row:
					scores = self.score
					self.board = self.removeRow(self.board, i)
					clearedRows += 1
					break
			else:
				break
		return clearedRows