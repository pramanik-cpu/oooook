import pandas as pd
import plotly.express as px

df = pd.read_csv("covid_chart")

fig= px.line(df,x="cases",y="country",color="country",title="cases per county")

fig.show()