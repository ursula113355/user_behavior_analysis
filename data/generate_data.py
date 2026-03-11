import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000

data = pd.DataFrame(
    {
        "user_id": range(1, n + 1),
        "age": np.random.randint(18, 60, n),
        "city": np.random.choice(["New York", "Boston", "Chicago", "Seattle"], n),
        "platform": np.random.choice(["iOS", "Android", "Web"], n),
        "purchase_amount": np.random.randint(5, 200, n),
        "visit_time": np.random.choice(["Morning", "Afternoon", "Evening"], n),
    }
)

data.to_csv("data/users.csv", index=False)
print("Dataset generated.")
