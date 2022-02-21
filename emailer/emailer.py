#TO DO:
    # pair with outlook 
    # keep some record of what's been received, sent, and not send
	# allow unsubscribing e.g. ${l://OptOutLink}
    # email subjects lines
    # collect time and send based on local time
    # Base64 encoding urls: https://www.qualtrics.com/support/survey-platform/survey-module/survey-flow/standard-elements/passing-information-through-query-strings/#QEED
    # careful about sussex's firewall: https://www.sussex.ac.uk/its/help/faq.php?faqid=1101

import glob # for listing files
import json # for reading files
import pandas as pd # for creating a dataframe
import datetime as dt
import smtplib, ssl #sending emails
from email.mime.text import MIMEText #writing emails
from email.mime.multipart import MIMEMultipart #writing emails
from emails import Emails
from collections import defaultdict
#import schedule
#import time
from apscheduler.schedulers.blocking import BlockingScheduler

#def emailer(): # here down needs indenting untill you get to the scheduler
survey_names = ['pre','day_1','day_2','day_3','day_4','day_5',
                'day_6','day_7','day_8','day_9','day_10','post']

surveys = {'pre':['SV_77GRlMXRzCRvbgO'],
'day_1':['SV_0UqMgw7opwUBsp0','SV_eVD50YlnreqHPeu'],
'day_2':['SV_1KTcbhp97aMsT8G','SV_8wWXdKWwB6PmRpQ'],
'day_3':['SV_9WQC7OK4XgA6u7s','SV_3F4yThgDP5no2fs'],
'day_4':['SV_2071gXkwXXxHhrM','SV_eeULxjJiThIUJbo'],
'day_5':['SV_bQ5EPRvJaZWEKaO','SV_1AnnMndzN0tu4yG'],
'day_6':['SV_2ccwKIVLKbjjuTk','SV_5tmjjk9Dpxufv6u'],
'day_7':['SV_errJ339HYHmYmh0','SV_7Xaly0kNutBbaiW'],
'day_8':['SV_b7uWUqNYHPgufXw','SV_7OiRNiarIJr8OJo'],
'day_9':['SV_1RfiSGF82QU4uhw','SV_eUUZbaMxDq1ExQG'],
'day_10':['SV_0pjWPj6lWsKPsVg','SV_8dzuF81uf8qQ8Oq'],
'post':['SV_23lPSvXFISsaPtk'],'materials':['SV_6D0mranYslx7qHc']}

#testing webservice
#surveys = {'pre':['SV_9LcOP6Rvbipyg9E'],
#    'day_1':['SV_0kSOgjUWwmD255I','SV_2aeM3wiLEzgersO'],
#    'day_2':['SV_4Tw8hoHySqSo3tA','SV_4HGXCP36erwAm7c'],
#    'day_3':['SV_9WQC7OK4XgA6u7s','SV_3F4yThgDP5no2fs'],
#    'post':['SV_8nXdamLUpsVVCoC']}

file_list = glob.glob('[relative_local_folder_path]/*.json')
datal = []
for file in file_list:
    f = open(file)
    datad = json.load(f)
    for key, value in surveys.items():
        if datad["survey"] in value:
            if "condition" in datad:
                datan = {'email':datad["email"], 'condition':datad["condition"], key:datad["date"]}
            else:
                datan = {'email':datad["email"], key:datad["date"]}
    datal.append(datan)

#Made up data for testing
##comment out datal creation above and edit these to test output:
#datal = [
#{'email':'email', 'condition': '[group]', '[survey_ID]': '[date]'},
#etc..
#]

datac = defaultdict(dict)
for d in datal:
    datac[d["email"]].update(d)

keys = ['email','condition','pre','day_1','day_2','day_3','day_4','day_5','day_6',
        'day_7','day_8','day_9','day_10','post']
datafl = [pd.DataFrame([{key: None for key in keys}])]

for d in list(datac.values()):
    dataf = pd.DataFrame([d])
    datafl.append(dataf)

dataset = pd.concat(datafl)
dataset = dataset.iloc[1: , :]
dataset = dataset.reset_index()  # make sure indexes pair with number of rows
dataset.to_csv()
for index, row in dataset.iterrows():
    
    #take the last column that has a number in it
    row_na = row.loc[pd.notna(row),]
    #get the date
    datef = dt.datetime.strptime(row_na[-1], "%m/%d/%Y")
    today = dt.datetime.today()
    elapsed = today - datef
    
    #screen out anyone not ready for an email:
    last_survey = row_na.index[-1] #last non-missing entry in the row
    if last_survey == 'post' or elapsed.days < 3 or (row['condition'] == 'control' and (elapsed.days < 23 or elapsed.days > 24)): 
        continue #skip if completed post-test or not ready for reminder yet (or control and not ready or too old)
    
    #select which survey to send
    survey_index = survey_names.index(last_survey) #index of last survey
    next_survey =  survey_names[survey_index+1] #name of next survey along
    if next_survey == 'post' or elapsed.days > 4 or (row['condition'] == 'control' and elapsed.days == 23):
        survey_ID = str(surveys['post'][0])
    elif row['condition'] == 'mental':
        survey_ID = str(surveys[next_survey][0]) #distribute reminder emails if 3 or 4 days have passed
    elif row['condition'] == 'world':
        survey_ID = str(surveys[next_survey][1])
    else:
        continue #these are used throughout just to be safe

    survey_url = "https://[qualtrics_SSO.com]/jfe/form/" + survey_ID + "?RecipientEmail=" + row['email']
    
    #select which email to send
    if row['condition'] == 'control':
        if elapsed.days == 22 or elapsed.days == 23:
            email_body = 'control_post'
        else:
            continue
    elif row['condition'] == 'mental' or row['condition'] == 'world': #emails are the same, survey URLs calculated separately above
        if next_survey == 'post' or elapsed.days > 4: 
            email_body = 'post'
        elif next_survey == 'day_1':
            email_body = 'day_1'
        elif next_survey == 'day_2':
            email_body = 'day_2'
        elif next_survey in ['day_3','day_4','day_5','day_6','day_7','day_8','day_9','day_10']:
            email_body = 'day_3'
    else:
        continue
    
    # N.B. through Qualtrics: elapsed==1, send next survey. if elapsed==2, first reminder
        # through python: Elapsed 3&4=reminder,elapsed 5=post, elapsed 6&7 = post reminder, elapsed 8=dropout
    #select which reminder to append
    if row['condition'] == 'control': #note: body is set above for clarity
        if elapsed.days == 22: 
            reminder = 'reminder_post'
        elif elapsed.days == 23:
            reminder = 'reminder_post_final' 
    elif next_survey == 'post': #post test is sent immediately
        if elapsed.days == 2:
            reminder = 'reminder_post'
        elif elapsed.days == 3:
            reminder = 'reminder_post_final'
        else:
            continue #if you've done 10 days you don't get drop-out reminders
    elif next_survey == 'day_1': #first day is sent immediately
        if elapsed.days == 2:
            reminder = 'reminder_days'
        elif elapsed.days == 3:
            reminder = 'reminder_days_final'
        elif elapsed.days == 4: 
            reminder = ''
            email_body = 'dropout' # change body to dropout if 5 days
        elif elapsed.days == 7:
            reminder = 'reminder_dropout'
            email_body = 'dropout'
        else: #includes if days == 5,6, or >7
            continue
    elif elapsed.days == 3: #days 2-10 sent next morning
        reminder = 'reminder_days'
    elif elapsed.days == 4:
        reminder = 'reminder_days_final'
    elif elapsed.days == 5 : 
        reminder = ''
        email_body = 'dropout' # change body to dropout if 5 days
    elif elapsed.days == 8:
        reminder = 'reminder_dropout'
        email_body = 'dropout'
    else: #includes if days == 6,7, or >8
        continue
    
    footer = dt.datetime.now() # makes sure bottom of email isn't hidden by gmail due to repeated content
    email_class = Emails(reminder,email_body,survey_url,footer)
    html_email = email_class.make_email()
    text_email = email_class.make_plaintext()

    ###SEND EMAIL

    #gmail set up
    port =  465
    smtp_server =  "smtp.gmail.com"
    sender_email =  "xxx"
    password =  "xxx"
    #input("Type your password and press enter: ")

    #outlook setup
    #port = 465 # 
    #smtp_server = "smtp.office365.com" # 
    #sender_email = "xxx"
    #password = "xxx" 
    
    receiver_email = row['email']

    message = MIMEMultipart("alternative")
    message["Subject"] = "A reminder for the Learning Mindfulness Online course"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text_email, "plain")
    part2 = MIMEText(html_email, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
    print([row['email'],reminder,email_body])
    





    
    #with smtplib.SMTP(smtp_server, port) as server:
    #    server.ehlo()  # Can be omitted
    #    server.starttls(context=context)
    #    server.ehlo()  # Can be omitted
    #    server.login(sender_email, password)
    #    server.sendmail(sender_email, receiver_email, message)

# automated using:
    # https://www.howtogeek.com/1   19028/how-to-make-your-pc-wake-from-sleep-automatically/
    # https://www.jcchouinard.com/python-automation-using-task-scheduler
    # could schedule in code with this:
        # https://stackoverflow.com/questions/30835547/how-to-execute-script-on-schedule
        # Scheduler: https://apscheduler.readthedocs.io/en/3.x/userguide.html
            # Try implement some backend holding for scheduler to run on.

##### notes for scheduling with code:

#schedule.every().day.at("06:00").do(emailer())
#while 1:
#    schedule.run_pending()
#    time.sleep(600)

#scheduler = BlockingScheduler()
#scheduler.add_job(emailer, 'cron', hour=6, id='emailer_Id')
##    #  misfire_grace_time
##scheduler.start()
#scheduler.remove_job('emailer_Id')

#if __name__ == '__main__':
#    scheduler = BlockingScheduler()
#    scheduler.add_job(emailer, 'cron', hour=6, id='emailer_Id')
#    try:
#        scheduler.start()
#    except (KeyboardInterrupt, SystemExit):
#        pass
