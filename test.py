import pandas as pd
#--- Read in dataset(hospitalisation_details.csv) ----
hosp_details = pd.read_csv("hospitalisation_details.csv")
#print(hosp_details)

null_values = hosp_details.isnull().sum()
# print(null_values)

datatype = hosp_details.dtypes
# print(datatype)

duplicates = hosp_details.duplicated().sum()
# print(duplicates)


hosp_details.drop_duplicates(inplace=True)
columns_to_remove = ["Has_Children", "Is_Frequent_Treatment"]
hosp_details.drop(columns=columns_to_remove, inplace=True)
new_columns = {
        'c_id': 'customer_id',
        'yr': 'year',
        'mth': 'month',
        'date?': 'date',
        'children?': 'children',
        'charges?':'charges',
        'host_tier':'hospital_tier',
        'Ct_tier':'city_tier',
        'st_id':'state_id'
    }

hosp_details= hosp_details.rename(columns=new_columns)
hosp_details.to_csv('hospitalisation_details_cleaned.csv', index=False)
#print(hosp_details)

med_exam = pd.read_csv("./medical_examinations.csv")
#print(med_exam)

null_values = med_exam.isnull().sum()
#print(null_values)


datatype = med_exam.dtypes
#print(datatype)

duplicates = med_exam.duplicated().sum()
#print(duplicates)




med_exam .drop_duplicates(inplace=True)
columns_to_remove = ["recovery_period"]
med_exam.drop(columns=columns_to_remove,  inplace=True)
new_columns = {
        'cid': 'customer_id',
        'b_m_i': 'BMI',
        'h_Issues': 'health_issues',
        'cancer_hist': 'cancer_history',
        'noofmajorsurgeries':'numberofmajorsurgeries',
        'smoker??':'smoker'
    }
med_exam  = med_exam .rename(columns=new_columns)
med_exam .to_csv('medical_examinations_cleaned.csv', index=False)
print(med_exam)

#--- Export the df as "medical_examinations_cleaned.csv" ---
med_exam .to_csv('medical_examinations_cleaned.csv', index=False)
print(med_exam)
