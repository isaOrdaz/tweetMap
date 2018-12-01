import json

# Enter your keys/secrets as strings in the following fields
credentials = {}
credentials['CONSUMER_KEY'] = rTVQFs0E39iDlT9z2HjtvoypP
credentials['CONSUMER_SECRET'] = i4ne9Z2k9cThWjR0FD2YMotGRT9qJcFUq6axkQHLZRXGfneqOm
credentials['ACCESS_TOKEN'] = 316920647-EqVEVvor9VYZ73beLSCXfwUsmGcsjCM9yxxgjnb5
credentials['ACCESS_SECRET'] = QF41oHaAVHExCKNZxO19fwoBzXcVzdGlpEpIUylFF1P4r

# Save the credentials object to file
with open("twitter_credentials.json", "w") as file:
    json.dump(credentials, file)
