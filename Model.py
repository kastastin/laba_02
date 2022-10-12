import numpy as np
from Despose import Despose
from Process import Process


class Model():
    def __init__(self, elements=[], display_logs=False):
        self.elements = elements
        self.tnext = 0
        self.event = elements[0]
        self.tcurr = self.tnext
        self.display_logs = display_logs
        
    def simulate(self, time):
        self.time_modeling = time
        while self.tcurr < self.time_modeling:
            self.tnext = np.inf

            for element in self.elements:
                tnext_min = np.min(element.tnexts) # Найменше значення моменту часу з усіх елементів
                if tnext_min < self.tnext and not isinstance(element, Despose):
                    self.tnext = tnext_min
                    self.event = element

            if self.display_logs:
                print(f'\nIt is time for event in {self.event.name}, time = {np.round(self.tnext, 9)}')
            
            for element in self.elements:
                element.do_statistics(self.tnext - self.tcurr) # вираховуємо статистики
                
            # Переміщення до операції завершення
            self.tcurr = self.tnext
            for element in self.elements:
                element.tcurr = self.tcurr
            
            self.event.out_act() # Операція завершення (вихід з елементу)
            
            # Введення здійснення відповідної події для всіх елементів,
            # у яких час наступної події == поточному моменту часу,
            # для зменшення обсягу обчислень
            for element in self.elements:
                if self.tcurr in element.tnexts:
                    element.out_act()

            self.print_info()

        return self.print_statistic()
        
    def print_info(self):
        for element in self.elements:
            element.print_info()
            
    def print_statistic(self):
        n_processors = 0
        global_mean_load_accumulator = 0
        print('\n----------RESULTS----------')
        
        for e in self.elements:
            e.print_statistic()
            if isinstance(e, Process):
                n_processors += 1
                mean_queue = e.mean_queue / self.tcurr
                failure_probability = e.failure / (e.failure + e.quantity) if (e.failure + e.quantity) != 0 else 0
                mean_load = e.quantity / self.time_modeling
                global_mean_load_accumulator += mean_load
                
                if self.display_logs:
                    print(f"Mean length of queue = {mean_queue}")
                    print(f"Failure Probability = {failure_probability}")
                    print(f"Average Loading: {mean_load}\n")
                
        global_mean_load = global_mean_load_accumulator / n_processors
        
        if self.display_logs:
            print(f"Average Global Loading: {global_mean_load}\n")
        
        return { "global_mean_load": global_mean_load }