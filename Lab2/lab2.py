from urllib import request 
import re
from datetime import datetime
import os
import pandas as pd
import anima

# csv_filename_format = "DATA\\NOAA_data_province_ID={}_time={}.csv"
# datetime_format = "%d-%m-%Y_%H_%M_%S"

#TODO check if data is already exists
def __request_province_data(proovince_id = 1):
    url = "https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?country=UKR&provinceID="+str(proovince_id)+"&year1=1981&year2=2023&type=Mean"
    wp = request.urlopen(url)
    data = wp.read()
    data = data.decode('utf-8')
    start_line = data.find("year,week, SMN,SMT,VCI,TCI, VHI")
    data = data[start_line:]
    data = re.sub(r'<.*?>', '', data)   # regex to getting rid of html tags
    return data

def write_province_data_into_file(str_csv_data_provinceID, folder_name="DATA"):
    data, num = str_csv_data_provinceID
    if(type(str_csv_data_provinceID)!=tuple):
        print("function write_province_data_into_file()\n       tuple of data and provinceID is required \n        for example (data, 1),\n        where data - str of csv and 1-noaa ukr region number of Cherkasy")
        return
    open(folder_name+"\\NOAA_data_province_ID="+str(num)+"_time="+datetime.now().strftime("%d-%m-%Y_%H_%M_%S")+".csv", 'w').write(data)

def save_all_province_datas(folder_name="DATA"):
    saving_time = datetime.now()
    if not os.path.isdir(folder_name):
        os.makedirs(folder_name)

    for i in range(1, 28):
        write_province_data_into_file((__request_province_data(i), str(i)), folder_name=folder_name)
        anima.update(i)
    print("Files are saved!")
    print("Saving process time: ", datetime.now()-saving_time)

def __get_id_from_name(str_name):
    if("ID=" not in str_name):
        print("Corrupted name given get_id_from_name() ...\n     in ... get_df_from_files()")
        return
    id = re.search("ID=(.*)_time", str_name).group(1)
    return int(id)

# headers = ['Year', 'Week', 'SMN', 'SMT', 'VCI', 'TCI', 'VHI']
def get_df_from_files(folder_name="DATA"):
    saved_csvs = dict()
    for file_name in os.listdir(folder_name):
        if(".csv" in file_name):
            print(file_name)
            df = pd.read_csv(folder_name+"\\"+file_name)
            saved_csvs[__get_id_from_name(file_name)] = df
    return(saved_csvs)

    



folder_name="DATA"
if(folder_name not in os.listdir() or len(os.listdir(folder_name)) == 0):
    save_all_province_datas(folder_name="DATA")
print(get_df_from_files()[1])