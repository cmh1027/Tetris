from random import randrange as rand
from Board import Board
from Block import Block
import os
import pygame
import math
import sys
from constants import *

class Gameplay(Block, Board):
	def __init__(self):
		if len(sys.argv)==1:
			self.dif = 'easy' # difficulty
		else:
			if sys.argv[1].lower() == 'easy':
				self.dif = 'easy'
				self.level = 1
			elif sys.argv[1].lower() == 'normal':
				self.dif = 'normal'
				self.level = 5
			elif sys.argv[1].lower() == 'hard':
				self.dif = 'hard'
				self.level = 10
			elif sys.argv[1].lower() == 'hell':
				self.dif = 'hell'
				self.level = 15
			else:
				self.dif = 'easy'
		pygame.init()
		rowscounter = 0
		pygame.key.set_repeat(250, 25)
		self.rlim = cellSize * columns
		self.default_font = pygame.font.SysFont("comicsansms", 17)
		self.dif_font = pygame.font.SysFont("comicsansms", 25)
		self.nextBlock = tetrisShapes[rand(len(tetrisShapes))]
		self.holdBlock = None
		self.holdBlock2 = None
		self.height = cellSize * rows
		self.bground_grid = [[0 for x in range(columns)]for y in range(rows)]
		for i in range(rows):
			for j in range(columns):
				if(i % 2 == j % 2):
					self.bground_grid[i][j] = 8
		self.width = cellSize * (columns + 12)
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.limit = self.rlim
		self.initialiseGame()
		self.slow=3
		self.remove=3
		self.bomb=3

	def updateScore(self, increment):
		self.score += increment

	def initialiseGame(self):
		self.board = self.newBoard()
		self.newBlock()
		self.score = initScore
		self.lines = initLines
		self.holdBlock = None
		self.holdBlock2 = None
		pygame.time.set_timer(pygame.USEREVENT + 1, int(1000*(0.8**(self.level-1))))

	def centreMsg(self, msg):
		for i, line in enumerate(msg.splitlines()):
			self.default_font.render(line, False, (254, 254, 254), (1, 1, 1))
			msgim_center_x = self.default_font.render(line, False, (254, 254, 254), (1, 1, 1)).get_size()[0]
			msgim_center_y = self.default_font.render(line, False, (254, 254, 254), (1, 1, 1)).get_size()[1]
			msgim_center_x = (int) (msgim_center_x / 2)
			msgim_center_y = (int) (msgim_center_x / 2)
			self.screen.blit(self.default_font.render(line, False, (254, 254, 254), (1, 1, 1)), ((int)(self.width / 2) - msgim_center_x, (int)(self.height / (trial - 10)) - msgim_center_y + i * (trial + 10)))

	def dispMsg(self, msg, topleft):
		x = topleft[0]
		y = topleft[1]
		trial = 12
		for line in msg.splitlines():
			arg = False
			self.screen.blit(self.default_font.render(line, arg, (white, white, white), (1, 1, 1)), (x, y))
			y += 14

	def difMsg(self, msg, topleft):
		x = topleft[0]
		y = topleft[1]
		trial = 12
		for line in msg.splitlines():
			arg = False
			self.screen.blit(self.dif_font.render(line, arg, (white, white, white), (1, 1, 1)), (x, y))
			y += 14
	def addClearedLines(self, n):
		linescores = [0, 100, 250, 450, 700, 1000]
		self.lines = self.lines + n
		self.updateScore(linescores[n] * self.level)
		if(self.lines >= self.level * lvlStep):
			self.level += 1
			newdelay = int(1000*(0.8**(self.level-1)))
			if(newdelay < 100):
				newdelay = 100
			if(newdelay > 100):
				newdelay
			else:
				newdelay
			pygame.time.set_timer(pygame.USEREVENT + 1, newdelay)

	def quit(self):
		pygame.display.update()
		sys.exit()

	def begin(self):
		if self.gameover:
			self.initialiseGame()
			self.gameover = False
			self.paused = False

	def switchPause(self):
		if(self.paused == True):
			self.paused = False
		else:
			self.paused = True

	def run(self):
		keyBindings = {
			'LEFT': lambda:self.moveLeft(),
			'RIGHT': lambda:self.moveRight(),
			'DOWN': lambda:self.drop(),
			'r': lambda:self.initialiseGame(),
			'ESCAPE': lambda:self.quit(),
			'p': lambda:self.switchPause(),
			'h': lambda:self.hold(),
			'g': lambda:self.hold2(),
			'RETURN': lambda:self.begin(),
			'SPACE': lambda:self.fallBottom(),
			's': lambda:self.rotate()
		}
		self.gameover = False
		self.paused = False
		if(self.gameover == True or self.paused == True):
			sys.exit(15)
		cpuLimit = pygame.time.Clock()
		while trial:
			self.screen.fill((0, 0, 0))
			if self.gameover:
				restart = 0
				self.centreMsg("""Game Over!\n \n \nYour score is: %d \n\nHit Enter to restart""" % self.score)
			else:
				if self.paused:
					self.centreMsg(pauseMsg)
				else:
					pygame.draw.line(self.screen, colourfav, (self.limit + 1, 0), (self.limit + 1, self.height - 1))
					self.dispMsg("\nNext:", (self.limit + cellSize, 1))
					if self.dif=='easy':
						self.difMsg("\nEASY\n\nMODE", (self.limit + cellSize + 115, 1))
					elif self.dif=='normal':
						self.difMsg("\nNOMRAL\n\n  MODE", (self.limit + cellSize + 100, 1))
					elif self.dif=='hard':
						self.difMsg("\nHARD\n\nMODE", (self.limit + cellSize + 115, 1))
					else:
						self.difMsg("\nHELL\n\nMODE", (self.limit + cellSize + 115, 1))

					self.dispMsg("\nHold 1:", (self.limit + cellSize, cellSize*4+5))
					self.dispMsg("\nHold 2:", (self.limit + cellSize + 120, cellSize*4+5))
					self.dispMsg("Items left", (self.limit + cellSize + 120, cellSize * 10+10))
					self.dispMsg("Slow ", (self.limit + cellSize + 115, cellSize * 11+15))
					if self.slow==0:
						self.dispMsg("N/A", (self.limit + cellSize + 165, cellSize * 11+15))
					else:
						for i in range(self.slow):
							self.dispMsg("O ", (self.limit + cellSize + 150 + 15*(i+1), cellSize * 11+15))
					self.dispMsg("Away ", (self.limit + cellSize + 115, cellSize * 12+15))
					if self.remove==0:
						self.dispMsg("N/A", (self.limit + cellSize + 165, cellSize * 12+15))
					else:
						for i in range(self.remove):
							self.dispMsg("O ", (self.limit + cellSize + 150 + 15*(i+1), cellSize * 12+15))
					self.dispMsg("Bomb ", (self.limit + cellSize + 115, cellSize * 13+15))
					if self.bomb==0:
						self.dispMsg("N/A", (self.limit + cellSize + 165, cellSize * 13+15))
					else:
						for i in range(self.bomb):
							self.dispMsg("O ", (self.limit + cellSize + 150 + 15*(i+1), cellSize * 13+15))
					self.dispMsg("Score: %d\n\nDifficulty: %d" % (self.score, self.level), (self.limit + cellSize, cellSize * 9+25))
					self.dispMsg("r : restart\n\np : pause\n\ng/h : hold\n\ns : rotate\n\nSpace:fall", (self.limit + cellSize, cellSize * 13))
					self.dispMsg("1 : Slow\n\n2 : Away\n\n3 : Bomb\n\n", (self.limit + cellSize+120, cellSize * 16))
					self.renderMatrix(self.bground_grid, (0, trial - 12), False)
					self.renderMatrix(self.board, (0, trial /2 - 6))
					emptyness = self.checkRowEmpty(5, self.board)
					self.renderMatrix(self.block, (self.blockX, self.blockY))
					self.renderMatrix(self.nextBlock, (columns + 1, 2))
					self.renderMatrix(self.holdBlock, (columns + 1, 6))
					self.renderMatrix(self.holdBlock2, (columns + 7, 6))
			pygame.display.update()
			funTime = True
			for event in pygame.event.get():
				if event.type == pygame.USEREVENT + 1:
					self.drop()
					funTime = True
				elif event.type == pygame.QUIT:
					self.quit()
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if(self.score >= 0 and self.level >= 0):
						for key in keyBindings:
							if event.key == eval("pygame.K_"+key):
								keyBindings[key]()
			cpuLimit.tick(60)

if __name__ == '__main__':
	App = Gameplay()
	App.run()