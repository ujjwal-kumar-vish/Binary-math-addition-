import pygame
import random
import sys
import webbrowser

pygame.init()

window=0
final_score=0
c=0
score=0
lev=0
hint=0
rand_var=0


running = True

base_font = pygame.font.Font(None, 32)
user_text = ''

# create rectangle
input_rect = pygame.Rect(200, 200, 140, 32)

# color_active stores color(lightskyblue3) which
# gets active when input box is clicked by user
color_active = pygame.Color('lightskyblue3')

# color_passive store color(chartreuse4) which is
# color of input box.
color_passive = pygame.Color('chartreuse4')
color = color_passive

active = False

res = (720,720)
screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()


# defining a font
smallfont = pygame.font.SysFont('Corbel',35)
normalfont = pygame.font.SysFont('Arial Black',25)
normal_font = pygame.font.SysFont('Arial Black',20)
bigfont = pygame.font.SysFont('Algerian',45)
color = (25,25,0)
  
# light shade of the button
color_light = (170,170,170)
color_light1 = (200,100,100)
  
# dark shade of the button
color_dark = (100,100,100)
color_dark1 = (150,0,150)
  
# stores the width of the
# screen into a variable
width = screen.get_width()
  
# stores the height of the
# screen into a variable
height = screen.get_height()


#scoreprint=str(score)

list1=['000000','000001','000010','000011','000100','000101','000110','000111','001000','001001','001010','001011','001100','001101','001110','001111',
'010000','010001','010010','010011','010100','010101','010110','010111','011000','011001','011010','011011','011100','011101','011110','011111',
'100000','100001','100010','100011','100100','100101','100110','100111','101000','101001','101010','101011','101100','101101','101110','101111',
'110000','110001','110010','110011','110100','110101','110110','110111','111000','111001','111010','111011','111100','111101','111110','111111']


inp1='0001'
inp2='0010'
inp4='0100'
inp8='1000'
list2=[inp1,inp2,inp4,inp8]

list3=['Start Game','View Score','Quit','Main Menu','How to play','About us']

list4=['Easy','Medium','Hard','Extream']

#seting icon and window name 
pygame.display.set_caption("Binary math's Game")
icon=pygame.image.load("binary.png")

b1=normalfont.render(list3[0] , True , color)
b1x=250
b1y=0
b2=normalfont.render(list3[1] , True , color)
b2x=250
b2y=150
b3=normalfont.render(list3[2] , True , color)
b3x=250
b3y=600
b4=normalfont.render(list3[3] , True , color)
b4x=250
b4y=300
b5=normalfont.render(list3[4] , True , color)
b5x=250
b5y=450
b6=normalfont.render(list3[5] , True , color)
b6x=250
b6y=300




a1=normalfont.render(list2[0] , True , color)
a1x=0
a1y=100-20
#a2=pygame.image.load("00010.png")
a2=normalfont.render(list2[1] , True , color)
a2x=0
a2y=200-20
#a4=pygame.image.load("00100.png")
a4=normalfont.render(list2[2] , True , color)
a4x=0
a4y=300-20
#a8=pygame.image.load("01000.png")
a8=normalfont.render(list2[3] , True , color)
a8x=0
a8y=400-20

#icon for the window
pygame.display.set_icon(icon)



  
# rendering a text written in
# this font

scoretxt = normalfont.render('score :' , True , color)
level = normalfont.render('Level :' , True , color)

hint_f = normalfont.render('Hint' , True , color)
hint_fx=280
hint_fy=620

dplay = smallfont.render(list1[c] , True , color)
dplayx = 300
dplayy = 50

submit = normalfont.render('Submit' , True , color)
submitx = 300
submity = 250

x=random.randint(1,3)


while running:

    
    screen.fill((255, 255, 255))

    mouse = pygame.mouse.get_pos()

    #buttons created
    
    if window==1:
        if a1x <= mouse[0] <= a1x+200 and a1y <= mouse[1] <= a1y+80:
            pygame.draw.rect(screen,color_light,[a1x,a1y,200,80])
		
        else:
            pygame.draw.rect(screen,color_dark,[a1x,a1y,200,80])

        if a2x <= mouse[0] <= a2x+200 and a2y <= mouse[1] <= a2y+80:
            pygame.draw.rect(screen,color_light,[a2x,a2y,200,80])
		
        else:
            pygame.draw.rect(screen,color_dark,[a2x,a2y,200,80])

        if a4x <= mouse[0] <= a4x+200 and a4y <= mouse[1] <= a4y+80:
            pygame.draw.rect(screen,color_light,[a4x,a4y,200,80])
		
        else:
            pygame.draw.rect(screen,color_dark,[a4x,a4y,200,80])

        if a8x <= mouse[0] <= a8x+200 and a8y <= mouse[1] <= a8y+80:
            pygame.draw.rect(screen,color_light,[a8x,a8y,200,80])
		
        else:
            pygame.draw.rect(screen,color_dark,[a8x,a8y,200,80])

        if dplayx <= mouse[0] <= dplayx+200 and dplayy <= mouse[1] <= dplayy+80:
            pygame.draw.rect(screen,color_light1,[dplayx,dplayy,200,80])
		
        else:
            pygame.draw.rect(screen,color_dark1,[dplayx,dplayy,200,80])

        if submitx <= mouse[0] <= submitx+200 and submity <= mouse[1] <= submity+80:
            pygame.draw.rect(screen,(100,105,200),[submitx,submity,200,80])
		
        else:
            pygame.draw.rect(screen,(250,75,100),[submitx,submity,200,80])
        
        if b3x+350 <= mouse[0] <= b3x+250+300 and b3y-100 <= mouse[1] <= b3y+80-100:
            pygame.draw.rect(screen,(255,50,50),[b3x+350,b3y-100,200,80])
		
        else:
            pygame.draw.rect(screen,(255,100,100),[b3x+350,b3y-100,200,80])

        if hint_fx <= mouse[0] <= hint_fx+60 and hint_fy <= mouse[1] <= hint_fy+40:
            pygame.draw.rect(screen,(255,205,205),[hint_fx,hint_fy,60,40])
		
        else:
            pygame.draw.rect(screen,(200,250,200),[hint_fx,hint_fy,60,40])
            
    
        pygame.draw.rect(screen,(100,150,75),[submitx+250,submity-110,100,100])
    
        
        screen.blit(a1,(a1x+50,a1y+20))
        screen.blit(a2,(a2x+50,a2y+20))
        screen.blit(a4,(a4x+50,a4y+20))
        screen.blit(a8,(a8x+50,a8y+20))

        screen.blit(scoretxt ,(width-200,height-100))
        screen.blit(submit,(submitx+50,submity+20))

        screen.blit(normalfont.render('Back' , True , color),(b1x+380,b1y+420+100))
        screen.blit(normalfont.render('Objective' , True , (20,25,220)),(b1x+280,b1y+100))
        screen.blit(normalfont.render('Current Binary' , True , (20,25,220)),(b1x+50,b1y-90+100))
        screen.blit(normal_font.render('Add the following :-' , True , (20,25,220)),(a1x+0,a1y-50))
        screen.blit(level ,(width-700,height-100))
        screen.blit(hint_f,(hint_fx+0,hint_fy+0))


    
    elif window==0:
        if b1x <= mouse[0] <= b1x+200 and b1y <= mouse[1] <= b1y+80:
            pygame.draw.rect(screen,color_light1,[b1x,b1y,200,80])
		
        else:
            pygame.draw.rect(screen,color_dark1,[b1x,b1y,200,80])

        if b2x <= mouse[0] <= b2x+200 and b2y <= mouse[1] <= b2y+80:
            pygame.draw.rect(screen,color_light1,[b2x,b2y,200,80])
		
        else:
            pygame.draw.rect(screen,color_dark1,[b2x,b2y,200,80])

        if b3x <= mouse[0] <= b3x+200 and b3y <= mouse[1] <= b3y+80:
            pygame.draw.rect(screen,(255,0,0),[b3x,b3y,200,80])
		
        else:
            pygame.draw.rect(screen,(255,100,100),[b3x,b3y,200,80])

        if b6x <= mouse[0] <= b6x+200 and b6y <= mouse[1] <= b6y+80:
            pygame.draw.rect(screen,color_light1,[b6x,b6y,200,80])
		
        else:
            pygame.draw.rect(screen,color_dark1,[b6x,b6y,200,80])

        if b5x <= mouse[0] <= b5x+200 and b5y <= mouse[1] <= b5y+80:
            pygame.draw.rect(screen,color_light1,[b5x,b5y,200,80])
		
        else:
            pygame.draw.rect(screen,color_dark1,[b5x,b5y,200,80])

        screen.blit(normalfont.render(list3[0] , True , color),(b1x+30,b1y+20))
        screen.blit(normalfont.render(list3[1] , True , color),(b2x+30,b2y+20))
        screen.blit(bigfont.render(list3[2] , True , color),(b3x+50,b3y+15))
        screen.blit(normalfont.render(list3[4] , True , color),(b6x+20,b6y+20))
        screen.blit(normalfont.render(list3[5] , True , color),(b5x+40,b5y+20))


    elif window==2:
        if b3x+350 <= mouse[0] <= b3x+250+300 and b3y-100 <= mouse[1] <= b3y+80-100:
            pygame.draw.rect(screen,(255,50,50),[b3x+350,b3y-100,200,80])
		
        else:
            pygame.draw.rect(screen,(255,100,100),[b3x+350,b3y-100,200,80])

        s = open('score board.txt','r')
        rand_var = 120
        lines = s.readlines()

        for line in lines:
            rand_var+=50
            screen.blit(normalfont.render(line , True , color),(200,rand_var))
            #print(line,end='\n')

        if active:
            color = color_active
        else:
            color = color_passive
        pygame.draw.rect(screen, color, input_rect)
        text_surface = base_font.render(user_text, True, (0, 255, 255))
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        input_rect.w = max(100, text_surface.get_width()+10)        
        
        screen.blit(normalfont.render('Back' , True , (0,0,0)),(b1x+380,b1y+420+100))
        screen.blit(bigfont.render('Score' , True , color),(300,80))
        s.close()


    elif window==3:
        if b1x <= mouse[0] <= b1x+200 and b1y+500 <= mouse[1] <= b1y+580:
            pygame.draw.rect(screen,color_light1,[b1x,b1y+500,200,80])
		
        else:
            pygame.draw.rect(screen,color_dark1,[b1x,b1y+500,200,80])

        screen.blit(bigfont.render('Game Over' , True , (255,0,0)),(b1x-30,b1y+20))
        screen.blit(normalfont.render(list3[3] , True , color),(b1x+30,b1y+520))
        screen.blit(scoretxt ,(width-450,height-500))
        

    

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
			
			
            
            if window==1:
                final_score = 0
                if submitx <= mouse[0] <= submitx+200 and submity <= mouse[1] <= submity+80:
                    hint=0
                    if c==x:
                        
                        score+=1
                        if score <= 5:
                            x=random.randint(1,7)
                            lev=0
                        elif score > 5 and score <= 10:
                            x=random.randint(8,15)
                            lev=1
                        elif score > 10 and score <=15 :
                            x=random.randint(15,31)
                            lev=2
                        elif score > 15  :
                            x=random.randint(31,63)
                            lev=3
                    elif c!=x:
                        window=3
                if a1x <= mouse[0] <= a1x+200 and a1y <= mouse[1] <= a1y+80:
                    c+=1
                    
                
                if a2x <= mouse[0] <= a2x+200 and a2y <= mouse[1] <= a2y+80:
                    c+=2
                    
                
                if a4x <= mouse[0] <= a4x+200 and a4y <= mouse[1] <= a4y+80:
                    c+=4
                    
                
                if a8x <= mouse[0] <= a8x+200 and a8y <= mouse[1] <= a8y+80:
                    c+=8
                    
                
                if c>=64:
                    screen.blit(normalfont.render('Error : value exided',True,color),(width/2,height/2))
                    c=0
                    
                if dplayx <= mouse[0] <= dplayx+200 and dplayy <= mouse[1] <= dplayy+80:
                    
                    c=0
                if b3x+300 <= mouse[0] <= b3x+200+300 and b3y-100 <= mouse[1] <= b3y+80-100:
                    window=0
                    
                if hint_fx <= mouse[0] <= hint_fx+60 and hint_fy <= mouse[1] <= hint_fy+40:
                    hint=1
                    score-=2
                    if score<=-5:
                        window=3


            elif window==2:
                if b3x+300 <= mouse[0] <= b3x+200+300 and b3y-100 <= mouse[1] <= b3y+80-100:
                    window=0

                
# draw rectangle and argument passed which should
	# be on screen
# render at position stated in arguments
# # set width of textfield so that text cannot get
	# outside of user's text input
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
                    
# get text input from 0 to -1 i.e. end.
# Unicode standard is used for string
			# formation
# Check for backspace
                
            elif window==0:
                c=0
                score=0
                lev=0
                hint=0
                if b1x <= mouse[0] <= b1x+200 and b1y <= mouse[1] <= b1y+80:
                    window=1
                if b2x <= mouse[0] <= b2x+200 and b2y <= mouse[1] <= b2y+80:
                    window=2
                if b3x <= mouse[0] <= b3x+200 and b3y <= mouse[1] <= b3y+80:
                    running=False
                if b5x <= mouse[0] <= b5x+200 and b5y <= mouse[1] <= b5y+80:
                    
                    webbrowser.open_new_tab('about us.html')
                if b6x <= mouse[0] <= b6x+200 and b6y <= mouse[1] <= b6y+80:
                    
                    webbrowser.open_new_tab('how to play.html')

            elif window==3:
                if b1x <= mouse[0] <= b1x+200 and b1y+500 <= mouse[1] <= b1y+580:
                    final_score = score
                    window=0
                    c=0
                    score=0
                    fs=str(final_score)
                    with open('score board.txt','a') as f:
                        f.write(fs)
                        f.write('\n')

            
        
        if window==1:
            score_value=str(score)
            rand_no=str(x)
            screen.blit(normalfont.render(list1[c] , True , (255,255,255)),(dplayx+50,dplayy+20))
            screen.blit(normalfont.render(score_value,True,color),(width-100,height-100))
            screen.blit(normalfont.render(rand_no,True,color),(submitx+290,submity-80))
            screen.blit(normalfont.render(list4[lev],True,(240,0,0)),(width-600,height-100))
            if hint==1:
                screen.blit(normalfont.render(list1[x] , True , (0,0,0)),(hint_fx+80,hint_fy+0))
            

        elif window==3:
            
            screen.blit(normalfont.render(score_value,True,color),(width-330,height-500))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1x <= mouse[0] <= b1x+200 and b1y+500 <= mouse[1] <= b1y+580:
                    
                    c=0

    pygame.display.flip()
    clock.tick(10)

pygame.quit()