#!/usr/bin/env python3

import pandas as pd

def split_date():
    d = df["Päivämäärä"].str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]

    hourmin = d["Hour"].str.split(":", expand=True)
    d["Hour"] = hourmin.iloc[:, 0]

    d["Weekday"] = d["Weekday"].map(days)
    d["Month"] = d["Month"].map(months)
    
    d = d.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    return d

def split_date_continues():
      # reading data from csv
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=";")

    # dropping unecessary rows and columns
    df = df.dropna(how = "all")
    df = df.dropna(axis = 1, how = "all")

    # extracting first column to separate var
    col = df.iloc[:,0] 
    df = df.drop(df.columns[0], axis=1) 

    # splitting data, translating
    col = col.str.split(expand = True)
    col.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    col['Hour'] = col['Hour'].str[0:2]
    
    weekdays = {
        "ma":"Mon",
        "ti":"Tue",
        "ke":"Wed",
        "to":"Thu",
        "pe":"Fri",
        "la":"Sat",
        "su":"Sun"
    }
    
    months = {
        "tammi" :1,
        "helmi" :2,
        "maalis" :3,
        "huhti" :4,
        "touko" :5,
        "kesä":6,
        "heinä" :7,
        "elo" :8,
        "syys" :9,
        "loka" :10,
        "marras" :11,
        "joulu" :12,
    }

    col["Weekday"] = col["Weekday"].map(weekdays)
    col["Month"] = col["Month"].map(months)
    col = col.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})

    res = pd.concat([col, df], axis = 1)

    return res


def cycling_weather():
    pass

def main():
    cycling_weather()

if __name__ == "__main__":
    main()
