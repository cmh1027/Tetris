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
			for i in range(0, 2):
				if self.blockX + i < columns:
					if not self.checkCollision(self.board, newBlock, (self.blockX+i, self.blockY)):
						self.blockX = self.blockX+i
						self.block = newBlock
						return
			for i in range(0, -2, -1):
				if self.blockX + i >= 0:
					if not self.checkCollision(self.board, newBlock, (self.blockX+i, self.blockY)):
						self.blockX = self.blockX+i
						self.block = newBlock
						return
			for i in range(2, 5):
				if self.blockX + i < columns:
					if not self.checkCollision(self.board, newBlock, (self.blockX+i, self.blockY)):
						self.blockX = self.blockX+i
						self.block = newBlock
						return
			for i in range(-2, -5, -1):
				if self.blockX + i >= 0:
					if not self.checkCollision(self.board, newBlock, (self.blockX+i, self.blockY)):
						self.blockX = self.blockX+i
						self.block = newBlock
						return
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
			else:
				newBlock = [[self.holdBlock[x][y] for x in range(len(self.holdBlock))] for y in range(len(self.holdBlock[0]) - 1, -1, -1)]
				if not self.checkCollision(self.board, newBlock, (self.blockX, self.blockY)):
					self.block, self.holdBlock = newBlock, self.block
	def hold2(self):
		if self.holdBlock2==None:
			self.holdBlock2 = self.block
			self.newBlock()
		else:
			if not self.checkCollision(self.board, self.holdBlock2, (self.blockX, self.blockY)):
				self.block, self.holdBlock2 = self.holdBlock2, self.block
			else:
				newBlock = [[self.holdBlock2[x][y] for x in range(len(self.holdBlock2))] for y in range(len(self.holdBlock2[0]) - 1, -1, -1)]
				if not self.checkCollision(self.board, newBlock, (self.blockX, self.blockY)):
					self.block, self.holdBlock2 = newBlock, self.block
	def removeBlock(self):
		if self.remove>0:
			self.remove -= 1
			pygame.mixer.Channel(5).play(self.skip)
			self.newBlock();
	def slowBlock(self):
		if self.slow>0:
			if not self.slowflag:
				pygame.mixer.Channel(6).play(self.slowdown)
				self.slow -= 1
				self.slowcount = 5
				self.slowflag = True
				self.currentdelay = int(self.currentdelay*2)
				pygame.time.set_timer(pygame.USEREVENT + 1, int(self.currentdelay))
	def bombBlock(self):
		if self.bomb>0:
			self.bomb -= 1
			self.newBlock(True)
	def ghost_toggle(self):
		self.ghost = not self.ghost
	def drop(self):
		if(self.gameover == False and self.paused == False):
			self.blockY += 1
			if self.checkCollision(self.board, self.block, (self.blockX, self.blockY)):
				if self.block != [[2]] and self.block != [[3]]:
					self.board = self.joinMatrices(self.board, self.block, (self.blockX, self.blockY))
					self.newBlock()
					clearedRows = 0
					clearedRows = self.checkRowFull(clearedRows)
					self.addClearedLines(clearedRows)
					if self.slowcount>0:
						if self.slowcount==1:
							pygame.mixer.Channel(6).play(self.fast)
							self.currentdelay=int(self.currentdelay/2)
							pygame.time.set_timer(pygame.USEREVENT + 1, self.currentdelay)
							self.slowflag = False
						self.slowcount -= 1
				elif self.block == [[3]]:
					pygame.mixer.Channel(4).play(self.explode)
					for i in range(rows):
						self.board[i][self.blockX] = 0
					self.newBlock()					
				else:
					pygame.mixer.Channel(4).play(self.explode)
					for i in range(-2, 3):
						for k in range(-2, 3):
							if self.blockX + i >= 0 and self.blockY + k >=0 and self.blockX + i <= columns-1 and self.blockY + k <= rows-1:
								self.board[self.blockY+k][self.blockX+i] = 0
					self.newBlock()
				return True
		return False

	def newBlock(self, bomb=False):
		if self.gameType == "Advanced":
			if not bomb:
				self.block = self.nextBlock
				ran = random.randrange(1000)
				if 100-self.level*3<=ran<=125+self.level*3:
					self.nextBlock = oddtetrisShapes2[rand(len(oddtetrisShapes))]
				elif 400-self.level*6<=ran<450+self.level*6:
					self.nextBlock = oddtetrisShapes[rand(len(oddtetrisShapes))]
				else:
					self.nextBlock = tetrisShapes[rand(len(tetrisShapes))]
				if 787<=ran<789:
					self.nextBlock = bombShape[0]
				if 815<=ran<820:
					self.nextBlock = bombShape[1]
				self.blockX = int(columns / 3 - len(self.block[0]) / 2 + trial - 7)
				self.blockY = initY
			else:
				self.block = bombShape[0]
				self.blockX = int(columns / 3 - len(self.block[0]) / 2 + trial - 7)
				self.blockY = initY
		else:
			self.block = self.nextBlock
			self.nextBlock = tetrisShapes[rand(len(tetrisShapes))]
			self.blockX = int(columns / 3 - len(self.block[0]) / 2 + trial - 7)
			self.blockY = initY
		if self.checkCollision(self.board, self.block, (self.blockX, self.blockY)):
			self.gameover = True
			pygame.mixer.Channel(7).play(self.over)
		else:
			False

	def renderMatrix(self, matrix, offset, flag=True, hold=True):
		if matrix!=None:
			if matrix!=[[2]] and matrix!=[[3]]:
				for y, row in enumerate(matrix):
					for x, val in enumerate(row):
						if flag:
							if val:
								if hold:
									if(self.score >= 0 and self.level >= 0):
										pygame.draw.rect(self.screen, colours[self.inside], pygame.Rect((offset[0] +x) * cellSize, (offset[1] + y) * cellSize, cellSize, cellSize), 0)
										pygame.draw.rect(self.screen, colours[self.border], pygame.Rect(((offset[0] +x) * cellSize)+2, ((offset[1] + y) * cellSize)+2, cellSize-4, cellSize-4), 0)
								else:
									if(self.score >= 0 and self.level >= 0):
										pygame.draw.rect(self.screen, colours[self.inside], pygame.Rect((offset[0] +x*0.75) * cellSize, (offset[1] + y*0.75) * cellSize, cellSize*0.75, cellSize*0.75), 0)
										pygame.draw.rect(self.screen, colours[self.border], pygame.Rect(((offset[0] +x*0.75) * cellSize)+2, ((offset[1] + y*0.75) * cellSize+1.5), cellSize*0.75-4, cellSize*0.75-4), 0)										

						else:
							if(self.score>=0 and self.level>=0):
								pygame.draw.rect(self.screen, [35,35,35], pygame.Rect((offset[0] +x) * cellSize, (offset[1] + y) * cellSize, cellSize, cellSize), 0)
								pygame.draw.rect(self.screen, [75,75,75], pygame.Rect(((offset[0] +x) * cellSize)+1, ((offset[1] + y) * cellSize)+1, cellSize-2, cellSize-2), 0)
			elif matrix==[[3]]:
				for y, row in enumerate(matrix):
					for x, val in enumerate(row):
						if hold:
							if(self.score >= 0 and self.level >= 0):
								pygame.draw.rect(self.screen, [0, 240, 240], pygame.Rect((offset[0] +x) * cellSize, (offset[1] + y) * cellSize, cellSize, cellSize), 0)
						else:
							if(self.score >= 0 and self.level >= 0):
								pygame.draw.rect(self.screen, [0, 240, 240], pygame.Rect((offset[0] +x*0.75) * cellSize, (offset[1] + y*0.75) * cellSize, cellSize*0.75, cellSize*0.75), 0)							
			else:
				for y, row in enumerate(matrix):
					for x, val in enumerate(row):
						if hold:
							if(self.score >= 0 and self.level >= 0):
								pygame.draw.rect(self.screen, [255, 0, 0], pygame.Rect((offset[0] +x) * cellSize, (offset[1] + y) * cellSize, cellSize, cellSize), 0)
						else:
							if(self.score >= 0 and self.level >= 0):
								pygame.draw.rect(self.screen, [255, 0, 0], pygame.Rect((offset[0] +x*0.75) * cellSize, (offset[1] + y*0.75) * cellSize, cellSize*0.75, cellSize*0.75), 0)			
	
	def renderGhostMatrix(self, matrix, offset):
		if matrix!=None:
			while not self.checkCollision(self.board, matrix, (offset[0], offset[1]+1)):
				offset = (offset[0], offset[1]+1)
			for y, row in enumerate(matrix):
				for x, val in enumerate(row):
					if val:
						if(self.score >= 0 and self.level >= 0):
							pygame.draw.rect(self.screen, [96,96,96], pygame.Rect((offset[0] +x) * cellSize, (offset[1] + y) * cellSize, cellSize, cellSize), 0)
							pygame.draw.rect(self.screen, [45,45,45], pygame.Rect(((offset[0] +x) * cellSize)+2, ((offset[1] + y) * cellSize)+2, cellSize-4, cellSize-4), 0)

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
