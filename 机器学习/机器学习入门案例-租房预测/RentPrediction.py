# 导入LSTM神经网络模型
from keras.layers import Dense, LSTM
from keras.models import Sequential
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import tensorflow.compat.v2 as tf
from keras import models
from keras.engine.functional import Functional
from sklearn.model_selection import train_test_split

# 1 导入租房因素相关数据
data = pd.read_csv("House_Rent_Dataset.csv")
print(data.head())

print(data.isnull().sum())

print(data.describe())

# 2 房屋的平均租金、中位数租金、最高租金和最低租金
print(f"Mean Rent: {data.Rent.mean()}")
print(f"Median Rent: {data.Rent.median()}")
print(f"Highest Rent: {data.Rent.max()}")
print(f"Lowest Rent: {data.Rent.min()}")

# 3 根据卧室、厅堂、厨房的数量来看一下不同城市的房屋租金情况
figure = px.bar(data, x=data["City"],
                y=data["Rent"],
                color=data["BHK"],
                title="Rent in Different Cities According to BHK")
figure.show()

# 4 根据地区类型来看一下不同城市的房屋租金情况
figure = px.bar(data, x=data["City"],
                y=data["Rent"],
                color=data["Area Type"],
                title="Rent in Different Cities According to Area Type")
figure.show()

# 5 根据房屋的装修情况，看看不同城市的房屋租金情况
figure = px.bar(data, x=data["City"],
                y=data["Rent"],
                color=data["Furnishing Status"],
                title="Rent in Different Cities According to Furnishing Status")
figure.show()

# 6 根据房子的大小来看看不同城市的房子租金情况
figure = px.bar(data, x=data["City"],
                y=data["Rent"],
                color=data["Size"],
                title="Rent in Different Cities According to Size")
figure.show()

# 7 根据数据集看一下不同城市的可出租房屋数量
cities = data["City"].value_counts()
label = cities.index
counts = cities.values
colors = ['gold', 'lightgreen']

fig = go.Figure(data=[go.Pie(labels=label, values=counts, hole=0.5)])
fig.update_layout(title_text='Number of Houses Available for Rent')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()

# 看看不同类型租户的房屋数量
# 租户的喜好
tenant = data["Tenant Preferred"].value_counts()
label = tenant.index
counts = tenant.values
colors = ['gold', 'lightgreen']

fig = go.Figure(data=[go.Pie(labels=label, values=counts, hole=0.5)])
fig.update_layout(title_text='Preference of Tenant in India')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# ****************************房屋租金预测模型****************************
# 1 把所有的分类特征转换成我们需要训练房屋租金预测模型的数值特征
data["Area Type"] = data["Area Type"].map({"Super Area": 1,
                                           "Carpet Area": 2,
                                           "Built Area": 3})
data["City"] = data["City"].map({"Mumbai": 4000, "Chennai": 6000,
                                 "Bangalore": 5600, "Hyderabad": 5000,
                                 "Delhi": 1100, "Kolkata": 7000})
data["Furnishing Status"] = data["Furnishing Status"].map({"Unfurnished": 0,
                                                           "Semi-Furnished": 1,
                                                           "Furnished": 2})
data["Tenant Preferred"] = data["Tenant Preferred"].map({"Bachelors/Family": 2,
                                                         "Bachelors": 1,
                                                         "Family": 3})
print(data.head())

# 把数据分成训练集和测试集
# 训练集：含有参考答案的数据，用来训练模型的已标注数据，用来建立模型，发现规律
# 验证集：模型训练过程中单独留出的样本集，用于调整模型的超参数和用于对模型的能力进行初步评估
# 测试集：用来评估模最终模型的泛化能力，但不能作为调参、选择特征等算法相关的选择的依据。已标注数据，通常做法是将标注隐藏，输送给训练好的模型，通过结果与真实标注进行对比，评估模型的学习能力

# 分割数据
# Scikit-learn（以前称为scikits.learn，也称为sklearn）是针对Python 编程语言的免费软件机器学习库

x = np.array(data[["BHK", "Size", "Area Type", "City",
                   "Furnishing Status", "Tenant Preferred",
                   "Bathroom"]])
y = np.array(data[["Rent"]])

xtrain, xtest, ytrain, ytest = train_test_split(x, y,
                                                test_size=0.10,
                                                random_state=42)
# Keras是一个由Python编写的开源人工神经网络库，可以作为Tensorflow、Microsoft-CNTK和Theano的高阶应用程序接口，进行深度学习模型的设计、调试、评估、应用和可视化
# 使用LSTM神经网络模型训练房屋租金预测模型
model = Sequential()
model.add(LSTM(128, return_sequences=True,
               input_shape=(xtrain.shape[1], 1)))
model.add(LSTM(64, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))
model.summary()


model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(xtrain, ytrain, batch_size=1, epochs=21)

# 使用经过训练的模型预测房屋租金
print("Enter House Details to Predict Rent")
a = int(input("Number of BHK: "))
b = int(input("Size of the House: "))
c = int(input("Area Type (Super Area = 1, Carpet Area = 2, Built Area = 3): "))
d = int(input("Pin Code of the City: "))
e = int(input("Furnishing Status of the House (Unfurnished = 0, Semi-Furnished = 1, Furnished = 2): "))
f = int(input("Tenant Type (Bachelors = 1, Bachelors/Family = 2, Only Family = 3): "))
g = int(input("Number of bathrooms: "))
features = np.array([[a, b, c, d, e, f, g]])
print("Predicted House Price = ", model.predict(features))
