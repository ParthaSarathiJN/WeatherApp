# WeatherApp
A weather app written on Kivy framework.

Displays the __Temperature, Weather, Humidity, Min.Temp__ and __Max.Temp__ from __[OpenWeatherMap](https://openweathermap.org/)__ API data.

___Run only the `kivyCode.py`.___

## Working
Executing `kivyCode.py` creates a window and the user is provided 2 input text boxes for entering Pin-Code and Country Abbreviation. Clicking the search button changes it to a new screen, where the Temperature, Humidity, etc are displayed. A back button is present on the bottom which switches back to the screen where it prompts the user to enter input once again or compute for the same input value again.

When `kivyCode.py` is run for the very first time, both the input fields are empty. However after the first time it will remember the previous session input and displays the previous values. 

Be sure to replace APIKEY with your API key, in `apiInteracter.py`.

### Error Handling
Furthermore if the values entered by the user are invalid/wrong and the user clicks on search, it displays a error message saying `Incorrect Pin Code or Country Abbreviation!` along with the error code.

___[Setting up Kivy.](https://github.com/kivy/kivy/wiki/Setting-Up-Kivy-with-various-popular-IDE's)___
