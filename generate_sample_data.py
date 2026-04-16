import pandas as pd
import numpy as np
import os

np.random.seed(42)

def generate():
    n=5000
    users=[f"user_{i}" for i in range(n)]
    variant=np.random.choice(['control','treatment'],n)
    scenario=np.random.choice(['coding','writing','general'],n)

    base=0.5
    data=[]
    for i in range(n):
        p=base
        if variant[i]=='treatment':
            if scenario[i]=='coding': p+=0.15
            elif scenario[i]=='writing': p-=0.05
            else: p+=0.02
        y=np.random.binomial(1,max(0.1,min(0.9,p)))
        data.append([users[i],variant[i],scenario[i],y])

    df=pd.DataFrame(data,columns=["user_id","variant","primary_scenario","retention_7d"])
    os.makedirs("data",exist_ok=True)
    df.to_csv("data/sample.csv",index=False)

if __name__=="__main__":
    generate()
