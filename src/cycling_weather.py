#!/usr/bin/env python3

import pandas as pd

#Do not modify
def split_date(df):
    split_data = df["Päivämäärä"].str.split(expand=True)
    split_data.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    split_data["Hour"] = split_data["Hour"].str[0:2]
    day_mapper = {"ma" : "Mon", "ti" : "Tue", "ke" : "Wed", 
                  "to" : "Thu", "pe" : "Fri", "la" : "Sat", "su" : "Sun"}
    split_data.replace(day_mapper, inplace=True)
    month_mapper = {
        "tammi": 1, "helmi" : 2, "maalis" : 3, "huhti" : 4, "touko" : 5,
        "kesä" : 6, "heinä" : 7, "elo" : 8, "syys" : 9, "loka" : 10, "marras" : 11,
        "joulu" : 12
    }
    split_data.replace(month_mapper, inplace= True)
    split_data = split_data.astype({"Day" : int, "Month" : int, "Year" : int, "Hour": int})
    return split_data

#Do not modify
def load_data():
    df = pd.read_csv("src\Helsingin_pyorailijamaarat.csv", sep = ";")
    df.dropna(how = "all", axis = 1, inplace = True)
    df.dropna(how = "all", inplace = True)
    return df

#Do not modify
def split_date_continues():
    df = load_data()
    split_data = split_date(df)
    return pd.concat([split_data, df.iloc[:,1:]], axis = 1)

def cycling_weather():
    df = split_date_continues()

def main():
    cycling_weather()

if __name__ == "__main__":
    main()
