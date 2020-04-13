# Don't forget to add you API key in APIKEY variable in apiInteracter.py.


import os
from os import path
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

# Changes the default background from black to Creamy Blue
# From range (0 - 1)
Window.clearcolor = (0.521, 0.737, 0.733, 0.4)


kivy.require("1.10.1")

if not path.exists('PinCountryCodeInput.txt'):
	with open('PinCountryCodeInput.txt', 'w') as InputFile:
		InputFile.write('')


class PinCountryCodePage(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)


		self.cols = 2
		self.rows = 20

		# Checks if there is already a value stored in the PinCountryCodeInput.txt by checking byte size. 
		# If it is empty(the first time the file is run), it'll show blank.
		# If a value was entered in any previous session, it remebers that and fills it automatically.

		if os.stat('PinCountryCodeInput.txt').st_size != 0:
			with open('PinCountryCodeInput.txt', 'r') as file:
				details = file.read().split(',')
				previousPinCode = details[0]
				previousCountryCode = details[1]
		else:
				previousPinCode = ''
				previousCountryCode = ''


		self.add_widget(Label(text='Enter Pin-Code: ', font_size=25, font_name='calibri'))
		self.pinCodeInput = TextInput(text=previousPinCode, multiline=False, size_hint_y=7, background_color=[0.819, 0.819, 0.819, 1], border=(1,1,1,1), font_size=25, font_name='calibri')
		self.add_widget(self.pinCodeInput)

		# Take this out if you don't need blank space in bottom after the Country Abbreviation input field.
		# Done this way becuase: Unlike many other toolkits, you cannot explicitly place a widget in a specific column/row. Each child is automatically 
		#		assigned a position determined by the layout configuration and the child’s index in the children list.

		self.add_widget(Label())
		self.blankWidget1 = Label()
		self.add_widget(self.blankWidget1)

		self.add_widget(Label(text='Enter Country Abbreviation: ', font_size=25, font_name='calibri'))
		self.countryCodeInput = TextInput(text=previousCountryCode, multiline=False, size_hint_y=7, background_color=[0.819, 0.819, 0.819, 1], border=(1,1,1,1), font_size=25, font_name='calibri')
		self.add_widget(self.countryCodeInput)

		# Same as the blankWidget1.

		self.add_widget(Label())
		self.blankWidget2 = Label()
		self.add_widget(self.blankWidget2)

		self.search = Button(text='Search', halign='right', font_size=16, size_hint_y=2, font_name='arial', background_color=[0.647, 0.760, 0.772, 1], background_down='atlas://data/images/defaulttheme/button_pressed', border=(1,1,1,1))
		self.search.bind(on_press=self.searchButton)
		self.add_widget(Label())
		self.add_widget(self.search)


	def searchButton(self, instance):
		WeatherApp.screen_manager.current = 'WeatherStats'


	# Sends the input from the text boxes to the apiInterater.py file and returns that input to the WeatherStatsPage
	def searchButton(self, instance):
		pinCodeInput = self.pinCodeInput.text
		countryCodeInput = self.countryCodeInput.text


		with open('PinCountryCodeInput.txt', 'w') as InputFile:
			InputFile.write(f"{pinCodeInput},{countryCodeInput}")
		

		import apiInteracter

		WeatherApp.WeatherStatsPage.updateInfo(apiInteracter.WeatherFunction(pinCodeInput, countryCodeInput))

		WeatherApp.screen_manager.current = 'WeatherStats'



class WeatherStatsPage(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.rows = 10
		row_default_height = 8

		self.message = Label(halign='center', valign='top', font_size=30, size_hint_y=8, font_name='calibri')

		self.message.bind(width=self.updateTextWidth)

		self.add_widget(self.message)

		self.back = Button(text='Back',halign='right', font_size=18, size_hint_y=1, font_name='arial', background_color=[0.647, 0.760, 0.772, 1], background_down='atlas://data/images/defaulttheme/button_pressed', border=(8,1,8,1))
		self.back.bind(on_press=self.backButton)
		self.add_widget(self.back)



	def backButton(self, instance):
		WeatherApp.screen_manager.current = 'PinCountryCode'		


	def updateInfo(self, message):
		self.message.text = message


	def updateTextWidth(self, *_):
		self.message.text_size = (self.message.width, None)



class MyApp(App):
	def build(self):
		# Creates 2 screens.

		self.screen_manager = ScreenManager()

		self.PinCountryCodePage = PinCountryCodePage()
		screen = Screen(name='PinCountryCode')
		screen.add_widget(self.PinCountryCodePage)
		self.screen_manager.add_widget(screen)

		self.WeatherStatsPage = WeatherStatsPage()
		screen = Screen(name='WeatherStats')
		screen.add_widget(self.WeatherStatsPage)
		self.screen_manager.add_widget(screen)

		return self.screen_manager



if __name__ == '__main__':
	WeatherApp = MyApp()
	WeatherApp.run()
