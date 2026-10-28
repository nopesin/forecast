import plotly.express as px
import streamlit as st
from main import get_data

# Add title, text input, slider, selectbox, and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider(
    "Forecast Days",
    min_value=1,
    max_value=5,
    help="Select the number of forecasted days",
)
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get the temperature/sky data
    filtered_data = get_data(place, days, option)
    print(filtered_data)

    if option == "Temperature":
        # Convert Kelvin to Celsius (subtract 273.15) if needed by your API preference
        temperatures = [
            (dictionary["main"]["temp"] - 273.15) for dictionary in filtered_data
        ]
        dates = [dictionary["dt_txt"] for dictionary in filtered_data]

        # Create a temperature plot
        figure = px.line(
            x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"}
        )
        st.plotly_chart(figure)

    if option == "Sky":
        images = {
            "Clear": "images/clear.png",
            "Clouds": "images/cloud.png",
            "Rain": "images/rain.png",
            "Snow": "images/snow.png",
        }
        sky_conditions = [
            dictionary["weather"][0]["main"] for dictionary in filtered_data
        ]
        image_paths = [images[condition] for condition in sky_conditions]

        # Display the weather images with timestamps underneath or in a grid row
        st.image(image_paths, width=115)