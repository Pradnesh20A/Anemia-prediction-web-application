import streamlit as st
import pandas as pd
import pickle
from PIL import Image

new_model = 'model.pkl'
model = pickle.load(open(new_model, 'rb'))



def process(hemoglobin, mcv, mch,gender):

    gender_map = {'Male': 0, 'Female': 1}
    gender = gender_map.get(gender, 0)

    hemoglobin = float(max(hemoglobin, 0.0))
    mch = max(mch,0)
    mcv = float(max(mcv, 0.0))

    # Create a dataframe with the input data
    data = {'Hemoglobin': [hemoglobin], 'MCV': [mcv],'MCH': [mch], 'Gender': [gender]}
    rm = pd.DataFrame(data)

    return rm


# predict anemia function
def anemia_prediction(hemoglobin,mcv,mch,gender):
    # Preprocess the input data
    rf = process(hemoglobin,mcv,mch,gender)

    # Predict anemia using the ensemble model
    prediction = model.predict(rf)

    # Return the prediction
    return prediction[0]
def causes():
    if st.button == 'CAUSES':
        st.write("--> Lack of Iron in Your Diet"
                 "--> An Inability to Absorb Iron")
        if st.button("PREVENTION"):
            st.write("--> Choose Iron Rich Food in Your Diet"
                     "--> Choose foods containing vitamin C to enhance iron absorption")



# develop the streamlit app using app()
def app():
    # Set the title and description

    st.title("Anemia Prediction")
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://imgs.search.brave.com/pxiExUtPdTFl0l7I9vyK8mQUIZl_5MeHM9D8k9wWKMU/rs:fit:860:0:0/g:ce/aHR0cHM6Ly91cGxv/YWRzLXNzbC53ZWJm/bG93LmNvbS81YTll/ZTY0MTZlOTBkMjAw/MDFiMjAwMzgvNjI4/OWYwYmZhOTIwYTk1/OGYyYjQxNmY3X2Js/YWNrLWdyYWRpZW50/LnBuZw");
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


    st.write("**Average Range of Hemoglobin ,HCT, MCV, MCH, MCHC (in units):**")
    average_range = {'Gender': ['Male', 'Female'],
                     'Hemoglobin': ['13.55 - 17.04 g/dL', '11.5 - 14.5 g/dL'],
                     'HCT': ['41.0 - 50.0 g/dL', '36.0 - 48.0 g/dL'],
                     'MCH': ['27.0 - 30.0pg','25.0-30.0 pg'],
                     'MCV': ['80.0 - 95.0 fL', '82.0 - 98.0 fL'],
                     'MCHC': ['32.0 - 36.0 g/dL', '32.0 - 36.0 g/dL']}
    rf_range = pd.DataFrame(average_range)
    st.table(rf_range)

    # Adding a divider for better vision
    st.markdown("<hr>", unsafe_allow_html=True)

    # getting input using input fields
    st.markdown("**Enter the RBC Indices information**")
    hemoglobin = st.number_input("Enter Hemoglobin (g/dL)", value=12.0, min_value=0.0, step=0.1)
    mch=st.number_input("Enter the MCH(pg)",value=27.0,min_value=0.0,step=0.1)
    mcv = st.number_input("Enter MCV (fL)", value=90.0, min_value=0.0, step=0.1)
    mcv2 = st.number_input("Enter MCHC (g/dL)", value=90.0, min_value=0.0, step=0.1)
    gender = st.radio("Select Gender", ['Male', 'Female'], index=0)

    # processing feeding the user data to the model to get the result
    if st.button("Predict"):
        if hemoglobin >= 0 and mcv >= 0:
            # the anemia prediction is called
            prediction = anemia_prediction(hemoglobin, mcv, mch, gender)

            prediction_label = 'Anemia' if prediction == 0 else 'Non Anemia'
            if prediction_label == 'Non Anemia':
                i1 = Image.open('not anemia.jpg')
                st.image(i1, caption='not anemic patient')

            # Display the prediction
            st.write("The patient has a ", prediction_label)

            if prediction_label == 'Anemia' and mcv < 80.0 and hemoglobin < 13.5 and mch < 27.0:
                st.write("Anemia Type: Iron Deficiency Anemia")
                i1 = Image.open('iron deficiency.jpg')
                st.image(i1, caption='Iron Deficiency anemia')
                st.subheader("CAUSES:")
                st.write("Lack of Iron in Your Diet")
                st.write("An Inability to Absorb Iron")
                st.subheader("PREVENTION:")
                st.write(" Choose Iron Rich Food in Your Diet")
                st.write("Choose foods containing vitamin C to enhance iron absorption")


            if prediction_label == 'Anemia' and mcv > 99.0 and mcv < 104.9 and hemoglobin < 13.5:
                st.write("Anemia Type: VitaminB12 Anemia")
                i2 = Image.open('anemia.jpg')
                st.image(i2, caption='Vitamin B12 Anemia')
                st.subheader("CAUSES:")
                st.write("Gastronomical Issues")
                st.write("Intestinal Problems")
                st.write("Lack of Vitamin B12 diet")
                st.write("Folate Deficiencies")
                st.subheader("PREVENTION:")
                st.write(" Choose Food Rich in Vitamin B12")
                st.write("Choose Food Rich in Folate")

            if prediction_label == 'Anemia' and mcv > 105.0:
                st.write("Anemia Type: A plastic Anemia")
                st.write("There is a increased chance of disease Lukemia or Lymphoma cancer because"
                         " Aplastic anemia is caused by a Disease called Lymphoma")
                st.write("Danger Kindly go and consult the doctor")
                i3 = Image.open('lukemia.jpg')
                st.image(i3, caption='Lymphoma')


        else:
            st.warning("Please enter valid values.")


    # Add a divider
    st.markdown("<hr>", unsafe_allow_html=True)





