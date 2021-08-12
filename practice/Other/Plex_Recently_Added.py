from email.mime import text
from plexapi.server import PlexServer
baseurl = 'http://plexserver:32400'
token = 'obfuscated'
plex = PlexServer(baseurl, token)

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_user = 'User Name for Email Service'
smtp_password = 'Password for Email Service'

recently_added = plex.library.recentlyAdded()
media_titles = []

for media in recently_added[:15]:
    media = str(media)
    if media[1:6] == 'Movie':
        movie = media.replace('-', ' ')
        movie = movie[1:7] + movie[12:-1]
        media_titles.append(movie)
    elif media[1:5] == "Show":
        show = media.replace('-', ' ')
        show = show[1:6] + show[11:-1]
        media_titles.append(show)

sender = 'email@domain.com'

receivers = ['email1@domain.com','email2@domain.com']

body = '\r\n'.join(media_titles) + """
\n This is an automated message listing the last 15 media titles that have been added to my plex server.
\n If you would like to unsubscribe or change your email address, please reply to this message and I will update the mailing list. 
\n Thanks for watching!
\n Regards,
\n First Name Last Name
"""

subject = 'Check out what\'s new on Plex!'

for receiver in receivers:
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    msg.attach(MIMEText(body,'plain'))
    text = msg.as_string()
    try:
        server = smtplib.SMTP(host='relay.dnsexit.com', port=587, timeout=120)
        #server.set_debuglevel(1)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(smtp_user, smtp_password)
        server.sendmail(sender, receiver, text)
        server.quit()
        print('Email sent!')
    except smtplib.SMTPConnectError:
        print('SMTP Connect Error')
    except smtplib.SMTPHeloError:
        print('SMTP Helo error')
    except smtplib.SMTPResponseException:
        print('SMTP Response error')
    except smtplib.SMTPSenderRefused:
        print('Sender Address Refused')
    except smtplib.SMTPRecipientsRefused:
        print('Recipient refused')
    except smtplib.SMTPAuthenticationError:
        print('Authentication Error')