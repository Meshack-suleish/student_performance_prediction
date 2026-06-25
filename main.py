import joblib
import numpy as np
import streamlit as st

model = joblib.load("student_performance.joblib")

st.title("Student Performance Prediction")
st.write(
    """
    This app predicts the performance of a student based on various features.
    Please input the required details below:
    """
)

# Custom CSS for button styling
st.markdown("""
    <style>
        .stButton>button {
            color: white;
            padding: 10px 20px;
            border-radius: 10px;
            border: none;
        }
        .stButton>button:hover {
            background-color: #3a6fd8;
        }
    </style>
""", unsafe_allow_html=True)


# Input fields
gender = st.selectbox("Gender", options=["Male", "Female"])
study_hours = st.slider("Study Hours per Week", min_value=0, max_value=100, value=10)
attendance_rate = st.slider("Attendance Rate (%)", min_value=0, max_value=100, value=75)
past_exam_scores = st.slider("Past Exam Scores", min_value=0, max_value=100, value=70)
parental_education = st.selectbox(
    "Parental Education Level",
    options=[
        "High School",
        "PhD",
        "Bachelor's Degree",
        "Master's Degree",
    ],
)
internet_access = st.selectbox("Internet Access at Home", options=["Yes", "No"])
extracurricular_activities = st.selectbox("Extracurricular Activities", options=["Yes", "No"])  

# Preprocess inputs
gender_encoded = 1 if gender == "Male" else 0
parental_education_mapping = {
    "Bachelor's Degree": 0,   
    "High School": 1,
    "Master's Degree": 2,
    "PhD": 3,
}
parental_education_encoded = parental_education_mapping[parental_education]
internet_access_encoded = 1 if internet_access == "Yes" else 0
extracurricular_activities_encoded = 1 if extracurricular_activities == "Yes" else 0

input_features = np.array([[
    gender_encoded,
    study_hours,
    attendance_rate,    
    past_exam_scores,
    parental_education_encoded,
    internet_access_encoded,
    extracurricular_activities_encoded,
]])

# Make prediction
if st.button("Predict Performance"):
    prediction = model.predict(input_features)
    # st.write(f"Predicted Performance Score: {prediction[0]:.2f}")
    if prediction[0] == 1:
        st.success("The student is likely to perform well!")
    else:
        st.error("The student may need additional support to perform well.")

                                                        
