'''
    
import kivy


import os.path


from datetime import date

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.button import Button

from kivy.lang import Builder
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.textfield import MDTextField
from kivy.uix.screenmanager import ScreenManager, Screen ,FadeTransition
from kivy.core.window import Window
from kivymd.app import MDApp

from random import randint
import threading as thr
import time

from kivy.uix.scrollview import ScrollView
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.progressbar import MDProgressBar
import os
import csv
'''
from lib.progressbar import MDProgressBar
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
import threading as thr
class Loading():
    def __init__ (self, address, bind):
        self.address = address
        self.bind = bind
    def build(self, instance=None):
        f = FloatLayout(size_hint=(1,1))
        b = Button(size_hint=(1,1),disabled = True,background_normal ='',color=(0,0,0,1), background_color=(0.8,0.8,0.8,0.8))
        b.background_disabled_normal= ''
        b.disabled_color=(0,0,0,0.8)
        f.add_widget(b)
        p = MDProgressBar(pos_hint={'y':0.50})
        p.type= "determinate"
        p.start()
        f.add_widget(p)
        self.f = f
        self.address.add_widget(f)
        self.thr1 =thr.Thread(target = self.treadstart, name=str(self.address)).start()
    def treadstart(self):
        self.bind()
        self.address.remove_widget(self.f)


       
'''
class MainApp(MDApp):

    
    def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.screen = Builder.load_string(KV)
    def calculate(self):
        print("calcalaet")
        time.sleep(2)
        
        self.screen.ids.main.ids.tool_AP.title=str((randint(0,255)))
        self.b.background_normal=''
        self.b.background_color = (randint(0,255)/255,randint(0,255)/255,randint(0,255)/255,1)

        print("finish")
    def closetab(self, instance=None):
        print("cahnge windows")
        

    def build(self):
        self.L= Loading(self.screen.ids.main.ids.F, self.calculate)
        
        self.b = Button(text="hello", size_hint=(0.5,0.5))
        self.b.bind(on_release=self.L.build)
        self.screen.ids.main.ids.F.add_widget(self.b)
        
        
        return self.screen



if __name__ == "__main__":
    MainApp().run()

'''