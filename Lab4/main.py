import pandas as pd
import numpy as np
import timeit as ti


def read():
    data = pd.read_csv("household_power_consumption.txt", sep=";")
    data = data.replace('?', np.nan)
    data = data.dropna()
    return data

df_pd = read()
df_np = df_pd.to_numpy()


#task 1
df_pd['Global_active_power'] = df_pd['Global_active_power'].astype(float)
def gl_ac_pow_more_5kw_pd():
    return df_pd[df_pd['Global_active_power']>=5.0]

df_np[:, 2] = df_np[:, 2].astype(float)
def gl_ac_pow_more_5kw_np():
    return df_np[df_np[:, 2]>=5.0]


print("Execution time for task1 pandas: ", ti.timeit(gl_ac_pow_more_5kw_pd, number=10))
print("Execution time for task1 numpy: ", ti.timeit(gl_ac_pow_more_5kw_np, number=10))
# print(gl_ac_pow_more_5kw_pd().head(10))
# print(gl_ac_pow_more_5kw_np()[:10])


#task 2
df_pd['Voltage'] = df_pd['Voltage'].astype(float)
def vol_more_235v_pd():
    return df_pd[df_pd['Voltage']>=235.0]

df_np[:, 4] = df_np[:, 4].astype(float)
def vol_more_235v_np():
    return df_np[df_np[:, 4]>=235.0]


print("Execution time for task2 pandas: ", ti.timeit(vol_more_235v_pd, number=10))
print("Execution time for task2 numpy: ", ti.timeit(vol_more_235v_np, number=10))
# print(vol_more_235v_pd().head(10))
# print(vol_more_235v_np()[:10])


#task 3
df_pd['Global_intensity'] = df_pd['Global_intensity'].astype(float)
df_pd['Sub_metering_2'] = df_pd['Sub_metering_2'].astype(float)
df_pd['Sub_metering_3'] = df_pd['Sub_metering_3'].astype(float)
def intensity_pd():
    df = df_pd[(df_pd['Global_intensity']>=19.0) & (df_pd['Global_intensity']<=20.0)]
    return df[df['Sub_metering_2']>df['Sub_metering_3']]

df_np[:, 7] = df_np[:, 7].astype(float)
df_np[:, 8] = df_np[:, 8].astype(float)
df_np[:, 5] = df_np[:, 5].astype(float)
def intensity_np():
    df = df_np[(df_np[:, 5]>=19.0) & (df_np[:, 5]<=20.0)]
    return df[df[:, 7]>df[:, 8]]


print("Execution time for task3 pandas: ", ti.timeit(intensity_pd, number=10))
print("Execution time for task3 numpy: ", ti.timeit(intensity_np, number=10))
# print(intensity_pd().head(10))
# print(intensity_np()[:10])