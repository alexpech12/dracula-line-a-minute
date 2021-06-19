from dracula_account_api import api

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
