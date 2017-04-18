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
            self.delayOfArrival = int(arr[1]);
            self.timeToExecute = float(arr[2]);
            self.countOfSystemCalls = float(arr[3]);
            self.waitingTime = float(arr[4]);
            self.priority = int(arr[5].split("\\")[0]);
            return True;
        else:
            return False;

    def execute(self):
        start = time.time();
        print "Start process %s: %s" % (time.ctime(),self.id)
        time.sleep(int(round(float(self.timeToExecute)/10)))
        print "End : %s" % time.ctime()
        total = time.time() - start
        return total;
