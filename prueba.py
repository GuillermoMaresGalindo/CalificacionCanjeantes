import pandas as pd
import streamlit as st
import streamlit_authenticator as stauth
 
names = ['Lewandowski','Hanafi Harron']
usernames = ['lewan','hanafi']
passwords = ['mth107','mth108']
 
hashed_passwords = stauth.hasher(passwords).generate()
authenticator = stauth.authenticate(names,usernames,hashed_passwords,
'AdLeS_cookie','AdLeS_key',cookie_expiry_days=30)
 
name, authentication_status = authenticator.login('Login','sidebar')
 
if authentication_status:
 st.write("Welcome *%s*" % (name))
 # your application
elif authentication_status == False:
 st.error("Username/password is incorrect")
elif authentication_status == None:
 st.warning("Please enter your username and password")