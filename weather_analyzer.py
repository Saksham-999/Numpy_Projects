import requests
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from datetime import datetime,timezone


def normalize(values, min_val, max_val):
    return [(v - min_val) / (max_val - min_val) * 100 for v in values]


def plot_radar(c1,c1_values,c2,c2_values,parameters):
     num_para=len(parameters)
     # Close the circle by repeating first value
     c1_values += c1_values[:1]
     c2_values += c2_values[:1]
     #angles for each parameter
     angles=np.linspace(0,2*np.pi,num_para,endpoint=False).tolist()
     angles += angles[:1]
     #creating figure and axes for plotting(radar plot)
     fig, ax =plt.subplots(subplot_kw=dict(polar=True))
     ax.plot(angles,c1_values,label=c1,marker='o',color="skyblue")
     ax.fill(angles,c1_values,color='skyblue',alpha=0.25)
     ax.plot(angles,c2_values,label=c2,marker='o',color="red")
     ax.fill(angles,c2_values,color='red',alpha=0.25)
     #defining position of axes(spokes)
     ax.set_xticks(angles[:-1])           #we have to leave last angle as we added 1st value again in last before
     ax.set_xticklabels(parameters)       #label each angle with parameter name
     ax.set_yticklabels([])               #showing nothing
     ax.set_title(f"{c1} VS {c2}",size=10,pad=10)
     ax.legend(loc="upper right", bbox_to_anchor=(1.2,1.1))
     plt.show()
     


cities=["Kathmandu","Pokhara","Bharatpur","Biratnagar","Hetauda","Butwal","Dhankuta"]
API_key="8dc880c4bb2b9e670aa3339d20e449f1"

#current weather
def current(cities,API_key):
     c_temps, c_humidities, c_winds, c_clouds = [], [], [], []
     for city in cities:
          url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
          response=requests.get(url)
          data=response.json()
          c_temps.append(data["main"]["temp"] - 273.15)
          c_humidities.append(data["main"]["humidity"])
          c_clouds.append(data["clouds"]["all"])
          c_winds.append(data["wind"]["speed"])

     c_temps=np.array(c_temps)
     c_humidities=np.array(c_humidities)
     c_clouds=np.array(c_clouds)
     c_winds=np.array(c_winds)

     index=np.where(c_temps==np.max(c_temps))     #gives tuple with one array
     index1=index[0][0]                           #1st array in tuple ,1st element
     print(f"Hottest city is {cities[index1]} with temp {np.max(c_temps)}")
     index=np.where(c_temps==np.min(c_temps))     #gives tuple with one array
     index2=index[0][0]                            #1st array in tuple ,1st element
     print(f"Coolest city is {cities[index2]} with temp {np.min(c_temps)}")
     print("Average Temp across all cities:", np.mean(c_temps))
     print("Average Humidity across all cities:", np.mean(c_humidities))
     print("Average Wind Speed across all cities:", np.mean(c_winds))
     print("Average Cloudiness acroess all cities:", np.mean(c_clouds))

     # Defining max and min for each parameter
     temp_range = (0, 57)      # °C
     humidity_range = (0, 100) # %
     wind_range = (0, 25)      # m/s
     clouds_range = (0, 100)   #%

     parameters= ["Temperature(% of 57C) ", "Humidity(%)", "Wind(% of 25m/s)", "Clouds(%)"]
     print()
     print("enter two cities to compare")
     c1=int(input("0.Kathmandu 1.Pokhara 2.Chitwan 3.Biratnagar 4.Hetauda 5.Butwal 6.Dhankuta "))
     c2=int(input("0.Kathmandu 1.Pokhara 2.Chitwan 3.Biratnagar 4.Hetauda 5.Butwal 6.Dhankuta "))
     # Normalize each city’s data
     c1_values = normalize([c_temps[c1]], *temp_range) + \
                 normalize([c_humidities[c1]], *humidity_range) + \
                normalize([c_winds[c1]], *wind_range) + \
                normalize([c_clouds[c1]], *clouds_range)

     c2_values = normalize([c_temps[c2]], *temp_range) + \
                normalize([c_humidities[c2]], *humidity_range) + \
                normalize([c_winds[c2]], *wind_range) + \
                normalize([c_clouds[c2]], *clouds_range)

     plot_radar(cities[c1],c1_values,cities[c2],c2_values,parameters)

def compare(API_key):
     city=input("enter valid city name")
     #current hour in 24h format and round to nearest 3-hour slot(intevals for the forecast)
     now=datetime.now(timezone.utc)
     current_hour=now.hour
     nearest_hour = (3 * round(current_hour / 3)) % 24
     str_time=f"{nearest_hour:02d}:00:00"

     #fetching data of 5 day forecast
     url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_key}&units=metric"
     data = requests.get(url).json()
     
     dates=[]
     temps=[]
     for entry in data['list']:
       if entry['dt_txt'].endswith(str_time):
           date = entry['dt_txt'].split(" ")[0]
           temp = entry['main']['temp']
           dates.append(date)
           temps.append(temp)

     temps=np.array(temps)         #numpy array for calculations

     mean_temp = np.mean(temps)
     max_temp = np.max(temps)
     min_temp = np.min(temps)
     i=0
     for date in dates:
        print("At this very time")
        print(f"date:{date} <-> {temps[i]} degree Celcius")
        i=i+1
     print("At this very time , temperature might reach following parameters")
     print(f"Mean: {mean_temp:.2f}°C, Max: {max_temp:.2f}°C, Min: {min_temp:.2f}°C")

     #plotting bar diagram
     height=6
     width=10
     #color based in temperatures
     colors = []
     for temp in temps:
       if temp < 10:
          colors.append("blue")       # cold
       elif 10 <= temp <= 25:
          colors.append("green")      # moderate
       else:
          colors.append("red")        # hot
     
     plt.figure(figsize=(width, height))
     bars=plt.bar(dates,temps,color=colors)
     # Create custom legend
     legend_elements = [
        Patch(facecolor='red', label='Hot'),
        Patch(facecolor='green', label='Moderate'),
        Patch(facecolor='blue', label='Cold')
     ]
     plt.legend(handles=legend_elements)
     plt.ylabel("Temperature (°C)")
     plt.title("Temperature at this time for different days")
     plt.show()


want=int(input("enter: \n      1 for current weather data \n      2 for temperature comparision of 5 days forecast"))
if(want==1):
    current(cities,API_key)
elif(want==2):
    compare(API_key)
else:
    print("Invalid input")


