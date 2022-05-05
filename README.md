# Interactive Map
_Customised and interactive map with Python’s Folium library and Pandas._

## 🚀 Getting Started  

_Folium is a python library allowing to call the Leaflet.js Javascript library. It allows you to manipulate your data with python and map them using the power of leaflet! It is really easy to call a map using this library. This app shows the map of Bogota, and includes important data of the city such as the delimitation of its localities, the immediate attention center of the Police, Fire stations and bike paths where bicycles can ride. The data is obtained from the page "Datos Abiertos Bogotá"_. [See here](https://datosabiertos.bogota.gov.co/)

_For the web version, the Flask framework is used._

## 📋 Pre-requisites

_You must have Python installed in your local machine. All the dependencies and required libraries are included in the file_ <code>requirements.txt</code> [See here](https://github.com/Barrero0717/Interactive_Map/blob/master/requirements.txt)

_To check the Python version in your machine, just open a terminal, and try this command:_

```
python --version
```

## 🔧 Installation  

1. _Clone the repository to your local machine. To do this, run this command inside your terminal:_
```
$ git clone https://github.com/<your-github-username>/Interactive_Map.git 
```

2. _Change your directory to the cloned repo:_ 
```
$ cd Interactive_Map
```

3. _Create a Python virtual environment named 'venv' and activate it:_

Windows User
```
$ python -m venv venv
```
```
$ venv\Scripts\activate.bat
```

Linux or macOs User
```
$ python3.9 -m venv env
```
```
$ source env/bin/activate
```

4. _Install all the dependencies and required libraries:_
```
$ pip install -r requirements.txt
```

## ⚙️ Running the app 

_Open terminal. Go into the cloned project directory, activate the Python virtual environment and type the following command:_

```
python main.py
```

_and then you must open the file Map1.html and you will be able to see the map:_
![image](https://user-images.githubusercontent.com/66132335/167026551-11e6df29-a94f-4299-96c8-c4c1e0d5ddd6.png)

_At the top right you can select what you want to see on the map:_
![image](https://user-images.githubusercontent.com/66132335/167026633-426c4fd0-3b96-442b-b267-30c861ec282a.png)

_To view the web version, which uses Flask, you must view the file_<code>flask_app.py</code>

## ✒️ Authors 

* **Andrés Felipe Barrero Arce** - [Barrero0717](https://github.com/barrero0717)
