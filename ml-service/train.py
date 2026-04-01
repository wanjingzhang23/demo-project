import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# 读取数据
df = pd.read_csv("data/events.csv")

X = df[["bet_amount", "win_rate", "session_time"]]
y = df["fraud"]

# 训练模型
model = LogisticRegression()
model.fit(X, y)

# 保存模型
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained successfully!")