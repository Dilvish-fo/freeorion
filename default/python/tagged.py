import requests
import time
import urlparse
import getpass

# For when you are really busy, swamped by notifications, and want to prioritize those where you are actually tagged.
# Prints subject line for all new notifications, and link for those where you are tagged

# WIP -- not sure if clickable link URL derivation works for all notification types

uname = None
if uname is None:
    uname = raw_input("Enter your github user name: ")
user_pw = None
if user_pw is None:
    user_pw = getpass.getpass("Enter the password for github user %s: " % uname)
auth = (uname, user_pw)
already_logged = set([''])
sep = u'/'
check_count = 0
preface = ''
while True:
    check_count += 1
    notifs_response = requests.get('https://api.github.com/repos/freeorion/freeorion/notifications', auth=auth)
    notifs = notifs_response.json()
    for notif in notifs:
        subject = notif.get('subject', {})
        this_log = preface + '* ' + subject.get('title', '')
        url = subject.get('url', '')
        comment_url = subject.get('latest_comment_url', '')
        this_type = subject.get('type', '')
        if comment_url not in already_logged:
            already_logged.add(comment_url)
            this_comment = requests.get(comment_url, auth=auth)
            comment = this_comment.json()
            body = comment.get('body', '')
            if uname.lower() in body.lower():
                # urlparts = urlparse.urlparse(url)
                # parts = urlparts._replace(netloc='github.com')
                # pathparts = parts.path.split(sep)
                # if pathparts[-2] == u'pulls':
                #     pathparts[-2] = u'pull'
                # parts = parts._replace(path=sep.join(pathparts[:1]+pathparts[2:]))
                # this_log += ": " + parts.geturl()
                this_log += ": " + comment.get(u'html_url', '')
            print this_log
            preface = ''
    if check_count >= 30:
        print ".",
        preface = '\n'
        check_count = check_count % 30
    time.sleep(30)

