from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from send_mail import *
from loadExcel import get_user_details
from mail_template import *
import base64
from ConfigParser import SafeConfigParser


def main():

    parser = SafeConfigParser()
    parser.read('config.ini')
    store = file.Storage('token.json')
    creds = store.get()
    service = build('gmail', 'v1', http=creds.authorize(Http()))
    user_details = get_user_details()
    DATE_TIME=parser.get('MAIL_INPUTS','DATE_TIME')
    SUBJECT=parser.get('MAIL_INPUTS','SUBJECT')+DATE_TIME
    for user_detail in user_details:
        if user_detail['email'] is not None:
            text_to_enc = DATE_TIME + "#" + user_detail['email'] + "#" + user_detail['userName'] + "#" + str(user_detail['adlCnt']) + "#" + str(user_detail['kdCnt'])
            encrypted_text = base64.b64encode(text_to_enc)
            confLink = CONFIRMATION_HYPERLINK.format(id=encrypted_text)
            send_message(service, 'me', create_message('me',user_detail['email'], SUBJECT, MAIL_BODY.format(dateTime=DATE_TIME,confirmationLink=confLink)))
            print("email sent to ",user_detail['email']," with body ", MAIL_BODY.format(dateTime=DATE_TIME,confirmationLink=confLink))


if __name__ == '__main__':
  main()