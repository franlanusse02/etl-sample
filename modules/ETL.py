import pandas as pd

# load the dataset
df = pd.read_csv('./downloaded_files/bi.csv', encoding='latin1')

# store raw data
df.to_csv('raw_data.csv')


# TRANSFORM SECTION

# check for empty values
df_empty = df[df.isna().any(axis=1)]


mean_python_score = df['Python'].mean()
df.fillna(mean_python_score, inplace=True)



# normalizing incorrect formats



# normalize countries

countries = df['country'].unique()
# print(countries) # debug print

normalized_country_dict = {
    'Rsa': 'South Africa',
    'Norge': 'Norway',
    'norway': 'Norway'
}

df['country'] = df['country'].apply(lambda x: normalized_country_dict.get(x, x))



# normalize gender

# print(df['gender'].unique()) # debug print

normalized_gender_dict = {
    'female':'Female',
    'F':'Female',
    'male':'Male',
    'M':'Male'
}

df['gender'] = df['gender'].apply(lambda x: normalized_gender_dict.get(x,x))
# print(df['gender'].unique()) # debug print



# normalize residence variations

# print(df['residence'].unique()) # debug print

normalized_residence_dict = {
    'BI-Residence':'BI Residence',
    'BI_Residence':'BI Residence',
    'BIResidence':'BI Residence'
}

df['residence'] = df['residence'].apply(lambda x: normalized_residence_dict.get(x,x))

# print(df['residence'].unique()) # debug print



# normalize previous_education variations

# print(df['prevEducation'].value_counts()) # debug print

normalized_education_dict = {
    'HighSchool':'High School',
    'Barrrchelors':'Bachelors',
    'diploma':'Diploma',
    'DIPLOMA':'Diploma',
    'Diplomaaa':'Diploma'
}

df['prevEducation'] = df['prevEducation'].apply(lambda x: normalized_education_dict.get(x,x))

# print(df['prevEducation'].unique()) # debug print

df.to_csv('clean_data.csv')