import datetime

def getDateTimeCurrent(query="%Y%m%d%H%M%S"):
    return datetime.datetime.now().strftime(query)