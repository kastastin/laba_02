import pandas as pd
from Element import Element
from Model import Model
from Create import Create
from Process import Process
from IPython.display import clear_output

n_param = 10
process_delay_list = [1] * n_param + [1] * n_param
creation_delay_list = [1] * n_param + [1] * n_param
max_Q_list = [3] * n_param + [5] * n_param
time_modeling_list = [i * 100 for i in range(1, n_param + 1)] + [i * 100 for i in range(1, n_param + 1)]

rows = []
df = pd.DataFrame()

for i in range(n_param * 2):
    Element.id = 0
    c = Create(delay_mean = creation_delay_list[i], name = 'CREATOR', distribution = 'exp')
    p = Process(maxqueue = max_Q_list[i], delay_mean = process_delay_list[i], name = 'PROCESSOR', distribution = 'exp')
    c.next_elements = [p]
    elements = [c, p]
    model = Model(elements, display_logs = False)
    simulation_result = model.simulate(time_modeling_list[i])
    param = { 'delay_mean_create': creation_delay_list[i],
              'delay_process_create': process_delay_list[i],
              'distribution': 'exp',
              'maxqueue': max_Q_list[i],
              'time_modeling': time_modeling_list[i] }
    rows.append( {**param, **simulation_result} )

df = df.append(rows)
clear_output()
with pd.option_context('display.max_rows', 10):
    print(df.to_string())