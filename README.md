# breath_count

JavaScript/HTML/CSS code for a breath counting task for integration with a qualtrics survey using a text/graphic question. 

Participants are instructed to press the up arrow 8 times, then the down arrow once, and then give a confidence rating of 'certain' they had the correct count (left arrow), or 'unsure' (right arrow) of their count, with the spacebar as a reset.

Working example: https://universityofsussex.eu.qualtrics.com/jfe/form/SV_38c0pGjHcapwlVA

Originally used as an 'objective' measure of mindfulness for use with a meta-d' analysis within an online mindfulness course.

Data produced is just a .csv file with a single row of RT and Keypress to extract data from.

Other files:
- PHP file to accept data from this task
- PHP file to parse Qualtrics Webservice URLs with query strings that give the survey taken, email, and date (used to get around Qualtrics email restrictions).
- Batch file to download files from the server - i.e. 1) Qualtrics survey data export automations, breath task data, and webservice JSON.
- Python file to take webservice JSON data and send emails if people missed a meditation session.
- Python file containing email content.
- XML file used to automate Python Emailer after automated data download task in Windows Task Scheduler was completed.

notes:
- all file paths and URLS have been removed.
- Note that qualtrics will not count emails sent with the emailer as the same person they recorded with this set up - best to use the 'prevent retakes option' in qualtrics aswell.

Feel free to email me at m.lovell [at] sussex [dot] ac [dot] uk with any questions or suggestions.
