#importing libraries
import streamlit as st 
import pandas as pd
import plotly.express as px

car_df = pd.read_csv('P:/DevTools/Projects/Python/Web-App-Project/vehicles_us.csv') #read csv file

st.title('Car Sales Data Explorer') #app title
st.write('--This web app allows you to explore and visualize data of car sales ads--') #description

st.header('Search a vehicle:') #header for searching a vehicle

ordered_models = sorted(car_df['model'].dropna().unique()) #sort models alphabetically
selected_model = st.selectbox('Please select a car brand', ordered_models) #select box for car brands

if selected_model:
    #show only years available for the selected model
    years_for_model = car_df[car_df['model'] == selected_model]['model_year'].dropna().unique()
    years_for_model = sorted(years_for_model)
    search_car_1 = st.selectbox('Please select the year', years_for_model)
    filtered_table = car_df[(car_df['model'] == selected_model) & (car_df['model_year'] == search_car_1)]
    st.dataframe(filtered_table) # show df of selected model and year

st.header("Explore Data Distributions") #header
st.write("Select a histogram type to visualize different aspects of the car sales data.") #write message

#options for the selectbox
hist_options = ["Price Distribution for Selected Model",
                "Odometer Distribution for Selected Model",
                "Cars Sold by Model Year",
                "Distribution by Condition",
                "Price Distribution by Fuel Type",
                "Distribution by Transmission Type"]

hist_choice = st.selectbox("Choose histogram type", hist_options) #select box for histogram options
hist_button = st.button('Create histogram') #press button to show histogram

if hist_button:
    if hist_choice == "Price Distribution for Selected Model":
        st.write(f'Histogram of prices for {selected_model}')
        filtered_df = car_df[car_df['model'] == selected_model]
        fig = px.histogram(filtered_df, x="price", 
                           title=f"Price Distribution for {selected_model}",
                           template="plotly_white"
                           )
        fig.update_layout(xaxis_title="Price (USD)",
                          yaxis_title="Number of Cars",
                          font=dict(size=14),
                          title_font=dict(size=20),
                          bargap=0.1 #gap between bars
        )
        st.plotly_chart(fig, use_container_width=True)
    elif hist_choice == "Odometer Distribution for Selected Model":
        st.write(f'Odometer distribution for {selected_model}')
        filtered_df = car_df[car_df['model'] == selected_model]
        fig = px.histogram(filtered_df, x="odometer", 
                           title=f"Odometer Distribution for {selected_model}",
                           template="plotly_white"
                           )
        fig.update_layout(xaxis_title="Odometer (miles)",
                          yaxis_title="Number of Cars",
                          font=dict(size=14),
                          title_font=dict(size=20),
                          bargap=0.1 #gap between bars
        )
        st.plotly_chart(fig, use_container_width=True)
    elif hist_choice == "Cars Sold by Model Year":
        st.write('Number of cars sold by model year')
        fig = px.histogram(car_df, x="model_year", 
                           title="Cars Sold by Model Year",
                           template="plotly_white"
                           )
        fig.update_layout(xaxis_title="Model Year",
                          yaxis_title="Number of Cars Sold",
                          font=dict(size=14),
                          title_font=dict(size=20),
                          bargap=0.1 #gap between bars
         )
        st.plotly_chart(fig, use_container_width=True)
    elif hist_choice == "Distribution by Condition":
        st.write('Distribution by car condition')
        fig = px.histogram(car_df, x="condition", 
                           title="Distribution by Condition",
                           template="plotly_white"
                           )
        fig.update_layout(xaxis_title="Condition",
                          yaxis_title="Number of Cars",
                          font=dict(size=14),
                          title_font=dict(size=20),
                          bargap=0.1 #gap between bars
        )
        st.plotly_chart(fig, use_container_width=True)
    elif hist_choice == "Price Distribution by Fuel Type":
        st.write('Price distribution by fuel type')
        fig = px.histogram(car_df, x="price", color="fuel", 
                           title="Price Distribution by Fuel Type",
                           template="plotly_white"
                           )
        fig.update_layout(xaxis_title="Price (USD)",
                          yaxis_title="Number of Cars",
                          font=dict(size=14),
                          title_font=dict(size=20),
                          bargap=0.1 #gap between bars
        )
        st.plotly_chart(fig, use_container_width=True)
    elif hist_choice == "Distribution by Transmission Type":
        st.write('Distribution by transmission type')
        fig = px.histogram(car_df, x="transmission", 
                           title="Distribution by Transmission Type",
                           template="plotly_white"
                           )
        fig.update_layout(xaxis_title="Transmission Type",
                          yaxis_title="Number of Cars",
                          font=dict(size=14),
                          title_font=dict(size=20),
                          bargap=0.1 #gap between bars
        )
        st.plotly_chart(fig, use_container_width=True)

st.header("Explore Relationships Between Variables") #header
st.write("Create a scatter plot to analyze relationships between car attributes.") #write message

#options for the selectbox
x_options = ["model_year", "odometer", "price"]
y_options = ["price", "odometer"]
categorize_options = ["condition", "fuel", "transmission", "paint_color"] 

x_axis = st.selectbox("Select X-axis", x_options, index=0) #select box for x-axis
y_axis = st.selectbox("Select Y-axis", y_options, index=0) #select box for y-axis
categorize_by = st.selectbox("Categorize by", categorize_options, index=0) #select box for "categorize by" option

scatt_button = st.button('Create a scatter plot') #press button to show scatter plot

if scatt_button:
    st.write(f'Scatter plot for: {selected_model}')
    filtered_df = car_df[car_df['model'] == selected_model]
    fig = px.scatter(filtered_df,
                     x=x_axis,
                     y=y_axis,
                     color=categorize_by,
                     hover_data=["odometer", "fuel", "transmission"],
                     template="plotly_white",
                     title=f"{y_axis.title()} vs {x_axis.title()} for {selected_model} (categorize by {categorize_by})"
    )
    fig.update_layout(font=dict(size=14), title_font=dict(size=20))
    st.plotly_chart(fig, use_container_width=True) 