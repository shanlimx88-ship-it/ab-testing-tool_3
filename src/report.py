from datetime import datetime

def generate(df):
    import os
    os.makedirs("output/reports", exist_ok=True)
    rows=""
    for _,r in df.iterrows():
        rows+=f"<tr><td>{r.group}</td><td>{r.lift:.2f}%</td><td>{r.p:.4f}</td></tr>"

    html=f'''
    <html>
    <head>
    <style>
    body{{font-family:Arial;padding:40px}}
    .card{{background:#eee;padding:20px;margin-bottom:20px}}
    table{{border-collapse:collapse;width:100%}}
    th,td{{border:1px solid #ddd;padding:8px}}
    th{{background:#333;color:white}}
    </style>
    </head>
    <body>
    <h1>Heterogeneity Dashboard</h1>
    <p>{datetime.now()}</p>

    <div class="card">
    <h2>Summary</h2>
    <p>Segments analyzed: {len(df)}</p>
    </div>

    <img src="../figures/bar.png" width="500"/>
    <img src="../figures/heatmap.png" width="500"/>

    <h2>Details</h2>
    <table>
    <tr><th>Group</th><th>Lift</th><th>p</th></tr>
    {rows}
    </table>

    </body></html>
    '''

    with open("output/reports/report.html","w") as f:
        f.write(html)
