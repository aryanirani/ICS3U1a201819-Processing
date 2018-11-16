#Bouncing ronaldo
delta_x = 100
delta_y = 100

ronaldo_pos_x = 100
ronaldo_pos_y = 100
ronaldo_size_x = 284
ronaldo_size_y = 178
ronaldo_speed_x = 5
ronaldo_speed_y = 3

click_number = 0
l_colour = "#ce2f04"
def setup():
    global webImg
    global Img_2
    size(600, 500)
    stadium = 'https://media-public.fcbarcelona.com/20157/0/document_thumbnail/20197/208/46/88/72888016/1.0-2/72888016.jpg?t=1520519732000'
    webImg = loadImage(stadium, "png")
    webImg.resize(width, height)
    ronaldo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSB3j9eJzMTrAF_YT7YO-FXO6BEObcVWDz4y2eZ6a1MAI5MEq72"
    Img_2 = loadImage(ronaldo, "png")

    
def draw():
    global l_colour
    global ronaldo_pos_x, ronaldo_pos_y
    global delta_x, delta_y, ronaldo_speed_x, ronaldo_speed_y
    background(0)
    image(webImg, 0, 0)
    image(Img_2, ronaldo_pos_x, ronaldo_pos_y)
    ronaldo_pos_x += ronaldo_speed_x
    ronaldo_pos_y += ronaldo_speed_y
    if ronaldo_pos_x < 0 or ronaldo_pos_x > width-ronaldo_size_x:
        ronaldo_speed_x *= -1
    elif ronaldo_pos_y < 0 or ronaldo_pos_y > height-ronaldo_size_y:
        ronaldo_speed_y *= -1

    # delta_x 
    
    noStroke()
    fill(255,255,255)
    ellipse(delta_x, height/2,50,50)
    
    fill(55,121,22)
    rect(delta_x+30, height/2/3,90,80)
    
    fill(209, 229, 55)
    triangle(75,30,75,58,20,86)
    fill(l_colour)
    textSize(300)
    textAlign(CENTER)
    text("L", width/2, height*4/9)

def mouseClicked():
    global click_number, l_colour
    click_number += 1
    if click_number % 2:
        l_colour = "#0f0da5"
    else:
        l_colour = "#ce2f04"
