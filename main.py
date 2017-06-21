from random import randrange as rand
from Board import Board
from Block import Block
import pickle
import os
import pygame
import math
import sys
from constants import *

class Gameplay(Block, Board):
	def __init__(self):
		pygame.mixer.init(44100, -16,2,2048)
		pygame.mixer.init(44100, -16,3,2048)
		pygame.mixer.init(44100, -16,4,2048)
		pygame.mixer.init(44100, -16,5,2048)
		pygame.mixer.init(44100, -16,6,2048)
		pygame.mixer.init(44100, -16,7,2048)
		self.blockfull = pygame.mixer.Sound('./music/blockfull.wav')
		self.levelup = pygame.mixer.Sound('./music/levelup.wav')
		self.explode = pygame.mixer.Sound('./music/bomb.wav')
		self.skip = pygame.mixer.Sound('./music/skip.wav')
		self.slowdown = pygame.mixer.Sound('./music/slow.wav')
		self.fast = pygame.mixer.Sound('./music/fast.wav')
		self.over = pygame.mixer.Sound('./music/over.wav')
		pygame.init()
		rowscounter = 0
		pygame.key.set_repeat(250, 25)
		self.rlim = cellSize * columns
		self.default_font = pygame.font.SysFont("comicsansms", 17)
		self.dif_font = pygame.font.SysFont("comicsansms", 26)
		self.title_font = pygame.font.SysFont("comicsansms", 60)
		self.menu_font = pygame.font.SysFont("comicsansms", 30)
		self.nextBlock = tetrisShapes[rand(len(tetrisShapes))]
		self.height = cellSize * rows
		self.bground_grid = [[0 for x in range(columns)]for y in range(rows)]
		for i in range(rows):
			for j in range(columns):
				if(i % 2 == j % 2):
					self.bground_grid[i][j] = 8
		self.width = cellSize * (columns + 12) + 10
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.limit = self.rlim
		self.screentype = 0
		self.lvlStep = 9
		self.gameType = "Advanced"
		self.volume = 5

	def updateScore(self, increment):
		self.score += increment

	def initialiseGame(self, dif):
		pygame.mixer.music.load('./music/'+dif+'.mp3')
		pygame.mixer.music.set_volume(self.volume/10)
		self.blockfull.set_volume(self.volume/10)
		self.levelup.set_volume(self.volume/10)
		self.explode.set_volume(self.volume/10)
		self.skip.set_volume(self.volume/10)
		self.slowdown.set_volume(self.volume/10)
		self.fast.set_volume(self.volume/10)
		self.over.set_volume(self.volume/10)
		pygame.mixer.music.rewind()
		self.dif=dif
		self.border = rand(len(colours))
		self.inside = 9-self.border
		self.board = self.newBoard()
		self.score = initScore
		self.lines = initLines
		self.holdBlock = None
		self.holdBlock2 = None
		self.slowcount = 0;
		self.slowflag = False
		self.ghost = False
		if self.dif=="easy":
			self.slow=3
			self.remove=3
			self.bomb=3
			self.level=1
			self.start=1
		if self.dif=="normal":
			self.slow=2
			self.remove=2
			self.bomb=2
			self.level=5
			self.start=5
		if self.dif=="hard":
			self.slow=1
			self.remove=1
			self.bomb=1
			self.level=10
			self.start=10
		if self.dif=="hell":
			self.slow=0
			self.remove=0
			self.bomb=0
			self.level=15
			self.start=15
		self.currentitem = 1
		if self.gameType == 'Classic':
			self.slow = 0
			self.remove = 0
			self.bomb = 0
		self.newBlock()
		self.currentdelay = int(1000*(0.8**(self.level-1)))
		pygame.time.set_timer(pygame.USEREVENT + 1, self.currentdelay)
		pygame.mixer.music.play(-1)

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
			y += 12

	def difMsg(self, msg, topleft):
		x = topleft[0]
		y = topleft[1]
		trial = 12
		for line in msg.splitlines():
			arg = False
			self.screen.blit(self.dif_font.render(line, arg, (white, white, white), (1, 1, 1)), (x, y))
			y += 16

	def titleMsg(self, msg, topleft):
		x = topleft[0]
		y = topleft[1]
		trial = 12
		for line in msg.splitlines():
			arg = False
			self.screen.blit(self.title_font.render(line, arg, (white, white, white), (1, 1, 1)), (x, y))
			y += 14

	def menuMsg(self, msg, topleft):
		x = topleft[0]
		y = topleft[1]
		trial = 12
		for line in msg.splitlines():
			arg = False
			self.screen.blit(self.menu_font.render(line, arg, (white, white, white), (1, 1, 1)), (x, y))
			y += 14

	def addClearedLines(self, n):
		linescores = [0, 100, 250, 450, 700, 1000]
		self.lines = self.lines + n
		if n>0:
			pygame.mixer.Channel(3).play(self.blockfull)
		self.updateScore(linescores[n] * self.level)
		if int(self.score/10000)>=self.currentitem and self.gameType=='Advanced':
			self.currentitem+=1
			if self.slow<4:
				self.slow+=1
			if self.remove<4:
				self.remove+=1
			if self.bomb<4:
				self.bomb+=1
		if(self.lines >= (self.level-self.start+1) * self.lvlStep):
			self.border = rand(len(colours))
			self.inside = 9-self.border
			while self.inside == self.border:
				self.inside = rand(len(colours))
			pygame.mixer.Channel(3).play(self.levelup)
			self.level += 1
			if self.slowcount>0:
				newdelay = int(1000*(0.8**(self.level-1))*2)
			else:
				newdelay = int(1000*(0.8**(self.level-1)))
			self.currentdelay = newdelay
			pygame.time.set_timer(pygame.USEREVENT + 1, newdelay)

	def quit(self):
		pygame.display.update()
		sys.exit()

	def begin(self):
		if self.gameover:
			self.gameover = False
			self.paused = False
			self.screentype = 0
			self.main()

	def switchPause(self):
		if(self.paused == True):
			pygame.mixer.music.unpause()
			self.paused = False
		else:
			pygame.mixer.music.pause()
			self.paused = True
	def upCursor(self, bottom):
		if self.selectNum>0:
			self.selectNum-=1
		else:
			self.selectNum=bottom
	def downCursor(self, bottom):
		if self.selectNum<bottom:
			self.selectNum+=1
		else:
			self.selectNum=0

	def main_select(self):
		if self.selectNum==0:
			self.screentype=1
			self.screen_dif()
		elif self.selectNum==2:
			self.screentype=4
			self.screen_config()
		elif self.selectNum==3:
			pygame.display.update()
			sys.exit()

	def config_select(self):
		if self.selectNum==0:
			self.screentype=2
			self.initialiseGame('easy')
			self.startGame()
		elif self.selectNum==1:
			self.screentype=2
			self.initialiseGame('normal')
			self.startGame()
		elif self.selectNum==2:
			self.screentype=2
			self.initialiseGame('hard')
			self.startGame()
		else:
			self.screentype=0
			self.main()

	def config_left(self):
		if self.selectNum==0:
			if self.gameType == 'Classic':
				self.gameType = 'Advanced'
			else:
				self.gameType = 'Classic'
		elif self.selectNum==1:
			if self.volume==0:
				self.volume=10
			else:
				self.volume-=1
		else:
			if self.lvlStep==5:
				self.lvlStep=15
			else:
				self.lvlStep-=1

	def config_right(self):
		if self.selectNum==0:
			if self.gameType == 'Classic':
				self.gameType = 'Advanced'
			else:
				self.gameType = 'Classic'
		elif self.selectNum==1:
			if self.volume==10:
				self.volume=0
			else:
				self.volume+=1
		else:
			if self.lvlStep==15:
				self.lvlStep=5
			else:
				self.lvlStep+=1

	def screen_config(self):
		self.selectNum = 0
		keyBindings = {
			'ESCAPE': lambda:self.quit(),
			'UP' : lambda:self.upCursor(3),
			'DOWN': lambda:self.downCursor(3),
			'RETURN': lambda:self.config_select(),
			'LEFT': lambda:self.config_left(),
			'RIGHT': lambda:self.config_right()
		}
		while self.screentype == 4:
			self.screen.fill((0, 0, 0))
			self.menuMsg("Type : ", (105, 110))
			self.menuMsg(self.gameType, (205, 110))
			self.menuMsg("Volume : ", (105, 170))
			self.menuMsg(str(self.volume), (235, 170))
			self.menuMsg("Levelup rows : ", (105, 230))
			self.menuMsg(str(self.lvlStep), (315, 230))
			self.menuMsg("Back to Menu", (150, 360))
			if self.selectNum==0:
				self.menuMsg(">", (85, 110))
			elif self.selectNum==1:
				self.menuMsg(">", (85, 170))
			elif self.selectNum==2:
				self.menuMsg(">", (85, 230))
			else:
				self.menuMsg(">", (120, 360))
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.quit()
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					for key in keyBindings:
						if event.key == eval("pygame.K_"+key):
							keyBindings[key]()

	def Gamequit(self):
		self.gameover = False
		self.paused = False
		pygame.mixer.music.stop()
		self.screentype=0
		self.main()

	def dif_select(self):
		if self.selectNum==0:
			self.screentype=2
			self.initialiseGame('easy')
			self.startGame()
		elif self.selectNum==1:
			self.screentype=2
			self.initialiseGame('normal')
			self.startGame()
		elif self.selectNum==2:
			self.screentype=2
			self.initialiseGame('hard')
			self.startGame()
		elif self.selectNum==3:
			self.screentype=2
			self.initialiseGame('hell')
			self.startGame()
		else:
			self.screentype=0
			self.main()

	def screen_dif(self):
		self.selectNum = 0
		keyBindings = {
			'ESCAPE': lambda:self.quit(),
			'UP' : lambda:self.upCursor(4),
			'DOWN': lambda:self.downCursor(4),
			'RETURN': lambda:self.dif_select()
		}
		while self.screentype == 1:
			self.screen.fill((0, 0, 0))
			self.menuMsg("Choose the difficulty", (85, 30))
			self.menuMsg("Easy", (195, 110))
			self.menuMsg("Normal", (195, 170))
			self.menuMsg("Hard", (195, 230))
			self.menuMsg("Hell", (195, 290))
			self.menuMsg("Back to Menu", (140, 360))
			if self.selectNum==0:
				self.menuMsg(">", (175, 110))
			elif self.selectNum==1:
				self.menuMsg(">", (175, 170))
			elif self.selectNum==2:
				self.menuMsg(">", (175, 230))
			elif self.selectNum==3:
				self.menuMsg(">", (175, 290))
			else:
				self.menuMsg(">", (110, 360))
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.quit()
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					for key in keyBindings:
						if event.key == eval("pygame.K_"+key):
							keyBindings[key]()

	def main(self):
		self.selectNum=0
		self.screentype=0
		keyBindings = {
			'ESCAPE': lambda:self.quit(),
			'UP' : lambda:self.upCursor(3),
			'DOWN': lambda:self.downCursor(3),
			'RETURN': lambda:self.main_select()
		}
		while self.screentype == 0:
			self.screen.fill((0, 0, 0))
			self.titleMsg("Tetris", (140, 25))
			self.menuMsg("Start Game", (155, 130))
			self.menuMsg("Load Game", (155, 190))
			self.menuMsg("Configuration", (155, 250))
			self.menuMsg("Quit", (155, 310))
			self.menuMsg("Press Enter to select", (95, 360))
			if self.selectNum==0:
				self.menuMsg(">", (135, 130))
			elif self.selectNum==1:
				self.menuMsg(">", (135, 190))
			elif self.selectNum==2:
				self.menuMsg(">", (135, 250))
			else:
				self.menuMsg(">", (135, 310))
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.quit()
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					for key in keyBindings:
						if event.key == eval("pygame.K_"+key):
							keyBindings[key]()

	def startGame(self):
		keyBindings = {
			'LEFT': lambda:self.moveLeft(),
			'RIGHT': lambda:self.moveRight(),
			'DOWN': lambda:self.drop(),
			'r': lambda:self.initialiseGame(),
			'ESCAPE': lambda:self.Gamequit(),
			'p': lambda:self.switchPause(),
			'g': lambda:self.hold(),
			'h': lambda:self.hold2(),
			'RETURN': lambda:self.begin(),
			'SPACE': lambda:self.fallBottom(),
			's': lambda:self.rotate(),
			'1': lambda:self.slowBlock(),
			'2': lambda:self.removeBlock(),
			'3': lambda:self.bombBlock(),
			't': lambda:self.ghost_toggle()
		}
		self.gameover = False
		self.paused = False
		if(self.gameover == True or self.paused == True):
			sys.exit(15)
		cpuLimit = pygame.time.Clock()
		while self.screentype==2:
			self.screen.fill((0, 0, 0))
			if self.gameover:
				pygame.mixer.music.stop()
				restart = 0
				if self.dif=="easy":
					self.centreMsg("""< Easy Mode >\n \n \n Game Over!\n \n \nYour score is: %d \n\nHit Enter to back to Menu""" % self.score)
				elif self.dif=="normal":
					self.centreMsg("""< Normal Mode >\n \n \n Game Over!\n \n \nYour score is: %d \n\nHit Enter to back to Menu""" % self.score)
				elif self.dif=="hard":
					self.centreMsg("""< Hard Mode >\n \n \n Game Over!\n \n \nYour score is: %d \n\nHit Enter to back to Menu""" % self.score)
				elif self.dif=="hell":
					self.centreMsg("""< Hell Mode >\n \n \n Game Over!\n \n \nYour score is: %d \n\nHit Enter to back to Menu""" % self.score)
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
					self.dispMsg("Score: %d\n\nDifficulty: %d" % (self.score, self.level), (self.limit + cellSize - 10, cellSize * 10 + 15))
					self.dispMsg("r : restart\n\np : pause\n\ng/h : hold\n\ns : rotate\n\nt : ghost\n\nSpace : fall", (self.limit - 10 + cellSize, cellSize * 13 + 5))
					if self.gameType == 'Advanced':
						self.dispMsg("Items left", (self.limit + cellSize + 120, cellSize * 10+20))
						self.dispMsg("Slow ", (self.limit + cellSize + 115, cellSize * 11+25))
						if self.slow==0:
							self.dispMsg("N/A", (self.limit + cellSize + 165, cellSize * 11+25))
						else:
							for i in range(self.slow):
								self.dispMsg("O ", (self.limit + cellSize + 150 + 15*(i+1), cellSize * 11+25))
						self.dispMsg("Away ", (self.limit + cellSize + 115, cellSize * 12+25))
						if self.remove==0:
							self.dispMsg("N/A", (self.limit + cellSize + 165, cellSize * 12+25))
						else:
							for i in range(self.remove):
								self.dispMsg("O ", (self.limit + cellSize + 150 + 15*(i+1), cellSize * 12+25))
						self.dispMsg("Bomb ", (self.limit + cellSize + 115, cellSize * 13+25))
						if self.bomb==0:
							self.dispMsg("N/A", (self.limit + cellSize + 165, cellSize * 13+25))
						else:
							for i in range(self.bomb):
								self.dispMsg("O ", (self.limit + cellSize + 150 + 15*(i+1), cellSize * 13+25))
						self.dispMsg("1 : Slow\n\n2 : Skip\n\n3 : Bomb\n\n", (self.limit + cellSize+120, cellSize * 15 + 10))
					self.dispMsg("Interval : %d" % self.currentdelay, (self.limit + cellSize+100, cellSize * 19 + 5))
					self.renderMatrix(self.bground_grid, (0, trial - 12), False)
					self.renderMatrix(self.board, (0, trial /2 - 6))
					emptyness = self.checkRowEmpty(5, self.board)
					if self.ghost:
						self.renderGhostMatrix(self.block, (self.blockX, self.blockY))
					self.renderMatrix(self.block, (self.blockX, self.blockY))
					self.renderMatrix(self.nextBlock, (columns + 1, 2), True, False)
					self.renderMatrix(self.holdBlock, (columns + 1, 6.5), True, False)
					self.renderMatrix(self.holdBlock2, (columns + 7, 6.5), True, False)
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
	App.main()
