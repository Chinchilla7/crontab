Pulling data from https://health.data.ny.gov/Health/Childhood-Blood-Lead-Testing-and-Elevated-Incidenc/d54z-enu8

Our cron jobs are:

Once a day: '48 23 * * */usr/bin/python3 /home/regina/crontab/assignment6.py > log.txt 2>&1 &'

Sunday at 10pm: '00 22 * * 7/usr/bin/python3 /home/regina/crontab/assignment6.py > log.txt 2>&1 &'

End of the quarter: 
'59 23 31 3,12 */usr/bin/python3 /home/regina/crontab/assignment6.py > log.txt 2>&1 &'
'59 23 30 6,9 */usr/bin/python3 /home/regina/crontab/assignment6.py > log.txt 2>&1 &'

Testing :'* * * * */usr/bin/python3 /home/regina/crontab/assignment6.pylog.txt 2>&1 &'

