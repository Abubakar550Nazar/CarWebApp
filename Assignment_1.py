# task 1 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

exercise = pd.read_csv("exercise.csv")
calories = pd.read_csv("calories.csv")

# print("Exercise size is : ",exercise.shape)
# print("Exercise size is : ",calories.shape)

# print("\nNew Data Display\n")

# print(exercise.head());
# print(calories.head());  

# task 2 starts 

data = pd.merge(exercise,calories,on="User_ID", how="inner")

# print("Merged data!\n")
# print(data);
# print("\nDisplay  rows only\n ")
# print(data.head());

# print("\nDisplay  lengths \n ")
# print("Lenght of rows are  : ",len(data));

# print("\nDisplay  unique rows\n ")

# print("Unique check are  : ",data["User_ID"].nunique())

# task 3
 
# print(data.info())
# print("Check Missing values \n")
# print(data.isnull().sum())

# print("Duplicate")
# print(data.duplicated().sum())
# print(data.describe())

# print(data["Gender"].value_counts())


# task 4 

# feature_plot = [
#     "Age","Height","Weight","Duration","Heart_Rate","Body_Temp"
# ]

# for feature in feature_plot:
#     plt.figure(figsize=(6,4))
#     plt.scatter(data[feature],data["Calories"],alpha=0.3)
#     plt.xlabel(feature)
#     plt.ylabel("Calories")
#     plt.title(f"{feature} vs Calories")
#     plt.tight_layout()
#     plt.show()

# understading require 
    
# plot craete hoga har predictor k against

# task-5 
# Eng feature create kiya 


# data["BMI"] = data["Weight"] / (data["Height"] / 100 ) ** 2
# data["Intensity"] = data["Heart_Rate"] * data["Duration"]
# data["Duration_sq"] = data["Duration"] ** 2 


# print(data[["BMI","Intensity","Duration_sq","Calories"]].head())
# print("Shape : ",data.shape); 



# task 6 

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# ecoder gender as number 
data["Gender"] = data["Gender"].str.lower().map({

    "female" : 0;
    "male" : 1;

})

print(data["Gender"].value_counts(dropna=False)) # verify encoding 

raw_feature = [
    "Gender", "Weight" ,"Height" , "Heart_Rate","Age","Duration","Body_Temp"]

Eng_Feature = raw_feature + ["BMI","Intensity","Duration_sq"]

model_data = data.drop(columns=["User_ID"]) # id hata de ga focus bss raining pr  


train_data , test_data = train_test_split(
    model_data,test_size=0.2,random_state=42

)

x_train_raw = train_data[raw_feature]
x_test_raw = train_data[raw_feature]

x_train_eng = train_data[Eng_Feature]
x_test_eng= test_data[Eng_Feature]

y_train = train_data[["Calories"]]
y_test = test_data[["Calories"]]

print("Training rows : ",len(train_data))
print("Testing rows",len(test_data))
print("Raw feature count : ",len(raw_feature))
print("Engineered feature count : ",len(Eng_Feature))

