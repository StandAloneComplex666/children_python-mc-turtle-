# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 23:35:02 2017

@author: hp
"""

import turtle
t = turtle.Pen()
t.penup()
turtle.bgcolor("white")
colors = ["red", "yellow", "blue", "green", "purple"]
for n in range(5):
    t.pencolor(colors[n%5])
    t.circle(100)
    t.left(72)
