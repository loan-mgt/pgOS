
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
import copy

class Popups( ):
    
	def __init__(self, address, **kwargs):
		
		self.address = address
		self.widget = kwargs.pop('widget', [])
		#self.UOC = kwargs.pop('UOC',None)

		self.f = None
		
	
	def show(self, instance=''):
		if self.f == None:
			f = FloatLayout()
			self.f= f
			b1=Button(disabled = False, pos_hint={'x':-0.1,'y':-0.1}, size_hint=(1.2,1.2),background_color=(0,0,0,0.5) )#,background_normal =''
			b1.bind(on_release=self.close)
			f.add_widget(b1)
			b2=Button(disabled = True, pos_hint={'x':0.1,'y':0.5}, size_hint=(0.8,0.4),background_normal ='',background_color=(1,1,1,1) )
			b2.background_disabled_normal= ''
			b2.disabled_color=(1,1,1,1)
			f.add_widget(b2)
			fond = Button(pos_hint={'x': 0.7, 'y': 0.5}, size_hint=(0.2, 0.05),text ="FERMER",background_normal ='',color=(0,0,0,1), background_color=(1,1,1,1))
			fond.bind(on_release=self.close)
			f.add_widget( fond)
			
			
			for i in self.widget:
				ii = (i)

				f.add_widget(ii)
			self.f= f
		self.address.add_widget(self.f)

	def close(self, instance=None):
		self.address.remove_widget(self.f)
		#self.UOC(self)
		#table(self)

