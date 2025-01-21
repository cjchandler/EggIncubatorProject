import matplotlib.pyplot as plt
import datetime
import numpy as np
import pandas as pd
from scipy.interpolate import CubicSpline
from pytz import timezone
utc = timezone('UTC')
from pysolar.solar import *
import os

# header with names
path = "/home/cjchandler/Git_Projects/incubator/"

v = "V2"
df = pd.read_csv(path + "2025-01-18_state"+ v+".csv")
df['datetime'] = pd.to_datetime(df['last_save_timestamp'], unit='s')
df = df.set_index('datetime')
print(df)
df = df.drop(['last_save_timestamp'], axis=1)

df1 = df

df = pd.read_csv( path + "2025-01-18_state"+ v+".csv")
df['datetime'] = pd.to_datetime(df['last_save_timestamp'], unit='s')
df = df.set_index('datetime')
print(df)
df = df.drop(['last_save_timestamp'], axis=1)

df2 = df 



final_df = pd.concat([  df2] )
final_df = final_df.sort_index()
final_df.drop(final_df.index[:5], inplace=True)
# ~ final_df["deltaT"] = final_df["temperature_1_C"] - final_df["temperature_2_C"] 
# ~ final_df["deltaTthermocouple"] = final_df["thermocouple_1"] - final_df["thermocouple_2"] 
# ~ final_df = final_df[["temperature_1_C" , "humidity_1", "temperature_2_C" , "humidity_2" , "deltaT" , "deltaTthermocouple", "near_switch" , "far_switch"]].copy()

final_df = final_df[["temperature_1_C" , "humidity_1","near_switch" , "heater_on","target_temperature",  "far_switch"]].copy()


final_df.plot()
plt.show()
