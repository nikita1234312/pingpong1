from pygame import * 
init()


size = [900, 700]
run = True
FPS = 360
score = 0
lvl = "one"
sp = 2
xr1 = -4
xr2 = 845
yr = 200


window = display.set_mode(size)
clock = time.Clock()

bg = transform.scale(image.load("images/bg pingpong.jpg"), (900,700))
bg2 = transform.scale(image.load("images/bg pingpong2.png"), (920,850))


menu_txt = font.SysFont("Arial", 35).render("Меню", True, (255,255,255))
restart_txt = font.SysFont("Arial", 70).render("Рестарт", True, (255,255,255))
exit_txt = font.SysFont("Arial", 70).render("Выход", True, (255,255,255))
shop_txt = font.SysFont("Arial", 70).render("Магазин", True, (255,255,255))


class GameSprite(sprite.Sprite): 
    def __init__(self, img, x, y, weight, height): 
        super().__init__() 
        self.w = weight 
        self.h = height 
        self.image = transform.scale(image.load(img),(self.w, self.h)) 
        self.rect = self.image.get_rect() 
        self.rect.x = x 
        self.rect.y = y 

    def rendering(self): 
        window.blit(self.image, (self.rect.x, self.rect.y)) 


class Ball(GameSprite): 
    def __init__(self, img, x, y, weight, height, speed_x, speed_y): 
        super().__init__(img, x, y, weight, height) 
        self.speed_x = speed_x 
        self.speed_y = speed_y 

    def move(self): 
        self.rect.x += self.speed_x  
        self.rect.y += self.speed_y  
        if self.rect.y <= 70: 
            self.speed_y *= -1 
        if self.rect.y >= 550: 
            self.speed_y *= -1

    def move_inv(self): 
        self.rect.x += self.speed_x  
        self.rect.y += self.speed_y  
        if self.rect.y <= 100: 
            self.speed_y *= -1 
        if self.rect.y >= 530: 
            self.speed_y *= -1


class Rocket(GameSprite):
    def __init__(self, img, x, y, weight, height, speed):
        super().__init__(img, x, y, weight, height)
        self.speed = speed
    def move_l(self):
        if keys[K_w] and self.rect.y >= 70:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <= 440:
            self.rect.y += self.speed

    def move_r(self):
        if keys[K_UP] and self.rect.y >= 70:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <= 440:
            self.rect.y += self.speed

    def move_l_inv(self):
        if keys[K_s] and self.rect.y >= 110:
            self.rect.y -= self.speed
        if keys[K_w] and self.rect.y <= 410:
            self.rect.y += self.speed

    def move_r_inv(self):
        if keys[K_DOWN] and self.rect.y >= 110:
            self.rect.y -= self.speed
        if keys[K_UP] and self.rect.y <= 410:
            self.rect.y += self.speed 


class Menu():
    def __init__(self, w, h, x, y, color):
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.color = color
        self.rect = Rect(self.x, self.y, self.w, self.h) 

    def set_block(self):
        draw.rect(window, self.color, self.rect)  

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)    


ball = Ball('images/ball.png',350, 250, 70, 70, 4, 4)
rocket1 = Rocket('images/rocket pingpong.png', xr1, yr, 60, 180, 4)
rocket2 = Rocket('images/rocket pingpong.png', xr2, yr, 60, 180, 4)

btn_menu = Menu(200,60, size[0]//2-100, 5, (13, 99, 12))
btn_menu2 = Menu(180,40, size[0]//2-90, 15, (25, 122, 23))

bg_menu = Menu(size[0], size[1], 0, 0, (175,238,238))
####buttons menu####
#button exit
btn_menu_exit = Menu(320, 120, size[0]//2-160, 500, (62, 95, 138))
btn_menu_exit2 = Menu(300, 100, size[0]//2-150, 510, (154, 206, 235))
#button restart
btn_menu_restart = Menu(320, 120, size[0]//2-160, 300, (62, 95, 138))
btn_menu_restart2 = Menu(300, 100, size[0]//2-150, 310, (154, 206, 235))
#button back
btn_menu_back = Menu(120, 120, 10, 10, (62, 95, 138))
btn_menu_back2 = Menu(100, 100, 20, 20, (154, 206, 235))
back_menu = GameSprite("images/back.png", 20, 20, 100, 100)
#button settings
btn_menu_settings = Menu(120, 120, size[0]-130, 10, (62, 95, 138))
btn_menu_settings2 = Menu(100, 100, size[0]-120, 20, (154, 206, 235))
settings_menu = GameSprite("images/settings.png", size[0]-120, 20, 100, 100)
#button shop
btn_menu_shop = Menu(320, 120, size[0]//2-160, 100, (62, 95, 138))
btn_menu_shop2 = Menu(300, 100, size[0]//2-150, 110, (154, 206, 235))

####shop_button####
#bg#
btn_shop_bg = Menu(200, 400, 50, 200, (62, 95, 138))
shop_bg = GameSprite("images/shop_bg.jpg", 60, 210, 180, 380)
#buy
#shop_bg2 = GameSprite("images/bg_shop2.avif", 100, 200, 500, 400)

#rocket
btn_shop_rocket = Menu(200, 400, 350, 200, (62, 95, 138))
btn_shop_rocket2 = Menu(180, 380, 360, 210, (154, 206, 235))
shop_rocket = GameSprite("images/shop_rocket.png", 340, 250, 220, 280)
#ball
btn_shop_ball = Menu(200, 400, 650, 200, (62, 95, 138))
btn_shop_ball2 = Menu(180, 380, 660, 210, (154, 206, 235))
shop_ball = GameSprite("images/shop_ball.png", 595, 250, 300, 300)


while run:
    keys = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            x, y = e.pos
            if btn_menu.collidepoint(x,y):
                lvl = "menu"
            #menu
            if btn_menu_back.collidepoint(x, y):
                if lvl == "menu":
                    lvl = "one"
                if lvl == "shop":
                    lvl = "menu"
                if lvl == "shop bg":
                    lvl = "shop"
            if btn_menu_exit.collidepoint(x, y) and lvl == "menu":
                run = False 
            if btn_menu_restart.collidepoint(x, y) and lvl == "menu":
                lvl = "one"
                ball.rect.x = 350
                ball.rect.y = 250
                rocket1.rect.y = 200
                rocket2.rect.y = 200
                score = 0
                ball.speed_y = 4
                ball.speed_x = 4
            if btn_menu_shop.collidepoint(x, y) and lvl == "menu":
                lvl = "shop"
            #shop
            if btn_shop_bg.collidepoint(x, y) and lvl == "shop":
                lvl = "shop bg"



    #counter
    score_txt = font.SysFont("Arial", 55).render("Очки:" + str(score), True, (255,255,255))
    

    if not lvl == "menu" and not lvl == "shop":
        window.blit(bg, (0,0))
        #render
        ball.rendering()
        rocket1.rendering()
        rocket2.rendering()
        #moves
        rocket1.move_l()
        rocket2.move_r()
        ball.move()
        #button and text
        window.blit(score_txt, (10,10))
        btn_menu.set_block()
        btn_menu2.set_block()
        window.blit(menu_txt, (size[0]//2-90+50,15))


    #collision
    if rocket1.rect.colliderect(ball.rect):
        ball.speed_x *= -1
        score += 1
    if rocket2.rect.colliderect(ball.rect):
        ball.speed_x *= -1
        score += 1


    #speed ball
    if score > sp:
        if ball.speed_y > 0 and ball.speed_y < 7: 
            ball.speed_y += 1
        if ball.speed_y < 0 and ball.speed_y < -7:
            ball.speed_y -= 1
        if ball.speed_x > 0 and ball.speed_x < 7: 
            ball.speed_x += 1
        if ball.speed_x < 0 and ball.speed_x < -7:
            ball.speed_x -= 1
        sp += 3

    
    if not lvl == "inv" and lvl == "one":
        if score > 1 and score < 3:
            lvl = "inv"
        else:
            lvl = "one"


    
    #inversion
    """if lvl == "inv":
        
        window.blit(bg2, (-10, -100))
        #render
        ball.rendering()
        rocket1.rendering()
        rocket2.rendering()
        #moves
        rocket1.move_l_inv()
        rocket2.move_r_inv()
        ball.move()"""        



    #menu
    if lvl == "menu":
        #bg menu
        bg_menu.set_block()
        #button exit
        btn_menu_exit.set_block()
        btn_menu_exit2.set_block()
        window.blit(exit_txt, (size[0]//2-95, 515))
        #button restart 
        btn_menu_restart.set_block()
        btn_menu_restart2.set_block()
        window.blit(restart_txt, (size[0]//2-115, 315))
        #button back
        btn_menu_back.set_block()
        btn_menu_back2.set_block()
        back_menu.rendering()
        #button settings
        btn_menu_settings.set_block()
        btn_menu_settings2.set_block()
        settings_menu.rendering()
        #button shop
        btn_menu_shop.set_block()
        btn_menu_shop2.set_block()
        window.blit(shop_txt, (size[0]//2-115, 115))

    
    if lvl == "shop":

        bg_menu.set_block()

        btn_menu_back.set_block()
        btn_menu_back2.set_block()
        back_menu.rendering()

        #bg
        btn_shop_bg.set_block()
        shop_bg.rendering()
        #rocket
        btn_shop_rocket.set_block()
        btn_shop_rocket2.set_block()
        shop_rocket.rendering()
        #ball
        btn_shop_ball.set_block()
        btn_shop_ball2.set_block()
        shop_ball.rendering()
    
    if lvl == "shop bg":
        bg_menu.set_block()

        btn_menu_back.set_block()
        btn_menu_back2.set_block()
        back_menu.rendering()

        #shop_bg2.rendering()




    

    

    display.update()
    clock.tick(FPS)  