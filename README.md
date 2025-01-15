# 
 
<h1 align="center">LinkedinAutoBot 🤖</h1>

<div align="center">
  <img src="https://github.com/SidneyTeodoroJr/LinkedinAutoBot/blob/main/bot_designer/LinkedIn-Auto%20Bot-%20home%20-light.png" alt="Banner LinkedinAutoBot">
</div>
</br>
</br>

<h2 align="center">Overview</h2>
<p>
 LinkedIn Auto Bot is an application that automates interactions on LinkedIn, making it easier to manage connections and interactions on the platform. The application has an intuitive graphical interface and allows the customization of various settings.
</p>

<h2>Download the Application</h2>

<a href="https://raw.githubusercontent.com/SidneyTeodoroJr/MoviePY/main/build_platforms/MoviePY.apk" download>Windows</a></br>

<h2>Execution Instruction</h2>

1. Download the file from the link above according to your operating system: Windows, macOS or Linux.
2. Select all the compressed files.
3. Click unzip.
4. Open the `LinkedinAutoBot win` folder.
5. Double-click the bot icon, `LinkedinAutoBot.exe`.

<h2>Technologies Used</h2>

- [Python](https://docs.python.org/3/)
- [Flet](https://flet.dev/docs/) (for building the graphical interface)
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) (for automation of interactions)
- [OpenCV](https://docs.opencv.org/4.x/index.html) (for image processing)

<div align="center">
  <img height=200 width=300 src="https://logosmarcas.net/wp-content/uploads/2021/10/Python-Logo.png" alt="Python"/>
  <img height=200 width=300 src="https://raw.githubusercontent.com/flet-dev/flet/main/media/logo/flet-logo.svg" alt="Flet"/>
</div>

<h2>Installation</h2>

<p>To run the project, you will need to have Python installed on your machine. Follow the steps below:</p>

1. Clone this repository:
   ```
   git clone https://github.com/SidneyTeodoroJr/LinkedinAutoBot.git
2. Navigate to the project directory:
   ```
   cd LinkedinAutoBot
4. Navigate to 'SRC'
   ```
   cd scrc
5. Install the required dependencies:
   ```
   pip install -r requirements.txt
5. To start the application, run the following command:
    ``` 
    flet -r main.py
 <h2>Code Structure</h2>
 
<p>The project is organized as follows:</p>

- [main.py](https://github.com/SidneyTeodoroJr/LinkedinAutoBot/blob/main/LinkedInAutoBot/src/main.py): Application entry point, where the interface is configured.
  
- [modules/GUI_elements.py](https://github.com/SidneyTeodoroJr/LinkedinAutoBot/blob/main/LinkedInAutoBot/src/modules/GUI_elements.py): Defines custom graphic elements such as text, buttons, and sliders.
  
- [pages/](https://github.com/SidneyTeodoroJr/LinkedinAutoBot/tree/main/LinkedInAutoBot/src/pages): Contains the application pages, such as the home page and the settings page.
  
- [modules/image_search.py](https://github.com/SidneyTeodoroJr/LinkedinAutoBot/blob/main/LinkedInAutoBot/src/modules/image_search.py): Contains the logic for locating elements on the screen using the ImageLocator class.

<div align="center">
  <img src="https://github.com/SidneyTeodoroJr/LinkedinAutoBot/blob/main/bot_designer/LinkedIn-Auto-Bot%20-setup-light.png" alt="Print LinkedinAutoBot light">
</div>

<h2>Classe ImageLocator</h2>

<p>The ImageLocator class is responsible for locating image elements on the screen and interacting with them. The main parameters and methods include:</p>

- <h3>Parameters:</h3>

1. `img_path:` Path of the image to be located.
2. `max_attempts:` Maximum number of attempts to locate the image.
3. `search_interval:` Time interval between search attempts.
4. `duration:` Duration of the mouse movement until the located position.
5. `confidence:` Confidence level when locating the image (from 0 to 1).

- <h3>start_search method:</h3>

1. Locates the image on the screen and performs a click if found.

2. If the image is not found after the maximum number of attempts, prints an error message.

<h2>Custom Components</h2>

<p>Below are the main custom components used in the application:</p>

1. `CustonAppBar:` An application bar that includes icons for information and switching between themes.
2. `CustonCard:` A card that can contain information and is styled with a custom background color.
3. `CustonSwitch:` A switch that can be used to toggle settings, with customizable active color and tooltip.
4. `CustonText:` A text component that allows you to customize color, weight, alignment, and size.
5. `bot_name:` ​​An input field for the bot name, with a lightning bolt icon.
6. `InputSearch:` An input field to search for terms, with a magnifying glass icon.
7. `time_slider:` A slider to adjust the time between clicks, with a range of 3 to 10 seconds.
8. `connects_slider:` A slider to set the number of connections per page, with a range of 1 to 7.
9. `pages_slider:` A slider to set the number of pages the bot will go through, with a range of 1 to 10.

<h2>Home Page</h2>

<p>The home page (home_page) consists of the following elements:</p>

1. `CustonAppBar:` An application bar that includes options for opening the GitHub repository and switching between themes.
2. `Welcome Text:` A central message that reads "Best engagement bot for LinkedIn".
3. `Image:` An icon representing the application, displayed at 350x350.
4. `Instructions:` Messages that encourage the user to log in to LinkedIn before proceeding.
5. `"Start Setup" Button:` A prominent button that starts the setup process, with a custom style.

<h2>Setup Page</h2>

<p>The setup_page allows users to customize the bot's settings. The main components include:</p>

1. `Banner:` A cover image with a description of the bot's functionality.

2. `Information Cards:` Display information about the number of connections, pages, and time configured by the user, using sliders.

3. `Automation Configuration:` Includes input fields for the bot name and search, as well as sliders for configuring the number of connections, pages, and time.

4. `"GO" Button:` A button that starts the automation, when clicked, triggers the AutoBot function.
   
<h2>AutoBot Function</h2>

<p>The AutoBot function is responsible for executing the automation process on LinkedIn. The main steps include:</p>

1. Minimize all windows and open LinkedIn.
2. Locate and interact with the search field.
3. Navigate through the results pages and send connection requests based on the user's settings.
4. Manage navigation between pages and the number of connections.
5. End the bot session and close the browser.

<h2>Main Functions</h2>

1. `open_website:` Opens the GitHub repository URL.
2. `toggle_theme:` Toggles between light and dark themes.
3. `start_setup:` Navigates to the setup page.
4. `start_home:` Returns to the home page.
5. `route_change:` Manages route changes in the application.
6. `AutoBot:` Function that starts the automation with the settings defined by the user.

<h2>Disclaimer</h2>

<p>The developer is not responsible for any LinkedIn account blocking, improper use of the system or any problems that may arise as a result of using the bot. The use is the sole responsibility of the user.</p>

<h2>License</h2>

<p>This project is licensed under the MIT License. Click on the link below for more details.</p>

[LICENSE](https://opensource.org/license/mit)

## Contributions
</br>

<p>
  Contributions are welcome! If you want to improve the project, add new features or fix bugs, feel free to do so.
</p>
<hr>
</br>

<div align="center">
<a href="https://sidney-personal-portifolio.netlify.app/"><img src="https://img.shields.io/badge/-Portifolio-%230077B5?style=for-the-badge&logo=portifolio&logoColor=white" style="border-radius: 30px" target="_blank" /></a>
<a href="https://www.instagram.com/sidneyteodoroaraujo" target="_blank"><img src="https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white" /></a>
<a href="https://www.linkedin.com/in/sidey-teodoro-a-jr/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" style="border-radius: 30px" target="_blank" /></a>
</div>
