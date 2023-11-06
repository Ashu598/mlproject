import streamlit as st
import csv
import pandas as pd


def recommend(profile):
    profile_index = profile_[profile_['Position'] == profile].index[0]
    distances = similarity[profile_index]
    profile_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x: x[1])[1:11]

    recomended_profiles = []
    for i in profile_list:
        recomended_profiles.append(profile_.iloc[i[0]][['Position', 'Date', 'Candidate Name', 'Rate', 'Visa', 'Phone', 'Email', 'LinkedIn']])
    return recomended_profiles


import pickle
profile_dict = pickle.load(open('profile_dict.pkl', 'rb'))
profile_ = pd.DataFrame(profile_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("My Resumes")

option = st.selectbox('Job profiles', profile_['Position'].values)

if st.button('Recommend Profiles'):
    recommendations = recommend(option)
    for i in recommendations:
        st.write(i)
