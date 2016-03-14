#! /usr/bin/env python
import datetime
import os
now = datetime.datetime.utcnow()
hour = now.hour
hour = str(hour)
SMDIR = '/home/lee/www/arlplanet/skymaps/'
s = open(SMDIR+"skymap.html", "w")
s.write("""
<!DOCTYPE HTML><html><head><meta http-equiv="refresh" content="2; url=%s"><meta content="text/html;charset=utf-8" http-equiv="Content-Type" /><meta content="width=device-width, initial-scale=1.0" name="viewport" /> <title>Arlington Skymap</title> </head>
        <body style="background: white;">
   Redirecting to sky map for current time. Click <a href="%s">here</a> if not redirected.
</body></html>
        """ % (hour, hour))
# os.system('find %s -mmin +1440 -exec rm {} \;' % SMDIR)
