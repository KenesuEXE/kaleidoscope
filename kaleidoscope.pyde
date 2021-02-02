"""
Kaleidoscope
by KenesuEXE
"""

def setup():
    size(750, 750)
    background(0)
    colorMode(HSB)

rad, rad_chg = 10, 0.5
hue_a, hue_b, hue_c = random(255), random(255), random(255)
hue_a_chg, hue_b_chg, hue_c_chg = random(0.1, 0.2), random(0.1, 1), random(0.1, 1)
sat_a, sat_b, sat_c = random(100, 200), random(100, 200), random(100, 200)
sat_a_chg, sat_b_chg, sat_c_chg = random(0.1, 1), random(0.1, 1), random(0.1, 1)

def draw():
    global rad, rad_chg, hue_a, hue_b, hue_c, hue_a_chg, hue_b_chg, hue_c_chg, sat_a, sat_b, sat_c, sat_a_chg, sat_b_chg, sat_c_chg

    noFill()
    strokeWeight(3)

    # Circle Set A
    stroke(hue_a, sat_a, 255, 200)
    circle(width/2, width/2, rad)
    circle(width, width/2, rad)
    circle(0, width/2, rad)
    circle(width/2, 0, rad)
    circle(width/2, width, rad)
    
    # Circle Set B
    stroke(hue_b, sat_b, 255, 200)
    circle(width/4, width/4, rad)
    circle(width/4, width*3/4, rad)
    circle(width*3/4, width/4, rad)
    circle(width*3/4, width*3/4, rad)
    
    # Circle Set C
    stroke(hue_c, sat_c, 255, 200)
    circle(0, 0, rad)
    circle(0, width, rad)
    circle(width, 0, rad)
    circle(width, width, rad)

    # Radius fluctuates up and down
    rad += rad_chg
    if rad < 5 or rad > width*2:
        rad_chg = -rad_chg

    # Hue loops from 1 to 255, then back to 1
    hue_a += hue_a_chg
    hue_a %= 255
    hue_b += hue_b_chg
    hue_b %= 255
    hue_c += hue_c_chg
    hue_c %= 255
    
    # Saturation fluctuates up and down
    sat_a += sat_a_chg
    if sat_a < 100 or sat_a > 200:
        sat_a_chg = -sat_a_chg
    sat_b += sat_b_chg
    if sat_b < 100 or sat_b > 200:
        sat_b_chg = -sat_b_chg
    sat_c += sat_c_chg
    if sat_c < 100 or sat_c > 200:
        sat_c_chg = -sat_c_chg
    

    # Save sketch into image
    if keyPressed and key == 'e':
        save("image.jpg")
        exit()
