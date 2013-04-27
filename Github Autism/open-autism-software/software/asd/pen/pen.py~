#Open Autism Software. http://www.openautismsoftware.org
#This software is provided under the GNU General Public License, version 3
#See the license at http://www.gnu.org/licenses/gpl.html
#Authors: Thomas Hansen, Juan Pablo Hourcade, Ricardo Auguste

from pymt import *

globalColor = (0, 0, 1, 1)

#this class handles the drawing with the pen
class Painter(MTWidget): # class declaration Painter
    def init(self):
        self.lines = []
        global globalColor
        self.color = globalColor #Changes the color the pen draws with
    def on_touch_down(self, touch):
        if touch.device == 'mouse': #was originially wm_pen
            global globalColor
            touch.userdata['line'] = [list(touch.pos), globalColor ]
            self.lines.append( touch.userdata['line'] )
            return True
    def on_touch_move(self, touch):
        if touch.device == 'mouse': #was originially wm_pen
            touch.userdata['line'][0].extend(touch.pos)
            return True
    def draw(self):
        for line in self.lines:
            set_color(*line[1])
            drawLine(line[0], width=3)
    def changeColor():
        newColor = (1, 0, 0, 1)

#class used for the color buttons used to change the color the pen draws with
class ColorButton(MTButton): # class declaration Painter
     # pass a color to the object when it's created through the attribute ink
    def __init__(self, **kwargs):
        super(ColorButton, self).__init__(**kwargs)
        self.buttonColor = kwargs.get('ink')

    def on_touch_down(self, touch):
	if touch.device != 'mouse': #was originially wm_pen
		if not self.collide_point(touch.x, touch.y):
	        	return False
	        if self._current_touch is not None:
	            return False
	        self._current_touch = touch
	        self.state = 'down'
	        self.dispatch_event('on_press', touch)
	        touch.grab(self)
	        return True
	else:
		return False

    def on_touch_move(self, touch):
	if touch.device != 'mouse': #was originially wm_pen
	        # take the grabbed touch for us.
        	if not touch.grab_current == self:
            		return False
        	return True
	else:
		return False

    def on_touch_up(self, touch):
	if touch.device != 'mouse': #was originially wm_pen
	        if not touch.grab_current == self:
        	    return False
	        touch.ungrab(self)
        	self._current_touch = None
        	self.state = 'normal'
        	if self.collide_point(*touch.pos):
            		self.dispatch_event('on_release', touch)
		return True
	else:
		return False

    def on_release(self, touch):
        if touch.device != 'mouse': #was originially wm_pen
            newColor = self.buttonColor
            global globalColor
            globalColor = newColor
            return True
        return False
        
    def on_press(self, touch):
        if touch.device != 'mouse': #was originially wm_pen
            print('touch')
            return True
        return False
        
# root node
root = MTWidget(fullscreen=True)


# scatter plane for drawing, panning, zooming
scatter = MTScatterPlane()
painter = Painter() #painter is where the drawing occurs
scatter.add_widget(painter)
root.add_widget(scatter)


# color buttons
button_layout = MTGridLayout(cols = 4, rows = 2)
root.add_widget(button_layout)
button = ColorButton(label = ' ', style = {'bg-color': (0,0,0)}, size = (65,65), ink = (0,0,0))
button_layout.add_widget(button)

button2 = ColorButton(label = ' ', style = {'bg-color':(0,0,1)}, size = (65,65), ink = (0,0,1))
button_layout.add_widget(button2)

button3 = ColorButton(label = ' ', style = {'bg-color':(0,1,0)}, size = (65,65), ink =( 0,1,0))
button_layout.add_widget(button3)

button4 = ColorButton(label = ' ', style = {'bg-color':(0,1,1)}, size = (65,65), ink = (0,1,1))
button_layout.add_widget(button4)

button5 = ColorButton(label = ' ', style = {'bg-color':(1,0,0)}, size = (65,65), ink = (1,0,0))
button_layout.add_widget(button5)

button6 = ColorButton(label = ' ', style = {'bg-color':(1,0,1)}, size = (65,65), ink = (1,0,1))
button_layout.add_widget(button6)

button7 = ColorButton(label = ' ', style = {'bg-color':(1,1,0)}, size = (65,65), ink = (1,1,0))
button_layout.add_widget(button7)

button8 = ColorButton(label = ' ', style = {'bg-color':(1,1,.5)}, size = (65,65), ink = (1,1,.5))
button_layout.add_widget(button8)

# run from root
runTouchApp(root)


