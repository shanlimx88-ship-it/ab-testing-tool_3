import pandas as pd
from src.analyzer import Analyzer
from src.visualization import plot
from src.report import generate

df=pd.read_csv("data/sample.csv")
res=Analyzer(df).run()
plot(res)
generate(res)
print("Done. Open output/reports/report.html")
