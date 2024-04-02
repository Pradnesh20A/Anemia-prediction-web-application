import streamlit as st
def app():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://imgs.search.brave.com/B3aVWzSA-crn7NqbuBJjs8l1aLoKjsw318mig4ZYUBM/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9zdDQu/ZGVwb3NpdHBob3Rv/cy5jb20vMTg0NDQ2/NzgvMjAyODMvaS80/NTAvZGVwb3NpdHBo/b3Rvc18yMDI4Mzgx/MTItc3RvY2stcGhv/dG8tdG9wLXZpZXct/YWdlZC1jb25jcmV0/ZS13YWxsLmpwZw");
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.title("What is Anemia?")
    st.write("Anemia is a medical condition characterized by a deficiency of red blood cells (RBCs) "
             "or a decrease in the quality or quantity of hemoglobin, a protein in RBCs that binds to oxygen "
             "and carries it to the body's tissues. Hemoglobin is essential for transporting oxygen from the "
             "lungs to various parts of the body and removing carbon dioxide from the body through the lungs."
             "There are several different types and causes of anemia, "
             "but the most common type is iron-deficiency anemia. "
             "Iron-deficiency anemia occurs when the body doesn't have enough "
             "iron to produce adequate amounts of hemoglobin, resulting in a decreased ability to carry oxygen.")

    st.write("It is important to identify and treat anemia promptly, "
             "as it can lead to complications such as heart problems, impaired cognitive function, "
             "and delayed growth and development in children.")
    st.subheader("Common symptoms and signs of anemia may include:")
    st.markdown("""1.Fatigue and weakness: People with anemia often feel tired and lacking in energy.""")
    st.markdown("""2.Pale skin: Anemia can cause a paleness of the skin and mucous membranes.""")
    st.markdown("""3.Shortness of breath: Due to the reduced oxygen-carrying capacity of the blood, individuals with 
                   anemia may experience difficulty breathing or shortness of breath.""")
    st.markdown("""4.Dizziness or light headedness: Anemia can lead to dizziness or feeling faint.""")
    st.markdown("""5.Cold hands and feet: Poor circulation may cause extremities to feel cold.""")
    st.markdown("""6.Headaches: Anemic individuals may experience frequent headaches.""")
    st.markdown("""7.Rapid or irregular heartbeat: The heart may need to beat faster to compensate for reduced oxygen supply.""")
    st.markdown("""8.Cognitive impairment: Severe anemia can affect concentration and cognitive function.""")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("Types of Anemia")
    st.markdown("**>> Iron-deficiency anemia**")
    st.markdown("**>> Vitamin-deficiency anemia**")
    st.markdown("**>> Aplastic anemia**")
    st.markdown("<hr>", unsafe_allow_html=True)

    st.title("This Application is Developed by")
    st.subheader("Developed By: Pradnesh A")
    if st.button("contact"):
        st.subheader("E-Mail: pradneshraj2002@gmail.com")


