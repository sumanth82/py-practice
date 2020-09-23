# Use pyglet library to create a hello world application 
# It should pop open a window which displays - Hello World; 
# pyglet library is used for gaming apps/softwares

import pyglet 
window = pyglet.window.Window()

label=pyglet.text.Label('Hello, World', 
                        font_name='Times New Roman',
                        font_size=36,
                        x=window.width//2, y=window.height//2,
                        anchor_x='center', anchor_y='center')

@window.event

def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()