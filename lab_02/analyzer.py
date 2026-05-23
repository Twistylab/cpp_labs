import csv
import matplotlib.pyplot as plt


if __name__ == "__main__":
    df_cpp = {"time": [], "n": []}

    with open("result_cpp.csv", 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            time = float(row["time"])
            n = int(row["n"])

            df_cpp["time"].append(time)
            df_cpp["n"].append(n)

    df_py = {"time": [], "n": []}

    with open("result_py.csv", 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            time = float(row["time"])
            n = int(row["n"])

            df_py["time"].append(time)
            df_py["n"].append(n)

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(1, 1, 1)

    ax.plot(df_cpp["time"], df_cpp["n"], color="red", label="cpp")
    ax.plot(df_py["time"], df_py["n"], color="blue", label="py")
    ax.legend()
    ax.set_xlabel("time")
    ax.set_ylabel("n")
    fig.savefig("result.png")

