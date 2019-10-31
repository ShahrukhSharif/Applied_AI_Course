'''
Pandas DataFrame ---
Most Populer Library
'''

'''
Important Points --->>>
1. Read And Write Csv File 
2. groupby function
3. concat function
4. merge function
5. loc and iloc
'''

#1. Read And Write Csv File 
import pandas as pd


df = pd.read_csv("nyc_weather.csv")
df.to_csv("Writing_csv_File_Into_file.csv")
df.shape


# 2. grouby Function weather_data_cities.csv

import pandas as pd
df1 = pd.read_csv("weather_data_cities.csv")

g = df1.groupby('city')

for city,city_df in g:
    print(city)
    print(city_df)
    
paris_df = g.get_group('paris')

# DataAnalysis on Full Group

print(g.max())

# 3. concat two DataFrame

df1 = pd.DataFrame({
        "City":["jaipur","Mumbai"],
        "Tempreture":[40,80]
        })
    
df2 = pd.DataFrame({
        "City":["Singapur","Moslo"],
        "Tempreture":[10,5]
        })
    
concat_both_Citeis = pd.concat([df1,df2])


# 4. Merge Functions Simmilar Like Joins
df1 = pd.DataFrame({
        "City":["jaipur","Mumbai","Delhi","Lucknow"],
        "Tempreture":[40,80,90,89]
        })
    
df2 = pd.DataFrame({
        "City":["jaipur","Mumbai","Delhi"],
        "Humidity":[1,2,3]
        })
    
# Combine two Columns Based On one column Column
   
inner_join = pd.merge(df1,df2,on='City')

outer_join = pd.merge(df1,df2,how='outer',on='City')

#5. loc And iloc 

c1 = pd.DataFrame([1,2,3,4,5,6,7,8,9,10],index=[10,11,12,4,5,6,7,8,9,10])

# Loc we can Access Based on index Value

c1.loc[11]

c1.iloc[1]










