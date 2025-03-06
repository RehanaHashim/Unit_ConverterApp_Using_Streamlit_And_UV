
import streamlit as st

def convert_units(value, unit_from, unit_to):
    conversions = {
        "metre_kilometer": 0.001,  # 1 meter = 0.001 kilometer
        "kilometer_metre": 1000,   # 1 kilometer = 1000 meters
        "gram_kilogram": 0.001,    # 1 gram = 0.001 kilogram 
        "kilogram_gram": 1000      # 1 kilogram = 1000 grams
    }

    key = f"{unit_from}_{unit_to}"  # Corrected key formatting

    if key in conversions:
        conversion_factor = conversions[key]  # Get the conversion factor
        return value * conversion_factor
    else:
        return "Conversion not found"

# Streamlit UI
st.title("🚀Unit Converter")  # App title

# User input for numerical value to convert
value = st.number_input("📃Enter your value:", min_value=0.0, format="%.6f")  # Allow decimals

# Dropdowns for selecting "from" and "to" units
unit_from = st.selectbox("Convert from:", ["metre", "kilometer", "gram", "kilogram"])
unit_to = st.selectbox("Convert to:", ["metre", "kilometer", "gram", "kilogram"])

# Button to trigger the conversion
if st.button("⚓Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted Value: {result}")
    