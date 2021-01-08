import kivy


import os.path
from fonction import *

from datetime import date

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.button import Button

from kivy.lang import Builder
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDIconButton
from kivy.uix.screenmanager import ScreenManager, Screen ,FadeTransition
from kivy.core.window import Window
from kivymd.app import MDApp

import threading as thr


from random import randint


from kivy.uix.scrollview import ScrollView
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.menu import MDDropdownMenu

import os
import csv
Window.clearcolor = (1, 1, 1, 1)


KV = '''


FloatLayout:
	id: fll


										
								
'''


class InfoPopup(FloatLayout):
	def __init__(self, address,  **kwargs):
		self.ad = address
		self.font_size = kwargs.pop('font_size', 30)
		self.dic = kwargs.pop('dic', None)
		self.ffList = kwargs.pop('ffList', None)
		self.fmList = kwargs.pop('fmList', None)
		self.root = kwargs.pop('root', None)
		self.origine = kwargs.pop('origine', None)
		if self.ffList == None:
			self.ffList = updatelist()[0]
			self.fmList = updatelist()[1]	

		
		if len(kwargs) >0:
			raise Exception("[ERROR] argument enter not accpeted")

	def show(self, source):
		self.source = source
		#print("source ",source)
		self.f = FloatLayout()
		back = Button(disabled = True,pos_hint={'x': 0, 'y': 0}, size_hint=(1, 1),text ="",background_normal ='', background_color=(0,0,0,0.5))
		back.background_disabled_normal= ''
		back.disabled_color=(0,0,0,0.5)
		layer_w = Button(disabled = True,pos_hint={'x': 0.1, 'y': 0.1}, size_hint=(0.8, 0.8),text ="",background_normal ='', background_color=(1,1,1,1))
		layer_w.background_disabled_normal= ''
		layer_w.disabled_color=(0,0,1,1)

		Parents =  Label(text='Parents',font_size=self.font_size+1, pos_hint= {'center_x': .2, 'center_y': .85},color=(0,0,0,1) )
		
		PM = Button(pos_hint={'x': 0.2, 'y': 0.5}, size_hint=(0.3, 0.3),text ="",background_normal ='', background_color=(0,0,1,0.6))
		PM.bind( on_release =self.show_caller_inner)
		

		PF = Button(pos_hint={'x': 0.5, 'y': 0.5}, size_hint=(0.3, 0.3),text ="",background_normal ='', background_color=(1,0,0,0.6))
		PF.bind( on_release= self.show_caller_inner)


		fermer = Button(pos_hint={'x': 0.75, 'y': 0.8}, size_hint=(0.1, 0.1),text ="FERMER",background_normal ='',color=(0,0,0,1), background_color=(1,1,1,0))
		fermer.bind(on_release=self.fermer)


		Genre_data = 'Femmelle'

		for i in range(len(self.fmList)):
				#print(self.fmList[i]['name'] ,'vs', self.source['name'] ,'and', self.fmList[i]['num'] ,'vs', self.source['num'])
				if self.fmList[i]['name'] == self.source['name'] and self.fmList[i]['num'] == self.source['num']:
					Genre_data = 'Mâle'
					break




		Nom = Label(text=source['name'],font_size=self.font_size, pos_hint= {'center_x': .4, 'center_y': .45},color=(0,0,0,1) )
		Num =  Label(text=source['num'],font_size=self.font_size-1, pos_hint= {'center_x': .35, 'center_y': .4},color=(0,0,0,1) )
		Genre =  Label(text=Genre_data,font_size=self.font_size-1, pos_hint= {'center_x': .7, 'center_y': .4},color=(0,0,0,1) )
		Nom_i = Label(text='Nom',font_size=self.font_size-1, pos_hint= {'center_x': .15, 'center_y': .45},color=(0,0,0,0.8) )
		Num_i =  Label(text='Num',font_size=self.font_size-1, pos_hint= {'center_x': .15, 'center_y': .4},color=(0,0,0,0.8) )
		Genre_i =  Label(text='Genre',font_size=self.font_size-1, pos_hint= {'center_x': .55, 'center_y': .4},color=(0,0,0,0.8) )
		Nb_petits = Label(text='Total petits',font_size=self.font_size, pos_hint= {'center_x': .25, 'center_y': .3},color=(0,0,0,0.8) )
		Nb_petits_ans = Label(text='Petits par ans',font_size=self.font_size, pos_hint= {'center_x': .5, 'center_y': .3},color=(0,0,0,0.8) )

		
		modifier = Button(pos_hint={'x': 0.55, 'y': 0.8},font_size = self.font_size, size_hint=(0.1, 0.1),text ="MODIFIER",background_normal ='',color=(0,0,0,1), background_color=(1,1,1,0))
		modifier.bind(on_release=self.edit)
		
		self.f.add_widget(back)
		self.f.add_widget(layer_w)
		self.Button_ID = {'M':PM, 'F':PF}
		self.f.add_widget(PM)
		self.f.add_widget(PF)
		if 'PM' in source and source['PM'] != 'Aucun':
			Nom_PM = Label(text=str(source['PM']['name']),font_size=self.font_size, pos_hint= {'center_x': .3, 'center_y': .7},color=(0,0,0,1) )
			Num_PM =  Label(text=str(source['PM']['num']),font_size=self.font_size-1, pos_hint= {'center_x': .35, 'center_y': .6},color=(0,0,0,1) )
		
			self.f.add_widget(Nom_PM)
			self.f.add_widget(Num_PM)
		else:
			Nom_PM = Label(text='Aucun',font_size=self.font_size, pos_hint= {'center_x': .3, 'center_y': .7},color=(0,0,0,1) )
			Num_PM =  Label(text='',font_size=self.font_size-1, pos_hint= {'center_x': .3, 'center_y': .6},color=(0,0,0,1) )
		
			self.f.add_widget(Nom_PM)
			self.f.add_widget(Num_PM)

		if 'PF' in source  and source['PF'] != 'Aucun':
			Nom_PF = Label(text=str(source['PF']['name']),font_size=self.font_size, pos_hint= {'center_x': .6, 'center_y': .7},color=(0,0,0,1) )
			Num_PF =  Label(text=str(source['PF']['num']),font_size=self.font_size-1, pos_hint= {'center_x': .65, 'center_y': .6},color=(0,0,0,1) )
		
			self.f.add_widget(Nom_PF)
			self.f.add_widget(Num_PF)
		else:
			Nom_PF = Label(text='Aucun',font_size=self.font_size, pos_hint= {'center_x': .6, 'center_y': .7},color=(0,0,0,1) )
			Num_PF =  Label(text='',font_size=self.font_size-1, pos_hint= {'center_x': .6, 'center_y': .55},color=(0,0,0,1) )
		
			self.f.add_widget(Nom_PF)
			self.f.add_widget(Num_PF)

		
		if 'NBP' in source  and source['NBP'] != []:
			#print("scollview", len(source['NBP']), 'size', len(source['NBP'])*0.35 )
			s = ScrollView(size_hint =(0.5,0.1) ,do_scroll_y=False,do_scroll_x=True, pos_hint=  {'center_x': .6, 'center_y': .2})
			sizex = 0.25 
			g = FloatLayout( size_hint=(len(source['NBP'])*0.35,1))
			COUNT = 0
			for i in range(len(source['NBP'])):
				COUNT += int(source['NBP'][i]['nombre'])
				print(sizex*i,sizex)
				g.add_widget(Button(background_normal='',background_color=(0,0,0,0.4),text=str(source['NBP'][i]['anne']) +'\n'+str(source['NBP'][i]['nombre']), color =(0,0,0,1),pos_hint = {'x':1/len(self.source['NBP'])*i}, size_hint =(1/len(source['NBP']),1)))
			s.add_widget(g)
			self.f.add_widget(s)
			total = Label(text=str(COUNT),font_size=self.font_size-5, pos_hint= {'center_x': .2, 'center_y': .2},color=(0,0,0,1) )
			self.f.add_widget(total)
		self.f.add_widget(Parents)
		self.f.add_widget(Nb_petits)
		self.f.add_widget(Nb_petits_ans)
		self.f.add_widget(fermer)
		self.f.add_widget(modifier)
		self.f.add_widget(Nom)
		self.f.add_widget(Num)
		self.f.add_widget(Genre)
		self.f.add_widget(Nom_i)
		self.f.add_widget(Num_i)
		self.f.add_widget(Genre_i)

		self.ad.add_widget(self.f)

	def edit(self, instance=None):
		
		self.fermer()
		source = self.source
		self.source_old = self.source

		#print("source ",source)
		self.f = FloatLayout()
		back = Button(disabled = True,pos_hint={'x': 0, 'y': 0}, size_hint=(1, 1),text ="",background_normal ='', background_color=(0,0,0,0.5))
		back.background_disabled_normal= ''
		back.disabled_color=(0,0,0,0.5)
		layer_w = Button(disabled = True,pos_hint={'x': 0.1, 'y': 0.1}, size_hint=(0.8, 0.8),text ="",background_normal ='', background_color=(1,1,1,1))
		layer_w.background_disabled_normal= ''
		layer_w.disabled_color=(0,0,1,1)

		Parents =  Label(text='Parents',font_size=self.font_size+1, pos_hint= {'center_x': .2, 'center_y': .85},color=(0,0,0,1) )
		
		PM = Button(pos_hint={'x': 0.2, 'y': 0.5}, size_hint=(0.3, 0.3),text ="",background_normal ='', background_color=(0,0,1,0.6))
		
		

		PF = Button(pos_hint={'x': 0.5, 'y': 0.5}, size_hint=(0.3, 0.3),text ="",background_normal ='', background_color=(1,0,0,0.6))
		


		fermer = Button(pos_hint={'x': 0.75, 'y': 0.8}, size_hint=(0.1, 0.1),text ="FERMER",background_normal ='',color=(0,0,0,1), background_color=(1,1,1,0))
		fermer.bind(on_release=self.fermer)
		Genre_data = 'Femmelle'

		for i in range(len(self.fmList)):
				#print(self.fmList[i]['name'] ,'vs', self.source['name'] ,'and', self.fmList[i]['num'] ,'vs', self.source['num'])
				if self.fmList[i]['name'] == self.source['name'] and self.fmList[i]['num'] == self.source['num']:
					Genre_data = 'Mâle'
					break


		self.genre_old = Genre_data

		self.Nom = MDTextField(text=source['name'],font_size=self.font_size, size_hint=(0.4,0.1),pos_hint= {'center_x': .4, 'center_y': .45})
		self.Num =  MDTextField(text=source['num'],font_size=self.font_size,size_hint=(0.32,0.1), pos_hint= {'center_x': .36, 'center_y': .4} )
		
		Genre = MDDropDownItem(font_size=self.font_size-3, pos_hint= {'center_x': .76, 'center_y': .405})
		Genre.text=Genre_data

		self.Genre =Genre

		self.menuG = MDDropdownMenu(
			caller=Genre,
			items=[{'text':'Femmelle'},{'text':'Mâle'}],
			position="auto",
			width_mult=4,
			callback=self.GS,
			
		)
		Genre.bind(on_release=self.menuG_open)

		Nom_i = Label(text='Nom',font_size=self.font_size-1, pos_hint= {'center_x': .15, 'center_y': .45},color=(0,0,0,0.8) )
		Num_i =  Label(text='Num',font_size=self.font_size-1, pos_hint= {'center_x': .15, 'center_y': .4},color=(0,0,0,0.8) )
		Genre_i =  Label(text='Genre',font_size=self.font_size-1, pos_hint= {'center_x': .59, 'center_y': .4},color=(0,0,0,0.8) )
		Nb_petits = Label(text='Total petits',font_size=self.font_size, pos_hint= {'center_x': .25, 'center_y': .35},color=(0,0,0,0.8) )
		Nb_petits_ans = Label(text='Petits par ans',font_size=self.font_size, pos_hint= {'center_x': .5, 'center_y': .35},color=(0,0,0,0.8) )

		
		modifier = Button(pos_hint={'x': 0.55, 'y': 0.8},font_size = self.font_size, size_hint=(0.1, 0.1),text ="VALIDER",background_normal ='',color=(0,0,0,1), background_color=(1,1,1,0))
		modifier.bind(on_release=self.edit_valider)
		
		self.f.add_widget(back)
		self.f.add_widget(layer_w)
		self.Button_ID = {'M':PM, 'F':PF}
		self.f.add_widget(PM)
		self.f.add_widget(PF)



		DM = MDDropDownItem(text='',pos_hint= {'center_x': 0.3, 'center_y': 0.6})
		DM.text='Aucun'
		
		DM.bind(on_release = self.DM_OPEN)

		#print('drpo male',[{'text':str(self.fmList[i]['name'])+'\n'+str(self.fmList[i]['num'])} for i in range(len(self.fmList))])
		item = [{'text':str(self.fmList[i]['name'])+'\n'+str(self.fmList[i]['num'])} for i in range(len(self.fmList))]
		item.append({'text':'Aucun'})
		self.menuM = MDDropdownMenu(
			caller=DM,
			items=item,
			position="auto",
			width_mult=4,
			callback=self.DM_SEL,
			
		)

		self.DM = DM
		DF = MDDropDownItem(text='',pos_hint= {'center_x': 0.6, 'center_y': 0.6})
		DF.text='Aucun'
		
		
		DF.bind(on_release = self.DF_OPEN)
		self.DF = DF
		#print([{'text':str(self.ffList[i]['name'])+'\n'+str(self.ffList[i]['num'])} for i in range(len(self.ffList))])
		item = [{'text':str(self.ffList[i]['name'])+'\n'+str(self.ffList[i]['num'])} for i in range(len(self.ffList))]
		item.append({'text':'Aucun'})
		self.menuF = MDDropdownMenu(
			caller=DF,
			items=item,
			position="auto",
			width_mult=4,
			callback=self.DF_SEL,
			
		)



		self.anne = MDTextField(size_hint=(0.2,0.1),font_size=self.font_size-2, pos_hint= {'center_x': .65, 'center_y': .29} )
		self.anne.hint_text='Année'
		self.nb =  MDTextField(size_hint=(0.2,0.1),font_size=self.font_size-2, pos_hint= {'center_x': .3, 'center_y': .29} )
		self.nb.hint_text='Nombre'
		add  = MDIconButton(icon= "plus",pos_hint= {"center_x": .875, "center_y": .3})
		add.bind(on_release=self.add_NBP)
		

		self.f.add_widget(self.anne)
		self.f.add_widget(self.nb)
		self.f.add_widget(add)




		if 'PM' in source and source['PM'] != 'Aucun':
			DM.text=str(source['PM']['name'])+'\n'+str(source['PM']['num'])
			
		else:
			DM.text=str('Aucun')
			

		if 'PF' in source  and source['PF'] != 'Aucun':
			DF.text=str(source['PF']['name'])+'\n'+str(source['PF']['num'])
		else:
			DF.text=str('Aucun')

		s = ScrollView(size_hint =(0.5,0.1) ,do_scroll_y=False,do_scroll_x=True, pos_hint=  {'center_x': .6, 'center_y': .2})
		self.s =s
		self.total = Label(text=str(0),font_size=self.font_size-5, pos_hint= {'center_x': .2, 'center_y': .2},color=(0,0,0,1) )
		self.f.add_widget(self.total)
		#if 'NBP' in source  and source['NBP'] != []:
		self.s.clear_widgets()
		if 'NBP' in source  :
			#print("scollview", len(source['NBP']), 'size', len(source['NBP'])*0.35 )
			sizex = 0.25 
			g = FloatLayout( size_hint=(len(source['NBP'])*0.35,1))
			COUNT = 0
			self.cross = {}
			for i in range(len(source['NBP'])):
				COUNT += int(source['NBP'][i]['nombre'])
				#print(sizex*i,sizex)

				y = MDIconButton(icon= 'close-outline', pos_hint = {'x':1/len(self.source['NBP'])*i+0.15, 'y':-0.15}, size_hint =(1/len(source['NBP']),1) )
				y.bind(on_release=  self.delete_date)

				self.cross[y] = i
				g.add_widget(Button(background_normal='',background_color=(0,0,0,0.4),text=str(source['NBP'][i]['anne']) +'\n'+str(source['NBP'][i]['nombre']), color =(0,0,0,1),pos_hint = {'x':1/len(self.source['NBP'])*i}, size_hint =(1/len(source['NBP']),1)))
				g.add_widget(y)
			s.add_widget(g)
			
			
			self.total.text=str(COUNT)
			#self.f.add_widget(self.total)

		self.f.add_widget(s)












		

		self.f.add_widget(Parents)
		self.f.add_widget(Nb_petits)
		self.f.add_widget(Nb_petits_ans)
		self.f.add_widget(fermer)
		self.f.add_widget(modifier)
		self.f.add_widget(self.Nom)
		self.f.add_widget(self.Num)
		self.f.add_widget(Genre)
		self.f.add_widget(Nom_i)
		self.f.add_widget(Num_i)
		self.f.add_widget(Genre_i)

		self.f.add_widget(DM)
		self.f.add_widget(DF)

		self.ad.add_widget(self.f)


	def addP(self, root=None):
		self.up = root
		
		
		source = {'name':'','num':'','PF': 'Aucun', 'PM': 'Aucun', 'NBP':[] }
		self.source =source
		self.source_old = self.source

		#print("source ",source)
		self.f = FloatLayout()
		back = Button(disabled = True,pos_hint={'x': 0, 'y': 0}, size_hint=(1, 1),text ="",background_normal ='', background_color=(0,0,0,0.5))
		back.background_disabled_normal= ''
		back.disabled_color=(0,0,0,0.5)
		layer_w = Button(disabled = True,pos_hint={'x': 0.1, 'y': 0.1}, size_hint=(0.8, 0.8),text ="",background_normal ='', background_color=(1,1,1,1))
		layer_w.background_disabled_normal= ''
		layer_w.disabled_color=(0,0,1,1)

		Parents =  Label(text='Parents',font_size=self.font_size+1, pos_hint= {'center_x': .2, 'center_y': .85},color=(0,0,0,1) )
		
		PM = Button(pos_hint={'x': 0.2, 'y': 0.5}, size_hint=(0.3, 0.3),text ="",background_normal ='', background_color=(0,0,1,0.6))
		
		

		PF = Button(pos_hint={'x': 0.5, 'y': 0.5}, size_hint=(0.3, 0.3),text ="",background_normal ='', background_color=(1,0,0,0.6))
		


		fermer = Button(pos_hint={'x': 0.75, 'y': 0.8}, size_hint=(0.1, 0.1),text ="FERMER",background_normal ='',color=(0,0,0,1), background_color=(1,1,1,0))
		fermer.bind(on_release=self.fermer)
		Genre_data = 'Femmelle'

		for i in range(len(self.fmList)):
				#print(self.fmList[i]['name'] ,'vs', self.source['name'] ,'and', self.fmList[i]['num'] ,'vs', self.source['num'])
				if self.fmList[i]['name'] == self.source['name'] and self.fmList[i]['num'] == self.source['num']:
					Genre_data = 'Mâle'
					break


		self.genre_old = Genre_data

		self.Nom = MDTextField(text=source['name'],font_size=self.font_size, size_hint=(0.4,0.1),pos_hint= {'center_x': .4, 'center_y': .45})
		self.Num =  MDTextField(text=source['num'],font_size=self.font_size,size_hint=(0.32,0.1), pos_hint= {'center_x': .36, 'center_y': .4} )
		
		Genre = MDDropDownItem(font_size=self.font_size-3, pos_hint= {'center_x': .76, 'center_y': .405})
		Genre.text=Genre_data

		self.Genre =Genre

		self.menuG = MDDropdownMenu(
			caller=Genre,
			items=[{'text':'Femmelle'},{'text':'Mâle'}],
			position="auto",
			width_mult=4,
			callback=self.GS,
			
		)
		Genre.bind(on_release=self.menuG_open)

		Nom_i = Label(text='Nom',font_size=self.font_size-1, pos_hint= {'center_x': .15, 'center_y': .45},color=(0,0,0,0.8) )
		Num_i =  Label(text='Num',font_size=self.font_size-1, pos_hint= {'center_x': .15, 'center_y': .4},color=(0,0,0,0.8) )
		Genre_i =  Label(text='Genre',font_size=self.font_size-1, pos_hint= {'center_x': .59, 'center_y': .4},color=(0,0,0,0.8) )
		Nb_petits = Label(text='Total petits',font_size=self.font_size, pos_hint= {'center_x': .25, 'center_y': .35},color=(0,0,0,0.8) )
		Nb_petits_ans = Label(text='Petits par ans',font_size=self.font_size, pos_hint= {'center_x': .5, 'center_y': .35},color=(0,0,0,0.8) )

		
		modifier = Button(pos_hint={'x': 0.55, 'y': 0.8},font_size = self.font_size, size_hint=(0.1, 0.1),text ="VALIDER",background_normal ='',color=(0,0,0,1), background_color=(1,1,1,0))
		modifier.bind(on_release=self.new_valider)
		
		self.f.add_widget(back)
		self.f.add_widget(layer_w)
		self.Button_ID = {'M':PM, 'F':PF}
		self.f.add_widget(PM)
		self.f.add_widget(PF)



		DM = MDDropDownItem(text='',pos_hint= {'center_x': 0.3, 'center_y': 0.6})
		DM.text='Aucun'
		
		DM.bind(on_release = self.DM_OPEN)

		#print('drpo male',[{'text':str(self.fmList[i]['name'])+'\n'+str(self.fmList[i]['num'])} for i in range(len(self.fmList))])
		item = [{'text':str(self.fmList[i]['name'])+'\n'+str(self.fmList[i]['num'])} for i in range(len(self.fmList))]
		item.append({'text':'Aucun'})
		self.menuM = MDDropdownMenu(
			caller=DM,
			items=item,
			position="auto",
			width_mult=4,
			callback=self.DM_SEL,
			
		)

		self.DM = DM
		DF = MDDropDownItem(text='',pos_hint= {'center_x': 0.6, 'center_y': 0.6})
		DF.text='Aucun'
		
		
		DF.bind(on_release = self.DF_OPEN)
		self.DF = DF
		#print([{'text':str(self.ffList[i]['name'])+'\n'+str(self.ffList[i]['num'])} for i in range(len(self.ffList))])
		item = [{'text':str(self.ffList[i]['name'])+'\n'+str(self.ffList[i]['num'])} for i in range(len(self.ffList))]
		item.append({'text':'Aucun'})
		self.menuF = MDDropdownMenu(
			caller=DF,
			items=item,
			position="auto",
			width_mult=4,
			callback=self.DF_SEL,
			
		)



		self.anne = MDTextField(size_hint=(0.2,0.1),font_size=self.font_size-2, pos_hint= {'center_x': .65, 'center_y': .29} )
		self.anne.hint_text='Année'
		self.nb =  MDTextField(size_hint=(0.2,0.1),font_size=self.font_size-2, pos_hint= {'center_x': .3, 'center_y': .29} )
		self.nb.hint_text='Nombre'
		add  = MDIconButton(icon= "plus",pos_hint= {"center_x": .875, "center_y": .3})
		add.bind(on_release=self.add_NBP)
		

		self.f.add_widget(self.anne)
		self.f.add_widget(self.nb)
		self.f.add_widget(add)




		if 'PM' in source and source['PM'] != 'Aucun':
			DM.text=str(source['PM']['name'])+'\n'+str(source['PM']['num'])
			
		else:
			DM.text=str('Aucun')
			

		if 'PF' in source  and source['PF'] != 'Aucun':
			DF.text=str(source['PF']['name'])+'\n'+str(source['PF']['num'])
		else:
			DF.text=str('Aucun')

		s = ScrollView(size_hint =(0.5,0.1) ,do_scroll_y=False,do_scroll_x=True, pos_hint=  {'center_x': .6, 'center_y': .2})
		self.s =s
		self.total = Label(text=str(0),font_size=self.font_size-5, pos_hint= {'center_x': .2, 'center_y': .2},color=(0,0,0,1) )
		self.f.add_widget(self.total)
		#if 'NBP' in source  and source['NBP'] != []:
		self.s.clear_widgets()
		if 'NBP' in source  :
			#print("scollview", len(source['NBP']), 'size', len(source['NBP'])*0.35 )
			sizex = 0.25 
			g = FloatLayout( size_hint=(len(source['NBP'])*0.35,1))
			COUNT = 0
			self.cross = {}
			for i in range(len(source['NBP'])):
				COUNT += int(source['NBP'][i]['nombre'])
				#print(sizex*i,sizex)

				y = MDIconButton(icon= 'close-outline', pos_hint = {'x':1/len(self.source['NBP'])*i+0.15, 'y':-0.15}, size_hint =(1/len(source['NBP']),1) )
				y.bind(on_release=  self.delete_date)

				self.cross[y] = i
				g.add_widget(Button(background_normal='',background_color=(0,0,0,0.4),text=str(source['NBP'][i]['anne']) +'\n'+str(source['NBP'][i]['nombre']), color =(0,0,0,1),pos_hint = {'x':1/len(self.source['NBP'])*i}, size_hint =(1/len(source['NBP']),1)))
				g.add_widget(y)
			s.add_widget(g)
			
			
			self.total.text=str(COUNT)
			#self.f.add_widget(self.total)

		self.f.add_widget(s)












		

		self.f.add_widget(Parents)
		self.f.add_widget(Nb_petits)
		self.f.add_widget(Nb_petits_ans)
		self.f.add_widget(fermer)
		self.f.add_widget(modifier)
		self.f.add_widget(self.Nom)
		self.f.add_widget(self.Num)
		self.f.add_widget(Genre)
		self.f.add_widget(Nom_i)
		self.f.add_widget(Num_i)
		self.f.add_widget(Genre_i)

		self.f.add_widget(DM)
		self.f.add_widget(DF)

		self.ad.add_widget(self.f)

	def delete_date(self, instance):
		#print(self.cross[instance])
		self.source['NBP'].pop(self.cross[instance])
		s =self.s
		s.clear_widgets()
		sizex = 0.25 
		#print(len(self.source['NBP']),len(self.source['NBP'])*0.35, )
		g = FloatLayout( size_hint=(len(self.source['NBP'])*0.35,1))
		COUNT =0
		self.cross = {}
		for i in range(len(self.source['NBP'])):
			COUNT += int(self.source['NBP'][i]['nombre'])
			#print(sizex*i,sizex)
			y = MDIconButton(icon= 'close-outline', pos_hint = {'x':1/len(self.source['NBP'])*i+0.2*(1/len(self.source['NBP'])), 'y':-0.15}, size_hint =(1/len(self.source['NBP']),1) )
			y.bind(on_release=  self.delete_date)

			self.cross[y] = i
			
	
			g.add_widget(Button(background_normal='',background_color=(0,0,0,0.4),text=str(self.source['NBP'][i]['anne']) +'\n'+str(self.source['NBP'][i]['nombre']), color =(0,0,0,1),pos_hint = {'x':1/len(self.source['NBP'])*i}, size_hint =(1/len(self.source['NBP']),1)))
			g.add_widget(y)

		s.add_widget(g)
		#self.s =s
		
		self.total.text = str(COUNT)
	def add_NBP(self, instance=None):
		print(self.anne.text)
		chiffre = True
		if self.anne.text != '' and self.nb.text != '':


			try:
				x = int(self.anne.text)
				x = int(self.nb.text)
				
			except Exception as e:
				print(e, 'pas chiffre')
				self.origine.Snac("Assurez-vous d'entrer des chiffres")
				chiffre = False
			if chiffre == True:
				found = False
				if 'NBP' not in self.source:
					self.source['NBP'] =[]
				for i in range(len(self.source['NBP'])):
					#print('NBP' in self.source, int(self.anne.text) == self.source['NBP'][i]['anne'])
					if 'NBP' in self.source and int(self.anne.text) == self.source['NBP'][i]['anne']:
						self.source['NBP'][i]['nombre'] += int(self.nb.text)
						found = True
						break
				if 'NBP' in self.source and found == False:
					self.source['NBP'].append({'anne':int(self.anne.text),'nombre':int(self.nb.text)})
				elif found == False: 
					self.source['NBP']=[{'anne':int(self.anne.text),'nombre':int(self.nb.text)}]
				
				s =self.s
				s.clear_widgets()
				sizex = 0.25 
				#print(len(self.source['NBP']),len(self.source['NBP'])*0.35, )
				g = FloatLayout( size_hint=(len(self.source['NBP'])*0.35,1))
				COUNT =0
				self.cross = {}
				for i in range(len(self.source['NBP'])):
					COUNT += int(self.source['NBP'][i]['nombre'])
					#print(sizex*i,sizex)
					y = MDIconButton(icon= 'close-outline', pos_hint = {'x':1/len(self.source['NBP'])*i+0.2*(1/len(self.source['NBP'])), 'y':-0.15}, size_hint =(1/len(self.source['NBP']),1) )
					y.bind(on_release=  self.delete_date)

					self.cross[y] = i
					
			
					g.add_widget(Button(background_normal='',background_color=(0,0,0,0.4),text=str(self.source['NBP'][i]['anne']) +'\n'+str(self.source['NBP'][i]['nombre']), color =(0,0,0,1),pos_hint = {'x':1/len(self.source['NBP'])*i}, size_hint =(1/len(self.source['NBP']),1)))
					g.add_widget(y)

				s.add_widget(g)
				#self.s =s
				
				self.total.text = str(COUNT)
		else:
			self.origine.Snac("Veuillez remplir les champs")
		
	def new_valider(self, instance=None):
		

		if self.Genre.text == 'Mâle':
			M_F = 'M'
		else:
			M_F = 'F'
		name = str(self.Nom.text)
		num = str(self.Num.text)
		PM = 'Aucun'
		PF = 'Aucun'
		for i in range(len(self.fmList)):
			if self.fmList[i]['name']+'\n'+self.fmList[i]['num'] == self.DM.text:
				PM = {'name':self.fmList[i]['name'], 'num':self.fmList[i]['num']}
				break
		for i in range(len(self.ffList)):
			if self.ffList[i]['name']+'\n'+self.ffList[i]['num'] == self.DF.text:
				PF = {'name':self.ffList[i]['name'], 'num':self.ffList[i]['num']}
				break
		if 'NBP' in self.source:
			NBP = self.source['NBP']
		else: 
			NBP =[]
		print('new',(M_F, name, num, PF, PM, NBP))
		list_write(M_F, name, num, PF, PM, NBP)
		self.fermer()
		self.ffList = updatelist()[0]
		self.fmList = updatelist()[1]
		self.up.update_t()
		thr.Thread(target = self.origine.up_drop_down).start()

	def edit_valider(self, instance=None):
		#print('old', self.genre_old, self.source_old)
		#print('new', self.Nom.text , self.Num.text, self.DF.text, self.DM.text, self.Genre.text)
		if self.genre_old == 'Mâle':
			M_F = 'M'
		else:
			M_F = 'F'
		name = self.source_old['name']
		num = self.source_old['num']
		list_remove(M_F, name, num)

		if self.Genre.text == 'Mâle':
			M_F = 'M'
		else:
			M_F = 'F'
		name = str(self.Nom.text)
		num = str(self.Num.text)
		PM = 'Aucun'
		PF = 'Aucun'
		for i in range(len(self.fmList)):
			if self.fmList[i]['name']+'\n'+self.fmList[i]['num'] == self.DM.text:
				PM = {'name':self.fmList[i]['name'], 'num':self.fmList[i]['num']}
				break
		for i in range(len(self.ffList)):
			if self.ffList[i]['name']+'\n'+self.ffList[i]['num'] == self.DF.text:
				PF = {'name':self.ffList[i]['name'], 'num':self.ffList[i]['num']}
				break
		if 'NBP' in self.source:
			NBP = self.source['NBP']
		else: 
			NBP =[]
		print('new',(M_F, name, num, PF, PM, NBP))
		list_write(M_F, name, num, PF, PM, NBP)
		self.fermer()
		self.ffList = updatelist()[0]
		self.fmList = updatelist()[1]
		self.root.update_t()
		thr.Thread(target = self.origine.up_drop_down).start()
		#self.ad.ST.build()

	def DM_OPEN(self, instance):
		self.menuM.open()

	def DF_OPEN(self, instance):
		
		self.menuF.open()
	def DF_SEL(self, instance):
		
		self.DF.text = instance.text
		self.menuF.dismiss()

	def DM_SEL(self, instance):
		self.DM.text = instance.text
		self.menuM.dismiss()
		


		

	def fermer(self, instance=None):

		
		self.f.clear_widgets()
            
   
	def show_caller(self, instance=None):
		
		self.show(instance)


	def menuG_open(self, instance=None):
		self.menuG.open()
	def GS(self, instance=None):
		
		self.Genre.text=instance.text

	def show_caller_inner(self, instance):
		if instance == self.Button_ID['M']:
			#print('m')
			#print(self.source['PM'])
			if 'PM' in self.source:
				for i in range(len(self.fmList)):
					#print(self.fmList[i]['name'] ,'vs', self.source['PM']['name'] ,'and', self.fmList[i]['num'] ,'vs', self.source['PM']['num'])
					if self.fmList[i]['name'] == self.source['PM']['name'] and self.fmList[i]['num'] == self.source['PM']['num']:
						#print("break")
						break
				self.fermer()
				self.show(self.fmList[i])
		else:

			if 'PF' in self.source:
				for i in range(len(self.ffList)):
					#print(self.ffList[i]['name'] ,'vs', self.source['PF']['name'] ,'and', self.ffList[i]['num'] ,'vs', self.source['PF']['num'])
					if self.ffList[i]['name'] == self.source['PF']['name'] and self.ffList[i]['num'] == self.source['PF']['num']:
						#print("break")
						break
				self.fermer()
				self.show(self.ffList[i])
'''


class MainApp(MDApp):

	
	def __init__(self, **kwargs):
			super().__init__(**kwargs)
			self.screen = Builder.load_string(KV)
			
	

	
	def build(self):

		
		but = Button(pos_hint={'x': 0.05, 'y': 0.05}, size_hint=(0.2, 0.2),text ="ouvrir",background_normal ='',color=(0,0,0,1), background_color=(0.5,0.5,0.5,1))
		but.bind(on_release=self.fond.show_caller)
		
		
		self.screen.add_widget(but)
	
		
		
		return self.screen




if __name__ == "__main__":
	MainApp().run()
'''
