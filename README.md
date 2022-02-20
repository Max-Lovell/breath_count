# breath_count

JavaScript/HTML/CSS code for a breath counting task for integration with a qualtrics survey using a text/graphic question. 

Participants are instructed to press the up arrow 8 times, then the down arrow once, and then give a confidence rating of 'certain' they had the correct count (left arrow), or 'unsure' (right arrow) of their count, with the spacebar as a reset.

Working example: https://universityofsussex.eu.qualtrics.com/jfe/form/SV_38c0pGjHcapwlVA

Originally used as an 'objective' measure of mindfulness for use with a meta-d' analysis.

Data produced is just a .csv file with a single row of RT and Keypress to extract data from.

Other files:
- PHP file to accept data from this task
- PHP file to parse Qualtrics Webservice URLs with query strings that give the survey taken, email, and date.
- Batch file to download files from the server - i.e. 1) Qualtrics survey data export automations, breath task data, and webservice JSON.
- Python file to take webservice JSON data and send emails if people missed a meditation session.
- Python file containing email content
- XML file used to automate Python Emailer after automated data download task in Windows Task Scheduler was completed

note all file paths and URLS have been removed.

Feel free to email me at m.lovell [at] sussex [dot] ac [dot] uk with any questions.
