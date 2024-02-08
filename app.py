import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt 
df = pd.read_csv("startup_cleaned_date.csv")
df["date"] = pd.to_datetime(df["date"] ,errors="coerce")
df["month"] = df["date"].dt.month
df["year"] =df["date"].dt.year
df["subvertical"].fillna("No Name" , inplace = True)



st.set_page_config(layout="wide", page_title="StartUp Analysis") # to reduce the padding at the LHS and page icon title

# year wise top startups on the basis of the money
def year_wise_top_startups(year):
    top_startups_year_wise = pd.DataFrame(df.groupby(["year" ,"startup"])["amount"].sum()[year].sort_values(ascending = False).head())
    st.dataframe(top_startups_year_wise)

    
def city_wise_funding(city):
    funding_of_city = round(df[df["city"].str.contains(city)]["amount"].sum())
    st.metric("CityWise FUNDING :" , str(funding_of_city) + " Cr")


def load_investors_details(investor):
    st.title(investor)
    # load the recent 5 investments of the investors 
    last5_df= df[df["investors"].str.contains(investor)].head()[["date","startup","vertical","city","round","amount"]]
    st.subheader("Most Recent Investments")
    st.dataframe(last5_df)


    col1 , col2 , col3, col4 = st.columns(4)
    with col1:
        # biggest investments 
        big_series = df[df["investors"].str.contains(investor)].groupby("startup")["amount"].sum().sort_values(ascending = False).head()
        st.subheader("Biggest Investments")
        #st.dataframe(big_series)# instead of showing series i need to show graph for that i have imported matplotlib
        fig , ax = plt.subplots()
        ax.bar(big_series.index , big_series.values )
        st.pyplot(fig)
    with col2:
        vertical_series = df[df["investors"].str.contains(investor)].groupby('vertical')["amount"].sum()
        st.subheader("Sectors invested in")
        fig1 , ax1 = plt.subplots()
        ax1.pie(vertical_series , labels= vertical_series.index, autopct="%0.01f%%")
        st.pyplot(fig1)
    with col3:
        stage_series = df[df["investors"].str.contains(investor)].groupby('round')["amount"].sum()
        st.subheader("Stage wise")
        fig2 , ax2 = plt.subplots()
        ax2.pie(stage_series, labels= stage_series.index, autopct="%0.01f%%")
        st.pyplot(fig2)

    with col4:
        city_series = df[df["investors"].str.contains(investor)].groupby('city')["amount"].sum()
        st.subheader("City wise")
        fig3 , ax3 = plt.subplots()
        ax3.pie(city_series, labels= city_series.index, autopct="%0.01f%%")
        st.pyplot(fig3)



    df["year"] =df["date"].dt.year
    year_series = df[df["investors"].str.contains(investor)].groupby('year')["amount"].sum()
    st.subheader("Year - On - Year - Investments")
    fig2 , ax2 = plt.subplots()
    ax2.plot(year_series.index ,year_series.values)
    st.pyplot(fig2)

def load_overall_analysis():
    st.title("Overall Analysis")
    # total invested amount 
    total =round(df["amount"].sum())
    

    # max amount invested 
    max_funding = round(df.groupby("startup")["amount"].sum().sort_values(ascending=False).head(1).values[0])

    # avg amount invested 
    avg_funding = round(df.groupby("startup")["amount"].sum().mean())

    # total funded startup 
    num_startups = df["startup"].nunique()
    


    col1 , col2 , col3 , col4 = st.columns(4)
    with col1:
        st.metric("TOTAL : " ,str(total)+ " Cr")
    with col2:
        st.metric("MAX FUNDING : " ,str(max_funding)+ " Cr")
    with col3:
        st.metric("Avg FUNDING :" , str(avg_funding) + " Cr")
    with col4:
        st.metric("TOTAL FUNDING :" , str(num_startups) + " Cr")



    col1, col2 =st.columns(2)

    with col1:
        st.header("Overall Top-10- Startups")
        overall_startups = pd.DataFrame(round(df.groupby("startup")["amount"].sum().sort_values(ascending = False))).head(10)
        st.dataframe(overall_startups)

    with col2:
        st.header("Overall Top-10- Investors")
        overall_investors = pd.DataFrame(round(df.groupby("investors")["amount"].sum().sort_values(ascending = False))).head(10)
        st.dataframe(overall_investors)


    


    st.header("Year-Wise Top Startups:- ")
    selected_year = st.selectbox("Select City" ,sorted(list(df["year"].unique())))
    btn2 = st.button("Find Year-Wise Top Startups Details")
    if btn2:
        year_wise_top_startups(selected_year)

    

    st.header("City-Wise Funding :- ")
    selected_city = st.selectbox("Select City" ,sorted(list(df["city"].unique())))
    btn1 = st.button("Find City Funding Details")
    if btn1:
        city_wise_funding(selected_city)

    



    st.header("Month on Month Graph")
    selected_option = st.selectbox("Select type" ,["Total","Count"])
    if selected_option=="Total":
        temp_df = df.groupby(["year","month"])["amount"].sum().reset_index()
    else:

        temp_df = df.groupby(["year","month"])["amount"].count().reset_index()

    temp_df["x_axis"]=temp_df["month"].astype("str")+"-"+temp_df["year"].astype("str")
    fig3 , ax3 = plt.subplots()
    ax3.plot(temp_df["x_axis"] ,temp_df["amount"])
    st.pyplot(fig3)


def load_company_pov_analysis(startup):
    st.subheader(startup)
    #st.metric("Startup:" , str(startup))
    # to find the founde of that particulr company 
    #industry_name = df.groupby("startup")["vertical"].sum()

    col1 , col2 , col3 ,col4 = st.columns(4)
    with col1:
         
        st.subheader("Industry : - ")
        industry_name= df[df["startup"].str.contains(startup)]["vertical"].values
        st.subheader(industry_name)
        
    with col2:
        st.subheader("SubIndustry : - ")
        subindustry_name= pd.DataFrame(df[df["startup"].str.contains(startup)]["subvertical"])
        st.dataframe(subindustry_name)
        
    with col3:
        st.subheader("Location : - ")
        location_name= df[df["startup"].str.contains(startup)]["city"].values[0]
        st.subheader(location_name)
    with col4:
        st.subheader("Year : - ")
        year_name= df[df["startup"].str.contains(startup)]["year"].values[0]
        st.subheader(year_name)
        

    





st.sidebar.title("STARTUP ANALYSIS")
option = st.sidebar.selectbox("Select One",["Overall Analysis" ,"Startup","Investor"])

if option  =="Overall Analysis":
        load_overall_analysis()
    
elif option =="Startup":
    selected_startup = st.sidebar.selectbox("SELECT STARTUP",sorted(df["startup"].unique().tolist()))
    btn1 = st.sidebar.button("Find StartUp Details")
    st.title("Startup Analysis")
    if btn1:
        load_company_pov_analysis(selected_startup)
else:
    selected_investor = st.sidebar.selectbox("SELECT STARTUP",sorted(set(df["investors"].str.split(",").sum())))
    btn2 = st.sidebar.button("Find Investors Details")
    if btn2:
        load_investors_details(selected_investor)

    
