#coding=utf-8
import pygame
import time
from pygame.locals import *
def main():
	createWindow();

def createUser():	
	return pygame.image.load("./resource/hero1.png");

def monitorKeyboard():
	pass;
def createWindow():	
	#创建窗口
	screen = pygame.display.set_mode((480,852),0,32);
	#创建一个背景
	background = pygame.image.load("./resource/background.png");
	
	#创建玩家
	user = createUser();

	#把背景图片放在窗口中显示
	while True:
		#需要显示的背景图
		screen.blit(background,(0,0));
		
		screen.blit(user,(0,0));
		
		#更新内容
		pygame.display.update();
		#监听键盘	
		
		for event in pygame.event.get():
			if event.type == QUIT:
				print("exit");
				exit();
			elif event.type == KEYDOWN:
				print(event.type);

				if event.key == K_a or event.key == K_LEFT:
					print("left");
				elif event.key == K_d or event.key == K_RIGHT:
					print("right");
				elif event.key == K_SPACE:
					print("space"); 

				#延时缓解高耗费cpu
				time.sleep(0.1);


#保证不是别人引用而是自己调用
if __name__ == "__main__":
	main();
