import time
class Process:
    """classe que representa cada processo"""
    id = ""
    arrivalOrder = ""
    delayOfArrival = ""
    timeToExecute = ""
    countOfSystemCalls = ""
    waitingTime = ""
    priority = ""

    def populateFromArray(self, arr):
        if(len(arr) == 6):
            self.id = arr[0];
            self.delayOfArrival = arr[1];
            self.timeToExecute = arr[2];
            self.countOfSystemCalls = arr[3];
            self.waitingTime = arr[4];
            self.priority = arr[5].split("\\")[0];
            return True;
        else:
            return False;

    def execute(self):
        print "Start process %s: %s" % (time.ctime(),self.id)
        time.sleep(int(round(float(self.timeToExecute)/10)))
        print "End : %s" % time.ctime()
        total = time.time - time
