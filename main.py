import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import graph_tool
import pandas as pd
from read_data import get_network_df, get_corrs

plt.rcParams.update({'font.size': 14})

net_df = get_network_df(Path('SiouxFalls') / 'SiouxFalls_net.tntp')
corrs = get_corrs(Path('SiouxFalls') / 'SiouxFalls_trips.tntp')

graph = graph_tool.Graph(net_df.values, eprops=[('capacity', 'double'), ('fft', 'double')])

from graph_tool.draw import graph_draw
graph_draw(graph, vertex_text=graph.vertex_index)

