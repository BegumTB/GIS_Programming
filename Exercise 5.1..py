>>> import time
>>> epoch =  time.time()
>>> total_sec = epoch %86400
>>> hours = int(total_sec/3600)
>>> total_min = int(total_sec/60)
>>> mins = total_min % 60
>>> sec = int(total_sec %60)
>>> days = int (epoch/86400)
>>> 
>>> print("Number of days since the epoch:", days,",", "Current time:", hours,"hours",mins,"minutes", sec, "seconds",".")
Number of days since the epoch: 18537 , Current time: 21 hours 34 minutes 24 seconds .
>>>
