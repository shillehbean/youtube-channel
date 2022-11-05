import time
import network
import urequests


def send_sms(ssid, password, recipient, sender,
             message, auth_token, account_sid):
    """
        Description: This is a function to send a recipient a message
        with a Twilio phone number.
        
        Parameters:
        
        ssid[str]: The name of your internet connection
        password[str]: Password for your internet connection
        recipient[str]: Phone number of recipient
        sender[str]: Phone number for twilio account
        message[str]: Message to recipient
        auth_token[str]: Token from twilio profile
        account_sid[str]: Sid from twilio profile
    """
    
    # Just making our internet connection
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    # Wait for connect or fail
    max_wait = 10
    while max_wait > 0:
      if wlan.status() < 0 or wlan.status() >= 3:
        break
      max_wait -= 1
      print('waiting for connection...')
      time.sleep(1)
    # Handle connection error
    if wlan.status() != 3:
       raise RuntimeError('network connection failed')
    else:
      print('connected')
      status = wlan.ifconfig()
      #print('ip = ' + status[0])
      
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = "To=" + recipient + "&From=" + sender + "&Body=" + message
    print("Attempting to send SMS")
    r = urequests.post("https://api.twilio.com/2010-04-01/Accounts/" +
                       account_sid + "/Messages.json",
                       data=data,
                       auth=(account_sid,auth_token),
                       headers=headers)
    if r.status_code >= 300 or r.status_code < 200:
        print("There was an error with your request to send a message. \n" +
              "Response Status: " + str(r.status_code))
    else:
        print("Success")
        print(r.status_code)
    r.close()
