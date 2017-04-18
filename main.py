from Process import Process;
from EscalonadorFCFS import EscalonadorFCFS
from EscalonadorSJF import EscalonadorSJF

f = open("tasks.txt", "r")
processList = [];
for line in f:
    p = Process();
    if(p.populateFromArray(line.split(" "))):
        processList.append(p);

#escalonador = EscalonadorFCFS(processList);
escalonador = EscalonadorSJF(processList);
escalonador.start();
