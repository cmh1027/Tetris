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
		self.button = pygame.mixer.Sound('./music/button.wav')
		pygame.init()
		rowscounter = 0
		pygame.key.set_repeat(250, 25)
		self.border = rand(len(colours))
		self.inside = len(colours)-self.border
		while self.inside == self.border:
			self.inside = rand(len(colours))
		self.rlim = cellSize * columns
		self.default_font = pygame.font.SysFont("comicsansms", 17)
		self.default_font2 = pygame.font.SysFont("comicsansms", 22)
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
		self.name = 'temp'
		self.record = None

	def loadRecord(self):
		if not os.path.isfile("record.bin"):
			recordList = []
			for i in range(2):
				gameType = []
				for j in range(4):
					gameDif = []
					for k in range(11):
						gameLvlstep = []
						for l in range(5):
							indivList = []
							indivList.append(None)
							indivList.append(None)
							indivList.append(None)
							gameLvlstep.append(indivList)
						gameDif.append(gameLvlstep)
					gameType.append(gameDif)
				recordList.append(gameType)
			with open('record.bin','wb') as f:
				pickle.dump(recordList,f)
			self.record = recordList

		else:
			with open('record.bin','rb') as f:
				self.record=pickle.load(f)
	def saveData(self, flag2=False):
		if flag2:
			if not os.path.isfile("data.bin"):
				data = [[], [], [], [], [], []] # recent game for index 0, saved game for 1~5
				data[0].append(self.name)
				data[0].append(self.gameType)
				data[0].append(self.level)
				data[0].append(self.dif)
				data[0].append(self.score)
				data[0].append(self.lvlStep)
				data[0].append(self.nextBlock)
				data[0].append(self.board)
				data[0].append(self.block)
				data[0].append(self.blockX)
				data[0].append(self.blockY)
				data[0].append(self.lines)
				data[0].append(self.holdBlock)
				data[0].append(self.holdBlock2)
				data[0].append(self.slowcount)
				data[0].append(self.slowflag)
				data[0].append(self.ghost)
				data[0].append(self.slow)
				data[0].append(self.remove)
				data[0].append(self.bomb)
				data[0].append(self.start)
				data[0].append(self.currentitem)
				data[0].append(self.currentdelay)
				data[0].append(self.border)
				data[0].append(self.inside)
				with open('data.bin','wb') as f:
					pickle.dump(data,f)
			else:
				with open('data.bin','rb') as f:
					data=pickle.load(f)
				data[0].append(self.name)
				data[0].append(self.gameType)
				data[0].append(self.level)
				data[0].append(self.dif)
				data[0].append(self.lvlStep)
				data[0].append(self.score)
				data[0].append(self.nextBlock)
				data[0].append(self.board)
				data[0].append(self.block)
				data[0].append(self.blockX)
				data[0].append(self.blockY)
				data[0].append(self.lines)
				data[0].append(self.holdBlock)
				data[0].append(self.holdBlock2)
				data[0].append(self.slowcount)
				data[0].append(self.slowflag)
				data[0].append(self.ghost)
				data[0].append(self.slow)
				data[0].append(self.remove)
				data[0].append(self.bomb)
				data[0].append(self.start)
				data[0].append(self.currentitem)
				data[0].append(self.currentdelay)
				data[0].append(self.border)
				data[0].append(self.inside)
				with open('data.bin','wb') as f:
					pickle.dump(data,f)			
		else:
			if not os.path.isfile("data.bin"):
				data = [[], [], [], [], [], []] # recent game for index 0, saved game for 1~5
				data[1].append(self.name)
				data[1].append(self.gameType)
				data[1].append(self.level)
				data[1].append(self.dif)
				data[1].append(self.score)
				data[1].append(self.lvlStep)
				data[1].append(self.nextBlock)
				data[1].append(self.board)
				data[1].append(self.block)
				data[1].append(self.blockX)
				data[1].append(self.blockY)
				data[1].append(self.lines)
				data[1].append(self.holdBlock)
				data[1].append(self.holdBlock2)
				data[1].append(self.slowcount)
				data[1].append(self.slowflag)
				data[1].append(self.ghost)
				data[1].append(self.slow)
				data[1].append(self.remove)
				data[1].append(self.bomb)
				data[1].append(self.start)
				data[1].append(self.currentitem)
				data[1].append(self.currentdelay)
				data[1].append(self.border)
				data[1].append(self.inside)
				with open('data.bin','wb') as f:
					pickle.dump(data,f)
			else:
				flag = False
				with open('data.bin','rb') as f:
					data=pickle.load(f)
				for i in range(1, 6):
					if data[i]==[]:
						data[i].append(self.name)
						data[i].append(self.gameType)
						data[i].append(self.level)
						data[i].append(self.dif)
						data[i].append(self.lvlStep)
						data[i].append(self.score)
						data[i].append(self.nextBlock)
						data[i].append(self.board)
						data[i].append(self.block)
						data[i].append(self.blockX)
						data[i].append(self.blockY)
						data[i].append(self.lines)
						data[i].append(self.holdBlock)
						data[i].append(self.holdBlock2)
						data[i].append(self.slowcount)
						data[i].append(self.slowflag)
						data[i].append(self.ghost)
						data[i].append(self.slow)
						data[i].append(self.remove)
						data[i].append(self.bomb)
						data[i].append(self.start)
						data[i].append(self.currentitem)
						data[i].append(self.currentdelay)
						data[i].append(self.border)
						data[i].append(self.inside)
						flag = True
						break
				if not flag:
					data[1] = []
					data[1].append(self.name)
					data[1].append(self.gameType)
					data[1].append(self.level)
					data[1].append(self.dif)
					data[1].append(self.score)
					data[1].append(self.lvlStep)
					data[1].append(self.nextBlock)
					data[1].append(self.board)
					data[1].append(self.block)
					data[1].append(self.blockX)
					data[1].append(self.blockY)
					data[1].append(self.lines)
					data[1].append(self.holdBlock)
					data[1].append(self.holdBlock2)
					data[1].append(self.slowcount)
					data[1].append(self.slowflag)
					data[1].append(self.ghost)
					data[1].append(self.slow)
					data[1].append(self.remove)
					data[1].append(self.bomb)
					data[1].append(self.start)
					data[1].append(self.currentitem)
					data[1].append(self.currentdelay)
					data[1].append(self.border)
					data[1].append(self.inside)
				with open('data.bin','wb') as f:
					pickle.dump(data,f)

	def load_data(self, data, index):
		self.name = data[index][0]
		self.gameType = data[index][1]
		self.level = data[index][2]
		self.dif = data[index][3]
		self.lvlStep = data[index][4]
		self.score = data[index][5]
		self.nextBlock = data[index][6]
		self.board = data[index][7]
		self.block = data[index][8]
		self.blockX = data[index][9]
		self.blockY = data[index][10]
		self.lines = data[index][11]
		self.holdBlock = data[index][12]
		self.holdBlock2 = data[index][13]
		self.slowcount = data[index][14]
		self.slowflag = data[index][15]
		self.ghost = data[index][16]
		self.slow = data[index][17]
		self.remove = data[index][18]
		self.bomb = data[index][19]
		self.start = data[index][20]
		self.currentitem = data[index][21]
		self.currentdelay = data[index][22]
		self.border = data[index][23]
		self.inside = data[index][24]

	def delete_data(self, index):
		with open('data.bin','rb') as f:
			data=pickle.load(f)
		data[index] = []
		with open('data.bin','wb') as f:
			pickle.dump(data,f)

	def updateScore(self, increment):
		self.score += increment

	def initialiseGame(self, dif, flag=False):
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
		if not flag:
			self.dif=dif
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
			self.currentdelay = int(1000*(0.82**(self.level-1)))
			self.border = rand(len(colours))
			self.inside = len(colours)-self.border
			while self.inside == self.border:
				self.inside = rand(len(colours))
		pygame.time.set_timer(pygame.USEREVENT + 1, self.currentdelay)
		pygame.mixer.music.play(-1)

	def centreMsg(self, msg):
		for i, line in enumerate(msg.splitlines()):
			self.default_font.render(line, False, (254, 254, 254), (1, 1, 1))
			msgim_center_x = self.default_font.render(line, False, (254, 254, 254), (1, 1, 1)).get_size()[0]
			msgim_center_y = self.default_font.render(line, False, (254, 254, 254), (1, 1, 1)).get_size()[1]
			msgim_center_x = (int) (msgim_center_x / 2)
			msgim_center_y = (int) (msgim_center_x / 2)
			self.screen.blit(self.default_font.render(line, False, (254, 254, 254), (1, 1, 1)), ((int)(self.width / 2) - msgim_center_x, (int)(self.height / (trial - 10)) - msgim_center_y + i * (trial) + 40))

	def dispMsg(self, msg, topleft):
		x = topleft[0]
		y = topleft[1]
		trial = 12
		for line in msg.splitlines():
			arg = False
			self.screen.blit(self.default_font.render(line, arg, (white, white, white), (1, 1, 1)), (x, y))
			y += 12

	def dispMsg2(self, msg, topleft):
		x = topleft[0]
		y = topleft[1]
		trial = 12
		for line in msg.splitlines():
			arg = False
			self.screen.blit(self.default_font2.render(line, arg, (white, white, white), (1, 1, 1)), (x, y))
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

		self.updateScore(linescores[n] * self.level)
		if int(self.score/15000)>=self.currentitem and self.gameType=='Advanced':
			self.currentitem+=1
			if self.slow<4:
				self.slow+=1
			if self.remove<4:
				self.remove+=1
			if self.bomb<4:
				self.bomb+=1
		if(self.lines >= (self.level-self.start+1) * self.lvlStep):
			self.border = rand(len(colours))
			self.inside = len(colours)-self.border
			while self.inside == self.border:
				self.inside = rand(len(colours))
			pygame.mixer.Channel(3).play(self.levelup)
			self.level += 1
			if self.slowcount>0:
				newdelay = int(1000*(0.82**(self.level-1))*2)
			else:
				newdelay = int(1000*(0.82**(self.level-1)))
			self.currentdelay = newdelay
			pygame.time.set_timer(pygame.USEREVENT + 1, newdelay)
		else:
			if n>0:
				pygame.mixer.Channel(2).play(self.blockfull)

	def quit(self):
		pygame.display.update()
		with open('record.bin','wb') as f:
			pickle.dump(self.record,f)
		sys.exit()

	def begin(self):
		if self.gameover:
			self.gameover = False
			self.paused = False
			self.screentype = 0
			with open('record.bin','wb') as f:
				pickle.dump(self.record,f)
			self.main()

	def switchPause(self):
		if(self.paused == True):
			pygame.mixer.music.unpause()
			self.paused = False
		else:
			pygame.mixer.music.pause()
			self.paused = True
	def upCursor(self, bottom):
		pygame.mixer.Channel(2).play(self.button)
		if self.selectNum>0:
			self.selectNum-=1
		else:
			self.selectNum=bottom
	def downCursor(self, bottom):
		pygame.mixer.Channel(2).play(self.button)
		if self.selectNum<bottom:
			self.selectNum+=1
		else:
			self.selectNum=0


	def screen_config(self):
		def config_quit():
			self.screentype=0
			self.main()
		def config_select():
			if self.selectNum==3:
				self.screentype=0
				self.main()
		def config_left():
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
				self.blockfull.set_volume(self.volume/10)
				pygame.mixer.Channel(2).play(self.blockfull)
			else:
				if self.lvlStep==5:
					self.lvlStep=15
				else:
					self.lvlStep-=1

		def config_right():
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
				self.blockfull.set_volume(self.volume/10)
				pygame.mixer.Channel(2).play(self.blockfull)
			else:
				if self.lvlStep==15:
					self.lvlStep=5
				else:
					self.lvlStep+=1
		self.selectNum = 0
		keyBindings = {
			'ESCAPE': lambda:config_quit(),
			'UP' : lambda:self.upCursor(3),
			'DOWN': lambda:self.downCursor(3),
			'RETURN': lambda:config_select(),
			'LEFT': lambda:config_left(),
			'RIGHT': lambda:config_right()
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



	def screen_name(self, dif):
		def name_quit():
			self.screentype=1
			self.screen_dif()
		def name_select(name, dif):
			if len(name)>0:
				self.name=name
				self.screentype=2
				self.initialiseGame(dif)
				self.startGame()
		keyBindings = {
			'ESCAPE': lambda:name_quit(),
			'RETURN': lambda:name_select(name, dif)
		}
		name = ""
		while self.screentype == 8:
			self.screen.fill((0, 0, 0))
			self.menuMsg("Type your name(Maximum 8)", (40, 110))
			self.menuMsg(name, (175, 190))
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.quit()
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					for key in keyBindings:
						if event.key == eval("pygame.K_"+key):
							keyBindings[key]()
							break
					if event.key == pygame.K_BACKSPACE:
						if name!="":
							name=name[:-1]
					else:
						if event.key != pygame.K_LSHIFT and event.key != pygame.K_RSHIFT:
							if len(name)<8:
								if chr(event.key).isalpha():
									if pygame.key.get_mods() & pygame.KMOD_SHIFT:
										name=name+chr(event.key).upper()
									else:
										name=name+chr(event.key)

	def screen_dif(self):
		def dif_quit():
			self.screentype=0
			self.main()
		def dif_select():
			if self.selectNum==0:
				self.screentype=8
				self.screen_name('easy')
			elif self.selectNum==1:
				self.screentype=8
				self.screen_name('normal')
			elif self.selectNum==2:
				self.screentype=8
				self.screen_name('hard')
			elif self.selectNum==3:
				self.screentype=8
				self.screen_name('hell')
			else:
				self.screentype=0
				self.main()
		self.selectNum = 0
		keyBindings = {
			'ESCAPE': lambda:dif_quit(),
			'UP' : lambda:self.upCursor(4),
			'DOWN': lambda:self.downCursor(4),
			'RETURN': lambda:dif_select()
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

	def screen_select_ranking(self):
		self.selectNum = 0
		gameType = "Advanced"
		diff = "Easy"
		lvl = 9
		keyBindings = {
			'ESCAPE': lambda:ranking_quit(),
			'UP' : lambda:self.upCursor(3),
			'DOWN': lambda:self.downCursor(3),
			'RETURN': lambda:screen_ranking(),
			'LEFT': lambda:ranking_left(),
			'RIGHT': lambda:ranking_right()
		}
		def ranking_quit():
			if self.screentype == 5:
				self.screentype=0
				self.main()
			else:
				self.screentype=5
		def ranking_left():
			nonlocal gameType
			nonlocal diff
			nonlocal lvl
			if self.selectNum==0:
				if gameType=="Classic":
					gameType="Advanced"
				else:
					gameType="Classic"
			elif self.selectNum==1:
				if diff=="Easy":
					diff="Hell"
				elif diff=="Normal":
					diff="Easy"
				elif diff=="Hard":
					diff="Normal"
				else:
					diff="Easy"
			elif self.selectNum==2:
				if 5<lvl:
					lvl-=1
				else:
					lvl=15
		def ranking_right():
			nonlocal gameType
			nonlocal diff
			nonlocal lvl
			if self.selectNum==0:
				if gameType=="Classic":
					gameType="Advanced"
				else:
					gameType="Classic"
			elif self.selectNum==1:
				if diff=="Easy":
					diff="Normal"
				elif diff=="Normal":
					diff="Hard"
				elif diff=="Hard":
					diff="Hell"
				else:
					diff="Easy"
			elif self.selectNum==2:
				if lvl<15:
					lvl+=1
				else:
					lvl=5
		def screen_ranking():
			if self.selectNum!=3:
				self.screentype = 6
			else:
				self.screentype = 0
				self.main()
		self.loadRecord()
		while self.screentype == 5 or self.screentype == 6:
			if self.screentype == 5:
				self.screen.fill((0, 0, 0))
				self.menuMsg("Type : ", (105, 110))
				self.menuMsg(gameType, (205, 110))
				self.menuMsg("Difficulty : ", (105, 170))
				self.menuMsg(diff, (270, 170))
				self.menuMsg("Levelup rows : ", (105, 230))
				self.menuMsg(str(lvl), (315, 230))
				self.menuMsg("Back to Menu", (150, 320))
				self.menuMsg("Press Enter to select", (90, 30))
				if self.selectNum==0:
					self.menuMsg(">", (85, 110))
				elif self.selectNum==1:
					self.menuMsg(">", (85, 170))
				elif self.selectNum==2:
					self.menuMsg(">", (85, 230))
				else:
					self.menuMsg(">", (120, 320))
			else:
				self.screen.fill((0, 0, 0))
				y = 50
				add = 50
				plus = 0
				if gameType=='Classic':
					p = 0
				else:
					p = 1
				if diff=="Easy":
					q = 0
				elif diff=="Normal":
					q = 1
				elif diff=="Hard":
					q = 2
				else:
					q = 3
				self.dispMsg("Name          Score          Level", (118, y-30))
				for i in self.record[p][q][lvl-5]:
					if i[0] != None and i[1] != None:
						if plus==0:
							self.dispMsg(" 1st     " + str(i[0]), (60, y+add*plus))
							self.dispMsg(str(i[1]), (215, y+add*plus))
							self.dispMsg(str(i[2]), (312, y+add*plus))
						elif plus==1:
							self.dispMsg("2nd     " + str(i[0]), (60, y+add*plus))
							self.dispMsg(str(i[1]), (215, y+add*plus))
							self.dispMsg(str(i[2]), (312, y+add*plus))					
						elif plus==2:
							self.dispMsg("3rd     " + str(i[0]), (60, y+add*plus))
							self.dispMsg(str(i[1]), (215, y+add*plus))
							self.dispMsg(str(i[2]), (312, y+add*plus))					
						elif plus==3:
							self.dispMsg("4th     " + str(i[0]), (60, y+add*plus))
							self.dispMsg(str(i[1]), (215, y+add*plus))
							self.dispMsg(str(i[2]), (312, y+add*plus))
						else:
							self.dispMsg("5th     " + str(i[0]), (60, y+add*plus))
							self.dispMsg(str(i[1]), (215, y+add*plus))
							self.dispMsg(str(i[2]), (312, y+add*plus))
					plus += 1
				self.menuMsg("Press esc to back to select", (40, 360))
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.quit()
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					for key in keyBindings:
						if event.key == eval("pygame.K_"+key):
							keyBindings[key]()

	def screen_select_load(self):
		self.selectNum = 0
		def load_quit():
			self.screentype = 0
			self.main()
		def load_startGame(data):
			if self.selectNum != 5:
				if data[self.selectNum+1]!=[]:
					self.load_data(data, self.selectNum+1)
					self.delete_data(self.selectNum+1)
					self.screentype = 2
					self.initialiseGame(self.dif, True)
					self.startGame()
			else:
				self.screentype = 0
				self.main()
		keyBindings = {
			'ESCAPE': lambda:load_quit(),
			'UP' : lambda:self.upCursor(5),
			'DOWN': lambda:self.downCursor(5),
			'RETURN': lambda:load_startGame(data),
		}
		if not os.path.isfile("data.bin"):
			data = [[], [], [], [], [], []]
		else:
			with open('data.bin','rb') as f:
				data=pickle.load(f)
		while self.screentype == 7:
			self.screen.fill((0, 0, 0))
			self.menuMsg("Saved games", (145, 30))
			for i in range(1, 6):
				if data[i]!=[]:
					self.dispMsg2(str(data[i][0])+" / "+str(data[i][1])+" / "+str(data[i][2])+" / "+str(data[i][3]), (90, 110+(i-1)*40))
				else:
					self.dispMsg2("Empty", (200, 110+(i-1)*40))
			self.menuMsg("Back to Menu", (145, 350))
			if self.selectNum!=5:
				self.dispMsg2(">", (70, 110 + self.selectNum*40))
			else:
				self.dispMsg2(">", (125, 110 + self.selectNum*40+45))
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.quit()
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					for key in keyBindings:
						if event.key == eval("pygame.K_"+key):
							keyBindings[key]()

	def screen_check_recent(self):
		self.selectNum = 0
		def recent_quit():
			self.screentype = 0
			self.main()
		def recent_select(data):
			if self.selectNum==0:
				if data[0]!=[]:
					self.load_data(data, 0)
					self.delete_data(0)
					self.screentype = 2
					self.initialiseGame(self.dif, True)
					self.startGame()
			elif self.selectNum == 1:
				self.delete_data(0)
				self.screentype=1
				self.screen_dif()
			else:
				self.screentype = 0
				self.main()
		keyBindings = {
			'ESCAPE': lambda:recent_quit(),
			'UP' : lambda:self.upCursor(2),
			'DOWN': lambda:self.downCursor(2),
			'RETURN': lambda:recent_select(data),
		}
		with open('data.bin','rb') as f:
			data=pickle.load(f)
		while self.screentype == 10:
			self.screen.fill((0, 0, 0))
			self.menuMsg("Wanna load recent game?", (60, 30))
			self.menuMsg("Yes", (145, 110))
			self.menuMsg("No", (145, 150))
			self.menuMsg("Back to Menu", (145, 190))
			self.menuMsg(">", (125, 110+self.selectNum*40))
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
		def main_select():
			if self.selectNum==0: # Start
				if os.path.isfile("data.bin"):
					with open('data.bin','rb') as f:
						data=pickle.load(f)
					if data[0]!=[]:
						self.screentype=10
						self.screen_check_recent()
					else:
						self.screentype=1
						self.screen_dif()						
				else:
					self.screentype=1
					self.screen_dif()
			elif self.selectNum==1:
				self.screentype=7
				self.screen_select_load()
			elif self.selectNum==2: # Ranking
				self.screentype=5
				self.screen_select_ranking()
			elif self.selectNum==3: # Configuration
				self.screentype=4
				self.screen_config()
			elif self.selectNum==4: # Quit
				pygame.display.update()
				sys.exit()
		self.selectNum=0
		self.screentype=0
		keyBindings = {
			'ESCAPE': lambda:self.quit(),
			'UP' : lambda:self.upCursor(4),
			'DOWN': lambda:self.downCursor(4),
			'RETURN': lambda:main_select()
		}
		while self.screentype == 0:
			self.screen.fill((0, 0, 0))
			self.titleMsg("Tetris", (140, 5))
			self.menuMsg("Start Game", (155, 100))
			self.menuMsg("Load Game", (155, 150))
			self.menuMsg("Ranking", (155, 200))
			self.menuMsg("Configuration", (155, 250))
			self.menuMsg("Quit", (155, 300))
			self.menuMsg("Press Enter to select", (95, 360))
			if self.selectNum==0:
				self.menuMsg(">", (135, 100))
			elif self.selectNum==1:
				self.menuMsg(">", (135, 150))
			elif self.selectNum==2:
				self.menuMsg(">", (135, 200))
			elif self.selectNum==3:
				self.menuMsg(">", (135, 250))
			else:
				self.menuMsg(">", (135, 300))
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

	def save(self):
		if not self.gameover and not self.paused:
			self.screentype = 9
			self.selectNum = 0
			pygame.mixer.music.pause()
			def restart():
				self.screentype = 2
				pygame.mixer.music.unpause()
				self.startGame()
			def save_select():
				if self.selectNum==0:
					self.saveData()
					self.Gamequit()
				elif self.selectNum==1:
					self.Gamequit()
				else:
					restart()
			keyBindings = {
				'ESCAPE': lambda:restart(),
				'UP' : lambda:self.upCursor(2),
				'DOWN': lambda:self.downCursor(2),
				'RETURN': lambda:save_select()
			}
			while self.screentype == 9:
				self.screen.fill((0, 0, 0))
				self.menuMsg("Save the game?", (125, 100))
				self.menuMsg("Yes", (155, 150))
				self.menuMsg("No", (155, 200))
				self.menuMsg("Back to game", (155, 250))
				if self.selectNum==0:
					self.menuMsg(">", (135, 150))
				elif self.selectNum==1:
					self.menuMsg(">", (135, 200))
				else:
					self.menuMsg(">", (135, 250))
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
			'r': lambda:self.initialiseGame(self.dif),
			'ESCAPE': lambda:self.save(),
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
		self.loadRecord()
		self.gameover = False
		self.paused = False
		save=False
		highscore = -1
		if(self.gameover == True or self.paused == True):
			sys.exit(15)
		cpuLimit = pygame.time.Clock()
		while self.screentype == 2:
			self.screen.fill((0, 0, 0))
			if self.gameover:
				pygame.mixer.music.stop()
				if self.gameType=='Classic':
					p = 0
				else:
					p = 1
				if self.dif=="easy":
					q = 0
				elif self.dif=="normal":
					q = 1
				elif self.dif=="hard":
					q = 2
				elif self.dif=="hell":
					q = 3
				y = 50
				add = 30
				plus = 0
				index = 0
				self.dispMsg("Name          Score          Level", (118, y-30))
				try:
					for i in self.record[p][q][self.lvlStep-5]:
						if i[0] != None and i[1] != None:
							if plus == 0:
								if self.score>i[1] and not save:
									highscore = 1
									self.record[p][q][self.lvlStep-5][4][2] = self.record[p][q][self.lvlStep-5][3][2]
									self.record[p][q][self.lvlStep-5][3][2] = self.record[p][q][self.lvlStep-5][2][2]
									self.record[p][q][self.lvlStep-5][2][2] = self.record[p][q][self.lvlStep-5][1][2]
									self.record[p][q][self.lvlStep-5][1][2] = self.record[p][q][self.lvlStep-5][0][2]
									self.record[p][q][self.lvlStep-5][4][1] = self.record[p][q][self.lvlStep-5][3][1]
									self.record[p][q][self.lvlStep-5][3][1] = self.record[p][q][self.lvlStep-5][2][1]
									self.record[p][q][self.lvlStep-5][2][1] = self.record[p][q][self.lvlStep-5][1][1]
									self.record[p][q][self.lvlStep-5][1][1] = self.record[p][q][self.lvlStep-5][0][1]
									self.record[p][q][self.lvlStep-5][4][0] = self.record[p][q][self.lvlStep-5][3][0]
									self.record[p][q][self.lvlStep-5][3][0] = self.record[p][q][self.lvlStep-5][2][0]
									self.record[p][q][self.lvlStep-5][2][0] = self.record[p][q][self.lvlStep-5][1][0]
									self.record[p][q][self.lvlStep-5][1][0] = self.record[p][q][self.lvlStep-5][0][0]
									self.record[p][q][self.lvlStep-5][0][2] = self.level
									self.record[p][q][self.lvlStep-5][0][1] = self.score
									self.record[p][q][self.lvlStep-5][0][0] = self.name
									save = True
								self.dispMsg(" 1st     " + str(i[0]), (60, y+add*plus))
								self.dispMsg(str(i[1]), (215, y+add*plus))
								self.dispMsg(str(i[2]), (312, y+add*plus))
							elif plus == 1:
								if highscore != 1 and self.score>i[1] and not save:
									self.record[p][q][self.lvlStep-5][4][2] = self.record[p][q][self.lvlStep-5][3][2]
									self.record[p][q][self.lvlStep-5][3][2] = self.record[p][q][self.lvlStep-5][2][2]
									self.record[p][q][self.lvlStep-5][2][2] = self.record[p][q][self.lvlStep-5][1][2]
									self.record[p][q][self.lvlStep-5][4][1] = self.record[p][q][self.lvlStep-5][3][1]
									self.record[p][q][self.lvlStep-5][3][1] = self.record[p][q][self.lvlStep-5][2][1]
									self.record[p][q][self.lvlStep-5][2][1] = self.record[p][q][self.lvlStep-5][1][1]
									self.record[p][q][self.lvlStep-5][4][0] = self.record[p][q][self.lvlStep-5][3][0]
									self.record[p][q][self.lvlStep-5][3][0] = self.record[p][q][self.lvlStep-5][2][0]
									self.record[p][q][self.lvlStep-5][2][0] = self.record[p][q][self.lvlStep-5][1][0]
									highscore = 2
									self.record[p][q][self.lvlStep-5][1][2] = self.level
									self.record[p][q][self.lvlStep-5][1][1] = self.score
									self.record[p][q][self.lvlStep-5][1][0] = self.name
									save = True
								self.dispMsg("2nd     " + str(i[0]), (60, y+add*plus))
								self.dispMsg(str(i[1]), (215, y+add*plus))
								self.dispMsg(str(i[2]), (312, y+add*plus))
							elif plus == 2:
								if highscore != 2 and self.score>i[1] and not save:
									self.record[p][q][self.lvlStep-5][4][2] = self.record[p][q][self.lvlStep-5][3][2]
									self.record[p][q][self.lvlStep-5][3][2] = self.record[p][q][self.lvlStep-5][2][2]
									self.record[p][q][self.lvlStep-5][4][1] = self.record[p][q][self.lvlStep-5][3][1]
									self.record[p][q][self.lvlStep-5][3][1] = self.record[p][q][self.lvlStep-5][2][1]
									self.record[p][q][self.lvlStep-5][4][0] = self.record[p][q][self.lvlStep-5][3][0]
									self.record[p][q][self.lvlStep-5][3][0] = self.record[p][q][self.lvlStep-5][2][0]
									highscore = 3
									self.record[p][q][self.lvlStep-5][2][2] = self.level
									self.record[p][q][self.lvlStep-5][2][1] = self.score
									self.record[p][q][self.lvlStep-5][2][0] = self.name
									save = True
								self.dispMsg("3rd     " + str(i[0]), (60, y+add*plus))
								self.dispMsg(str(i[1]), (215, y+add*plus))
								self.dispMsg(str(i[2]), (312, y+add*plus))
							elif plus == 3:
								if highscore != 3 and self.score>i[1] and not save :
									self.record[p][q][self.lvlStep-5][4][2] = self.record[p][q][self.lvlStep-5][3][2]
									self.record[p][q][self.lvlStep-5][4][1] = self.record[p][q][self.lvlStep-5][3][1]
									self.record[p][q][self.lvlStep-5][4][0] = self.record[p][q][self.lvlStep-5][3][0]
									highscore = 4
									self.record[p][q][self.lvlStep-5][3][2] = self.level
									self.record[p][q][self.lvlStep-5][3][1] = self.score
									self.record[p][q][self.lvlStep-5][3][0] = self.name
									save = True
								self.dispMsg("4th     " + str(i[0]), (60, y+add*plus))
								self.dispMsg(str(i[1]), (215, y+add*plus))
								self.dispMsg(str(i[2]), (312, y+add*plus))
							else:
								if highscore != 4 and self.score>i[1] and not save :
									highscore = 5
									self.record[p][q][self.lvlStep-5][4][2] = self.level
									self.record[p][q][self.lvlStep-5][4][1] = self.score
									self.record[p][q][self.lvlStep-5][4][0] = self.name
									save = True
								self.dispMsg("5th     " + str(i[0]), (60, y+add*plus))
								self.dispMsg(str(i[1]), (215, y+add*plus))
								self.dispMsg(str(i[2]), (312, y+add*plus))
						else:
							if plus == 0:
								if not save:
									self.record[p][q][self.lvlStep-5][0][1] = self.score
									highscore = 1
									self.record[p][q][self.lvlStep-5][0][0] = self.name
									self.record[p][q][self.lvlStep-5][0][2] = self.level
									save = True
							elif plus == 1:
								if not save:
									self.record[p][q][self.lvlStep-5][1][1] = self.score
									highscore = 2
									self.record[p][q][self.lvlStep-5][1][0] = self.name
									self.record[p][q][self.lvlStep-5][1][2] = self.level
									save = True
							elif plus == 2:
								if not save:
									self.record[p][q][self.lvlStep-5][2][1] = self.score
									highscore = 3
									self.record[p][q][self.lvlStep-5][2][0] = self.name
									self.record[p][q][self.lvlStep-5][2][2] = self.level
									save = True
							elif plus == 3:
								if not save:
									self.record[p][q][self.lvlStep-5][3][1] = self.score
									highscore = 4
									self.record[p][q][self.lvlStep-5][3][0] = self.name
									self.record[p][q][self.lvlStep-5][3][2] = self.level
									save = True
							else:
								if not save:
									self.record[p][q][self.lvlStep-5][4][1] = self.score
									highscore = 5
									self.record[p][q][self.lvlStep-5][4][0] = self.name
									self.record[p][q][self.lvlStep-5][4][2] = self.level
									save = True
						plus += 1
				except:
					self.loadRecord()
				if highscore == 1:
					self.dispMsg("     You've got 1st Score!\n\nPress enter to back to Menu", (125, 360))
				elif highscore == 2:
					self.dispMsg("     You've got 2nd Score!\n\nPress enter to back to Menu", (125, 360))
				elif highscore == 3:
					self.dispMsg("     You've got 3rd Score!\n\nPress enter to back to Menu", (125, 360))
				elif highscore == 4:
					self.dispMsg("     You've got 4th Score!\n\nPress enter to back to Menu", (125, 360))
				elif highscore == 5:
					self.dispMsg("     You've got 5th Score!\n\nPress enter to back to Menu", (125, 360))
				else:
					self.dispMsg("Enter to back to Menu", (155, 360))
				self.centreMsg("Game type : "+self.gameType+"\n\n"+"Difficulty : "+self.dif[0].upper()+self.dif[1:]+"\n\n"+"Levelup rows : "+str(self.lvlStep)+"\n\n"+"Score : "+str(self.score)+"\n\n"+"Level : "+str(self.level))
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
					self.dispMsg("Rows left : ", (self.limit + cellSize + 105, cellSize * 10+20))
					self.dispMsg(str(self.lvlStep-(self.lines - (self.level - self.start)*self.lvlStep)), (self.limit + cellSize + 200, cellSize * 10+20))
					if self.gameType == 'Advanced':
						self.dispMsg("Slow ", (self.limit + cellSize + 105, cellSize * 11+25))
						if self.slow==0:
							self.dispMsg("N/A", (self.limit + cellSize + 165, cellSize * 11+25))
						else:
							for i in range(self.slow):
								self.dispMsg("O ", (self.limit + cellSize + 150 + 15*(i+1), cellSize * 11+25))
						self.dispMsg("Away ", (self.limit + cellSize + 105, cellSize * 12+25))
						if self.remove==0:
							self.dispMsg("N/A", (self.limit + cellSize + 165, cellSize * 12+25))
						else:
							for i in range(self.remove):
								self.dispMsg("O ", (self.limit + cellSize + 150 + 15*(i+1), cellSize * 12+25))
						self.dispMsg("Bomb ", (self.limit + cellSize + 105, cellSize * 13+25))
						if self.bomb==0:
							self.dispMsg("N/A", (self.limit + cellSize + 165, cellSize * 13+25))
						else:
							for i in range(self.bomb):
								self.dispMsg("O ", (self.limit + cellSize + 150 + 15*(i+1), cellSize * 13+25))
						self.dispMsg("1 : Slow\n\n2 : Skip\n\n3 : Bomb\n\n", (self.limit + cellSize+115, cellSize * 15 + 10))
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
					if not self.gameover:
						self.saveData(True)
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
