import time
class EscalonadorSJF:
    """classe que represnta o Escalonador SJF"""
    processList = []
    resFileName = 'resultadosSJF.txt'
    resFile = ""

    def __init__(self,pl):
        self.processList = pl
        self.resFile = open(self.resFileName, "w+")


    def start(self):
        total = 0
        self.processList = sorted(self.processList, key=lambda process: process.timeToExecute)
        for process in self.processList:
            process.execute()
            self.writeResults(total, process)
            total += process.timeToExecute

    def writeResults(self, total, process):
        self.resFile.write(process.id + " " + str(total) + " " + str(total+process.timeToExecute) + "\n")
