#Loading all libraries

import streamlit as st
# For Streamlit capabilities

import pandas as pd        
# For data manipulation and analysis

import plotly.express as px
# For creating more historgrams and scatterplots

# Reading the dataset's CSV file into a Pandas DataFrame
Vehicles= pd.read_csv("vehicles_us (1).csv")

st.header("Sprint 4, Software Development Tools: Project, by Ashley Dutt ")
st.markdown("In this project I will first review the data given from a .csv that holds sales information of a car dealership. After reviewing the data, I will then conduct an EDA that will include a histogram and scatterplot with a checkbox that changes the behavior of the components.")

st.header("Initial Observation of Data")

st.header('Data Viewer')
st.dataframe(Vehicles)
st.markdown("There are 51525 total lines of data.")
st.markdown("Parts of the data set that have missing (NaN) data are within the following columns: model_year, cylinders, odometer, paint_color, is_4wd. Parts of the data set that have missing (NaN) data are within the following columns: model_year, cylinders, odometer, paint_color, is_4wd. Due to the lack of context, I can not clean up the data to ensure that all NaN values are replaced with accurate data. However, I will replace the Nan values under cylinder and attempt to define the number of cylinders with a high confidence level that if I group the data by model and model's year and then take a median number of cylinders.")
st.markdown("The best comparison and most accurate analysis of this data can be done with the following columns: price, model, condition, fuel, transmission, type, date_posted and days_listed.")
st.markdown("Some analysis that I would like to perform on this given data set is a comparison of how different types of car types compare against each other in prices, and analyze if car models correlate with days_listed.")

st.header("Analysis of Car Types and Prices")

# Creating the scatter plot
fig = px.scatter(
       Vehicles,
       x='type',
       y='price',
       color='type',
       title='Car Type vs. Price',
       labels={'price': 'Price', 'type': 'Car Type'}
   )
# Display with Streamlit
st.title('Car Price Analysis')
st.plotly_chart(fig)

st.header("Analysis Conclusion")
st.markdown("Based on the histogram above, the most expensive vehicles tend to be convertibles or trucks. Hatchbacks, buses, and 'other' types of cars are the cheapest. This histogram also shows that convertibles, trucks, and coupes have the highest volume of sales. Hatchbacks have the lowest sales.We can say that convertibles are this dealership's most popular and highest revenue generating commodity while hatchbacks are it's lowest.")


st.header("Analysis of Fastest and Slowing Selling Cars")

show_histogram = st.checkbox('Show Histogram')

if show_histogram:
    fig = px.histogram(
        Vehicles,
        x='days_listed',
        color='type',
        title='Fastest and Slowest Selling Car Types',
        labels={'days_listed': 'Days Listed', 'type': 'Car Type'},
        color_discrete_sequence=px.colors.qualitative.Set1)  
           # Use a predefined color sequence

st.plotly_chart(fig)

st.markdown("From this histogram, we can see that buses are the slowest selling cars on this lot. We can also conclude that on average, cars are listed between 20-40 days.")

st.header("Overall Conclusion")
st.markdown("Trucks and pickups make the most and fastest money for this dealership. If I had to guide this dealership on where to spend it's advertisement money, I would advise to spend it on advertising their buses to increase their lowest revenue and slowest selling products based on the analysis above.")



