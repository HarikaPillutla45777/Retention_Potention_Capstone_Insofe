import numpy as np 
import pickle 
import streamlit as st

#loading our saved model
loaded_model=pickle.load(open('C:/Users/venka/OneDrive/Desktop/retention_model.sav','rb'))

#retention prediction 
def retention_prediction(input_data):
  input_array=np.asarray(input_data)
  input_reshaped=input_array.reshape(1,-1)
  prediction=loaded_model.predict(input_reshaped)
  print(prediction)

  if (prediction==0):
    return 'Low'

  elif (prediction==1):
    return 'Medium'

  else:
    return 'High'


#website 
def main():
  st.title('Retention Prediction Web App')
  
  
  OnlineCommunication = st.text_input('OnlineCommunication')
  AutomaticRefill = st.text_input('AutomaticRefill')
  DoorstepDelivery=st.text_input('DoorstepDelivery')
  Types_of_mails_received= st.text_input('Types_of_mails_received')
  No_of_times_mail_clicked=st.text_input('No_of_times_mail_clicked')
  No_of_times_mail_opened=st.text_input('No_of_times_mail_opened')
  OrderQuantity_sum=st.text_input('OrderQuantity_sum')
  OrderQuantity_count=st.text_input('OrderQuantity_count')
  Engagement_Percentage =st.text_input('Engagement_Percentage')
  AverageOrderValue=st.text_input('AverageOrderValue')
  City_CITY1=st.text_input('City_CITY1')
  City_CITY2=st.text_input('City_CITY2')
  City_CITY3=st.text_input('City_CITY3')
  City_CITY4=st.text_input('City_CITY4')
  PreferredDeliveryDay_Friday=st.text_input('PreferredDeliveryDay_Friday') 
  PreferredDeliveryDay_Monday=st.text_input('PreferredDeliveryDay_Monday')
  PreferredDeliveryDay_Saturday=st.text_input('PreferredDeliveryDay_Saturday')
  PreferredDeliveryDay_Sunday=st.text_input('PreferredDeliveryDay_Sunday')
  PreferredDeliveryDay_Thursday=st.text_input('PreferredDeliveryDay_Thursday')
  PreferredDeliveryDay_Tuesday=st.text_input('PreferredDeliveryDay_Tuesday')
  PreferredDeliveryDay_Wednesday=st.text_input('PreferredDeliveryDay_Wednesday') 
  

  diagnosis = ''

   #creating a button for prediction
  if st.button('Result'):
    diagnosis = retention_prediction([OnlineCommunication,AutomaticRefill,DoorstepDelivery,
           Types_of_mails_received,No_of_times_mail_clicked,
           No_of_times_mail_opened,OrderQuantity_sum,OrderQuantity_count,
           Engagement_Percentage,AverageOrderValue,City_CITY1,
           City_CITY2,City_CITY3,City_CITY4,PreferredDeliveryDay_Friday,
           PreferredDeliveryDay_Monday,PreferredDeliveryDay_Saturday,
           PreferredDeliveryDay_Sunday,PreferredDeliveryDay_Thursday,
           PreferredDeliveryDay_Tuesday,PreferredDeliveryDay_Wednesday])
  
  st.success(diagnosis)


if __name__=='__main__':
  main()
