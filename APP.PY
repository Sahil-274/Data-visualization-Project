
from flask import Flask, render_template
import pandas as pd
import plotly.express as px

app = Flask(__name__)

# Load your dataset
df = pd.read_csv(r"C:\Users\singh\OneDrive\Desktop\projects\DATAVISUALIZATION\sales_data.csv")

@app.route('/')
def dashboard():
    # ---- Chart 1: Sales by Region ----
    fig1 = px.bar(df,
                  x='Region',
                  y='SALES',
                  color='Region',
                  title="Total Sales by Region")

    # ---- Chart 2: Monthly Sales Trend (per Year) ----
    fig2 = px.line(df,
                   x='MONTH',
                   y='SALES',
                   color='YEAR_ID',
                   markers=True,
                   title="Monthly Sales Trend (by Year)")

    # ---- Chart 3: Product Line Sales ----
    fig3 = px.pie(df,
                  names='PRODUCTLINE',
                  values='SALES',
                  title="Sales Distribution by Product Line")

    # Convert charts to HTML for embedding
    chart1 = fig1.to_html(full_html=False)
    chart2 = fig2.to_html(full_html=False)
    chart3 = fig3.to_html(full_html=False)

    # Pass the DataFrame (not as HTML string)
    return render_template(
        'dashboard.html',
        chart1=chart1,
        chart2=chart2,
        chart3=chart3,
        df=df
    )

if __name__ == '__main__':
    app.run(debug=True)
