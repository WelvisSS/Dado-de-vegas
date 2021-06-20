# Disponível em: https://github.com/WelvisSS/dado-de-vegas
import OpenGL
import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image
from random import randint

def timer_rotated_x():
    global timer_x, girar_eixo_x, rotacionar_x, random_axis
    
    if timer_x > 1: 
        timer_x -= 0.1
    else:
        timer_x = 0 
        if ((int(rotacionar_x))%90 == 0): 
            girar_eixo_x = False
            rotacionar_x = int(rotacionar_x)
        else: rotacionar_x += 0.8

    return timer_x

def timer_rotated_y():
    global timer_y, girar_eixo_y, rotacionar_y, random_axis

    if timer_y > 1: 
        timer_y -= 0.1
    else:
        timer_y = 0 
        if ((int(rotacionar_y))%90 == 0): 
            girar_eixo_y = False
            rotacionar_y = int(rotacionar_y)
        else: 
            rotacionar_y += 0.8

    return timer_y

def timer_rotated_z():
    global timer_z, girar_eixo_z, rotacionar_z, random_axis

    if timer_z > 1: 
        timer_z -= 0.1
    else:
        timer_z = 0 
        if ((int(rotacionar_z))%90 == 0): 
            girar_eixo_z = False
            rotacionar_z = int(rotacionar_z)
        else: 
            rotacionar_z += 0.8

    return timer_z

def key_press(key, x, y):
    global girar_eixo_x, girar_eixo_y, girar_eixo_z
    global random_axis, timer_x, timer_y, timer_z, random_values_translate

    if key == b'\r':# Tecla enter
        timer_x = randint(5, 20)
        timer_y = randint(5, 20)
        timer_z = randint(5, 20)

        random_values_translate = [3, 1, 1]

        girar_eixo_x = True
        girar_eixo_y = True
        girar_eixo_z = True

        random_axis = [
            randint(0, 1), 
            randint(0, 1), 
            randint(0, 1)
        ]
        #Impedindo que x, y e z sejam 0 na hora de jogar o dado.
        while (random_axis[0] + random_axis[1] + random_axis[2]) <= 1:
            random_axis = [
                randint(0, 1), 
                randint(0, 1), 
                randint(0, 1)
            ]

def automatic_rotated():
    global rotacionar_x, rotacionar_y, rotacionar_z
    tempo = 0
    if girar_eixo_x:
        tempo = timer_rotated_x()
        rotacionar_x += tempo

    if girar_eixo_y:
        tempo = timer_rotated_y()
        rotacionar_y += tempo
    
    if girar_eixo_z:
        tempo = timer_rotated_z()
        rotacionar_z += tempo

def create_gl_texture(width, height, pbits):
    id_texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, id_texture)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, pbits)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glGenerateMipmap(GL_TEXTURE_2D)

    return id_texture

def load_texture(filename):
    image = Image.open(f'src/texture/{filename}')
    ix = image.size[0]
    iy = image.size[1]
    pbits = image.convert("RGBA").tobytes("raw", "RGBA")
    id_texture = create_gl_texture(ix, iy, pbits)
    return id_texture

def init_gl():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-200.0, 200, -200.0, 200, -150, 150)
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_TEXTURE_2D)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

def dado():    
    glBindTexture(GL_TEXTURE_2D, id_textures[0])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, -1.0,  1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, -1.0,  1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0,  1.0,  1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0,  1.0,  1.0)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, id_textures[1])
    glBegin(GL_QUADS)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0,  1.0, -1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0,  1.0, -1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, id_textures[2])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0,  1.0, -1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0,  1.0,  1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0,  1.0,  1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0,  1.0, -1.0)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, id_textures[3])
    glBegin(GL_QUADS)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0,  1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0,  1.0)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, id_textures[4])
    glBegin(GL_QUADS)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0,  1.0, -1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0,  1.0,  1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0,  1.0)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, id_textures[5])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0,  1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0,  1.0,  1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0,  1.0, -1.0)
    glEnd()
    
def showScreen():
    global id_textures
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    
    glRotatef(rotacionar_x, random_axis[0], 0, 0)
    glRotatef(rotacionar_y, 0, random_axis[1], 0)
    glRotatef(rotacionar_z, 0, 0, random_axis[2])

    glScalef(40, 40, 40)

    glTranslatef(
        random_values_translate[0],
        random_values_translate[1], 
        random_values_translate[2]
    )
    dado()

    automatic_rotated()
    glutKeyboardFunc(key_press)
    glutSwapBuffers()

def load_textures():
    global id_textures
    ids = [load_texture(f'lado{i}.png') for i in range(1, 7)]    
    id_textures = ids

def init():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(800, 800)
    glutInitWindowPosition(600, 100)
    glutCreateWindow('Dado de Vegas')
    init_gl()
    load_textures()
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)

    glutMainLoop()

random_axis = [0,0,0]
id_textures = []

rotacionar_x = 0
rotacionar_y = 0
rotacionar_z = 0

timer_x = 20
timer_y = 30
timer_z = 30

girar_eixo_x = False
girar_eixo_y = False
girar_eixo_z = False

random_values_translate = [0, 0, 0]

init()