import OpenGL
import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image
from random import randint

def timer_rotated():
    global timer, glRotatef_x, glRotatef_y, glRotatef_z, girar
    if timer > 0: timer -= 0.1
    else: 
        girar = False
        timer = 0 
        #print(f'X: {glRotatef_x}\nY: {glRotatef_y}\nZ: {glRotatef_z}\n')

    return timer

def key_control(key, x, y):
    global rotacionar
        
    if key == GLUT_KEY_UP:
        rotacionar += 50
    elif key == GLUT_KEY_DOWN:
        rotacionar -= 50

def key_control_start(key, x, y):
    global girar, timer, random_values_rotate, random_values_translate
       
    if key == b'\r':# Tecla enter
        timer = 20
        girar = True
        
        random_values_rotate = [
            randint(1, 30),
            randint(1, 100),
            randint(1, 60)
        ]
        # random_values_translate = [
        #     randint(1, 3), 
        #     randint(1, 3), 
        #     randint(1, 3)
        # ]
        
def automatic_rotated():
    global rotacionar, glRotatef_x, glRotatef_y, glRotatef_z

    if girar:
        tempo = timer_rotated()
        rotacionar += tempo
        glRotatef_x += random_values_rotate[0]
        glRotatef_y += random_values_rotate[1]
        glRotatef_z += random_values_rotate[2]

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
    image = Image.open(filename)
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

def cubo():
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
    global rotacionar
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glRotatef(rotacionar, glRotatef_x, glRotatef_y, glRotatef_z)
    glScalef(40, 40, 40)
    glTranslatef(
        random_values_translate[0],
        random_values_translate[1], 
        random_values_translate[2]
    )
    cubo()
    automatic_rotated()
    glutKeyboardFunc(key_control_start)
    glutSwapBuffers()

def load_textures():
    global id_textures
    ids = [load_texture(f'd{i}.png') for i in range(1, 7)]    
    id_textures = ids

def init():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(1000, 1000)
    glutInitWindowPosition(-200, -200)
    glutCreateWindow('Dado OpenGL')
    init_gl()
    load_textures()
    glutSpecialFunc(key_control)
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)

    glutMainLoop()

id_textures = []
rotacionar = 0
glRotatef_x = 1
glRotatef_y = 1 
glRotatef_z = 0

glTranslatef_x = 0
glTranslatef_y = 0
glTranslatef_z = 0
timer = 20
random_values_translate = [0, 0, 0]
random_values_rotate = [1, 1, 1]
girar = False
init()