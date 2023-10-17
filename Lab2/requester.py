from urllib import request 
from datetime import datetime
import pandas as pd
import re
import os
from settings import change_map
from settings import header
import anima


def request_province_data(proovince_id = 1):
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
        write_province_data_into_file((request_province_data(i), str(i)), folder_name=folder_name)
        anima.update(i)
    print("Files are saved!")
    print("Saving process time: ", datetime.now()-saving_time)


def get_id_from_name(str_name):
    if("ID=" not in str_name):
        print("Corrupted name given get_id_from_name() ...\n     in ... get_df_from_files()")
        return
    id = re.search("ID=(.*)_time", str_name).group(1)
    return int(id)


def get_df_from_files(folder_name="DATA"):
    saved_csvs = dict()
    for file_name in os.listdir(folder_name):
        if(".csv" in file_name):
            df = pd.read_csv(folder_name+"\\"+file_name, usecols = ['year', 'week', ' SMN', 'SMT', 'VCI', 'TCI', ' VHI'])
            df.columns = header
            saved_csvs[get_id_from_name(file_name)] = df
    return(saved_csvs)


def change_indices(dict_to_change, change_layout):
    if(type(change_layout) is not dict):
        return
    rewritten_dict = dict()
    for key in dict_to_change:
        rewritten_dict[change_layout[key]] = dict_to_change[key]
    return rewritten_dict


def VHI_extr(df):
    vhi_df = df[['Year','VHI']]
    return(vhi_df, min(vhi_df['VHI']), max(vhi_df['VHI']))


def VHI_drought_above(df, min_VHI):
    return df[(min_VHI<df["VHI"]) & (df["VHI"]<40)][["Year", "VHI"]].reset_index(drop=True)


def moderate_VHI_below(df, max_VHI):
    return df[(60<df["VHI"]) & (df["VHI"]<max_VHI)][["Year","VHI"]].reset_index(drop=True)


def request_data():
    folder_name="DATA"
    if(folder_name not in os.listdir() or len(os.listdir(folder_name)) == 0):
        save_all_province_datas(folder_name=folder_name )
    dfs = get_df_from_files()
    dfs = change_indices(dfs, change_map)

    begin = sorted(list(dfs.keys()))[0]
    for df_ind in range(begin, len(dfs)+begin):
        dfs[df_ind] = dfs[df_ind].drop(
            dfs[df_ind].loc[dfs[df_ind]["VHI"]<=-0.9].index)
            
    return dfs


def lab2_task_folower():
    dfs = request_data()

    #min max VHI
    vhi_1, minv, maxv = VHI_extr(dfs[1])
    print("min_vhi: ", minv, "\n","max_vhi: ", maxv)
    print(vhi_1)

    #drough VHI
    cond_VHI = VHI_drought_above(dfs[1], 30)
    print(cond_VHI)

    #moderate VHI
    moderate_VHI = moderate_VHI_below(dfs[1], 80)
    print(moderate_VHI)