this is an automation program that can automate login in into website. current captcha is not enabled. to make it work, all you need to do is follow the following steps: 

first -> pip install -r requirements.txt

second -> change the link to target in test_login.py

third -> change the ids, xpaths, classes .etc. required for spotting the element. 

fourth -> change the credentials in the csv file and if you expect it to succeed or fail. 

finally -> change the assertion lines in test_login.py according to what appears when you are logged in. 


after this just run test_login.py from outside the src directory. 

P.S the linuxdriver i uploaded in only for linux so windows users need to download their own. 
