from datetime import datetime

class getTime :
    def year() :
        return datetime.now().year
    
    def month() :
        return datetime.now().month
    
    def day() :
        return datetime.now().day
    
    def hour() :
        return datetime.now().hour
    
    def minute() :
        return datetime.now().minute
    
    def second() :
        return datetime.now().second
    
    def date() :
        date_now = '{0:02d}/{1:02d}/{2:d}'.format(datetime.now().day , datetime.now().month , datetime.now().year)
        return date_now
    
    def time() :
        time_now = '{0:02d}:{1:02d}:{2:02d}'.format(datetime.now().hour , datetime.now().minute , datetime.now().second)
        return time_now

    def timeall() :
        return datetime.now()
