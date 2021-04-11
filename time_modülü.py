from datetime import datetime,timedelta
result=datetime.now()
now=result
result=result.year
result=datetime.today()
#result=datetime.ctime(result)
result=datetime.strftime(result,"%A")

t="29 February 2001"
#gün,ay,yıl=t.split()
dt=datetime.strptime(t,"%d %B %Y")
result=datetime(2001,2,2,15,30,20)
result=datetime.timestamp(result)
result=datetime.fromtimestamp(result)
result=now-dt
result=now+timedelta(days=20,minutes=90)
#print(gün)
#print(ay)
#print(yıl)
#print(result.days)
print(result)
#print(dt.year)