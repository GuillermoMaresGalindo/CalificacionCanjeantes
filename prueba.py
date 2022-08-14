import pandas as pd
import streamlit as st
import streamlit_authenticator as stauth
 
names = ['Lewandowski','Hanafi Harron']
usernames = ['lewan','hanafi']
passwords = ['mth107','mth108']
 
hashed_passwords = stauth.hasher(passwords).generate()
authenticator = stauth.authenticate(names,usernames,hashed_passwords,
'AdLeS_cookie','AdLeS_key',cookie_expiry_days=30)
 
name, authentication_status = authenticator.login('Login','main')
 
if authentication_status:
  st.title('Welcome *%s* to Pakistan' % (name))
  st.write("Our first Streamlit App")
 
  st.write(
    pd.DataFrame({
      'A': [1, 2, 3, 4],
      'B': [5, 6, 7, 8]
        })
     )
 
elif authentication_status == False:
  st.error('Username/password is incorrect')
elif authentication_status == None:
  st.warning('Please enter your username and password')