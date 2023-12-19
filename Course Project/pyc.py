import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("amazon.csv")
# print(df)


# df[['category']] = str(df[['category']]).split("|")
df['category'] = df['category'].str.split('|').str[1]
print(df[['category']])
print(str(df[['category']]).split("|"))



df = df.fillna(method="bfill")

num_df = df.iloc[:, 2:8]
spec_idx = num_df[num_df['rating'] == "|"].index[0]
num_df.iloc[spec_idx] = num_df.iloc[spec_idx-1]


def parse_cash(value):
    return float(value[1:].replace(",", ""))


def parse_percentage(value):
    return int(value[:-1])


def parse_to_int(value):
    return int(value.replace(",", ""))


def parse_to_flt(value):
    return float(value.replace(",", ""))


num_df['discounted_price'] = num_df['discounted_price'].apply(parse_cash)
num_df['actual_price'] = num_df['actual_price'].apply(parse_cash)
num_df['discount_percentage'] = num_df['discount_percentage'].apply(parse_percentage)
num_df['rating_count'] = num_df['rating_count'].apply(parse_to_int)
num_df['rating'] = num_df['rating'].apply(parse_to_flt)


print('=========================Before standartisation=====================')
print(num_df.head(2))
print(num_df.mean())


def mean(df_col):
    return df_col.sum()/len(df_col)
def standart_diviation(df_col):   # <--- Dispersion
    mean_f = mean(df_col)
    sum_of_the_squered_differences = 0
    for i in range(len(df_col)):
        sum_of_the_squered_differences += (df_col[i]-mean_f)**2
    return math.sqrt(sum_of_the_squered_differences/len(df_col))
def standartise(df_column):
    return (df_column-mean(df_column)) / standart_diviation(df_column)

std_num_df = num_df.copy()
std_num_df ['discounted_price'] = standartise(num_df['discounted_price'])
std_num_df ['actual_price'] = standartise(num_df['actual_price'])
std_num_df ['rating'] = standartise(num_df['rating'])
std_num_df ['discount_percentage'] = standartise(num_df['discount_percentage'])
std_num_df ['rating_count'] = standartise(num_df['rating_count'])

print('=========================After standartisation=====================')
print(std_num_df.head(2))
print(std_num_df.mean())



scaler = StandardScaler()

scaler_num_df = pd.DataFrame(scaler.fit_transform(num_df.iloc[:,1:]), columns=num_df.columns[1:])

print('=========================After scaler=====================')
print(scaler_num_df.head(2))
print(scaler_num_df.mean())



