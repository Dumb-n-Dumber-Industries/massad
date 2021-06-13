import pygame
import random
pygame.init() #настройка 
win = pygame.display.set_mode((400 , 300)) #размеры окна

pygame.display.set_caption("jew, old, cool jew") #название окна

tri_one_x_1 = 0
tri_one_y_1 = 100
tri_one_x_2 = 400 
tri_one_y_2 = 100 
tri_one_x_3 = 200
tri_one_y_3 = 300 
tri_two_x_1 = 0
tri_two_y_1 = 200
tri_two_x_2 = 400 
tri_two_y_2 = 200
tri_two_x_3 = 200
tri_two_y_3 = 0 
color_tri_one = (0, 0, 255)
color_standart = (250, 250, 250)
run = True
point_one_x = 300
point_one_y = 300 
point_two_x = 200
point_two_y = 200
win.fill(color_standart)
while run == True:
	pygame.time.delay(10) #скорость обновления окна

	for event in pygame.event.get():
		if event.type == pygame.QUIT: #события ввода
			run = False    #Основной выход
	chioce = random.randint(1,3)
	if chioce == 1:
		point_one_x=(tri_one_x_1 + point_one_x)/2 
		point_one_y=(tri_one_y_1 + point_one_y)/2
		point_two_x=(tri_two_x_1 + point_two_x)/2
		point_two_y=(tri_two_y_1 + point_two_y)/2

	if chioce == 2:
		point_one_x=(tri_one_x_2 + point_one_x)/2 
		point_one_y=(tri_one_y_2 + point_one_y)/2
		point_two_x=(tri_two_x_2 + point_two_x)/2
		point_two_y=(tri_two_y_2 + point_two_y)/2

	if chioce == 3:
		point_one_x=(tri_one_x_3 + point_one_x)/2 
		point_one_y=(tri_one_y_3 + point_one_y)/2
		point_two_x=(tri_two_x_3 + point_two_x)/2
		point_two_y=(tri_two_y_3 + point_two_y)/2
	
	pygame.draw.circle(win, color_tri_one, (point_one_x, point_one_y), 2, 2)
	pygame.draw.circle(win, color_tri_one, (point_two_x, point_two_y), 2, 2)
	pygame.display.update()