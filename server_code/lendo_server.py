import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def add_lendor_frist_form(name,gender,date_of_birth,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['full_name'] = name
    row[0]['gender'] = gender
    row[0]['date_of_birth'] = date_of_birth

@anvil.server.callable
def add_lendor_second_form(mobile,email,photo,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    #row[0]['investment'] = investment
    row[0]['mobile'] = mobile
    row[0]['mail_id'] = email
    row[0]['user_photo'] = photo


@anvil.server.callable
def add_lendor_third_form(aadhaar_photo, pan_card, pan_id,aadhaar_card,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['pan_photo'] = pan_id
    row[0]['pan_number'] = pan_card
    row[0]['aadhaar_no'] = aadhaar_card
    row[0]['aadhaar_photo'] = aadhaar_photo



@anvil.server.callable
def add_lendor_four_form(street_adress_1,street_address_2,city,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['street_adress_1'] = street_adress_1
    row[0]['street_address_2'] = street_address_2
    row[0]['city'] = city


                          
@anvil.server.callable
def add_lendor_five_form(postal_zip,state,country,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['state'] = state
    row[0]['country'] = country
    row[0]['pincode'] = postal_zip



@anvil.server.callable
def add_lendor_six_form(lending_type, investment,lending_period, user_id):
  row = app_tables.lender.add_row(investment=investment, lending_type=lending_type,lending_period=lending_period,coustmer_id=user_id)
    
    
@anvil.server.callable
def add_lendor_individual_form_1(company_name,org_type,emp_type,user_id):
  row = app_tables.lender.search(coustmer_id=user_id)
  if row:
    row[0]['company_name']=company_name
    row[0]['organization_type']=org_type
    row[0]['employment_type']=emp_type

    

@anvil.server.callable
def add_lendor_individual_form_2(business_phone_number, landmark,comp_address,user_id):
  row = app_tables.lender.search(coustmer_id=user_id)
  if row:
    row[0]['business_no']=business_phone_number
    row[0]['company_landmark']=landmark
    row[0]['company_add']=comp_address      


@anvil.server.callable
def add_lendor_individual_form_3(user_id):
    row = app_tables.lender.search(coustmer_id=user_id)
       
  
@anvil.server.callable
def add_lendor_individual_bank_form_1(user_id):
    row = app_tables.lender.search(coustmer_id=user_id)
       
  
@anvil.server.callable
def add_lendor_individual_bank_form_2(user_id):
    row = app_tables.lender.search(coustmer_id=user_id)

@anvil.server.callable
def add_rtr_form(top_up,fin_rta):
  #row = app_tables.lender.search()
  row = app_tables.lender.search(tables.order_by("date_time", ascending=False))
  if row:
    row[0]['top_up'] = top_up
    row[0]['fin_rta'] = fin_rta