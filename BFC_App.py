import streamlit as st
import pandas as pd
import math

# Quick Reference Table
data = {
    "Category": ["Essential Fat", "Athletes", "Fitness", "Average", "Obese"],
    "Women (%)": ["10.0 - 13.0", "13.1 - 20.0", "20.1 - 24.0", "24.1 - 32.0", "32.1+"],
    "Men (%)": ["2.0 - 5.0", "5.1 - 13.0", "13.1 - 17.0", "17.1 - 25.0", "25.1+"]
}

df = pd.DataFrame(data)

# Female Body Fat Calculator
def body_fat_female(age, height_in, weight_kg, neck, waist, hip):
    bf_percent = (
        163.205 * math.log10(waist + hip - neck)
        - 97.684 * math.log10(height_in)
        - 78.387
    )
    fat_mass_kg = weight_kg * (bf_percent / 100)
    lean_mass_kg = weight_kg - fat_mass_kg
    return bf_percent, fat_mass_kg, lean_mass_kg

# Male Body Fat Calculator
def body_fat_male(age, height_in, weight_kg, neck, waist):
    bf_percent = (
        86.010 * math.log10(waist - neck)
        - 70.041 * math.log10(height_in)
        + 36.76
    )
    fat_mass_kg = weight_kg * (bf_percent / 100)
    lean_mass_kg = weight_kg - fat_mass_kg
    return bf_percent, fat_mass_kg, lean_mass_kg

# Streamlit App
st.set_page_config(page_title="Body Fat Calculator")

st.title("Body Fat Calculator")
st.markdown(
    "<p style='font-size:20px;'>Enter your details below to calculate your <b>Body Fat %</b>, <b>Fat Mass</b>, and <b>Lean Mass</b>.</p>",
    unsafe_allow_html=True
)

# ---- Input Section ----
gender = st.radio("Select Gender", ["Female", "Male"])

col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age", min_value=1, max_value=120, value=25)
    height_ft = st.number_input("Height (Feet)", min_value=1, max_value=8, value=5)
    height_in_extra = st.number_input("Height (Extra Inches)", min_value=0.0, max_value=11.99, value=5.0)
    weight_kg = st.number_input("Weight (Kg)", min_value=10.0, max_value=300.0, value=65.0)
with col2:
    neck = st.number_input("Neck Circumference (inches)", min_value=5.0, max_value=80.0, value=15.0)
    waist = st.number_input("Waist Circumference (inches)", min_value=10.0, max_value=100.0, value=30.0)
    hip = None

    if gender == "Female":
        hip = st.number_input("Hip Circumference (inches)", min_value=10.0, max_value=100.0, value=35.0)

# Convert total height to inches
height_in = height_ft * 12 + height_in_extra

# ---- Calculate Button ----
if st.button("Calculate"):
    if gender == "Female":
        bf, fat, lean = body_fat_female(age, height_in, weight_kg, neck, waist, hip)
    else:
        bf, fat, lean = body_fat_male(age, height_in, weight_kg, neck, waist)

    st.subheader("Results")
    st.write(f"Body Fat Percentage: **{bf:.2f}%**")
    st.write(f"Fat Mass: **{fat:.2f} kg**")
    st.write(f"Lean Mass: **{lean:.2f} kg**")

    st.markdown("----")
    st.markdown("### 📝 Quick Reference (For Adults)")
    st.dataframe(df, hide_index=True)

st.markdown("----")
st.caption("**Developed by Nate!**")
