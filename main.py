import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.icon_definitions import md_icons
####from kivymd.theming import ThemeManager
from kivymd.uix.picker import MDDatePicker
Window.clearcolor = (1, 1, 1, 1)



class MainApp(MDApp):
	##date_selectionneur= ObjectProperty(None)
	
	def show_datepicker(self):
		picker = MDDatePicker(callback = self.got_date)
		picker.open()

	def got_date(self, the_date):
		print(the_date)

	def build(self):
			pass
        


if __name__ == "__main__":
     MainApp().run()
