import pygame
import random


from pygame.mask import from_surface


pygame.init()
dis = pygame.display.set_mode((800,600))
pygame.display.set_caption("Little Snake")
dis.fill((255,255,255))
pygame.display.update()
f_st = pygame.font.SysFont(None,50)
f_st1 = pygame.font.SysFont(None,40)
f_st2 = pygame.font.SysFont(None,30)
f_st3 = pygame.font.SysFont(None,30)


def snake(s_l):
    for i in s_l:
        pygame.draw.rect(dis,(0,0,255),[i[0],i[1],10,10])
    pygame.display.update()
def message():
    msg = "GAME OVER"
    msg2 = "press SPACE for PLAY again"
    msg3 = "press ESC for QUIT"
    k = f_st.render(msg,True,(255,0,0))
    p = f_st2.render(msg2,True,(0,255,0))
    q = f_st3.render(msg3,True,(0,0,255))
    dis.blit(k,[290,200])
    dis.blit(p,[270,250])
    dis.blit(q,[300,270])
    pygame.display.update()
def c_score(l):
    msg = "Score :"+str(l)
    k = f_st1.render(msg,True,(0,255,0))
    dis.blit(k,[0,0])
    pygame.display.update()

def h_score(h):
    msg = "High Score :"+str(h)
    k = f_st1.render(msg,True,(0,255,0))
    dis.blit(k,[600,0])
    pygame.display.update()




HIGH = 1
def main():
    x = 300
    y = 300
    xc = 0
    yc = 0

    s_l = []

    l = 1
    global HIGH
    

    fx = int(random.randrange(10,780))
    fy = int(random.randrange(30,580))

    clk = pygame.time.Clock()
    speed = 15
    gameover = False
    while not gameover:
        for i in pygame.event.get():

            if i.type==pygame.QUIT:
                gameover = True

            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_LEFT:
                    xc = -10
                    yc = 0
                elif i.key == pygame.K_RIGHT:
                    xc = 10
                    yc = 0
                elif i.key == pygame.K_DOWN:
                    xc = 0
                    yc = 10
                elif i.key == pygame.K_UP:
                    xc = 0
                    yc = -10
        if x>780 or x<10 or y>580 or y<30:
            sub_main()

        dis.fill((255,255,255),(0,0,800,30))
        c_score(l)


        h_score(HIGH)


    

        x+=xc
        y+=yc
        s_l.append([x,y])
        
        if len(s_l) > l:
            del s_l[0]
        dis.fill((0,0,0),(10,30,790,590))
        dis.fill((255,255,255),(0,30,10,600))
        dis.fill((255,255,255),(790,30,800,600))
        dis.fill((255,255,255),(0,590,800,600))
        pygame.draw.circle(dis,(255,0,0),[fx,fy],10)
        snake(s_l)
        
        if x in range(fx-10,fx+10) and y in range(fy-10,fy+10):
            fx = int(random.randrange(10,780))
            fy = int(random.randrange(30,580))
            l+=1
            speed+=1

        
        clk.tick(speed)
        if HIGH <l:
            HIGH = l


def sub_main():
    
    dis.fill((0,0,0),(10,30,780,560))
    message()
    gameover = True
    while gameover:
        for i in pygame.event.get():
            print(i)
            if i.type == pygame.KEYDOWN:
                if i.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if i.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif i.key == pygame.K_SPACE:
                    main()
                
main()
pygame.quit()
quit()
