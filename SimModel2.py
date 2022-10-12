from Model import Model
from Process import Process
from Create import Create
from Despose import Despose


class SimModel2():
    def __init__(self):
        c = Create(delay_mean = 1, name = 'CREATOR', distribution = 'exp')
        p1 = Process(maxqueue = 2, delay_mean = 1.0, name = 'PROCESSOR_01', distribution = 'exp')
        p2 = Process(maxqueue = 2, delay_mean = 1.0, name = 'PROCESSOR_02', distribution = 'exp')
        p3 = Process(maxqueue = 2, delay_mean = 1.0, name = 'PROCESSOR_03', distribution = 'exp')
        d = Despose(delay_mean = 0, name = 'DESPOSER')
        
        c.next_elements = [p1]
        p1.next_elements = [p2]
        p2.next_elements = [p3]
        p3.next_elements = [d]
        
        c.p = [1]
        p1.p = [1]
        p2.p = [1]
        p3.p = [1]
        
        elements = [c, p1, p2, p3, d]

        model = Model(elements, display_logs = True)
        model.simulate(50)