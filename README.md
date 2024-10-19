## Sprint-4-Project by Ashley Dutt
TripleTen Sprint 4 Project 

# Initialization
I created a profile within Github and created this very repository with a README.md file and .gitignore file as a Python template. I made a new python environment and installed the following packages: pandas, streamlit, plotly.express, and altair. I then created an account on render.com and linked it to my GitHub. I then installed VS Code and loaded the project into VS Code using git to clone. Throughout my time working on this project, I was commiting and then pushing back the changes to the GitHub Repository. 

# Inital Review of Data
Since we weren't given a specifc task to perofrm analysis on the dataset. I did a first review with the following python methodologies: Vehicles.info(), Vehicles.describe(), Vehicles.duplicated().sum(), Vehicles.sample(), Vehicles.head().

## Initial Observation
There are 51525 total lines of data. Parts of the data set that have missing (NaN) data are within the following columns: model_year, cylinders, odometer, paint_color, is_4wd. Due to the lack of context, I can not clean up the data to ensure that all NaN values are replaced with accurate data. The best comparison and most accurate analysis of this data can be done with the following columns: price, model, condition, fuel, transmission, type, date_posted and days_listed. Some analysis that I would like to perform on this given data set is a comparison of how different types of car types compare against each other in prices, and analyze if car type correlates with days_listed. 

# Analysis of Car Types and Prices 
I used the following plotly.express code to create a scatterplot to help me perform the analysis below:
<img width="539" alt="image" src="https://github.com/user-attachments/assets/2b75a35d-94d9-4e37-a5ad-aeabfe51008b">

Based on the histogram above, the most expensive vehicles tend to be trucks and pickups. Sedans and SUV's are the cheapest. This histogram also shows that SUV, pickups, and truck's have the highest volume of sales. Offraods and bus types have the lowest sales and volumes.We can claim that trucks and pickups are this dealership's most popular and highest revenue generating commodity while buses are it's lowest.

# Analysis of Car Types and Days Listed
I used the following plotly.express code to create a histogram to help me perform the analysis below:
<img width="512" alt="image" src="https://github.com/user-attachments/assets/0f861b70-ddc8-4409-91db-394ea414538a">

From this histogram, we can see that buses are the slowest selling cars on this lot. We can also conclude that on average, cars are listed between 20-40 days. 

# Overall Conclusion
Trucks and pickups make the most and fastest money for this dealership. If I had to guide this dealership on where to spend it's advertisement money, I would advise to spend it on advertising their buses to increase their lowest revenue and slowest selling products based on the analysis above. 

## Project Wrap-up
After finishing up the code, I translated all my pthyon code housed in the .ipynb file into the app.py for streamlit. After I created the app.py, I used "streamlit run app.py" to view my web app on the https;//localhost:8501 page and saw that my code was indeed protraying my analysis how I intended it to. 
