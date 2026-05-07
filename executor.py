import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_sql(goal):

    if "klientu" in goal.lower():
        return "SELECT mēnesis, klienti FROM table"

    return "SELECT mēnesis, summa FROM table"


def generate_fake_data(goal):

    if "klientu" in goal.lower():
        return {
            "Mēnesis": ["Jan", "Feb", "Mar"],
            "Klienti": [120, 150, 180]
        }

    return {
        "Mēnesis": ["Jan", "Feb", "Mar"],
        "Summa": [500, 700, 650]
    }


def process_plan_item(item, index):

    sql = generate_sql(item["sql_goal"])
    data = generate_fake_data(item["sql_goal"])

    df = pd.DataFrame(data)

    plt.figure()

    x = df.columns[0]
    y = df.columns[1]

    if item["chart_type"] == "bar":
        df.plot(x=x, y=y, kind="bar")
    else:
        df.plot(x=x, y=y, kind="line")

    os.makedirs("output", exist_ok=True)

    path = f"output/chart_{index}.png"
    plt.savefig(path)
    plt.close()

    return {
        "title": item["title"],
        "sql": sql,
        "image": path
    }