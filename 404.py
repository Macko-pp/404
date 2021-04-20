#Imports-----------------------------------------------------------------------

import streamlit as st
import webbrowser

#Text--------------------------------------------------------------------------

st.title("404")
st.header("Page not Found")
st.subheader("This Page no longer exists")
co1, co2, co3, co4, co5 = st.beta_columns(5)

#DownArrow---------------------------------------------------------------------

arr = 1

if arr == 1:
    co4.image('DownArrow.png')

#Go-Back-&-Colomns-------------------------------------------------------------

col1, col2, col3, col4, col5 = st.beta_columns(5)
goBack = col4.button('Go Back')
colu1, colu2, colu3, colu4, colu5 = st.beta_columns(5)
colum1, colum2, colum3, colum4, colum5 = st.beta_columns(5)

if goBack:
    #webbrowser.open('https://share.streamlit.io/macko-py/aloeverawebsite/main/EnglishWebsite.py')
    colu4.write("SIKE! You gotta close the tab")
    arr = 2

#LeftArrow--------------------------------------------------------------------

if arr == 2:
    colum5.image("LeftArrow.png")

#Close-Tab---------------------------------------------------------------------

closeTab = colum4.button("Close Tab")
col1, col2, col3, column4, col5 = st.beta_columns(5)

if closeTab:
    column4.write("Sorry, I can't do that.")
    arr = 3

#LeftArrow2--------------------------------------------------------------------

columns1, columns2, columns3, columns4, columns5 = st.beta_columns(5)

if arr == 3:
    columns5.image("LeftArrow2.png")

#Do-That-----------------------------------------------------------------------

doThat = columns4.button("Do That")
columnss1, columnss2, columss3, columnss4, columnss5 = st.beta_columns(5)
if doThat:
    columnss4.markdown("No but you *actually* have to close the tab in you browser.")

#End---------------------------------------------------------------------------
