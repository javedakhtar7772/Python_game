import pgzrun

HEIGHT = 300
WIDTH  = 800
p= Actor('ironman',(100,100))
c= Actor('cookie_img')

def draw():
    screen.fill('white')
    p.draw()
    c.draw()

def update():
    p.x -= 5
    p.angle=-10
    if p.x < 0: # agar player lest side se  bahar gyye to
       p.x=WIDTH
    print(p.x, p.y)


pgzrun.go()