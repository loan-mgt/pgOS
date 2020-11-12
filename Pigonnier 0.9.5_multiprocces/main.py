def up_glo_list():
		global list_table_item
		global list_table
		list_table=[]
		list_table_item = []
		temp_list_pig = updatelist([],[])[0]
		temp_list_pig.update(updatelist([],[])[1])
		print(temp_list_pig)
		print('list',temp_list_pig)
		for i in (temp_list_pig):
				print(i)
				list_table.append(i)
				list_table_item.append(temp_list_pig[i])
import kivy
from fonction import *

from zipfile import ZipFile
import pickle
import os.path
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.http import MediaIoBaseDownload
import io


#### attention
import urllib.request
import json
import threading as thr





from datetime import date

from kivy.utils import platform
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.lang import Builder
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.textfield import MDTextField
from kivy.uix.screenmanager import ScreenManager, Screen ,FadeTransition
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.icon_definitions import md_icons
####from kivymd.theming import ThemeManager
from kivymd.uix.picker import MDDatePicker
from kivy.properties import ObjectProperty, StringProperty
from kivymd.uix.menu import MDDropdownMenu
from kivymd.toast import toast
from kivymd.uix.snackbar import Snackbar
from kivy.properties import StringProperty
from kivy.clock import Clock

import os
import csv
Window.clearcolor = (1, 1, 1, 1)

KV = '''
WindowManager:
		MainWin:
				id:main
		ListPige:
				id: LP
		AddPige:
				id: AP
		Login:
				id:LO

<MainWin>:
		name:"main"

		Screen:
				MDBottomNavigation:
						id: MDN
					##"date_selectionneur" : "date_selectionneur"
						MDBottomNavigationItem:
								name: "screnn1"
								#icon: "duck"
								icon: 'format-list-bulleted'
								FloatLayout:
        								id: FLAY
        
        								orientation: "vertical"

								        MDToolbar:
									            id: edit_menu
									            pos_hint: {'x': 0, 'y': 0.93}
									            title: "Liste des Pigeons"
									            right_action_items: [["dots-vertical", lambda x: app.menu_list.open()]]
									            md_bg_color: (0.5,0.5,0.5,1)

								        

								        ScrollView:
									            pos_hint: {'x': 0, 'y': 0}
									            size_hint: 1, 0.93
									            id: scroll_pg
										                


											

						MDBottomNavigationItem:
								name: "screnn2"
								id: screnn2
								icon: "home-outline"
								FloatLayout:
										MDToolbar:
									            id: Home_tool
									            pos_hint: {'x': 0, 'y': 0.93}
									            title: "Acceuil"
									            right_action_items: [["dots-vertical", lambda x: app.menu_list_ac.open()]]
									            md_bg_color: (0.5,0.5,0.5,1)
									
								
								
										
										ScrollView:
												pos_hint: {'x': 0, 'y': 0}
												size_hint: 1, 0.93
												id: scroll_main



										

								
						MDBottomNavigationItem:
								name: "scren3"
								id: screen3
								icon: "calendar"
								FloatLayout:
										Label:
												color: (0, 0, 0, 1)
												font_size: 40
												text: "Couvaison"
												pos_hint: {'x':0, 'y': 0.3}
										Button:
												id: date_selectionneur
												text: 'Date de Ponte'
												size_hint: (0.4, 0.1)
												font_size: 40
												
												pos_hint: {'x': 0.3, 'y': 0.45}
												on_release:
														app.show_datepicker()
														#app.labeltext()
											
						
										Button:
												id: valide_couv
												text: 'Valider'
												pos_hint: {'center_x': 0.5, "center_y": 0.2}
												font_size: 40
												size_hint: (0.4, 0.1)
												on_release:
														app.write_csv_classe(app.label_date,app.fm_select,app.ff_select)
														app.Snac("Date ajouter")
														

										MDDropDownItem:
												id: field
												text: ""
												font_size: 40
												pos_hint: {'center_x': 0.3, 'center_y': 0.35}
												dropdown_bg: [1, 1, 1, 1]
												on_release: app.menu.open()
										MDDropDownItem:
												id: field2
												text: ""
												font_size: 40
												pos_hint: {'center_x': 0.6, 'center_y': 0.35}
												dropdown_bg: [1, 1, 1, 1]
												on_release: app.menu2.open()

<AddPige>:
		name: "AP" 

		Screen:
				
				FloatLayout:
						MDToolbar:
					            id: tool_AP
					            pos_hint: {'x': 0, 'y': 0.93}
					            title: "Ajouter un Pigeon"
					            left_action_items: [["window-close", lambda x: app.current("main")]]
					            md_bg_color: (0.5,0.5,0.5,1)

						Button:
								text: 'Ajouter le Pigeon'
								size_hint: (0.4, 0.1)

								font_size: 40
												
								pos_hint: {'x': 0.3, 'y': 0.15}
								on_release:
										app.btn_valide()
						MDTextField:
								id: nom
								required: True
								font_size : 40
								size_hint: (0.2,0.08)
								pos_hint:{'x': 0.25, 'y': 0.7}
								hint_text: "Nom du Pigeon"
						MDTextField:
								id: num
								required: True
								font_size: 40
								size_hint: (0.2,0.08)
								pos_hint:{'x': 0.55, 'y': 0.7}
								hint_text: "Numéro de Bague"
						MDCheckbox:
								id: check_M
								required: True
								group: 'M/F'
								size_hint: None, None
								size: dp(48), dp(48)
								pos_hint: {'center_x': .25, 'center_y': .4}
								on_active:
										app.M_call(self.active)
						Label:
								color: (0, 0, 0, 1)
								text:"Malle"
								font_size: 35
								pos_hint: {'center_x': .35, 'center_y': .4}
						MDCheckbox:
								id: check_F
								group: 'M/F'
								size_hint: None, None
								size: dp(48), dp(48)
								pos_hint: {'center_x': .55, 'center_y': .4}
								on_active:
										app.F_call(self.active)
										print(self.active)
						Label:
								color: (0, 0, 0, 1)
								text:"Femmelle"
								font_size: 35
								pos_hint: {'center_x': .70, 'center_y': .4}


<ListPige>:
	    name: "LP"
	    FloatLayout:
		        id: FLAY
		        
		        orientation: "vertical"

		        MDToolbar:
			            id: edit_menu
			            pos_hint: {'x': 0, 'y': 0.93}
			            title: "Liste des Pigeons"
			            right_action_items: [["dots-vertical", lambda x: app.menu.open()]]
			            md_bg_color: (0.5,0.5,0.5,1)


		        ScrollView:
			            pos_hint: {'x': 0, 'y': 0}
			            size_hint: 1, 0.93
			            id:scroll_edit
<Login>:
	    name: "LO"
	    FloatLayout:
		        #id: lay
		        
		        orientation: "vertical"

		        MDToolbar:
			            id: tool__log
			            pos_hint: {'x': 0, 'y': 0.93}
			            title: "Sauvegarde"
			            left_action_items: [["window-close", lambda x: app.currentLO("main")]]
			            md_bg_color: (0.5,0.5,0.5,1)
			    FloatLayout:
		        		id:lay_drop
		        		Button:
		        				id: btn_drop
		        				text:'Selectioner une Sauvegarde'
		        				size_hint: (0.3,0.1)
		        				#pos_hint:{'x': -0.6, 'y': 0.6}
		        				pos_hint:{'x': -0.6, 'y': 0.6}
		        				color:(0,0,0,1)
		        				background_normal :''
		        				background_color:(0.8,0.8,0.8,1)
		        				on_release: app.back_list.open()
		        		FloatLayout:
		        				id:lay
					



									
								
'''

#############"Google
#ADMIN_UPDATE


print("platform", platform)
if platform != "win":
	size_g = 0.16
	font_size_g = 45
else:

	size_g = 0.16
	font_size_g = 15


####"





list_table=[]
list_table_item = []



#scroll_main
def table(self):
		global size_g
		global font_size_g
		self.screen.ids.main.ids.scroll_main.clear_widgets() 
		print("yesssssssssssssssssssssssssssssssssssssssssssssssssssss")
		list_table = list_for_tabel()
		print(list_table)
		if len(list_table)!=0:

				conv_size = 1/len(list_table)
				#print(self.screen.ids.main.ids.grid.size_hint)
				grif =  FloatLayout(pos_hint={'x': 0, 'y': 0},size_hint = (1,size_g/conv_size),id='grid_pg')
				print(grif.size_hint)
				
				for i in range(len(list_table)):
						print([list_table[i]])
					
						colorr = (0.8,0.8,0.8,1)
						tempp = int((temps_restant(list_table[i][0])))
						print(tempp)
						if tempp < 0:
								colorr = (0,0,0,0.4)
						elif tempp <= 3:
								colorr = (1,0.8,0.8,1)
						elif tempp <= 6:
								colorr = (1,1,0.8,1)
						else:
								colorr = (0.8,1,0.8,1)



						wid = FloatLayout(size_hint=(1,conv_size),pos_hint={'y':1-conv_size*(i+1) }, id= str(i)+"float")
						lbl1 = Button(pos_hint={'x': 0, 'y': 0}, size_hint=(1, 1),text ="",background_normal ='',color=(0,0,0,1), background_color=colorr)
						label = Label(font_size=font_size_g,color=(0,0,0,1), bold = True ,pos_hint={'x': -0.3, 'y': 0.3}, size_hint=(1, None),text =list_table[i][0])
						label2 = Label(font_size=font_size_g,color=(0,0,0,1),pos_hint={'x': 0, 'y': 0.15},halign = "left", size_hint=(1, None),text =list_table[i][1]+"  /  "+list_table[i][2])
						#label3 = Label(font_size=font_size_g,color=(0,0,0,1),pos_hint={'x': 0.3, 'y': 0.2}, size_hint=(1, None),text =list_table[i][2])
						wid.add_widget(lbl1)
						wid.add_widget(label)
						wid.add_widget(label2)
						#wid.add_widget(label3)
						grif.add_widget(wid) 
				self.screen.ids.main.ids.scroll_main.add_widget(grif)

class WindowManager(ScreenManager):
     pass

class MainWin(Screen):
     pass
class ListPige(Screen):
	pass

class AddPige(Screen):
     pass

class Login(Screen):
	pass





ALL_Check_Status = []











class MainApp(MDApp):

	

	def tread_update(self, df=1):
		print("try")
		with open('data.json', 'r') as json_file:
			data = json.load(json_file)
		if data['auto_update'] == 'True':
			
			
			id_folder =  data['id_folder']

			if id_folder != "None":
				print('id_folder != None',id_folder)
				try :
					urllib.request.urlopen('http://www.guimp.com')
					#id_folder
					print("updateing")

					global creds
					with open('token.pickle', 'rb') as token:
						creds = pickle.load(token)
							    
					global service
					service = build('drive', 'v3', credentials=creds)

					rep = service.files().list(q="'"+str(id_folder)+"' in parents", fields="files(name,id)").execute()['files']
					

					print("choisi",rep[0]['name'],'from',rep)

					name = rep[0]['name']
					print(name)
					
					
					
					
					
					print("est a jour?", data['version'],name)
					if data['version'] != name:

					
						id = rep[0]['id']

						file_id = str(id)
						request = service.files().get_media(fileId=file_id)
						fh = io.FileIO(str(name),mode='w')
						downloader = MediaIoBaseDownload(fh, request)
						done = False
						while done is False:
						      	status, done = downloader.next_chunk()
						print("finish downloade",id)

						zip = ZipFile(name)
						zip.extractall()
						up_glo_list()
						
						
						try:
							os.remove(i['name'])
						except:
							print("coundt remove")

						self.ret_value_value = 1.0
						data['version']=str(name)

						with open('data.json', 'w') as outfile:
						    json.dump(data, outfile)
					else:
						print('id_folder == None',id_folder)
						self.ret_value_value = 3.0
				except Exception as e:
					print('e',e)
					
			else:
				self.ret_value_value = 4.0


	def down(self, id, name):
		    creds = None    

		    with open('token.pickle', 'rb') as token:
		        creds = pickle.load(token)
		    
		    print("service used")
		    service = build('drive', 'v3', credentials=creds)
		    file_id = str(id)
		    request = service.files().get_media(fileId=file_id)
		    fh = io.FileIO(str(name),mode='w')
		    downloader = MediaIoBaseDownload(fh, request)
		    done = False
		    while done is False:
		        	status, done = downloader.next_chunk()
		    print("finish downloade",id)

	def back(self,force):
			print("rebuild")
			#up_glo_list()


			if force == True:
					self.screen.current="main"

			#print("len bifor",self.screen.ids.main.ids.scroll_pg.children[0].size_hint_y)
			self.screen.ids.main.ids.scroll_pg.clear_widgets()
			global list_table
			global list_table_item
			global size_g
			global font_size_g
			print(len(list_table))
			print(list_table)
			if len(list_table) != 0:
					conv_size = 1/len(list_table)

					
					grif =  FloatLayout(size_hint = (1,size_g/conv_size), id='grid_pg')
					#self.screen.ids.main.ids.grid_pg.size_hint_y = size_g*len(list_table)
					#print(self.screen.ids.main.ids.scroll_pg.children[0].size_hint_y)
					for i in range(len(list_table)):

				            wid = FloatLayout(pos_hint={'y':1-conv_size*(i+1) },size_hint=(1,conv_size), id= str(i)+"float")
				            lbl1 = Button(pos_hint={'x': 0, 'y': 0}, size_hint=(1, 1),text ="",background_normal ='',color=(0,0,0,1), background_color=(0.8,0.8,0.8,1))
				            label = Label(font_size=font_size_g,color=(0,0,0,1),pos_hint={'x': -0.25, 'y': 0.2}, size_hint=(1, None),text =list_table[i])
				            label2 = Label(font_size=font_size_g,color=(0,0,0,1),pos_hint={'x': 0.15, 'y': 0.2}, size_hint=(1, None),text =list_table_item[i])
				            wid.add_widget(lbl1)
				            wid.add_widget(label)
				            wid.add_widget(label2)
				            grif.add_widget(wid) 
					self.screen.ids.main.ids.scroll_pg.add_widget(grif)

                
			self.menu_list = MDDropdownMenu(
	                caller=self.screen.ids.main.ids.edit_menu,
	                items=[{"text":"add"},{"text":"edit"}],
	                position="auto",
	                callback=self.set_item_list_pg,
	                width_mult=4,
	            	)
	
			
	def boot(self,df=1):
		self.creds = None
		self.service = None
		##date_selectionneur= ObjectProperty(None)
		up_glo_list()
		ranger_csv("data_couv")

		self.ffList = updatelist([],[])[0]
		self.fmList = updatelist([],[])[1]
		self.list_table = list_for_tabel()
		self.label_accueil = StringProperty('')
		self.label_date = StringProperty('')
		self.ffList_0= StringProperty('')
		self.fmList_0= StringProperty('')
		print(self.fmList,self.ffList)



		if len(self.ffList) == 0:
			self.ff_select = "Aucun Pigeon"

		else: 
			self.ff_select = list(self.ffList.keys())[0]

		if len(self.fmList) == 0:
			self.fm_select = "Aucun Pigeon"
		else: 
			self.fm_select = list(self.fmList.keys())[0]

		self.screen.ids.main.ids.field.text = self.fm_select
		self.screen.ids.main.ids.field2.text = self.ff_select

		
		
		self.M_F = None
		self.login_name=None
		self.login_satus=[]

		with open('data.json', 'r') as json_file:
			self.data= json.load(json_file)

		if self.data['login_satus'] == 'False':
			self.login_satus=[{"text":"se connecter"}]
		else:
			self.login_name = self.data['login_name']
			self.login_satus = [{"text":"Sauvegarde"}]
			self.id_folder = self.data['id_folder']





		


		print("login_satus",self.login_satus,",","login_name",self.login_name)

		
		
		print(self.screen.ids.main.ids.MDN.current)
		self.ret_value_value = 0
		#self.screen.ids.main.ids.MDN.refresh_tabs()
		table(self)
		self.screen.transition = FadeTransition(duration=0.1)
		fmList =self.fmList 
		ffList = self.ffList
		if fmList != {}:
			menu_items = list_to_drop_down(dic_to_list(fmList))
		else:
			menu_items = list_to_drop_down(dic_to_list({"Aucun Pigeon":""}))
		if ffList != {}:
			menu_items2 = list_to_drop_down(dic_to_list(ffList))
		else:
			menu_items2 = list_to_drop_down(dic_to_list({"Aucun Pigeon":""}))
		self.menu2 = MDDropdownMenu(
			caller=self.screen.ids.main.ids.field,
			items=menu_items2,
			position="auto",
			callback=self.set_item2,
			width_mult=4,
		)
		self.menu = MDDropdownMenu(
			caller=self.screen.ids.main.ids.field,
			items=menu_items,
			position="auto",
			callback=self.set_item,
			width_mult=4,
		)
		self.menu_list_ac = MDDropdownMenu(
			caller=self.screen.ids.main.ids.Home_tool,
			items=self.login_satus,
			position="auto",
			callback=self.set_item_ac,
			width_mult=4,
		)
		self.back(False)

		########"tread upodate"

		
		thr.Thread(target = self.tread_update).start()
		self.event  = Clock.schedule_interval(self.Boot_updater, 1)

	def __init__(self, **kwargs):
			super().__init__(**kwargs)
			self.screen = Builder.load_string(KV)
			thr.Thread(target = self.boot).start()
			#self.screen.ids.main.ids.MDN.switch_tab("screnn2")
			
			#self.screen.ids.main.ids.MDN.switch_tab("screnn1")
			#self.screen.ids.main.ids.MDN.switch_tab("screnn2")
			#"screnn2"
			#scren3
			#p1 = multiprocessing.Process(traget = init_muti)


			#### to do
			#Clock.schedule_once(self.startupdate,1)
			#Clock.schedule_once(self.last_update,5)
			

			#Clock.schedule_once(self.tread_update, 5)
			


	def Boot_updater(self,df):
		if self.ret_value_value != 0.0:
			self.event.cancel()
			print(self.ret_value_value)
			
			if self.ret_value_value == 1.0:
				Clock.schedule_once(self.temp_Snac,1)
				print("updating lyout")
				up_glo_list()
				table(self)
				self.back(False)
			elif self.ret_value_value == 3.0:
				print("allreday ûptodat")
	def temp_Snac(self,df=1):
		self.Snac("Installation de la dernière version")

	

			
	
			
	def select_back(self, instance):
			print(instance.text)
			self.screen.ids.LO.ids.btn_drop.text = instance.text
			#print(self.screen.ids.LO.ids.btn_drop.pos_hint)
			self.back_list.dismiss()	

	def download_chosen(self, name):
		names = name
		name = name[:len(name)-4]
		global list_table
		print("service used")
		rep = service.files().list(q="'"+str(self.id_folder)+"' in parents", fields="files(name, id)").execute()['files']
		found = False
		for i in rep:
			
			print(i['name'][:len(i)-6], (' vs '),name)

			if i['name'][:len(i)-6] == name:
				print('found')
				found = True
				break
		print(i)
		self.down(i['id'],i['name'])
		zip = ZipFile(i['name'])
		zip.extractall()

		#self.screen.ids.LO.ids.btn_drop.text = 'Selectioner une Sauvegarde'

		self.Snac('Charger!')
		up_glo_list()
		table(self)
		self.back(False)
		with open('data.json', 'r') as json_file:
			data= json.load(json_file)
		data['version'] = str(names)

		with open('data.json', 'w') as outfile:
		    json.dump(data, outfile)
		try:
			os.remove(i['name'])
		except:
			print("coundt remove")

	def valid_down(self, instance):
		global list_table
		print("service used")
		rep = service.files().list(q="'"+str(self.id_folder)+"' in parents", fields="files(name, id)").execute()['files']
		found = False
		for i in rep:
			
			print(i['name'][:len(i)-6])

			if i['name'][:len(i)-6] == self.screen.ids.LO.ids.btn_drop.text:
				print('found')
				found = True
				break
		print(i)
		self.down(i['id'],i['name'])
		zip = ZipFile(i['name'])
		zip.extractall()

		#self.screen.ids.LO.ids.btn_drop.text = 'Selectioner une Sauvegarde'

		self.Snac('Charger!')
		up_glo_list()
		table(self)
		self.back(False)
		try:
			os.remove(i['name'])
		except:
			print("coundt remove")

	def set_item_list_pg(self, instance):

        #time.sleep(0.05)
	        self.menu_list.dismiss()
	        if instance.text == 'edit':
		            print(self.screen)
		            print("ici",self.screen.current)
		            self.screen.current="LP"
		            #self.screen.transition = FadeTransition(duration=0.5)
		            self.edit()
		            #self.back(False)
	        if instance.text == "add":
		            self.screen.current='AP'

	def set_item_ac(self, instance):
			print("service used")
			print("self.login_satus",self.login_satus)
			if self.login_satus==[{"text":"se connecter"}]:
					text_in =  MDTextField(font_size= 40,size_hint= (0.2,0.1),pos_hint={'x': 0.55, 'y': 0.7},hint_text= "Identifiant")
					btn_ac  = Button(text='valider',size_hint= (0.2,0.1),pos_hint={'x': 0.55, 'y': 0.3})
					btn_ac.bind(on_release=self.btn_login)
					self.screen.ids.LO.ids.lay.add_widget(text_in)
					self.screen.ids.LO.ids.lay.add_widget(btn_ac)
			if self.login_satus==[{"text":"Sauvegarde"}]:

					
					btn_ac  = Button(text='Faire une Sauvegarde',size_hint= (0.2,0.1),pos_hint={'x': 0.2, 'y': 0.4})
					btn_ac.bind(on_release=self.backup)
					
					btn_ac_val  = Button(text='Charger',size_hint= (0.2,0.1),pos_hint={'x': 0.65, 'y': 0.4})
					btn_ac_val.bind(on_release=self.valid_down)
					if self.data['auto_update'] == 'False':
						check_LU = MDCheckbox(pos_hint={'x': 0.25, 'y': 0.57}, size_hint = (0.1,0.1))
					else:
						check_LU = MDCheckbox(pos_hint={'x': 0.25, 'y': 0.57}, active = True,size_hint = (0.1,0.1))

					check_LU.bind(on_release=self.auto_update_status)
					lb = Label(text = 'Mise a jour automatique :',pos_hint={'x': -0.2, 'y': 0.2}, color=(0,0,0,1))
					self.screen.ids.LO.ids.lay.add_widget(lb)
					self.screen.ids.LO.ids.lay.add_widget(check_LU)
					self.screen.ids.LO.ids.lay.add_widget(btn_ac)
					
					self.screen.ids.LO.ids.lay.add_widget(btn_ac_val)
					print(self.screen.ids.LO.ids.btn_drop.pos_hint)
					
					self.screen.ids.LO.ids.btn_drop.pos_hint={'x': 0.6, 'y': 0.6}
					
					#self.screen.ids.LO.ids.btn_drop.text = 'Selectioner une Sauvegarde'
					print(self.screen.ids.LO.ids.lay.children)
					
					

					#btn_ac_drop  = Button(text='Selectioner une Sauvegarde',size_hint= (0.3,0.1),pos_hint={'x': 0.6, 'y': 0.6}, color=(0,0,0,1),background_normal ='', background_color=(0.8,0.8,0.8,1))
					#btn_ac_drop.bind(on_release=self.back_list.open)
					#self.screen.ids.LO.ids.lay.add_widget(btn_ac_drop)

					

					#self.back_list.open()
					
		

			self.menu_list_ac.dismiss()
			global creds
			with open('token.pickle', 'rb') as token:
				creds = pickle.load(token)
			    
			global service
			service = build('drive', 'v3', credentials=creds)
		       
			if instance.text == 'se connecter':
					print(self.screen)
					print("ici",self.screen.current)
					self.screen.current="LO"

			if instance.text == 'Sauvegarde':
				
					print("ici",self.screen.current)
					self.back_list = MDDropdownMenu(
						caller=self.screen.ids.LO.ids.lay.children[1],
						items=list_to_drop_down_zip(service.files().list(q="'"+str(self.id_folder)+"' in parents", fields="files(name)").execute()['files']),
						position="auto",
						callback=self.select_back,
						width_mult=4,
					)
					self.screen.current="LO"
			
		       
	
	def auto_update_status(self, instance= None):
		print(self, instance)
		print(instance.active)
		self.data['auto_update'] = str(instance.active)
		with open('data.json', 'w') as outfile:
			json.dump(self.data, outfile)
		

	def edit(self):
	        global ALL_Check_Status
	        global list_table
	        global list_table_item
	        global lliste
	        global size_g
	        global font_size_g
	        ALL_Check_Status = [False]*len(list_table)
	        self.screen.ids.LP.ids.scroll_edit.clear_widgets()
	        
	        self.check_selected = 0
	        
	       
	        print(len(list_table))
	        print(list_table)
	        if len(list_table) != 0:
			        conv_size = 1/len(list_table)

					
			        grif =  FloatLayout(size_hint = (1,size_g/conv_size), id='grid_pg')
					#self.screen.ids.main.ids.grid_pg.size_hint_y = size_g*len(list_table)
					#print(self.screen.ids.main.ids.scroll_pg.children[0].size_hint_y)
			        for i in range(len(list_table)):

			                    wid = FloatLayout(pos_hint={'y':1-conv_size*(i+1) },size_hint=(1,conv_size), id= str(i)+"float")


			                    
			                    lbl1 = Button(id= "B"+str(i),pos_hint={'x': 0, 'y': 0}, size_hint=(1, 1),text ="",background_normal ='',color=(1,0,0,1), background_color=(0.8,0.8,0.8,1))
			                    lbl1.bind(on_release=self.checker)
			                    
			                    label = Label(font_size=font_size_g,color=(0,0,0,1),pos_hint={'x': -0.25, 'y': 0.2}, size_hint=(1, None),text =list_table[i])
			                    label2 = Label(font_size=font_size_g,color=(0,0,0,1),pos_hint={'x': 0.15, 'y': 0.2}, size_hint=(1, None),text =list_table_item[i])
			                   
			                    wid.add_widget(lbl1)
			                    wid.add_widget(label)
			                    wid.add_widget(label2)
			                    
			                    self.check = MDCheckbox(id = str(i),disabled = True,pos_hint={'x': 0.8, 'y': 0}, size_hint=(0, None))
			                    self.check.background_disabled_normal= ''
			                    self.check.disabled_color=(0,0,1,1)
			                    


			                    #check.bind(on_active= printt())
			                    #disabled: True
			                    #disabled_color: 0, 0, 1, 1
			                    wid.add_widget(self.check)
			                    

			                    grif.add_widget(wid)
			        self.screen.ids.LP.ids.scroll_edit.add_widget(grif)
			        self.screen.ids.LP.ids.edit_menu.title= str(self.check_selected)+" selected"
			        self.screen.ids.LP.ids.edit_menu.left_action_items= [["window-close", lambda x: self.back(True)]]
			        self.screen.ids.LP.ids.edit_menu.right_action_items= [["trash-can-outline", lambda x: self.Deleter()]]



	        print("helo")
	        print(self.screen.ids.LP.ids.scroll_edit.children[0].children)



	def checker(self,instance):
	        global ALL_Check_Status


	        print("checked "+str(instance.id))
	        print(instance)
	        id_selct = str(instance.id)
	        id_selct = int(id_selct[1:])

	        print(len(self.screen.ids.LP.ids.scroll_edit.children[0].children), id_selct)
	        id_selct_rev = (len(self.screen.ids.LP.ids.scroll_edit.children[0].children)-1)-id_selct
	        if self.screen.ids.LP.ids.scroll_edit.children[0].children[id_selct_rev].children[0].active == False:
	            self.screen.ids.LP.ids.scroll_edit.children[0].children[id_selct_rev].children[0].active = True
	            ALL_Check_Status[id_selct]= True
	        else:
	            self.screen.ids.LP.ids.scroll_edit.children[0].children[id_selct_rev].children[0].active = False
	            ALL_Check_Status[id_selct]= False
	        print(self.screen.ids.LP.ids.scroll_edit.children[0].children[id_selct_rev].children[0].active)
	        print(ALL_Check_Status)
	        self.check_selected = 0
	        for z in ALL_Check_Status:
	            if z == True:
	                self.check_selected+=1
	        self.screen.ids.LP.ids.edit_menu.title= str(self.check_selected)+" selected"
	        


	def Deleter(self):
		global ALL_Check_Status
		global list_table
		list_to_rem = []
		for i in range(len(ALL_Check_Status)):
			if ALL_Check_Status[i] == True:
				print(list_table[i])
				list_to_rem.append(list_table[i])
		for i in list_to_rem:
			try:
				list_remove("M",i,"")
			except:
				list_remove("F",i,"")
		print("deleted")
		up_glo_list()
		self.back(True)
		self.Snac("Suppression Réussie")

	def Snac(self, text):
		Snackbar(text=text).show()

	def set_item(self, instance):
			
			self.screen.ids.main.ids.field.text = instance.text
			self.fm_select = instance.text
	def set_item2(self, instance):
			self.screen.ids.main.ids.field2.text = instance.text
			self.ff_select =instance.text
	def show_datepicker(self):
		picker = MDDatePicker(callback = self.got_date)
		picker.open()

	def got_date(self, the_date):
		print(the_date)
		self.label_date = str(the_date)
		self.screen.ids.main.ids.date_selectionneur.text = self.label_date
		self.screen.ids.main.ids.MDN.switch_tab("screnn2")
	def btn_login(self,instance):
		print("service used")
		print(self.screen.ids.LO.ids.lay.children[1].text)
		with open('data.json', 'r') as json_file:
			self.data= json.load(json_file)
		self.data['login_name'] = str(self.screen.ids.LO.ids.lay.children[1].text)
		#open('log.'+str(self.screen.ids.LO.ids.lay.children[1].text),'w')
		found =  False
		results = service.files().list(
        	pageSize=10, fields="files(id, name)").execute()
		for i in results['files']:
			print(i['name'])
			if i['name'] == self.screen.ids.LO.ids.lay.children[1].text:
				found = True

				self.id_folder = i['id']
				print("found",self.id_folder)

		if found== False:
			print("ni found")
			file_metadata = {
	            'name':str(self.screen.ids.LO.ids.lay.children[1].text),
	            'mimeType': 'application/vnd.google-apps.folder'
	        }
			file = service.files().create(body=file_metadata,fields='id').execute()
			self.id_folder = file.get('id')
		self.data['id_folder'] = str(self.id_folder)
		#open('id.'+str(self.id_folder),'w')
		self.menu_list_ac = MDDropdownMenu(
				caller=self.screen.ids.main.ids.Home_tool,
				items=[{"text":"Sauvegarde"}],
				position="auto",
				callback=self.set_item_ac,
				width_mult=4,
			)
		self.login_satus=[{"text":"Sauvegarde"}]
		self.currentLO("main")
		print(self.screen.ids.LO.ids.btn_drop.pos_hint)
		self.screen.ids.LO.ids.btn_drop.pos_hint={'x': 0.6, 'y': 0.6}
		self.screen.ids.LO.ids.btn_drop.text = 'Selectioner une Sauvegarde'
		print(self.screen.ids.LO.ids.btn_drop.pos_hint)
		
		self.data['login_satus'] = 'True'
		

		with open('data.json', 'w') as outfile:
			json.dump(self.data, outfile)
		self.Snac("connecter")
	def currentLO(self, text):
		print(self.screen.ids.LO.ids.lay.children)
		self.screen.current=text
		self.screen.ids.LO.ids.lay.clear_widgets()
		#.screen.ids.LO.ids.lay.children[0].size_hint = (0,0)
		#self.screen.ids.LO.ids.lay.remove_widget(self.screen.ids.LO.ids.lay.children[1])
		#btn_ac  = Button(text='Faire une Sauvegarde',size_hint= (0.2,0.1),pos_hint={'x': 0.3, 'y': 0.5})
		#btn_ac.bind(on_release=self.backup)
					
		#self.screen.ids.LO.ids.lay.add_widget(btn_ac)

	def backup(self, instance=None):
		print("service used")
		print(date.today())
		zip_back = ZipFile(str(date.today())+'.zip','w')
		zip_back.write('data_couv.csv')
		zip_back.write('Flist.txt')
		zip_back.write('Mlist.txt')
		zip_back.close()
		print(self.id_folder)
		file_metadata = {'name': str(date.today())+'.zip', 'parents':[self.id_folder]}	
		media = MediaFileUpload(str(date.today())+'.zip', mimetype='file/zip')
		file = service.files().create(body=file_metadata,
	                                        media_body=media,
	                                        fields='id').execute()
		self.Snac("Sauvegarde Effectué")
	    

	def btn_valide(self):
		global M_F
		try:
			
			global fmList
			global ffList
			print(ffList,fmList)

			list_write(M_F,self.screen.ids.AP.ids.nom.text,self.screen.ids.AP.ids.num.text)
			ffList = updatelist([],[])[0]
			fmList = updatelist([],[])[1]

			print("M_F",M_F,"name", self.screen.ids.AP.ids.nom.text, "email", self.screen.ids.AP.ids.num.text)
			if fmList != {}:
				menu_items = list_to_drop_down(dic_to_list(fmList))
			else:
				menu_items = list_to_drop_down(dic_to_list({"Aucun Pigeon":""}))
			if ffList != {}:
				menu_items2 = list_to_drop_down(dic_to_list(ffList))
			else:
				menu_items2 = list_to_drop_down(dic_to_list({"Aucun Pigeon":""}))
			print("recall")
			self.menu2 = MDDropdownMenu(
					caller=self.screen.ids.main.ids.field,
					items=menu_items2,
					position="auto",
					callback=self.set_item2,
					width_mult=4,
				)
			self.menu = MDDropdownMenu(
					caller=self.screen.ids.main.ids.field,
					items=menu_items,
					position="auto",
					callback=self.set_item,
					width_mult=4,
				)
		except:
			print("error")

		self.screen.ids.AP.ids.nom.text = ''
		self.screen.ids.AP.ids.num.text = ''
		self.screen.ids.AP.ids.check_F.active = False
		self.screen.ids.AP.ids.check_M.active = False
		self.Snac("Un Pigeon a était Ajouter")
		up_glo_list()
		self.back(False)
		try:
			thr.Thread(target = self.backup).start()
		except:
			print("hors conection")

	def current(self,text):
			self.screen.current=text

	
	def write_csv_classe(self,date,M,F):
		print(M)
		print(F)
		write_csv(date,M,F)
		#self.screen.ids.main.ids.grid.clear_widgets()
		#print("clear?")
		table(self)
		self.Snac("L'événement a été ajouté")
		try:
			thr.Thread(target = self.backup).start()
		except:
			print("hors conection")

	

	def M_call(self,statue):
		if statue == True:
			global M_F
			M_F = "M"
			print(M_F)
	def F_call(self,statue):
		if statue == True:
			global M_F
			M_F = "F"
			print(M_F)



	def add_pg(self):
		pass



			
	

	def build(self):
		print("build")
		
		
		return self.screen



if __name__ == "__main__":

	MainApp().run()
