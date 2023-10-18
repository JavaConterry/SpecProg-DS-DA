import requester

data = requester.request_data()
# print(data[3])
df_copy = data[3].copy()

# print(df_copy)
# 
df_copy = df_copy.reset_index(drop=True)
for i in range(len(df_copy[['Year','Week']].values)):
    df_copy['Week'][i] = str(df_copy['Year'][i]).join(str(df_copy['Week'][i]))

print(df_copy)
