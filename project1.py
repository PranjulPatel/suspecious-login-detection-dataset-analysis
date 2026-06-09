import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("/home/kasm-user/Desktop/python/tableConvert.com_1cil4b.csv")

print(data.head())

print(data.isnull().sum())

data.drop("Round-Trip Time [ms]",axis=1,inplace=True)

print(data.isnull().sum())

data.dropna(subset=["City","Region"],inplace=True)
print(data.isnull().sum())

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