from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def dol():
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    #  face
    glColor(0, 0, 1)
    glBegin(GL_POLYGON)
    glVertex2d(0.25, 0.7)
    glVertex2d(0.25, 0.35)
    glVertex2d(-0.25, 0.35)
    glVertex2d(-0.25, 0.7)
    glEnd()
    glColor(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2d(0.15, 0.5)
    glVertex2d(0.15, 0.45)
    glVertex2d(-0.15, 0.45)
    glVertex2d(-0.15, 0.5)
    glEnd()
    glColor(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2d(0.0, 0.55)
    glVertex2d(0.05, 0.6)
    glVertex2d(-0.05, 0.6)

    glEnd()

    #circle right eye
    glColor(1, 1, 1)
    glBegin(GL_POLYGON)
    r = 0.05
    x0 = 0.15
    y0 = 0.6
    for theta in np.arange(0, 2 * pi, 0.001):
        x = x0 + r * cos(theta)
        y = y0 + r * sin(theta)
        glVertex2d(x, y)
    glEnd()
    glFlush()

    #circle left eye
    #glColor(1, 1, 1)
    glBegin(GL_POLYGON)
    r = 0.05
    x0 = -0.15
    y0 = 0.6
    for theta in np.arange(0, 2 * pi, 0.001):
        x = x0 + r * cos(theta)
        y =y0 +  r * sin(theta)
        glVertex2d(x, y)
    glEnd()
    glFlush()
    glColor3d(1,0, 0)
    glBegin(GL_POLYGON)
    glVertex2d(0.07, 0.3)
    glVertex2d(0.07, 0.35)
    glVertex2d(-0.07, 0.35)
    glVertex2d(-0.07, 0.3)
    glEnd()
    #glColor3d(0,1, 0)
    glBegin(GL_POLYGON)
    glVertex2d(0.3, 0.3)
    glVertex2d(0.3, -0.3)
    glVertex2d(-0.3, -0.3)
    glVertex2d(-0.3, 0.3)
    glEnd()
    #right leg
    glColor3d(0, 0,1)
    glBegin(GL_POLYGON)
    glVertex2d(0.15, -0.3)
    glVertex2d(.25, -0.3)
    glVertex2d(0.25, -0.7)
    glVertex2d(0.15, -0.7)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2d(0.15, -0.7)
    glVertex2d(0.15, -0.8)
    glVertex2d(0.4, -0.8)
    glVertex2d(0.4, -0.7)
    glEnd()
    #left leg
    #glColor3d(0, 1,0)
    glBegin(GL_POLYGON)
    glVertex2d(-0.15, -0.3)
    glVertex2d(-0.15, -0.7)
    glVertex2d(-0.25, -0.7)
    glVertex2d(-0.25, -0.3)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2d(-0.15, -0.7)
    glVertex2d(-0.15, -0.8)
    glVertex2d(-0.4, -0.8)
    glVertex2d(-0.4, -0.7)
    glEnd()
    #right hand
    glColor3d(1, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2d(0.3, 0.3)
    glVertex2d(0.7, 0.0)
    glVertex2d(0.65, -0.1)
    glVertex2d(0.3, 0.2)
    glEnd()
    #left hand
    glBegin(GL_POLYGON)
    glVertex2d(-0.3, 0.3)
    glVertex2d(-0.7, 0.0)
    glVertex2d(-0.65, -0.1)
    glVertex2d(-0.3, 0.2)
    glEnd()
    glFlush()
#__main function
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(700, 700)   # Set the window's initial width & height
glutCreateWindow(b":intial carton man report")
glutDisplayFunc(dol)
glutMainLoop()
