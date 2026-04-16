import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot(df):
    os.makedirs("output/figures",exist_ok=True)

    plt.figure()
    plt.bar(df['group'], df['lift'])
    plt.title("Lift by Segment")
    plt.savefig("output/figures/bar.png")
    plt.close()

    plt.figure()
    sns.heatmap(df[['lift']].T, annot=True)
    plt.savefig("output/figures/heatmap.png")
    plt.close()
