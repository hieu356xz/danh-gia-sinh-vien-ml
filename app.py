
import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('student_performance_regressor.joblib')

# Title of the app
st.title('Dự đoán kết quả học tập của học sinh')

st.write("""
Đây là một ứng dụng web đơn giản để dự đoán điểm cuối kỳ (G3) của học sinh
dựa trên các thông tin về học thuật và xã hội.
""")

# --- Input Fields ---
st.header("Nhập thông tin của học sinh")

# Create columns for layout
col1, col2 = st.columns(2)

# Get the categorical and numerical features from the model pipeline
# This is a bit of a workaround to get the feature names the model was trained on
try:
    preprocessor = model.named_steps['preprocessor']
    cat_features = preprocessor.transformers_[1][2]
    num_features = preprocessor.transformers_[0][2]
except (KeyError, IndexError):
    # Fallback if the pipeline structure is different
    st.error("Không thể tự động lấy danh sách các thuộc tính từ model. Vui lòng kiểm tra lại file model.")
    # Define them manually as a fallback
    num_features = ['age', 'Medu', 'Fedu', 'traveltime', 'studytime', 'failures', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences', 'G1', 'G2']
    cat_features = ['school', 'sex', 'address', 'famsize', 'Pstatus', 'Mjob', 'Fjob', 'reason', 'guardian', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic']


# Create dictionaries to hold the input data
input_data = {}

with col1:
    st.subheader("Thông tin cá nhân & Gia đình")
    input_data['school'] = st.selectbox('Trường học (school)', ['GP', 'MS'])
    input_data['sex'] = st.selectbox('Giới tính (sex)', ['F', 'M'])
    input_data['age'] = st.slider('Tuổi (age)', 15, 22, 16)
    input_data['address'] = st.selectbox('Khu vực sống (address)', ['U', 'R'])
    input_data['famsize'] = st.selectbox('Sĩ số gia đình (famsize)', ['LE3', 'GT3'])
    input_data['Pstatus'] = st.selectbox('Tình trạng sống chung của bố mẹ (Pstatus)', ['T', 'A'])
    input_data['Medu'] = st.slider('Học vấn của mẹ (Medu)', 0, 4, 4)
    input_data['Fedu'] = st.slider('Học vấn của bố (Fedu)', 0, 4, 4)
    input_data['Mjob'] = st.selectbox('Nghề nghiệp của mẹ (Mjob)', ['teacher', 'health', 'services', 'at_home', 'other'])
    input_data['Fjob'] = st.selectbox('Nghề nghiệp của bố (Fjob)', ['teacher', 'health', 'services', 'at_home', 'other'])
    input_data['guardian'] = st.selectbox('Người giám hộ (guardian)', ['mother', 'father', 'other'])
    input_data['famrel'] = st.slider('Chất lượng mối quan hệ gia đình (famrel)', 1, 5, 4)


with col2:
    st.subheader("Thói quen & Kết quả học tập")
    input_data['G1'] = st.slider('Điểm kỳ 1 (G1)', 0, 20, 10)
    input_data['G2'] = st.slider('Điểm kỳ 2 (G2)', 0, 20, 10)
    input_data['studytime'] = st.slider('Thời gian học mỗi tuần (studytime)', 1, 4, 2) # 1: <2h, 2: 2-5h, 3: 5-10h, 4: >10h
    input_data['failures'] = st.slider('Số lần trượt môn trước đây (failures)', 0, 4, 0)
    input_data['absences'] = st.slider('Số buổi vắng học (absences)', 0, 93, 0)
    input_data['goout'] = st.slider('Thời gian đi chơi với bạn bè (goout)', 1, 5, 3)
    input_data['health'] = st.slider('Tình trạng sức khỏe (health)', 1, 5, 5)
    input_data['internet'] = st.selectbox('Có Internet ở nhà (internet)', ['yes', 'no'])
    input_data['romantic'] = st.selectbox('Trong một mối quan hệ lãng mạn (romantic)', ['no', 'yes'])
    input_data['higher'] = st.selectbox('Muốn học lên cao hơn (higher)', ['yes', 'no'])

# --- Prediction ---
if st.button('Dự đoán điểm cuối kì (G3)'):
    # Create a DataFrame from the input data
    # The order of columns must match the order used during training
    all_features = num_features + cat_features
    
    # Create a dictionary with the correct feature order
    ordered_input_data = {feature: input_data.get(feature) for feature in all_features}

    input_df = pd.DataFrame([ordered_input_data])

    # Ensure all columns are present and in the correct order
    # This is crucial for the preprocessor
    X_cols = num_features + cat_features
    input_df = input_df[X_cols]

    # Make prediction
    prediction = model.predict(input_df)
    predicted_score = prediction[0]

    st.success(f'Điểm G3 dự đoán là: **{predicted_score:.2f}**')

    if predicted_score >= 16:
        st.info("Học sinh này được dự đoán có học lực **Giỏi**.")
    elif predicted_score >= 14:
        st.info("Học sinh này được dự đoán có học lực **Khá**.")
    elif predicted_score >= 10:
        st.info("Học sinh này được dự đoán có học lực **Trung bình**.")
    elif predicted_score >= 5:
        st.info("Học sinh này được dự đoán có học lực **Yếu**.")
    else:
        st.warning("Học sinh này được dự đoán có học lực **Kém**.")
