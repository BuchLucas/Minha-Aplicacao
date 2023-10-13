import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder



kv = """
<ServerCS>:
	BoxLayout:
		orientation: "vertical"
		BoxLayout:
			size_hint_y: .4
			Label:
				text: "Contabilidade"
		
		BoxLayout:
			orientation: "vertical"
			size_hint_y: 2
			BoxLayout:
				size_hint_y: .1
				Button:
					text: "Grande rocho"
					on_press: root.GR()
				Button:
					text: "Pequeno rocho"
					on_press: root.PR()
				Button:
					text: "Feijao Verde"
					on_press: root.FV()
			BoxLayout:
				Label:
					id: Gr
					text: "0"
				Label:
					id: Pr
					text: "0"
				Label:
					id: kgf
					text: "0"
				
		BoxLayout:
			size_hint_y: None
			heiht: 100
			padding: 100,30,100,30
			size_hint_y: .3	
			Button:
				text: "Carregar Informacao"
				
				
"""

Builder.load_string(kv)

class ServerCS(BoxLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
	def GR(self):
		dados = open("/storage/emulated/0/BUCH/cbdd/dado.txt","r")
		dado = dados.read()
		dadoT = str(dado).split("\n")
		
		dadoG = dadoT[0]
		p = dado[1]
		f = dado[2]
		
		status = dadoG
		
		status = int(status)
		newDate = int(status)+1
		
		self.ids.Pr.text = str(newDate)
		da = open("/storage/emulated/0/BUCH/cbdd/dado.txt","w")
		da.write(str(newDate)+"\n"+p+"\n"+f)
	def PR(self):
		dados = open("/storage/emulated/0/BUCH/cbdd/dado.txt","r")
		dado = dados.read()
		dadoT = str(dado).split("\n")
		
		dadoG = dadoT[1]
		g = dado[0]
		f = dado[2]
		
		status = dadoG
		
		status = int(status)
		newDate = int(status)+1
		
		self.ids.Pr.text = str(newDate)
		da = open("/storage/emulated/0/BUCH/cbdd/dado.txt","w")
		da.write(g+"\n"+str(newDate)+"\n"+f)
	def FV(self):
		status = self.ids.kgf.text
		
		status = int(status)
		newDate = status+1
		
		self.ids.kgf.text = str(newDate)

class Construtor(App):
	def build(self):
		return ServerCS()

Construtor().run()