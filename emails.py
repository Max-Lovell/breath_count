class Emails:
    def __init__(self, reminder, body, url, footer):
        self.reminder = reminder
        self.body = body
        self.survey_url = url
        self.footer = footer

    def make_email(self):

        #Set reminder header
        if self.reminder == 'reminder_days':
            reminder = """\
                <p><i>This is a friendly reminder about your mindfulness practice.</i><br>
                <i>I will send one more reminder, and after 3 days the survey link will close so that we can keep the course timings similar across participants.</i>
                </p><br/>
                """
        elif self.reminder == 'reminder_days_final':
            reminder = """\
                <p><i>This is a friendly reminder about your mindfulness practice. Note that after 3 days since the last survey, this survey link will close so that we can keep the course timings similar across participants.<br>
                If you do not complete the session today, we will email you tomorrow asking you to complete the post-course survey.
                </i></p><br>
                """
        elif self.reminder == 'reminder_post':  
            reminder = """\
                <p><i>This is a friendly reminder about the final survey.</i><br>
                <i>I will send one more reminder, and after 3 days the survey link will close so that we can keep the course timings similar across participants.</i>
                </p><br/>
                """
        elif self.reminder == 'reminder_post_final':
            reminder = """\
                This is a friendly reminder about the final survey.
                I will not send another reminder, and after 3 days the survey link will close so that we can keep the course timings similar across participants.
                """
        elif self.reminder == 'reminder_dropout':
            reminder = """\
                <p><i>This is a friendly reminder about the final survey, and the last time we will contact you if you do not wish to take the survey.<br>
                Note that this is the last day you can do the survey, and we would very much appreciate having useable data from every participant, as well as your feedback.<br>
                Many thanks for your time
                </i></p><br/>
                """
        elif self.reminder == '':
            reminder = """\
                """

        #Set main email body
        if self.body == 'day_1':
            body = f"""\
                <p>Thank you for completing the first survey - your participation is very much appreciated!<br/><br/>
                The first meditation session (preceded by an induction and initial survey) can be found at the following link:<br/>
                <a href={self.survey_url}>Take the survey</a></p>
                <p><i>Or copy and paste the URL below into your internet browser:</i><br/><i>{self.survey_url}</i></p>
                <p>We'll send you a reminder email if you don't manage to complete the session today.</br>
                Note that after 3 reminders we will assume you have dropped out of the study, and will invite you to take the post-course follow-up survey.</br>
                I will send tomorrows practice automatically the day after you complete the session linked above.</p>
                <p>You are welcome to meditate for as long as you like following this first day's practice, or bring this awareness to another activity in your day.</br>
                However, we ask that for the ten days of this intervention, you do not look up any information on mindfulness and meditation outside of this study.</p>
                <p><br/>If you have any questions please contact <i>mel29@sussex.ac.uk.</i><br/><br/>
                Thanks again! Your help really is appreciated. We believe the research will prove valuable for helping many people.
                <br/><br/><br/>The Mindfulness research group<br/><br/>
                <p>Please email m.lovell@sussex.ac.uk to unsubscribe from future emails.</p>
                <br>{self.footer}
                """
        elif self.body == 'day_2':
            body = f"""\
                <p>Thank you for completing yesterday’s practice and survey!</p>
                <p>When practicing mindfulness you might feel restless. 
                This is normal but we encourage you to commit to finishing the session. 
                Acknowledge the urge to get up without judging or trying to change it, but bring your attention back to your breath (again and again if necessary), without giving yourself a hard time if possible. 
                We would also like to encourage you to practice bringing mindful awareness to a routine activity at least once a day. 
                The more you practice mindfulness makes a difference to the way you experience it.</p>
                <p>The second practice, and a question about your practice, can be found here: <a href={self.survey_url}>Take the survey</a></p>
                <p><i>Or copy and paste the URL below into your internet browser:</i><br/><i>{self.survey_url}</i></p>
                <p>We'll send you a reminder email if you don't manage to complete the session today.</br>
                Note that after 3 reminders we will assume you have dropped out of the study, and will invite you to take the post-course follow-up .</br>
                I will send tomorrows practice automatically the day after you complete the session linked above.</p>
                <p>You are welcome to repeat today’s practice as many times as you want, but don’t attempt to go beyond it until tomorrows session. 
                Also feel free to tell me about any experiences you had, either during the sitting practice or during other daily activities.</p><br/>
                <br/><b>If you have any questions please contact&nbsp;<i>mel29@sussex.ac.uk.</i></b><br/><br/>
                The Mindfulness research group</p><p>&nbsp;</p>
                <p>Please email m.lovell@sussex.ac.uk to unsubscribe from future emails.</p>
                <br>{self.footer}
                """
        elif self.body == 'day_3':
            body = f"""\
                <p>Thank you for completing yesterday’s practice and survey!</p>
                <p>The next practice, and a question about your practice, can be found here: <a href={self.survey_url}>Take the survey</a></p>
                <p><i>Or copy and paste the URL below into your internet browser:</i><br/><i>{self.survey_url}</i></p>
                <p>We'll send you a reminder email if you don't manage to complete the session today.</br>
                Note that after 3 reminders we will assume you have dropped out of the study, and will invite you to take the post-course follow-up survey.</br>
                I will send tomorrows practice automatically the day after you complete the session linked above.</p>
                <p>You are welcome to repeat today’s practice as many times as you want, but don’t attempt to go beyond it until tomorrows session.<br/>
                Feel free to tell me about any experiences you had, either during the sitting practice or during other daily activities.
                <br/><b>If you have any questions please contact me at <i>mel29@sussex.ac.uk.</i></b>
                <br/><br/>The Mindfulness research group</p>
                <p>Please email m.lovell@sussex.ac.uk to unsubscribe from future emails.</p>
                <br>{self.footer}
                """
        elif self.body == 'post':
            body = f"""\
                <p>Thank you for taking part in this study about learning mindfulness online!<br/><br/>
                Now we are ready for the crucial second survey, which is similar to the first survey, and is available here:&nbsp;<a href={self.survey_url}>Take the survey</a></p>
                <p>Or copy and paste the URL below into your internet browser:<br/><i>{self.survey_url}</i><br/><br/>
                <strong>(NOTE: As this final survey contains a keyboard task, you will need a computer to fill it in - it is not mobile friendly)</strong>
                <br/>Afterwards, we will send you more information so you can continue your practice if you wish.
                <br/><br/>Thanks again,<br/><br/>
                The Mindfulness research group<br/></p>
                <p>Please email m.lovell@sussex.ac.uk to unsubscribe from future emails.</p>
                """
        elif self.body == 'dropout':
            body = f"""\
                <p>Dear Participant,</p><br/>
                <p>As you didn't complete the last survey within three days we have assumed you have dropped out of the study and the link for that survey has closed.</p><br/>
                <p>We would be very thankful if you would complete the follow-up second main survey, so we can retain your data.</p>
                <p>You can find this survey at the following link: <a href={self.survey_url}>Take the survey</a></p>
                <p>Or, copy and paste the following URL into your browser:<br/><i>{self.survey_url}</i></p>
                <p>(Note: As this final survey contains a keyboard task, you will need a computer to fill it in - it is not mobile friendly)</p><br/>
                <p>Upon finishing the above survey, you will be given access to all course materials.</p>
                <p>We will send one reminder email about this post test survey before it closes, after which we will not email you again.</p><br/>
                <p>If you wish to not recieve this next email or have any further questions, please email me at m.lovell@sussex.ac.uk</p><br/><br/>
                <p>Many thanks for your time on this project,</p><br/>
                <p>Max Lovell</p>
                """
        elif self.body == 'control_post':
            body = f"""\
                <p>This is a follow-up email for the study about learning Mindfulness online course. Thank you for taking part.</p>
                <p>You are now ready to complete the second survey, after which you will have access to all our mindfulness course materials, and an explanation of the study:</p>
                <p><a href={self.survey_url}>Take the survey</a><br/>   
                Or copy and paste the URL below into your internet browser:<br/><i>{self.survey_url}</i></p>
                <p>After the second survey you will be contacted with details of the mindfulness course itself, and given access to all our resources for how to learn mindfulness.
                <br/><br/>If you have any questions please contact <i>mel29@sussex.ac.uk</i></p>
                <p><br/><br/>Thanks again,<br/><br/>
                The Mindfulness research group</p>
                """
        return  f"""\
            <html>
              <body>
                {reminder}
                {body}
                <span style="opacity: 0">{self.footer}</span>
              </body>
            </html>
            """
    
    def make_plaintext(self):
        if self.reminder == 'reminder_days':
            reminder = """\
                This is a friendly reminder about your mindfulness practice.
                I will send one more reminder, and after 3 days the survey link will close so that we can keep the course timings similar across participants.
                """
        elif self.reminder == 'reminder_days_final':
            reminder = """\
                This is a friendly reminder about your mindfulness practice.
                I will not send another reminder, and after 3 days the survey link will close so that we can keep the course timings similar across participants.
                """
        elif self.reminder == 'reminder_post':
            reminder = """\
                This is a friendly reminder about the final survey.
                I will not send another reminder, and after 3 days the survey link will close so that we can keep the course timings similar across participants.
                """
        elif self.reminder == 'reminder_post_final':
            reminder = """\
                This is a friendly reminder about the final survey.
                I will not send another reminder, and after 3 days the survey link will close so that we can keep the course timings similar across participants.
                """
        elif self.reminder == 'reminder_dropout':
            reminder = """\
                This is a friendly reminder about the final survey, and the last time we will contact you if you do not wish to take the survey.
                Note that this is the last day you can do the survey, and we would very much appreciate having useable data from every participant, as well as your feedback.
                Many thanks for your time.
                """
        elif self.reminder == '':
            reminder = """\
                """

        if self.body == 'day_1':
            body = f"""\
                This is a plain text version of this email as the HTML couldn't be loaded at this time.

                Thank you for completing the first survey - your participation is very much appreciated!
                The first meditation session (preceded by an induction and initial survey) can be found at the following link:
                Today's practice can be found at the following URL: {self.survey_url}

                We'll send you a reminder email if you don't manage to complete the survey today. 
                Note that after 3 reminders we will assume you have dropped out of the study, and will invite you to take the second survey. 
                You are welcome to meditate for as long as you like following this first day's practice, or bring this awareness to another activity in your day. 
                However, we ask that for the 10 days of this intervention, you do not look up any information on mindfulness and meditation outside of this study.
                If you have any questions please contact m.lovell@sussex.ac.uk.

                Thanks again! Your help really is appreciated. We believe the research will prove valuable for helping many people.

                The Mindfulness research group
                Please email m.lovell@sussex.ac.uk to unsubscribe from future emails.
                """
        elif self.body == 'day_2':
            body = f"""\
                This is a plain text version of this email as the HTML couldn't be loaded at this time.

                Thank you for completing yesterday’s practice and survey!
                When practicing mindfulness you might feel restless. This is normal but we encourage you to commit to finishing the session. 
                Acknowledge the urge to get up without judging or trying to change it, but bring your attention back to your breath (again and again if necessary), without giving yourself a hard time if possible. 
                We would also like to encourage you to practice bringing mindful awareness to a routine activity at least once a day. 
                The more you practice mindfulness makes a difference to the way you experience it.
                
                Today's practice can be found at the following URL: {self.survey_url}
                We'll send you a reminder email if you don't manage to complete the survey today. 
                Note that after 3 reminders we will assume you have dropped out of the study, and will invite you to take the second survey. 
                You are welcome to repeat today’s practice as many times as you want, but don’t attempt to go beyond it until tomorrows session. 
                I will send tomorrows practice automatically the day after you complete the session linked above.
                Also feel free to tell me about any experiences you had, either during the sitting practice or during other daily activities.
                If you have any questions please contact m.lovell@sussex.ac.uk.
                The Mindfulness research group
                Please email m.lovell@sussex.ac.uk to unsubscribe from future emails.
                """
        elif self.body == 'day_3':
            body = f"""\
                This is a plain text version of this email as the HTML couldn't be loaded at this time.

                Thank you for completing yesterday’s practice and survey!
                Today's practice can be found at the following URL: {self.survey_url}
                We'll send you a reminder email if you don't manage to complete the survey today.

                Note that after 3 reminders we will assume you have dropped out of the study, and will invite you to take the second survey.
                You are welcome to repeat today’s practice as many times as you want, but don’t attempt to go beyond it until tomorrows session. 
                I will send tomorrows practice automatically the day after you complete the session linked above.
                Also feel free to tell me about any experiences you had, either during the sitting practice or during other daily activities.
                If you have any questions please contact mel29@sussex.ac.uk.
                
                The Mindfulness research group
                Please email m.lovell@sussex.ac.uk to unsubscribe from future emails.
                """
        elif self.body == 'post':
            body = f"""\
                Thank you for taking part in this study about learning mindfulness online!
                Now we are ready for the crucial second survey, which is similar to the first survey, and is available at the following URL: {self.survey_url}
                (NOTE: As this final survey contains a keyboard task, you will need a computer to fill it in - it is not mobile friendly)
                Afterwards, we will send you more information so you can continue your practice if you wish.
                
                Thanks again,
                
                The Mindfulness research group
                Please email m.lovell@sussex.ac.uk with any issues.
                """
        elif self.body == 'dropout':
            body = f"""\
                Dear Participant,
                
                As you didn't complete the last survey within three days we have assumed you have dropped out of the study and the link for that survey has closed.
                We would be very thankful if you would complete the follow-up second main survey, so we can retain your data.
                You can find this survey at the following link: {self.survey_url}
                (Note: As this final survey contains a keyboard task, you will need a computer to fill it in - it is not mobile friendly)
                
                Upon finishing the above survey, you will be given access to all course materials.
                We will send one reminder email about this post test survey before it closes, after which we will not email you again.
                
                If you wish to not recieve this next email or have any further questions, please email me at m.lovell@sussex.ac.uk
                
                Many thanks for your time on this project,
                
                Max Lovell
                """
        elif self.body == 'control_post':
            body = f"""\
                This is a follow-up email for the study about learning Mindfulness online. Thank you for taking part.
                You are now ready to complete the second survey, after which you will have access to all our mindfulness course materials, and an explanation of the study. 
                You can find the survey at the following URL: {self.survey_url}
                
                After the second survey you will be contacted with details of the mindfulness course itself, and given access to all our resources for how to learn mindfulness.
                
                If you have any questions please contact mel29@sussex.ac.uk
                Many thanks for your time on this project,
                
                Max Lovell
                """

        return  f"""\
            {reminder}
            {body}
            {self.footer}
            """