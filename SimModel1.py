from Model import Model
from Create import Create
from Process import Process


class SimModel1():
    def __init__(self):
        c = Create(delay_mean = 1.0, name = 'CREATOR', distribution = 'exp')
        p = Process(maxqueue = 2, delay_mean = 10.0, name = 'PROCESSOR_01', distribution = 'exp')

        c.next_elements = [p]
        elements = [c, p]
        model = Model(elements, display_logs = True)
        model.simulate(100)