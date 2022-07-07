from itertools import count
import streamlit as st 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt  
import pandas as pd
from PIL import Image
import altair as alt
import chart_studio.plotly as py
import plotly.graph_objects as go
import plotly.graph_objs as go
import plotly.express as px
import seaborn as sns
from streamlit_option_menu import option_menu
import plotly.figure_factory as ff

st.set_page_config(page_icon="woman.png",layout="wide")

##Home Title
col1, col2, col3 = st.columns([1,6,1])
col1.write("")
col2.title('Pregnancy Health Risks')
col3.write("")

##Menu Bar; contains Home, Dataset, Dashboard, Results and References.
Menu = option_menu(None, ["Home","Dataset","Dashboard"],icons=['house',"cloud","clipboard-check"],menu_icon="cast", default_index=0, orientation="horizontal", styles={"container": {"padding": "0!important", "background-color": "Pastel1[8]"},"icon": {"color": "Vivid[4]", "font-size": "25px"}, "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},"nav-link-selected": {"background-color": "Vivid[4]"},})

DATA_URL = ('Maternal Health Risk Data Set.csv')

@st.experimental_memo
def get_data() -> pd.DataFrame:
    return pd.read_csv(DATA_URL)
data=get_data()

##Home Image
image = Image.open('31409733.jpg')

if Menu=="Home": col1, col2, col3 = st.columns(3)
if Menu=="Home": col1.write("")
if Menu=="Home": col2.image(image, width=400)
if Menu=="Home": col3.write("")

##Home Introduction
if Menu=="Home": "The objective of this project is to present a dashboard to **ABAAD-Resource Center for Gender Equality** by means of launching a campaign to help women, without healthcare resources, get proper knowledge of the many health risks that are involved during pregnancy. Pregnancy symptoms and complications can range from mild and annoying discomforts to severe, sometimes life-threatening, illnesses."
if Menu=="Home": "Many problems are mild and do not progress; however, when they do, they may harm the mother or her baby."
if Menu=="Home": "Among the complications that can be found in pregnant women:"
if Menu=="Home": "- High Blood Pressure"
if Menu=="Home": "- Gestational Diabetes"
if Menu=="Home": "- Infections"
if Menu=="Home": "- Preeclampsia"
if Menu=="Home": "- Iron Deficiency Anemia"
if Menu=="Home": "- Depression"
if Menu=="Home": "- Miscarriage"
if Menu=="Home": "To avoid any complications, monitoring of the vital signs is an essential during pregnancy. These are done during prenatal visits that include tests and screenings."

image1=Image.open('vitals.JPG')
if Menu=="Home": st.image(image1)

##Dataset Metrics
if Menu=="Dataset":mcol1, mcol2, mcol3= st.columns(3)
if Menu=="Dataset":mcol1.metric("Dataset Count📋", value=data['Age'].count())
if Menu=="Dataset":mcol2.metric("Age⏳", "10-40+ yrs")
if Menu=="Dataset":mcol3.metric("Normal BP🩺", "< 120/80mmHg")

if Menu=="Dataset":col4, col5, col6= st.columns(3)
if Menu=="Dataset":col4.metric("Normal BS🍯", "7.8mmol/L")
if Menu=="Dataset":col5.metric("Normal HR❤️", "70-90b/min")
if Menu=="Dataset":col6.metric("Risk Level🔥", "High-Mid-Low")

##Table Dataset
if Menu=="Dataset":st.subheader('Dataset Overview')
if Menu=="Dataset":st.write('Data has been collected from different hospitals, community clinics, maternal health cares through the IoT based risk monitoring system.')
if Menu=="Dataset": "Dataset URL: https://www.kaggle.com/datasets/csafrit2/maternal-health-risk-data "
if Menu=="Dataset":st.write(data, width=800)

##Dataset Information
if Menu=="Dataset":st.write('**Age**: Age in years when a woman is pregnant.')
if Menu=="Dataset":st.write('**SystolicBP**: Upper value of Blood Pressure in mmHg, another significant attribute during pregnancy.')
if Menu=="Dataset":st.write('**DiastolicBP**: Lower value of Blood Pressure in mmHg, another significant attribute during pregnancy.')
if Menu=="Dataset":st.write('Healthy Blood Pressure for pregnant women should be **less than 120/80mmHg**')
if Menu=="Dataset":st.write('**BS**: Blood glucose levels is in terms of a molar concentration, mmol/L. **A normal Blood Glucose Level should be lower than 7.8mmol/L.**')
if Menu=="Dataset":st.write('**HeartRate**: A normal resting heart rate in beats per minute for pregnant a woman is about **70 to as high as 90 beats per minute.**')
if Menu=="Dataset":st.write('**BodyTemp**: A normal body temperature for pregnant a woman is about **37°C.**')
if Menu=="Dataset":st.write('**Risk Level**: Predicted Risk Intensity Level during pregnancy considering the previous attribute.') 

##Dashboards
if Menu=="Dashboard": col1, col2, col3 = st.columns(3)

#1. Pie Chart of the risk levels on pregnant women
if Menu=="Dashboard": col1.caption("**% of Women with different types of risks during pregnancy**")
labels= {"High Risk":"235", "Mid Risk":"311", "Low Risk":"373"}
colors = ['#FF9DA6', '#FED4C4','#FF6692']
sizes = (235,311,373)
explode = (0,0,0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=90)
ax1.axis('equal')
if Menu=="Dashboard": col1.write(fig1)

#2.Bar Plot of the Risk Level per age
df = (data.groupby(['Age'])['RiskLevel'].value_counts(normalize=True).rename('% RiskPerAge').mul(100).reset_index().sort_values('RiskLevel'))
fg=plt.figure(figsize=(10,8))
sns.barplot(x="RiskLevel", y="% RiskPerAge", hue="Age", palette="flare", data=df)
plt.xlabel("Risk Level")
plt.show()
if Menu== "Dashboard":col2.markdown("Risk Level vs Age")
if Menu=="Dashboard": col2.pyplot(fg)


#3. Pie Chart of range of age of pregnant women
if Menu=="Dashboard": col3.caption("**Age count of pregnant women**")
labels= {"10-15yrs":"114", "16-20yrs":"187", "21-25yrs":"205", "26-30yrs":"110","31-35yrs":"130","36-40yrs":"53","40+yrs":"120"}
colors = ['#FF9DA6', '#FED4C4','#FF6692','#F8A19F','#E377C2','#DD4477','#DA60CA']
sizes = (114,187,205,110,130,53,120)
explode = (0,0,0,0,0,0,0)
fig2, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=90)
ax1.axis('equal')
if Menu=="Dashboard": col3.write(fig2)


if Menu=="Dashboard": col1, col2, col3=st.columns(3)
#4. Bar Chart of the risk level of blood pressure on pregnant women
if Menu=="Dashboard":col1.caption("**Bar Chart of the risk level of blood pressure on pregnant women**")
if Menu=="Dashboard":fig3= alt.Chart(data).mark_bar().encode(
    x='DiastolicBP',
    y='SystolicBP',
    color='RiskLevel'
)
if Menu=="Dashboard":col1.write(fig3)

#5. Bar Chart of the risk level of blood sugar levels depending on age
if Menu=="Dashboard":col2.caption("**Bar Chart of the risk level of blood sugar levels depending on the age**")
if Menu=="Dashboard":fg1= alt.Chart(data).mark_circle(size=60).encode(
    y='Age',
    x='BS',
    color='RiskLevel',
    tooltip=['Age', 'BS', 'RiskLevel']
).interactive()
if Menu=="Dashboard":col2.write(fg1, width=800)

#6. Bar Chart of the age and level of blood pressure on pregnant women
if Menu=="Dashboard":col3.caption("**Bar Chart of the age and level of blood pressure on pregnant women**")
if Menu=="Dashboard":fig4= alt.Chart(data).mark_bar().encode(
    x='DiastolicBP',
    y='SystolicBP',
    color='Age'
)
if Menu=="Dashboard":col3.write(fig4)


#7. Heatmap of the Age and Risk Level
if Menu=="Dashboard":fig6_col1, fig7_col2 = st.columns(2)
if Menu=="Dashboard":fig6_col1.markdown("Density Heatmap showing the risk level per age")
fig6 = px.density_heatmap(
        data_frame=data, y="Age", x="RiskLevel"
    )
if Menu=="Dashboard":fig6_col1.write(fig6)

#8. Heatmap of age and systolic blood pressure
if Menu=="Dashboard":fig7_col2.markdown("Density Heatmap of Age and Systolic Blood Pressure")
fig7 = px.density_heatmap(
        data_frame=data, x="Age", y="SystolicBP"
    )
if Menu=="Dashboard": fig7_col2.write(fig7)
