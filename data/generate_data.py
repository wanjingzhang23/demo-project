import random
import pandas as pd

data = []

for i in range(1000):
    bet_amount = random.randint(10, 10000)
    win_rate = random.random()
    session_time = random.randint(1, 60)

    fraud = 1 if (bet_amount > 5000 and win_rate > 0.8) else 0

    data.append([bet_amount, win_rate, session_time, fraud])

df = pd.DataFrame(data, columns=["bet_amount", "win_rate", "session_time", "fraud"])
df.to_csv("events.csv", index=False)

print("Data generated successfully!")