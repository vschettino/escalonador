
class EscalonadorFCFS:
    """classe que represnta o Escalonador FCFS"""
    processList = []

    def __init__(self,pl):
        self.processList = pl;


    def start(self):
        for process in self.processList:
            start = time.time();
            process.execute();
            total = time.time() - start;
