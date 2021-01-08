def up_glo_list():
		global list_table_item
		global list_table
		list_table=[]
		list_table_item = []
		temp_list_pig = updatelist()[0] + updatelist()[1]
		
		#print('list',temp_list_pig)
		for i in range(len(temp_list_pig)):
				#print(i)
				list_table.append(temp_list_pig[i]['name'])
				list_table_item.append(temp_list_pig[i]['num'])
import kivy
from fonction import *
import time
from kivymd.uix.button import MDIconButton
from zipfile import ZipFile
import pickle
import os.path
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.http import MediaIoBaseDownload
import io

from supertable import SuperTable
from SimplePopup import Popups
from loading import Loading
#### attention
import urllib.request
import json

import threading as thr

from kivy.uix.scrollview import ScrollView

import shutil


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
from kivymd.uix.button import MDFlatButton


from kivy.uix.boxlayout import BoxLayout

import os
import csv
Window.clearcolor = (1, 1, 1, 1)

KV = '''
#: import font_size_g __main__.font_size_g
#: import tool_bar_pos __main__.tool_bar_pos


WindowManager:
		MainWin:
				id:main
		ListPige:
				id: LP
		AddPige:
				id: AP
		Login:
				id:LO
		TablePige:
	    		id:TPG


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

									            pos_hint: {'x': 0, 'y': tool_bar_pos}
									            title: "Liste des Pigeons"

									            right_action_items: [["dots-vertical", lambda x: app.menu_list.open()]]
									            md_bg_color: (0.5,0.5,0.5,1)

								        

								        FloatLayout:
									            pos_hint: {'x': 0, 'y': 0}
									            size_hint: 1, tool_bar_pos
									            id: scroll_pg
										                


											

						MDBottomNavigationItem:
								name: "screnn2"
								id: screnn2
								icon: "home-outline"
								FloatLayout:
										MDToolbar:
									            id: Home_tool
									            pos_hint: {'x': 0, 'y': tool_bar_pos}
									            title: "Acceuil"
									            right_action_items: [["dots-vertical", lambda x: app.menu_list_ac.open()]]
									            md_bg_color: (0.5,0.5,0.5,1)
									
								
								
										
										ScrollView:
												pos_hint: {'x': 0, 'y': 0}
												size_hint: 1, tool_bar_pos
												id: scroll_main



										

								
						MDBottomNavigationItem:
								name: "scren3"
								id: screen3
								icon: "calendar"
								FloatLayout:
										Label:
												color: (0, 0, 0, 1)
												font_size: font_size_g+15
												text: "Couvaison"
												pos_hint: {'x':0, 'y': 0.3}
										Button:
												id: date_selectionneur
												text: 'Date de Ponte'
												size_hint: (0.4, 0.1)
												font_size: font_size_g
												
												pos_hint: {'x': 0.3, 'y': 0.45}
												on_release:
														app.show_datepicker()
														#app.labeltext()
											
						
										Button:
												id: valide_couv
												text: 'Valider'
												pos_hint: {'center_x': 0.5, "center_y": 0.2}
												font_size: font_size_g
												size_hint: (0.4, 0.1)
												on_release:
														app.add_couv(app.label_date,app.fm_select,app.ff_select)
														
														

										MDDropDownItem:
												id: field
												text: ""
												font_size: font_size_g
												pos_hint: {'center_x': 0.3, 'center_y': 0.3}
												dropdown_bg: [1, 1, 1, 1]
												on_release: app.menu.open()
										MDDropDownItem:
												id: field2
												text: ""
												font_size: font_size_g
												pos_hint: {'center_x': 0.6, 'center_y': 0.4}
												dropdown_bg: [1, 1, 1, 1]
												on_release: app.menu2.open()

<AddPige>:
		name: "AP" 

		Screen:
				
				FloatLayout:
						MDToolbar:
					            id: tool_AP
					            pos_hint: {'x': 0, 'y': tool_bar_pos}
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
								pos_hint:{'x': 0.25, 'y': 0.5}
								hint_text: "Nom du Pigeon"
						MDTextField:
								id: num
								required: True
								font_size: 40
								size_hint: (0.2,0.08)
								pos_hint:{'x': 0.55, 'y': 0.5}
								hint_text: "Numéro de Bague"


						Label:
								color: (0, 0, 0, 1)
								text:"Parent Mâle:"
								font_size: 35
								pos_hint: {'center_x': .3, 'center_y': .85}

						MDDropDownItem:
								id: PM
								text: "Aucun"
								font_size: 40
								pos_hint: {'center_x': 0.3, 'center_y': 0.75}
								dropdown_bg: [1, 1, 1, 1]
								on_release: app.menu_PM.open()
						Label:
								color: (0, 0, 0, 1)
								text:"Parent Femmelle:"
								font_size: 35
								pos_hint: {'center_x': .7, 'center_y': .85}

						MDDropDownItem:
								id: PF
								text: "Aucun"
								font_size: 40
								pos_hint: {'center_x': 0.7, 'center_y': 0.75}
								dropdown_bg: [1, 1, 1, 1]
								on_release: app.menu_PF.open()


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
								text:"Mâle"
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
										#print(self.active)
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
			            pos_hint: {'x': 0, 'y': tool_bar_pos}
			            title: "Liste des Pigeons"
			            right_action_items: [["dots-vertical", lambda x: app.menu.open()]]
			            md_bg_color: (0.5,0.5,0.5,1)


		        FloatLayout:
			            pos_hint: {'x': 0, 'y': 0}
			            size_hint: 1, tool_bar_pos
			            id:scroll_edit
<TablePige>:
	    name: "TPG"
	    FloatLayout:
		        id: FLAY
		        
		        orientation: "vertical"

		        MDToolbar:
			            id: edit_menu
			            pos_hint: {'x': 0, 'y':tool_bar_pos}
			            title: "Liste des Couvaisons"
			            left_action_items: [["window-close", lambda x: app.back_TPG()]]
			            right_action_items: [["trash-can-outline", lambda x: app.Deleter_TPG()]]
			            md_bg_color: (0.5,0.5,0.5,1)


		        FloatLayout:
			            pos_hint: {'x': 0, 'y': 0}
			            size_hint: 1, tool_bar_pos
			            id:scroll_edit
<Login>:
	    name: "LO"
	    FloatLayout:
		        #id: lay
		        
		        orientation: "vertical"

		        MDToolbar:
			            id: tool__log
			            pos_hint: {'x': 0, 'y': tool_bar_pos}
			            title: "Régalge"
			            left_action_items: [["window-close", lambda x:app.currentLO("main") ]]
			            md_bg_color: (0.5,0.5,0.5,1)
			    ScrollView:
			            pos_hint: {'x': 0, 'y': 0}
			            size_hint: 1, tool_bar_pos
		        		id:lay_drop_scroll
		        		FloatLayout:
		        				id: lay
				        		
				        		
				        				
				        				
					
				        		#FloatLayout:
				        				#id:lay
					



						
								
'''

#############"Google
#ADMIN_UPDATE

tool_bar_pos = 0.91
print("[INFO   ] [MOI         ]","Platform", platform)
if platform != "win":
	size_g = 0.16
	font_size_g = 45
	from android.permissions import request_permissions, Permission
else:

	size_g = 0.16
	font_size_g = 14
	sx = 350
	Window.top = 25
	Window.size = (sx,sx*(2129/1080))



####"





list_table=[]
list_table_item = []



#scroll_main
def table(self):
		global size_g
		global font_size_g
		self.screen.ids.main.ids.scroll_main.clear_widgets() 
		print("[INFO   ] [MOI         ] Tableau construit")
		list_table = list_for_tabel()
		#print(list_table)
		if len(list_table)!=0:

				conv_size = 1/len(list_table)
				#print(self.screen.ids.main.ids.grid.size_hint)
				grif =  FloatLayout(pos_hint={'x': 0, 'y': 0},size_hint = (1,size_g/conv_size),id='grid_pg')#
				#print(grif.size_hint)
				self.add_nb_petit ={}
				
				for i in range(len(list_table)):
						#print([list_table[i]])
						
						colorr = (0.8,0.8,0.8,1)
						tempp = int((temps_restant(list_table[i][0])))
						#print(tempp)
						
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
						wid.add_widget(lbl1)
						if tempp < 0:
							print(list_table[i][3],list_table[i] )
							if list_table[i][3] != "":
								print('1')
								b= MDFlatButton(text=list_table[i][3], font_size= font_size_g,pos_hint={'x': 0.89, 'y': 0.5}, size_hint=(0.05, 0.25))
								b.bind(on_release=self.PopC)
								self.add_nb_petit[b] = {'id':i,'D':list_table[i][0],'M':list_table[i][1],'F':list_table[i][2], 'NM':list_table[i][4], 'NF':list_table[i][5]}
								wid.add_widget(b)
								
							else:
								print("2")
								add  = MDIconButton(icon= "plus",pos_hint= {'x': 0.85, 'y': 0.5})
								add.bind(on_release=self.PopC)
								self.add_nb_petit[add] = {'id':i,'D':list_table[i][0],'M':list_table[i][1],'F':list_table[i][2], 'NM':list_table[i][4], 'NF':list_table[i][5]}
								wid.add_widget(add) 
								

						#label3 = Label(font_size=font_size_g,color=(0,0,0,1),pos_hint={'x': 0.3, 'y': 0.2}, size_hint=(1, None),text =list_table[i][2])
							
						wid.add_widget(label)
						wid.add_widget(label2)
						#wid.add_widget(label3)
						grif.add_widget(wid) 
				self.screen.ids.main.ids.scroll_main.add_widget(grif)
def edit_table(self):
		global size_g
		global font_size_g
		self.screen.ids.TPG.ids.scroll_edit.clear_widgets() 
		print("[INFO   ] [MOI         ] Tableau construit")
		list_table = list_for_tabel()
		print('list_table', list_table)
		#print(list_table)
		if len(list_table)!=0:

				conv_size = 1/len(list_table)
				#print(self.screen.ids.main.ids.grid.size_hint)
				grif =  FloatLayout(pos_hint={'x': 0, 'y': 0},size_hint = (1,size_g/conv_size),id='grid_pg')
				#print(grif.size_hint)
				self.add_nb_petit_TPG ={}
				self.tp_Delete_TPG = []
				
				for i in range(len(list_table)):
						#print([list_table[i]])
						
						colorr = (0.8,0.8,0.8,1)
						tempp = int((temps_restant(list_table[i][0])))
						#print(tempp)
						
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
						lbl1.bind(on_release=self.checker_TPG)
						label = Label(font_size=font_size_g,color=(0,0,0,1), bold = True ,pos_hint={'x': -0.3, 'y': 0.3}, size_hint=(1, None),text =list_table[i][0])
						label2 = Label(font_size=font_size_g,color=(0,0,0,1),pos_hint={'x': 0, 'y': 0.15},halign = "left", size_hint=(1, None),text =list_table[i][1]+"  /  "+list_table[i][2])
						wid.add_widget(lbl1)
						check = MDCheckbox(disabled = True,pos_hint={'x': 0.9, 'y': 0.2}, size_hint=(0, None))
						check.background_disabled_normal= ''
						check.disabled_color=(0,0,1,1)
						self.add_nb_petit_TPG[lbl1] = {'check_status':False,'check':check,'id':i,'D':list_table[i][0],'M':list_table[i][1],'F':list_table[i][2], 'NM':list_table[i][4], 'NF':list_table[i][5]}
								
								

						#label3 = Label(font_size=font_size_g,color=(0,0,0,1),pos_hint={'x': 0.3, 'y': 0.2}, size_hint=(1, None),text =list_table[i][2])
						
						
						wid.add_widget(check)
						wid.add_widget(label)
						wid.add_widget(label2)
						#wid.add_widget(label3)
						grif.add_widget(wid) 
				ss = ScrollView(size_hint=(1,1))
				ss.add_widget(grif)
				self.screen.ids.TPG.ids.scroll_edit.add_widget(ss)#ids.scroll_edit.
				self.screen.current="TPG"



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

class TablePige(Screen):
	pass




ALL_Check_Status = []











class MainApp(MDApp):

	

	def tread_update(self, df=1):
		print("[INFO   ] [MOI         ] Verification mise a jour")
		with open('data.json', 'r') as json_file:
			data = json.load(json_file)
		if data['auto_update'] == 'True':
			
			
			id_folder =  data['id_folder']

			if id_folder != "None":
				#print('id_folder != None',id_folder)
				try :
					urllib.request.urlopen('http://www.guimp.com')
					#id_folder
					print("[INFO   ] [MOI         ] Mise a jour trouvé")

					global creds
					with open('token.pickle', 'rb') as token:
						creds = pickle.load(token)
							    
					global service
					service = build('drive', 'v3', credentials=creds)

					rep = service.files().list(q="'"+str(id_folder)+"' in parents", fields="files(name,id)").execute()['files']
					

					#print("choisi",rep[0]['name'],'from',rep)

					name = rep[0]['name']
					#print(name)
					
					
					
					
					
					#print("est a jour?", data['version'],name)
					if data['version'] != name:

					
						id = rep[0]['id']

						file_id = str(id)
						request = service.files().get_media(fileId=file_id)
						fh = io.FileIO(str(name),mode='w')
						downloader = MediaIoBaseDownload(fh, request)
						done = False
						while done is False:
						      	status, done = downloader.next_chunk()
						#print("finish downloade",id)

						zip = ZipFile(name)
						zip.extractall()
						up_glo_list()
						
						
						try:
							os.remove(i['name'])
						except:
							print("[FAIL   ][MOI         ] Suppression annulé")

						self.ret_value_value = 1.0
						data['version']=str(name)

						with open('data.json', 'w') as outfile:
						    json.dump(data, outfile)
					else:
						#print('id_folder == None',id_folder)
						self.ret_value_value = 3.0
				except Exception as e:
					print('[ERREUR ][MOI         ] ',e)
					
			else:
				self.ret_value_value = 4.0


	def down(self, id, name):
		    creds = None    

		    with open('token.pickle', 'rb') as token:
		        creds = pickle.load(token)
		    
		    #print("service used")
		    service = build('drive', 'v3', credentials=creds)
		    file_id = str(id)
		    request = service.files().get_media(fileId=file_id)
		    fh = io.FileIO(str(name),mode='w')
		    downloader = MediaIoBaseDownload(fh, request)
		    done = False
		    while done is False:
		        	status, done = downloader.next_chunk()
		    #print("finish downloade",id)
	'''
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
	'''
	def add_petit(self, instance):
		
		print(self, instance)
		print(self.add_nb_petit[instance])
		############################################################## ca sert a quoi?
	
			
	def boot(self,df=1):
		thr.Thread(target = self.build_login).start()
		print("[INFO   ] [MOI         ] Boot run")
		self.creds = None
		self.service = None
		self.dialog = None
		self.connection = True
		##date_selectionneur= ObjectProperty(None)
		up_glo_list()
		ranger_csv("data_couv")
		print("[INFO   ] [MOI         ] Boot ranger")
		
		self.ffList = updatelist()[0]
		self.fmList = updatelist()[1]
		print("[INFO   ] [MOI         ] update_data")
		self.list_table = list_for_tabel()
		self.label_accueil = StringProperty('')
		self.label_date = StringProperty('')
		self.ffList_0= StringProperty('')
		self.fmList_0= StringProperty('')
		#print(self.fmList,self.ffList)
		print("[INFO   ] [MOI         ] start")
		self.PM_select = 'Aucun'
		self.PF_select = 'Aucun'

		if len(self.ffList) == 0:
			self.ff_select = "Aucun Pigeon"

		else: 
			self.ff_select = self.ffList[0]['name']+'\n'+ self.ffList[0]['num']

		if len(self.fmList) == 0:
			self.fm_select = "Aucun Pigeon"
		else: 
			self.fm_select = self.fmList[0]['name']+'\n'+ self.fmList[0]['num']

		self.screen.ids.main.ids.field.text = self.fm_select
		self.screen.ids.main.ids.field2.text = self.ff_select

		print("[INFO   ] [MOI         ] 1/2")
		
		self.M_F = None
		self.login_name=None
		self.login_satus=[]

		with open('data.json', 'r') as json_file:
			self.data= json.load(json_file)


		if self.data['login_satus'] == 'False':
			self.login_satus=[{"text":"se connecter"},{"text":"edit"}]
		else:
			self.login_name = self.data['login_name']
			self.login_satus = [{"text":"Sauvegarde"},{"text":"edit"}]
			self.id_folder = self.data['id_folder']
		if self.data['need_to_up'] == 'True':
			thr.Thread(target = self.backup).start()
		global font_size_g
		#global tool_bar_pos
		#self.tool_bar_pos = 0.90 
		global size_g


		self.add_nb_petit_instance = None
		self.FF = MDTextField( pos_hint={'x':0.2,'y':0.7},hint_text= "Nombre",size_hint=(0.6,0.1), font_size=font_size_g)
		V = Button(text='VALIDER', pos_hint={'x':0.5,'y':0.5}, size_hint=(0.2,0.05), font_size= font_size_g)
		V.bind(on_release=self.PopCB)
		L = Button(text='Nombre De Petits',bold=True,disabled=True,color=(0,0,0,1), pos_hint={'x':0.2,'y':0.85}, size_hint=(0.2,0.05), font_size=font_size_g)
		L.background_disabled_normal= ''
		L.background_disabled_color=(0,0,0,0)
		L.disabled_color=(0,0,0,1)
		self.P = Popups(self.screen.ids.main, widget=[self.FF,V,L])#, UOC=table


		#print("login_satus",self.login_satus,",","login_name",self.login_name)

		
		
		#print(self.screen.ids.main.ids.MDN.current)
		self.ret_value_value = 0
		#self.screen.ids.main.ids.MDN.refresh_tabs()
		print("[INFO   ] [MOI         ] Befor table")
		table(self)
		print("[INFO   ] [MOI         ] Table build")
		self.screen.transition = FadeTransition(duration=0.1)
		fmList =self.fmList 
		ffList = self.ffList
		if fmList != {}:
			menu_items = [{'text': fmList[i]['name']+'\n'+fmList[i]['num']} for i in range(len(fmList))]
		else:
			menu_items = list_to_drop_down(dic_to_list({"Aucun Pigeon":""}))
		if ffList != {}:
			menu_items2 = [{'text': ffList[i]['name']+'\n'+ffList[i]['num']} for i in range(len(ffList))]
		else:
			menu_items2 = list_to_drop_down(dic_to_list({"Aucun Pigeon":""}))
		self.menu2 = MDDropdownMenu(
			caller=self.screen.ids.main.ids.field2,
			items=menu_items2,
			position="auto",
			callback=self.set_item2,
			width_mult=20,
		)
		self.menu = MDDropdownMenu(
			caller=self.screen.ids.main.ids.field,
			items=menu_items,
			position="auto",
			callback=self.set_item,
			width_mult=20,
		)
		self.menu_list_ac = MDDropdownMenu(
			caller=self.screen.ids.main.ids.Home_tool,
			items=self.login_satus,
			position="auto",
			callback=self.set_item_ac,
			width_mult=4,
		)
		self.menu_PF = MDDropdownMenu(
			caller=self.screen.ids.AP.ids.PF,
			items=menu_items2,
			position="auto",
			callback=self.menu_PF_ac,
			width_mult=4,
			
		)
		self.menu_PM = MDDropdownMenu(
			caller=self.screen.ids.AP.ids.PF,
			items=menu_items,
			position="auto",
			width_mult=4,
			callback=self.menu_PM_ac,
			
		)
		#width_mult=4,
		self.menu_list = MDDropdownMenu(
	                caller=self.screen.ids.main.ids.edit_menu,
	                items=[{"text":"add"},{"text":"edit"}],
	                position="auto",
	                callback=self.set_item_list_pg,
	                width_mult=4,
	            	)


		ta = updatelist()[0]+updatelist()[1]
		ta = [[i['name']  for i in ta],[i['num']  for i in ta]]
		
		self.ST = SuperTable( address= self.screen.ids.main.ids.scroll_pg, table= ta, font_size=font_size_g , ligne_size= size_g,
			pos_hint = {'x': 0, 'y': 0}, size_hint = (1,1), color=(0.8,0.8,0.8,1), origine =self)

		#self.back(False)
		self.ST.build()


		########"tread upodate"

		print("[INFO   ] [MOI         ] Boot finish")
		thr.Thread(target = self.tread_update).start()
		
		self.event  = Clock.schedule_interval(self.Boot_updater, 1)

	def __init__(self, **kwargs):
			super().__init__(**kwargs)
			self.screen = Builder.load_string(KV)
			thr.Thread(target = self.boot).start()
	def up_drop_down(self):
		self.ffList = updatelist()[0]
		self.fmList = updatelist()[1]
		fmList =self.fmList 
		ffList = self.ffList
		if fmList != {}:
			menu_items = [{'text': fmList[i]['name']+'\n'+fmList[i]['num']} for i in range(len(fmList))]
		else:
			menu_items = list_to_drop_down(dic_to_list({"Aucun Pigeon":""}))
		if ffList != {}:
			menu_items2 = [{'text': ffList[i]['name']+'\n'+ffList[i]['num']} for i in range(len(ffList))]
		else:
			menu_items2 = list_to_drop_down(dic_to_list({"Aucun Pigeon":""}))
		self.menu2 = MDDropdownMenu(
			caller=self.screen.ids.main.ids.field2,
			items=menu_items2,
			position="auto",
			callback=self.set_item2,
			width_mult=20,
		)
		self.menu = MDDropdownMenu(
			caller=self.screen.ids.main.ids.field,
			items=menu_items,
			position="auto",
			callback=self.set_item,
			width_mult=20,
		)
		self.menu_list_ac = MDDropdownMenu(
			caller=self.screen.ids.main.ids.Home_tool,
			items=self.login_satus,
			position="auto",
			callback=self.set_item_ac,
			width_mult=4,
		)
		self.menu_PF = MDDropdownMenu(
			caller=self.screen.ids.AP.ids.PF,
			items=menu_items2,
			position="auto",
			callback=self.menu_PF_ac,
			width_mult=4,
			
		)
		self.menu_PM = MDDropdownMenu(
			caller=self.screen.ids.AP.ids.PF,
			items=menu_items,
			position="auto",
			width_mult=4,
			callback=self.menu_PM_ac,
			
		)
		#width_mult=4,
		self.menu_list = MDDropdownMenu(
	                caller=self.screen.ids.main.ids.edit_menu,
	                items=[{"text":"add"},{"text":"edit"}],
	                position="auto",
	                callback=self.set_item_list_pg,
	                width_mult=4,
	            	)
	def checker_TPG(self, instance):
		print(self, instance)
		print(self.add_nb_petit_TPG[instance])
		if self.add_nb_petit_TPG[instance]['check_status'] == False:
			self.add_nb_petit_TPG[instance]['check'].active= True
			self.add_nb_petit_TPG[instance]['check_status'] = True
			self.tp_Delete_TPG.append(self.add_nb_petit_TPG[instance])
		else:
			self.add_nb_petit_TPG[instance]['check'].active= False
			self.add_nb_petit_TPG[instance]['check_status'] = False
			print('before',self.tp_Delete_TPG)
			self.tp_Delete_TPG.remove(self.add_nb_petit_TPG[instance])
			print('after',self.tp_Delete_TPG)
	def back_TPG(self, instance=None):
		print("back")
		
		self.screen.current="main"
		table(self)

	def Deleter_TPG(self, instance=None):
		print(self, instance)
		print('self.tp_Delete_TPG',self.tp_Delete_TPG)

		remove_csv(self.tp_Delete_TPG)
		edit_table(self)
	def add_couv(self,label_date,fm_select, ff_select):
		print(label_date)
		if type(label_date) != type(StringProperty('')):
			print(label_date)
			self.write_csv_classe(label_date,fm_select,ff_select)
			self.Snac("Date ajouter")	
		else:
			self.Snac("Veuillez choisir une date")	
	def PopC (self, instance=None):
		try: 
			if instance.text != '':

				self.FF.text = instance.text
			
			else:
				self.FF.text = ''
		except:
			self.FF.text = ''
		self.P.show()


		print(instance,self.add_nb_petit[instance])
		self.add_nb_petit_instance = instance
	def add_NDP_TOOL(self, source,D, N):
		print("[INFO   ] [MOI         ] ", source, D, N)
		found = False
		if 'NBP' not in source:
			source['NBP'] =[]
		for i in range(len(source['NBP'])):
			#print('NBP' in source, int(self.anne.text) == source['NBP'][i]['anne'])
			if  int(D) == source['NBP'][i]['anne']:
				source['NBP'][i]['nombre'] += int(N)
				found = True
				break
		if 'NBP' in source and found == False:
			source['NBP'].append({'anne':int(D),'nombre':int(N)})
		elif found == False: 
			source['NBP']=[{'anne':int(D),'nombre':int(N)}]
		return source


	def add_NDP(self, source, N):
		M = source['M']
		NM = source['NM']
		F = source['F']
		NF = source['NF']
		print('M',M,'NM', NM,'F', F,'NF', NF)
		self.ffList = updatelist()[0]
		self.fmList = updatelist()[1]
		#print(self.ffList) 
		#for i in self.fmList:
		#	print(i['name'] , M , i['num'] , NM)
		#	print(( i['name'] == M and i['num'] == NM))
		erreur = False

		try:
			Msource = next(item for item in self.fmList if item['name'] == M and item['num'] == NM)
			Fsource = next(item for item in self.ffList if item['name'] == F and item['num'] == NF)
		except Exception as e :
			print(e, "verssion ansicein pigeon pas touver")
			self.Snac("Erreur version ancienne")
			erreur = True
		if erreur == False:
			new_Msource = self.add_NDP_TOOL(Msource,int(source['D'][6:]), N)

			
			new_Fsource  = self.add_NDP_TOOL(Fsource,int(source['D'][6:]), N)
			
			list_remove('M', M, NM)
			if 'PF' not in new_Msource:
				new_Msource['PF'] = 'Aucun'
			if 'PM' not in new_Msource:
				new_Msource['PM'] = 'Aucun'
			
			
			list_write('M', new_Msource['name'], new_Msource['num'], new_Msource['PF'], new_Msource['PM'], new_Msource['NBP'])
			list_remove('F', F, NF)
			if 'PF' not in new_Fsource:
				new_Fsource['PF'] = 'Aucun'
			if 'PM' not in new_Fsource:
				new_Fsource['PM'] = 'Aucun'
			list_write('F', new_Fsource['name'], new_Fsource['num'], new_Fsource['PF'], new_Fsource['PM'], new_Fsource['NBP'])
			self.ffList = updatelist()[0]
			self.fmList = updatelist()[1]
		


			
	def PopCB(self, instance=None):
		x = self.add_nb_petit[self.add_nb_petit_instance]
		print(x['D'],x['M'],x['F'],self.FF.text)
		write_NBP(x['D'],x['M'],x['F'],self.FF.text)
		table(self)
		self.P.close()
		self.add_NDP(x,self.FF.text )
		self.ST.build()
		


	def Boot_updater(self,df):
		if self.ret_value_value != 0.0:
			self.event.cancel()
			print(self.ret_value_value)
			
			if self.ret_value_value == 1.0:
				Clock.schedule_once(self.temp_Snac,1)
				print("updating lyout")
				up_glo_list()
				table(self)
				#self.back(False)
				self.ST.build()
			elif self.ret_value_value == 3.0:
				print("allreday ûptodat")
	def temp_Snac(self,df=1):
		self.Snac("Installation de la dernière version")

	
	def menu_PF_ac(self, instance=None):
		self.screen.ids.AP.ids.PF.text = instance.text
		self.PF_select = instance.text
		self.menu_PF.dismiss()
	def menu_PM_ac(self, instance=None):
		self.screen.ids.AP.ids.PM.text = instance.text
		self.PM_select = instance.text
		self.menu_PM.dismiss()
			
	
			
	def select_back(self, instance):
			#print(instance.text)
			self.btn_drop.text = instance.text
			#print(self.screen.ids.LO.ids.btn_drop.pos_hint)
			self.back_list.dismiss()	

	def download_chosen(self, name):
		print("[INFO   ] [MOI         ] Download start")
		names = name
		name = name[:len(name)-4]
		global list_table
		#print("service used")
		rep = service.files().list(q="'"+str(self.id_folder)+"' in parents", fields="files(name, id)").execute()['files']
		found = False
		for i in rep:
			
			#print(i['name'][:len(i)-6], (' vs '),name)

			if i['name'][:len(i)-6] == name:
				print('[INFO   ] [MOI         ] Found')
				found = True
				break
		#print(i)
		self.down(i['id'],i['name'])
		zip = ZipFile(i['name'])
		zip.extractall()

		#self.screen.ids.LO.ids.btn_drop.text = 'Selectioner une Sauvegarde'

		self.Snac('Charger!')
		up_glo_list()
		table(self)
		ta = updatelist()[0]+updatelist()[1]
		ta = [[i['name']  for i in ta],[i['num']  for i in ta]]
		self.ST.update_data(ta)
		self.ST.build()
		with open('data.json', 'r') as json_file:
			data= json.load(json_file)
		data['version'] = str(names)

		with open('data.json', 'w') as outfile:
		    json.dump(data, outfile)
		try:
			os.remove(i['name'])
		except:
			print("[FAIL   ][MOI         ] suppression annulé")

	def valid_down(self, instance):
		global list_table
		#print("service used")
		try:
			rep = service.files().list(q="'"+str(self.id_folder)+"' in parents", fields="files(name, id)").execute()['files']
			self.connection =True
		except Exception as e:
			print(e, "Hors connection")
			self.connection = False
		if self.connection == True:
			found = False
			for i in rep:
				
				#print(i['name'][:len(i)-6])

				if i['name'][:len(i)-6] == self.btn_drop.text:
					#print('found')
					found = True
					break
			#print(i)
			self.down(i['id'],i['name'])
			zip = ZipFile(i['name'])
			zip.extractall()

			with open('data.json', 'r') as json_file:
				data= json.load(json_file)

			data['version']=str(i['name'][:len(i)-6])

			with open('data.json', 'w') as outfile:
			    json.dump(data, outfile)

			#self.screen.ids.LO.ids.btn_drop.text = 'Selectioner une Sauvegarde'

			self.Snac('Charger!')
			up_glo_list()
			table(self)
			#self.back(False)
			self.ST.update_t()
			
			self.ST.build()
			try:
				os.remove(i['name'])
			except:
				print("[FAIL   ][MOI         ] Suppression annulé")
		else:
			self.Snac("Hors Connection")

	def set_item_list_pg(self, instance):

        #time.sleep(0.05)
	        self.menu_list.dismiss()
	        if instance.text == 'edit':
		            #print(self.screen)
		            #print("ici",self.screen.current)
		            self.screen.current="LP"
		            #self.screen.transition = FadeTransition(duration=0.5)
		            self.edit()
		            #self.back(False)
	        if instance.text == "add":
		            self.ST.addPP()
	def back_list_open(self, instance=None):
		print("self.back_list.open()")
		self.back_list.open()

	def build_login(self, instance=None):
		self.new_connection = FloatLayout()
		
		self.mdfield = MDTextField(hint_text="Identifiant",size_hint= (0.2,0.09),font_size = font_size_g,pos_hint = {'x': 0.5, 'y': 0.75} )
		
		       				
		btn_ac  = Button(text='Valider',size_hint= (0.15,0.05),pos_hint={'x': 0.6, 'y': 0.7})
		btn_ac.bind(on_release=self.btn_login)
					
		self.new_connection.add_widget(btn_ac)
		self.new_connection.add_widget(self.mdfield)
		self.new_connection.add_widget(Label(text = 'Profile :',font_size = font_size_g + 6,pos_hint={'x': -0.3, 'y': 0.4}, color=(0,0,0,1)))
		self.new_connection.add_widget(Label(text = 'Identifiant :',font_size = font_size_g ,pos_hint={'x': -0.2, 'y': 0.3}, color=(0.5,0.5,0.5,1)))
		

		self.normal_connection = FloatLayout()
		btn_ac  = Button(text='Faire une Sauvegarde',size_hint= (0.4,0.05),pos_hint={'x': 0.5, 'y': 0.5})
		btn_ac.bind(on_release=self.backup)
		self.normal_connection.add_widget(Label(text = 'Profile:',font_size = font_size_g + 6,pos_hint={'x': -0.3, 'y': 0.4}, color=(0,0,0,1)))
		self.normal_connection.add_widget(Label(text = 'Sauvegarde:',font_size = font_size_g + 6,pos_hint={'x': -0.3, 'y': 0.2}, color=(0,0,0,1)))
		self.normal_connection.add_widget(Label(text = 'Identifiant :',font_size = font_size_g ,pos_hint={'x': -0.2, 'y': 0.3}, color=(0.5,0.5,0.5,1)))
					
					
		btn_csv  = Button(text='Exporter',size_hint= (0.15,0.05),pos_hint={'x': 0.6, 'y': 0.075})
		btn_csv.bind(on_release=self.exp_csv_thread)
							
		btn_ac_val  = Button(text='Charger',size_hint= (0.15,0.05),pos_hint={'x': 0.6, 'y': 0.34})
		btn_ac_val.bind(on_release=self.valid_down)
		self.btn_drop = Button(pos_hint={'x': 0.6, 'y': 0.4},text='Selectioner une Sauvegarde',size_hint= (0.2,0.05),color=(0,0,0,1),background_normal ='',background_color=(0.8,0.8,0.8,1))
		self.btn_drop.bind(on_release= self.back_list_open)
		self.normal_connection.add_widget(self.btn_drop)
		self.normal_connection.add_widget(btn_ac)
		self.normal_connection.add_widget(btn_ac_val)
		self.normal_connection.add_widget(btn_csv)
		self.normal_connection.add_widget(Label(text = 'Dernière Sauvegarde :',font_size = font_size_g ,pos_hint={'x': -0.2, 'y': 0.1}, color=(0.5,0.5,0.5,1)))
		self.normal_connection.add_widget(Label(text = 'Dernière Sauvegarde :',font_size = font_size_g ,pos_hint={'x': -0.2, 'y': 0.1}, color=(0.5,0.5,0.5,1)))
		self.normal_connection.add_widget(Label(text = 'Charger une Sauvegarde :',font_size = font_size_g ,pos_hint={'x': -0.2, 'y': -0.07}, color=(0.5,0.5,0.5,1)))
		self.normal_connection.add_widget(Label(text = 'Mise a jour automatique :',font_size = font_size_g,pos_hint={'x': -0.2, 'y': -0.2}, color=(0.5,0.5,0.5,1)))
		self.normal_connection.add_widget(Label(text = 'Exportation :',font_size = font_size_g + 6,pos_hint={'x': -0.3, 'y': 0.-0.3}, color=(0,0,0,1)))
		self.normal_connection.add_widget(Label(text = 'Exporter en CSV :',font_size = font_size_g,pos_hint={'x': -0.2, 'y': -0.4}, color=(0.5,0.5,0.5,1)))
		
	def sauvegarde_loading(self):
					with open('data.json', 'r') as json_file:
						self.data= json.load(json_file)
					self.screen.ids.LO.ids.lay.add_widget(self.normal_connection)
					self.screen.ids.LO.ids.lay.add_widget(Label(text = self.data['login_name'],font_size = font_size_g ,pos_hint={'x': 0.1, 'y': 0.3}, color=(0,0,0,1)))

					self.screen.ids.LO.ids.lay.add_widget(Label(text = self.data['version'],font_size = font_size_g ,pos_hint={'x': 0.1, 'y': 0.1}, color=(0,0,0,1)))

					
					if self.data['auto_update'] == 'False':
						check_LU = MDCheckbox(pos_hint={'x': 0.6, 'y': 0.25}, size_hint = (0.1,0.1))
					else:
						check_LU = MDCheckbox(pos_hint={'x': 0.6, 'y': 0.25}, active = True,size_hint = (0.1,0.1))

					check_LU.bind(on_release=self.auto_update_status)
					
					self.screen.ids.LO.ids.lay.add_widget(check_LU)
					if self.connection == True:
						load = service.files().list(q="'"+str(self.id_folder)+"' in parents", fields="files(name)").execute()['files']
					else:
						load = [{'name':"None.zip"}]
						self.Snac("Hors Connection")
					if len(load) !=0:
						self.btn_drop.text= str(load[0]['name'][:-4])
					else:
						self.btn_drop.text= str('None')

					print(self.screen.ids.LO.ids.lay.children)
					#print("ici",self.screen.current)
					self.back_list = MDDropdownMenu(
						caller=self.btn_drop,
						items=list_to_drop_down_zip(load),
						position="auto",
						callback=self.select_back,
						width_mult=4,
					)


	def set_item_ac(self, instance):
			global font_size_g
			#print("service used")
			#print("self.login_satus",self.login_satus)
		

			self.menu_list_ac.dismiss()
			global creds
			with open('token.pickle', 'rb') as token:
				creds = pickle.load(token)
			    
			global service
			try:
				service = build('drive', 'v3', credentials=creds)
				self.connection = True
			except Exception as e:
				print(e ," hors connection")
				self.connection = False
		       
			if instance.text == 'se connecter':
					#print(self.screen)
					#print("ici",self.screen.current)
					self.screen.ids.LO.ids.lay.clear_widgets()
					self.screen.ids.LO.ids.lay.add_widget(self.new_connection)
					self.screen.current="LO"

			if instance.text == 'Sauvegarde':
					l = Loading(self.screen.ids.LO.ids.lay, self.sauvegarde_loading)
					
					self.screen.ids.LO.ids.lay.clear_widgets()
					
					self.screen.current="LO"
					l.build()
					

					
			if instance.text == 'edit':
				edit_table(self)
			
	def exp_csv_thread(self,instantce):
		self.event_exp  = Clock.schedule_interval(self.exp_csv, 1)
		
	def exp_csv(self,df=1):
		request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
		
		
		try:
			shutil.copy2('data_couv.csv', '/sdcard/Download/'+str(time.time())+'_data_couv.csv')
			self.Snac("Exportation reussi vers 'Download'")
			self.event_exp.cancel()



		except Exception as e:
			print("[INFO   ] [MOI         ] ",'waiting',e)
		
	
	def auto_update_status(self, instance= None):
		#print(self, instance)
		#print(instance.active)
		self.data['auto_update'] = str(instance.active)
		with open('data.json', 'w') as outfile:
			json.dump(self.data, outfile)
		

	def edit(self):
		'''
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
			'''
		self.ST.build_edit(self.screen.ids.LP.ids.scroll_edit,self.screen.ids.LP.ids.edit_menu)
			
		self.screen.ids.LP.ids.edit_menu.title= str(self.ST.getCount())+" selected"
		self.screen.ids.LP.ids.edit_menu.left_action_items= [["window-close", lambda x: self.runtback()]]
		self.screen.ids.LP.ids.edit_menu.right_action_items= [["trash-can-outline", lambda x: self.Deleter()]]



	       

	def runtback(self):
		ta = updatelist()[0]+updatelist()[1]
		ta = [[i['name']  for i in ta],[i['num']  for i in ta]]
		self.ST.update_data(ta)
		self.ST.build()
		self.screen.current="main"


	def checker(self,instance):
	        global ALL_Check_Status


	        #print("checked "+str(instance.id))
	        #print(instance)
	        id_selct = str(instance.id)
	        id_selct = int(id_selct[1:])

	        #print(len(self.screen.ids.LP.ids.scroll_edit.children[0].children), id_selct)
	        id_selct_rev = (len(self.screen.ids.LP.ids.scroll_edit.children[0].children)-1)-id_selct
	        if self.screen.ids.LP.ids.scroll_edit.children[0].children[id_selct_rev].children[0].active == False:
	            self.screen.ids.LP.ids.scroll_edit.children[0].children[id_selct_rev].children[0].active = True
	            ALL_Check_Status[id_selct]= True
	        else:
	            self.screen.ids.LP.ids.scroll_edit.children[0].children[id_selct_rev].children[0].active = False
	            ALL_Check_Status[id_selct]= False
	        #print(self.screen.ids.LP.ids.scroll_edit.children[0].children[id_selct_rev].children[0].active)
	        #print(ALL_Check_Status)
	        self.check_selected = 0
	        for z in ALL_Check_Status:
	            if z == True:
	                self.check_selected+=1
	        self.screen.ids.LP.ids.edit_menu.title= str(self.check_selected)+" selected"
	        


	def Deleter(self):
		self.ST.Deleter()
		
		
		self.Snac("Suppression Réussie")

		ta = updatelist()[0]+updatelist()[1]
		ta = [[i['name']  for i in ta],[i['num']  for i in ta]]
		self.ST.update_data(ta)
		self.ST.build()
		self.screen.current="main"

		ffList = updatelist()[0]
		fmList = updatelist()[1]
		self.ffList = ffList
		self.fmList = fmList
		
		if fmList != []:
			menu_items = [{'text': fmList[i]['name']+' '+fmList[i]['num']} for i in range(len(fmList))]
		else:
			menu_items = list_to_drop_down(dic_to_list([{"Aucun Pigeon":""}]))
		if ffList != []:
			menu_items2 = [{'text': ffList[i]['name']+' '+ffList[i]['num']} for i in range(len(ffList))]
		else:
			menu_items2 = list_to_drop_down(dic_to_list([{"Aucun Pigeon":""}]))

		
		self.Snac("Suppression Réussie")
		self.menu2 = MDDropdownMenu(
					caller=self.screen.ids.main.ids.field,
					items=menu_items2,
					position="auto",
					callback=self.set_item2,
					width_mult=20,
				)
		self.menu = MDDropdownMenu(
					caller=self.screen.ids.main.ids.field,
					items=menu_items,
					position="auto",
					callback=self.set_item,
					width_mult=20,
				)
		self.menu_PF = MDDropdownMenu(
			caller=self.screen.ids.AP.ids.PF,
			items=menu_items2,
			position="auto",
			callback=self.menu_PF_ac,
			width_mult=4,
			
			)
		self.menu_PM = MDDropdownMenu(
				caller=self.screen.ids.AP.ids.PF,
				items=menu_items,
				position="auto",
				width_mult=4,
				callback=self.menu_PM_ac,
				
			)

	def Snac(self, text):
		Snackbar(text=text).show()

	def set_item(self, instance):
			
			self.screen.ids.main.ids.field.text = instance.text
			self.fm_select = instance.text
			self.menu.dismiss()
	def set_item2(self, instance):
			self.screen.ids.main.ids.field2.text = instance.text
			self.ff_select =instance.text
			self.menu2.dismiss()
	def show_datepicker(self):
		picker = MDDatePicker(callback = self.got_date)
		picker.open()

	def got_date(self, the_date):
		print("[INFO   ] [MOI         ] Date ", the_date)
		self.label_date = str(the_date)
		self.screen.ids.main.ids.date_selectionneur.text = self.label_date
		#self.screen.ids.main.ids.MDN.switch_tab("screnn2")
	def btn_login(self,instance):
		print("[INFO   ] [MOI         ] Boutton login")
		#print(self.screen.ids.LO.ids.mdfield.text)
		with open('data.json', 'r') as json_file:
			self.data= json.load(json_file)
		self.data['login_name'] = str(self.mdfield.text)
		#open('log.'+str(self.screen.ids.LO.ids.lay.children[1].text),'w')
		found =  False
		results = service.files().list(
        	pageSize=10, fields="files(id, name)").execute()
		for i in results['files']:
			#print(i['name'])
			if i['name'] ==self.mdfield.text:
				found = True

				self.id_folder = i['id']
				print("found",self.id_folder)

		if found== False:
			print("[INFO   ] [MOI         ] Nouveau compte")
			file_metadata = {
	            'name':str(self.mdfield.text),
	            'mimeType': 'application/vnd.google-apps.folder'
	        }
			file = service.files().create(body=file_metadata,fields='id').execute()
			self.id_folder = file.get('id')
		self.data['id_folder'] = str(self.id_folder)
		#open('id.'+str(self.id_folder),'w')
		self.menu_list_ac = MDDropdownMenu(
				caller=self.screen.ids.main.ids.Home_tool,
				items=[{"text":"Sauvegarde"},{"text":"edit"}],
				position="auto",
				callback=self.set_item_ac,
				width_mult=4,
			)
		self.login_satus=[{"text":"Sauvegarde"},{"text":"edit"}]
		self.currentLO("main")
		
		
		self.data['login_satus'] = 'True'
		

		with open('data.json', 'w') as outfile:
			json.dump(self.data, outfile)
		#self.mdfield.pos_hint = {'x': -1.3, 'y': 0.75}
		self.Snac("connecter")
	def currentLO(self, text):
		#print(self.screen.ids.LO.ids.lay.children)
		self.screen.current=text
		self.screen.ids.LO.ids.lay.clear_widgets()
		#.screen.ids.LO.ids.lay.children[0].size_hint = (0,0)
		#self.screen.ids.LO.ids.lay.remove_widget(self.screen.ids.LO.ids.lay.children[1])
		#btn_ac  = Button(text='Faire une Sauvegarde',size_hint= (0.2,0.1),pos_hint={'x': 0.3, 'y': 0.5})
		#btn_ac.bind(on_release=self.backup)
					
		#self.screen.ids.LO.ids.lay.add_widget(btn_ac)

	def backup(self, instance=None):
		if self.data['login_satus'] == 'True':
			print("[INFO   ] [MOI         ] Backup")
			global creds
			with open('token.pickle', 'rb') as token:
				creds = pickle.load(token)
				    
			global service
			try:

				service = build('drive', 'v3', credentials=creds)
				self.connection = True
			except Exception as e:
				print(e, "hors connecttion")
				self.connection = False
			if self.connection == True:
				zip_back = ZipFile(str(date.today())+'.zip','w')
				zip_back.write('data_couv.csv')
				zip_back.write('Flist.txt')
				zip_back.write('Mlist.txt')
				zip_back.close()
				
				file_metadata = {'name': str(date.today())+'.zip', 'parents':[self.id_folder]}	
				media = MediaFileUpload(str(date.today())+'.zip', mimetype='file/zip')
				file = service.files().create(body=file_metadata,
			                                        media_body=media,
			                                        fields='id').execute()
				with open('data.json', 'r') as json_file:
					self.data= json.load(json_file)
				self.data['need_to_up'] = 'False'
			

				with open('data.json', 'w') as outfile:
					json.dump(self.data, outfile)
				self.Snac("Sauvegarde Effectué")
			else:
				self.Snac("Hors Connection")
				with open('data.json', 'r') as json_file:
					self.data= json.load(json_file)
				self.data['need_to_up'] = 'True'
			

				with open('data.json', 'w') as outfile:
					json.dump(self.data, outfile)

	    

	def btn_valide(self):
			global M_F
		
			
			global fmList
			global ffList
			fmList =self.fmList
			ffList = self.ffList
			PF_select = 'Aucun'
			PM_select =  'Aucun'
			#print(self.PM_select, self.PF_select)
			for i in range(len(fmList)):
				#print(fmList[i]['name']+' '+fmList[i]['num'], 'vs', self.PM_select)
				if fmList[i]['name']+' '+fmList[i]['num'] == self.PM_select:
					PM_select = {'name': fmList[i]['name'], 'num': fmList[i]['num']}
					break

			for i in range(len(ffList)):
				#print(ffList[i]['name']+' '+ffList[i]['num'] ,'vs',self.PF_select)
				if ffList[i]['name']+' '+ffList[i]['num']  == self.PF_select:
					PF_select =  {'name': ffList[i]['name'], 'num': ffList[i]['num']}
					break


			
			list_write(M_F,self.screen.ids.AP.ids.nom.text,self.screen.ids.AP.ids.num.text, PF_select, PM_select)
			ffList = updatelist()[0]
			fmList = updatelist()[1]
			self.ffList = ffList
			self.fmList = fmList

			print("[INFO   ] [MOI         ] Pigeon ajouté")
			if fmList != []:
				menu_items = [{'text': fmList[i]['name']+' '+fmList[i]['num']} for i in range(len(fmList))]
			else:
				menu_items = list_to_drop_down(dic_to_list([{"Aucun Pigeon":""}]))
			if ffList != []:
				menu_items2 = [{'text': ffList[i]['name']+' '+ffList[i]['num']} for i in range(len(ffList))]
			else:
				menu_items2 = list_to_drop_down(dic_to_list([{"Aucun Pigeon":""}]))
			
			self.menu2 = MDDropdownMenu(
					caller=self.screen.ids.main.ids.field,
					items=menu_items2,
					position="auto",
					callback=self.set_item2,
					width_mult=20,
				)
			self.menu = MDDropdownMenu(
					caller=self.screen.ids.main.ids.field,
					items=menu_items,
					position="auto",
					callback=self.set_item,
					width_mult=20,
				)
			self.menu_PF = MDDropdownMenu(
			caller=self.screen.ids.AP.ids.PF,
			items=menu_items2,
			position="auto",
			callback=self.menu_PF_ac,
			width_mult=4,
			
			)
			self.menu_PM = MDDropdownMenu(
				caller=self.screen.ids.AP.ids.PF,
				items=menu_items,
				position="auto",
				width_mult=4,
				callback=self.menu_PM_ac,
				
			)
			self.screen.ids.AP.ids.nom.text = ''
			self.screen.ids.AP.ids.num.text = ''
			self.screen.ids.AP.ids.checpk_F.active = False
			self.screen.ids.AP.ids.check_M.active = False
			self.Snac("Un Pigeon a était Ajouter")
			up_glo_list()
			self.ST.build()
			#self.back(False)
			try:
				#thr.Thread(target = self.backup).start()
				pass
			except:
				print("[INFO   ] [MOI         ] Hors conection")
		
		

	def current(self,text):
			self.screen.current=text

	
	def write_csv_classe(self,date,M,F):
		MI = M.find('\n')
		FI = F.find('\n')



		write_csv(date,M[:MI],F[:FI], M[MI+1:], F[FI+1:])
		
		table(self)
		self.Snac("L'événement a été ajouté")
		self.screen.ids.main.ids.MDN.switch_tab("screnn2")
		try:
			thr.Thread(target = self.backup).start()
		except:
			print("[INFO   ] [MOI         ] Hors conection")

	

	def M_call(self,statue):
		if statue == True:
			global M_F
			M_F = "M"
			#print(M_F)
	def F_call(self,statue):
		if statue == True:
			global M_F
			M_F = "F"
			#print(M_F)



	def add_pg(self):
		pass



			
	

	def build(self):
		print("[INFO   ] [MOI         ] Build")
		
		
		return self.screen



if __name__ == "__main__":

	MainApp().run()

