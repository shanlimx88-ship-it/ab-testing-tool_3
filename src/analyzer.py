import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

class Analyzer:
    def __init__(self,df):
        self.df=df

    def run(self):
        res=[]
        for g in self.df.primary_scenario.unique():
            sub=self.df[self.df.primary_scenario==g]
            c=sub[sub.variant=='control'].retention_7d
            t=sub[sub.variant=='treatment'].retention_7d
            if len(c)==0 or len(t)==0: continue
            lift=0 if c.mean()==0 else (t.mean()-c.mean())/c.mean()
            _,p=proportions_ztest([c.sum(),t.sum()],[len(c),len(t)])
            res.append({"group":g,"lift":lift*100,"p":p})
        return pd.DataFrame(res)
