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

from fonction import *

from kivy.uix.scrollview import ScrollView
from kivymd.uix.menu import MDDropdownMenu


from infopopup import InfoPopup


import os
import csv
Window.clearcolor = (1, 1, 1, 1)


def goodcolor():
	
	return (randint(0,100)/100,randint(0,100)/100,randint(0,100)/100,1)




KV = '''


FloatLayout:
	MDToolbar:
		title: "MDToolbar"
		id: main_t
		pos_hint: {'y':0.9}
		right_action_items: [["dots-vertical", lambda x: app.menu_list.open()]]

	FloatLayout:
		pos_hint: {'y':0}
		id: view													

										

									
								
'''


class SuperTable():
	def __init__ (self, address, **kwargs ):


		self.address = address
		self.table = kwargs.pop('table', [])
		self.font_size = kwargs.pop('font_size', 30)
		self.ligne_size = kwargs.pop('ligne_size', 0.2)
		self.pos_hint = kwargs.pop('pos_hint', {'x':0,'y':0})
		self.size_hint = kwargs.pop('size_hint', (1,1))
		self.color = kwargs.pop('color', (0.8,0.2,0.5,1))
		#print((len(kwargs))
		if len(kwargs) >0:
			raise Exception("[ERROR] argument enter not accpeted")
		self.IP = InfoPopup(self.address, font_size = self.font_size)
	def update_data (self, table ):
		self.table = table
		
	def addPP(self, instance=None):
		self.IP.addP(self)

	def update_t(self):
		ta = updatelist()[0]+updatelist()[1]
		ta = [[i['name']  for i in ta],[i['num']  for i in ta]]
		self.update_data(ta)
		self.build()
	def update_setting (self, **kwargs ):
		
		self.font_size = kwargs.pop('font_size', 30)
		self.ligne_size = kwargs.pop('ligne_size', 0.2)
		self.pos_hint = kwargs.pop('pos_hint', {'x':0,'y':0})
		self.size_hint = kwargs.pop('size_hint', (1,1))
		self.color = kwargs.pop('color', (0,0,0,1))
		#print((kwargs,len(kwargs))
		
		if len(kwargs) >0:
			raise Exception("[ERROR] argument enter not accpeted ")

		
	def build(self):
			self.address.clear_widgets()
			if len(self.table) != 0:
				conv_size = self.ligne_size*(len(self.table[0]))
				
				longueur = len(self.table[0])
				view = ScrollView(pos_hint = self.pos_hint, size_hint= self.size_hint)
				
				base_wi =  FloatLayout(size_hint = (1,conv_size))
				nb_colone = len(self.table)
				coordonne = [[-0.05],[-0.3,0.2],[-0.3,-0.1,0.1]]
				self.get = {}
				for i in range(len(self.table[0])):

					#print((1-i*self.ligne_size, i*self.ligne_size)
					base = FloatLayout(pos_hint={'y':1-i*1/longueur - 1/longueur },size_hint=(1,1/longueur))
					fond = Button(pos_hint={'x': 0, 'y': 0}, size_hint=(1, 1),text ="",background_normal ='',color=(0,0,0,1), background_color=self.color)
					fond.bind(on_release = self.showpopup)
					base.add_widget(fond)
					self.get[fond] = {'name':str(self.table[0][i]),'num':str(self.table[1][i])}
					for z in range(nb_colone):      
						lab = Label(font_size=self.font_size,color=(0,0,0,1),pos_hint={'x': coordonne[nb_colone-1][z], 'y': 0.2}, size_hint=(1, None),text =str(self.table[z][i]))
						base.add_widget(lab)
						
					base_wi.add_widget(base)
				view.add_widget(base_wi)
				self.address.add_widget(view)

	def showpopup(self, instance):
		#print((self.get)
		#print((self.get[instance])
		f  = updatelist()[0]
		found = False
		for i in range(len(f)):
			if f[i]['name'] == self.get[instance]['name'] and f[i]['num'] == self.get[instance]['num'] :
				found = True
				self.IP.show_caller(f[i])
				break
		if found == False:
			m = updatelist()[1]
			for i in range(len(m)):
				if m[i]['name'] == self.get[instance]['name'] and m[i]['num'] == self.get[instance]['num'] :
					found = True
					self.IP.show_caller(m[i])
					break


	def build_edit(self, new_address= None, address_check_count=None ):
		if new_address != None:
			old_adress = self.address
			self.address = new_address
		if address_check_count != None:
			self.address_check_count = address_check_count
		self.ALL_Check_Status = [False]*len(self.table[0])
		
		self.address.clear_widgets()
		self.ids_table_edit ={}
		if len(self.table) != 0:

			conv_size = self.ligne_size*(len(self.table[0]))
			longueur = len(self.table[0])
			view = ScrollView(pos_hint = self.pos_hint, size_hint= self.size_hint)
			base_wi =  FloatLayout(size_hint = (1,conv_size))
			nb_colone = len(self.table)
			coordonne = [[-0.05],[-0.3,0.2],[-0.3,-0.1,0.1]]

			for i in range(len(self.table[0])):
				#print((1-i*self.ligne_size, i*self.ligne_size)
				base = FloatLayout(pos_hint={'y':1-i*1/longueur - 1/longueur },size_hint=(1,1/longueur))
				fond = Button(pos_hint={'x': 0, 'y': 0}, size_hint=(1, 1),text ="",background_normal ='',color=(0,0,0,1), background_color=self.color)
				fond.bind(on_release=self.checker)
				check = MDCheckbox(disabled = True,pos_hint={'x': 0.8, 'y': 0.2}, size_hint=(0, None))
				check.background_disabled_normal= ''
				check.disabled_color=(0,0,1,1)
				base.add_widget(fond)
				base.add_widget(check)
				for z in range(nb_colone):      
					lab = Label(font_size=self.font_size,color=(0,0,0,1),pos_hint={'x': coordonne[nb_colone-1][z], 'y': 0.2}, size_hint=(1, None),text =str(self.table[z][i]))
					base.add_widget(lab)
				self.ids_table_edit[str(i)+'float'] = base
				self.ids_table_edit[str(i)+'check'] = check
				self.ids_table_edit[fond] = str(i)

				base_wi.add_widget(base)
			view.add_widget(base_wi)
			self.address.add_widget(view)
		if new_address != None:
			 
			self.address = old_adress

	        
		
	def checker(self, instance=None):
		instance.background_color= self.color
		
		if self.ids_table_edit[self.ids_table_edit[instance]+ 'check'].active == False:
			self.ids_table_edit[self.ids_table_edit[instance]+ 'check'].active = True
			self.ALL_Check_Status[int(self.ids_table_edit[instance])] = True
		else:
			self.ids_table_edit[self.ids_table_edit[instance]+ 'check'].active = False
			self.ALL_Check_Status[int(self.ids_table_edit[instance])] = False
		if self.address_check_count !=None:
			self.address_check_count.title= str(self.getCount())+" selected"

	def getCheckerRes(self):
		return self.ALL_Check_Status
	def getCount(self):
		count = 0
		for i in self.ALL_Check_Status:
			if i == True:
				count+=1
		return count




	def Deleter(self):
		new =[[] for i in range(len(self.table))]

		for i  in range(len(self.table[0])) :
			for z in range(len(self.table)):
				#print((self.getCheckerRes()[i], i,self.getCheckerRes() )
				if self.getCheckerRes()[i]  == False:

					new[z].append(self.table[z][i]) 
		self.update_data(new)
	


'''

class MainApp(MDApp):

	
	def __init__(self, **kwargs):
			super().__init__(**kwargs)
			self.screen = Builder.load_string(KV)
			
			ta = updatelist()[0]+updatelist()[1]
			ta = [[i['name']  for i in ta],[i['num']  for i in ta]]

			
			self.table = SuperTable( address= self.screen.ids.view, table= ta, font_size= 15, ligne_size= 0.5,
				pos_hint = {'x': 0.1, 'y': 0.1}, size_hint = (0.8,0.8), color=(0.8,0.8,0.8,1))

			self.table.build()
			



			self.menu_list = MDDropdownMenu(
	                caller=self.screen.ids.main_t,
	                items=[{"text":"update"},{"text":"edit"},{"text":"checkall"}, {"text": "delete"}],
	                position="auto",
	                callback=self.set_item_list_pg,
	                width_mult=4,
	            	)

	def callback_table_pg_list(self):
		self.menu_list.show()
	def set_item_list_pg(self, instance):
		#print((self, instance, instance.text)
		if instance.text == 'update':
			self.table.update_data([['quatre','cinq','six']])
			self.table.build()
		elif 'checkall' == instance.text:
			#print((self.table.getCheckerRes())
		elif 'edit' == instance.text:
			self.table.build_edit()
		elif 'delete' == instance.text:
			self.table.Deleter()

			self.table.build()


	def build(self):
		
		return self.screen



if __name__ == "__main__":
	MainApp().run()

'''