from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
import math
from PIL import Image, ImageDraw, ImageFont
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivy.lang import Builder
Screens = ["First", "Second"]
Operations = ["exit", "save"]

KV = '''
Screen:
    screen_man:screen_man
    button_outside:button_outside
    GridLayout:
        rows: 2
        cols: 1
        MDRaisedButton:
            id: button_outside
            text: "Outside Screen Manager"
            pos_hint: {"center_x": .1, "center_y": .9}
            size_hint: 0.1 , 0.1
            on_release: app.launch_menu(self)

        ScreenManager:
            id:screen_man
            ScreenMain:
            LenPasword:
            


<ScreenMain>:
    name:"First"
    id:"first_screen"
    label: label
    MDLabel:
        id: label
        text: "Console"
        font_size: "20dp"
        pos_hint: {"center_x": .9, "center_y": 0.9}
    


<LenPasword>:
    name:"Second"
    

'''


class ScreenMain(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)
        self.trees = {'el': 32.5, 'bereza': 17.5, 'dub': 26, 'klen': 13, 'topol': 13, 'sosna': 32.5, 'person': 1.7, 'truck': 2.25, 'tank': 2.75, 'countryhouse': 6.5, 'car': 1.5}
        boxlayout = BoxLayout(orientation="vertical", spacing=5, padding=[10])

        button_new_pasword = Button(
            text="Map >",
            background_color=[0, 1.5, 3, 1],
            size_hint=[1, 0.1],
            on_press=self._on_press_button_new_pasword,
        )

        boxlayout.add_widget(button_new_pasword)
        self.add_widget(boxlayout)
        
        self.label1 = Label(text='console')
        boxlayout.add_widget(self.label1)
        #self.label = ObjectProperty()
        #self.add_widget(self.label)
        self.text_input1 = TextInput(hint_text='Enter text 1', size_hint=(1, 0.1))
        boxlayout.add_widget(self.text_input1)
        #self.add_widget(self.text_input1)
        
        self.text_input2 = TextInput(hint_text='Enter text 2', size_hint=(1, 0.1))
        boxlayout.add_widget(self.text_input2)
        #self.add_widget(self.text_input2)
        
        self.button = Button(text='Submit', on_press=self.on_submit, size_hint=(1, 0.1))
        boxlayout.add_widget(self.button)
        #self.add_widget(self.button)
        
    def show_items(self):
        items = ""
        for i in self.trees:
            items += (f"{i} - {self.trees[i]} meters\n")
        return items
    def test_digit(self, num1, num2):
       try:
           num1 = float(num1)
           num2 = float(num2)
           return num1, num2
       except:
           try:
               num1 = float(self.trees[num1])
               num2 = float(num2)
               return num1, num2
           except:
               self.error_message = "invalid input"
               return False, None
    def calculate_distance(self,real_height, nominal_height):
        real_height = float(real_height)
        nominal_height = float(nominal_height)
        distance = 100 / (nominal_height * 2) * real_height
        return str(distance)
    def on_submit(self, instance):
        
        text1 = self.text_input1.text
        if text1 == "items":
            distance = self.show_items()
        else:
            text2 = self.text_input2.text
            text1, text2 = self.test_digit(text1, text2)
            if text1 == False:
                distance = self.error_message
            else:
                distance = self.calculate_distance(text1, text2)
        
        self.label.text = distance


    def _on_press_button_new_pasword(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'Second'


class LenPasword(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global items, pidoras
        items = [['pidoras ebani syka']]
        self.new_dot = 0
        

        boxlayout = BoxLayout(orientation="vertical", spacing=5, padding=[10])

        button_new_pasword = Button(
            text="< Distance meter",
            background_color=[2, 1.5, 3, 1],
            size_hint=[1, 0.1],
            on_press=self._on_press_button_new_pasword,
        )


        boxlayout.add_widget(button_new_pasword)
        self.add_widget(boxlayout)
        self.canvas_widget = Widget()
        pidoras = self.canvas_widget
        boxlayout.add_widget(self.canvas_widget)
        #self.add_widget(self.canvas_widget)

        self.input_x = TextInput(hint_text='Azimith',size_hint=(1, 0.1))
        self.input_y = TextInput(hint_text='Distance',size_hint=(1, 0.1))
        boxlayout.add_widget(self.input_x)
        boxlayout.add_widget(self.input_y)
        '''
        self.add_widget(self.input_x)
        self.add_widget(self.input_y)
        '''

        add_button = Button(text='Add Point',size_hint=(1, 0.1))
        add_button.bind(on_press=self.add_point)
        boxlayout.add_widget(add_button)
        undo_button = Button(text='undo',size_hint=(1, 0.05))
        undo_button.bind(on_press=self.undod)
        boxlayout.add_widget(undo_button)

    
    def choose_operation(self):
        #print(self)
        im = Image.open('map_pattern.png')
        draw = ImageDraw.Draw(im)
        for a in items:
            for i in range(len(a) - 1):
                x1 = int(a[i][1][0])
                y1 = int(2400 - a[i][1][1])
                x2 = int(a[i + 1][1][0])
                y2 = int(2400 - a[i + 1][1][1])
                draw.line((x1, y1, x2, y2), fill = 'black', width = 4)#366
        draw.line((270,150,770,150), fill = 'black', width = 4)
        ffont = ImageFont.truetype("arial.TTF", size=10)
        draw.text((1000, 1000), '500')
        im.save('map2.png', quality = 95)
        
    def add_point(self, instance):
        def calculate_coords(azim, dist):
            azim *= 6
            angle = 270 - azim
            x_dist = dist * math.cos(math.radians(angle))
            y_dist = dist * math.sin(math.radians(angle)) 
            x = self.const_x + x_dist
            y = self.const_y + y_dist
            #print(angle, x_dist, y_dist)
            return x, y
        try:
            
            azim = float(self.input_x.text)
            dist = float(self.input_y.text)
            x, y =  calculate_coords(azim, dist)
            
            #x = self.const_x
            #y = self.const_y
            print(f"const({self.const_x},{self.const_y}) normal({x},{y})")
            with self.canvas_widget.canvas:
                Color(1, 0, 0)  # Red 2180
                d = 30.
                print(f"const({self.const_x},{self.const_y}) normal({x},{y})")
                #dot = Ellipse(pos=(x,  y), size=(d, d))
                dot = Line(points = (self.const_x, self.const_y, x, y), width = 5)
                self.const_x = x
                self.const_y = y
                
                items[self.new_dot].append((dot,(x,y)))
                
        except ValueError:
            print("Please enter valid coordinates.")
    
    def on_touch_down(self, touch):
        
        with self.canvas_widget.canvas:
            Color(0, 1, 0)
            d = 30.
            
            if (touch.y - d / 2) > 580 and (touch.y - d / 2) < 1980:
                dot = Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
                #dot = Line(points = (self.const_x, self.const_y, x, y))
                self.const_x = touch.x
                self.const_y = touch.y
                items.append([])
                self.new_dot += 1
                print(items,'suchara ebanaya 228')
                items[self.new_dot].append((dot,(touch.x,touch.y)))
                print(items)
                # self.new_dot += 1
                #print(self.const_y)
        return super().on_touch_down(touch)
    def _on_press_button_new_pasword(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'First'
    def undod(self, instance):
        
        
        len_small_list = len(items[len(items) - 1]) - 1
        obj = (items[len(items)-1][len_small_list][0])
        #obj = items[1][0][0]
        self.canvas_widget.canvas.remove(obj)
        items[len(items)-1].pop()
        self.const_x, self.const_y = items[len(items)-1][len_small_list - 1][1]
    

class PaswordingApp(MDApp, LenPasword):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'Example'
        self.screen = Builder.load_string(KV)
        threeD_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.threeD_refresh(x),
            } for i in Operations
        ]

        self.threeD_menu = MDDropdownMenu(
            caller=self.screen.button_outside,
            items=threeD_items,
            width_mult=4,
        )
    def build(self):
        
        sm = ScreenManager()
        sm.add_widget(self.screen)
        sm.add_widget(ScreenMain(name='main_screen'))
        sm.add_widget(LenPasword(name='lenpasword'))

        return sm
    def undo(self):
        PaswordingApp.stop(self)
        '''
        len_small_list = len(items[len(items) - 1]) - 1
        #obj = (items[len(items)-1][len_small_list][0])
        obj = items[1][0][0]
        self.canvas_widget.canvas.remove(obj)
        items[len(items)-1].pop()
        self.const_x, self.const_y = items[len(items)-1][len_small_list - 1][1]
        '''
    def save_image(self):
        
        im = Image.open('map_pattern.png')
        draw = ImageDraw.Draw(im)
        for a in items:
            for i in range(len(a) - 1):
                x1 = int(a[i][1][0])
                y1 = int(2400 - a[i][1][1])
                x2 = int(a[i + 1][1][0])
                y2 = int(2400 - a[i + 1][1][1])
                draw.line((x1, y1, x2, y2), fill = 'black', width = 4)#366
        draw.line((270,150,770,150), fill = 'black', width = 4)
        ffont = ImageFont.truetype("arial.TTF", size=10)
        draw.text((1000, 1000), '500')
        im.save('map2.png', quality = 95)
    def threeD_refresh(self, operation):
        #self.save_image()
        
        print(operation)
        operation_list = {'exit': self.undo,'save':self.save_image}
        operation_list[operation]()
        
    
    def launch_menu(self, my_caller):
        #print(my_caller,'my caller')
        self.threeD_menu.caller=my_caller
        self.threeD_menu.open()
        #print('opa')




if __name__ == "__main__":
    PaswordingApp().run()
