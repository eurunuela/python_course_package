import plotly.express as px

def create_hr_graph(df, outfile):
    fig = px.scatter(df, x="time", y="HR", color="HR zone", hover_data=['VO2', 'VCO2', 'Speed', 'RR', 'VE', 'HR zone'])
    fig.write_html(outfile)