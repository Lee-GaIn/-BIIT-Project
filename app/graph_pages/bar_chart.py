from pickle import NONE
from turtle import title
import streamlit as st
import pandas as pd
import altair as alt


def app():
    # Hide menu
    hide_menu = """
    <style>
    #MainMenu { visibility: hidden;}
    </style>
    """
    st.markdown(hide_menu, unsafe_allow_html=True)

    st.title("Bar chart")

    # Link css footer
    st.markdown(
        '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
        unsafe_allow_html=True)

    # Function
    # CSV file
    csv = 'https://raw.githubusercontent.com/Lee-GaIn/-BIIT-Project/main/lib/data/data.csv'
    df = pd.read_csv(csv)

    st.write("The bar chart show the Number of flight which each airline branches has in business and economy on a specific date from the user input. The statistic can only be view in latest 3 months.")
    st.write("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **For example:** Today is 30th April 2022, the statistic can be view in any date from March to May 2022.")
    st.text("Please input following format: dd/mm/yyyy")
    # Declair text input
    d = st.text_input('**Choose the date**', max_chars = 10)


    ###Price_bar
    pricechart = alt.Chart(df).mark_bar().encode(
        y=alt.Y('count(airline):O', title="Number of flight"),
        x=alt.X('class:N', title="Class"),
        color='class:N',
        column='airline:N'
    ).transform_filter(alt.FieldEqualPredicate(field='date', equal=d)
                    ).properties(height=500, width=60)
    
    pricechart_default = alt.Chart(df).mark_bar().encode(
    y=alt.Y('count(airline):O', title="Number of flight"),
    x=alt.X('class:N', title="Class"),
    color='class:N',
    column='airline:N'
    ).properties(height=500, width=60)


    ##Price button


    if d:
        st.write(pricechart)
    else:
        st.write(pricechart_default)
 
    # Footer
    st.markdown("""
    <nav class="navbar fixed-bottom navbar-expand-xl navbar-dark" style="background-color: #234362; border-top-style: solid;">
    <div style="padding-left: 650px; color: #FFFFFF; "> ©All Rights Reserved By STAFLINDA</div>
    </nav>
    """, unsafe_allow_html=True)
