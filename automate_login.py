from autologin import AutoLogin
import warnings
warnings.simplefilter("ignore", DeprecationWarning)

file = open('file.txt',mode='rt')       #file containing list of ip's
for ip in file:
    ip = ip.rstrip()
    url = 'http://'+ip
    username = 'admin'  #Enter username
    password = 'admin'  #Enter password
    a = AutoLogin()
    try:
        cookies = a.auth_cookies_from_url(url,username,password)
        print("Login Successful")
        with open('output.txt',mode='a') as output_file:        #output file
            output_file.write(str(ip)+'\n')
    except:
        print("Try Again")


# import requests
#
# file = open('zmap_output.txt',mode='rt')
# for ip in file:
#     ip = ip.rstrip()
#     response = requests.get('http://'+ip, auth=('admin','admin'))
#     with open('output.txt',mode='a') as output:
#         output.writelines(str(response.status_code)+' '+str(ip)+'\n')
