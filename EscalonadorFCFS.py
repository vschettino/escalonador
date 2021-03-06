import time
class EscalonadorFCFS:
    """classe que represnta o Escalonador FCFS"""
    processList = []
    resFileName = 'resultadosFCFS.txt'
    resFile = ""

    def __init__(self,pl):
        self.processList = pl
        self.resFile = open(self.resFileName, "w+")


    def start(self):
        total = 0
        for process in self.processList:
            process.execute()
            self.writeResults(total, process)
            total += process.timeToExecute

    def writeResults(self, total, process):
        self.resFile.write(process.id + " " + str(total) + " " + str(total+process.timeToExecute) + "\n")
