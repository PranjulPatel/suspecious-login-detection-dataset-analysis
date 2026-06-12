import pandas as pd
import matplotlib.pyplot as plt

# reading the dataset
data=pd.read_csv("dataset/tableConvert.com_1cil4b.csv")

print(data.head())

#checking null values
print(data.isnull().sum())

#removing null data
data.drop("Round-Trip Time [ms]",axis=1,inplace=True)

print(data.isnull().sum())

#removing null values
data.dropna(subset=["City","Region"],inplace=True)
print(data.isnull().sum())

#remove duplicate values
data.drop_duplicates(inplace=True)
data.to_csv("cleaned_login_data.csv",index=False)

print(data.isnull().sum())
print("Duplicate Records:", data.duplicated().sum())

#top 10 login countries 
country_counts=data["Country"].value_counts().head(10)
plt.figure(figsize=(8,5))
plt.bar(country_counts.index, country_counts.values)
plt.title("Top 10 login countries")
plt.xlabel("Country")
plt.ylabel("Number of Logins")
plt.xticks(rotation=45)
plt.savefig("top10plot.png", dpi=300,bbox_inches="tight")
plt.close()

# Device usage analysis
device_counts = data['Device Type'].value_counts()

plt.figure(figsize=(6,4))
plt.bar(device_counts.index,device_counts.values)

plt.title("Device usage")
plt.xlabel("Device Type")
plt.ylabel("Count")
plt.savefig("deviceUsage.png", dpi=300,bbox_inches="tight")
plt.close()
plt.show()

#Browse Usage Analysis
browser_count=data["Browser Name and Version"].value_counts()

plt.figure(figsize=(8,5))
plt.bar(browser_count.index,browser_count.values)

plt.title("Browser usage")
plt.xlabel("Browser")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.savefig("BrowseUsage.png", dpi=300,bbox_inches="tight")
plt.close()

plt.show()

#Failed Attempt Distribution
plt.figure(figsize=(8,5))

plt.hist(data["Is Attack IP"].astype(int))
plt.title("Failed login attempts")
plt.xlabel("Failed Attempts")
plt.ylabel("frequency")
plt.savefig("Failedattempts.png", dpi=300,bbox_inches="tight")
plt.close()
plt.show()

# threat monitoring scatter plot
data["Login Timestamp"]=pd.to_datetime(data["Login Timestamp"])
attack_data=data[data["Is Attack IP"]==True]
plt.figure(figsize=(12,6))

plt.scatter(
    attack_data["Login Timestamp"],
    attack_data["User ID"],
    alpha=0.6
)

plt.title("Threat Monitoring Scatter Plot")
plt.xlabel("Login Timestamp")
plt.ylabel("User ID")

plt.xticks(rotation=45)

plt.savefig("ThreatMonitoringScatter Plot.png",dpi=300,bbox_inches="tight")
plt.close()

#Current threat guage
attack_count=data["Is Attack IP"].sum()
safe_count=len(data)-attack_count

plt.figure(figsize=(6,6))

plt.pie(
    [attack_count,safe_count],
    labels=["Threats","Safe"],
    autopct="%1.1f%%"
)

plt.title("current Threat Gauge")
plt.savefig("currentthreatGuage Plot.png",dpi=300,bbox_inches="tight")
plt.close()

# Suspecious login Loacation Analysis 
Suspecious = data[data["Is Attack IP"]==True]
location_counts = Suspecious["Country"].value_counts().head(10)
plt.figure(figsize=(10,5))
plt.bar(location_counts.index,
        location_counts.values)
plt.title("Suspicious Login Locations")
plt.xlabel("Country")
plt.ylabel("Attack Count")
plt.xticks(rotation=45)
plt.savefig("SuspiciousLocations.png", dpi=300, bbox_inches="tight")
plt.close()