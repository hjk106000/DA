#############################################################################################
# File: networkX.py
#
# textbook: Introduction to Data Science Using Python, Afrand Agah, PA-ADOPT, 2024
# https://it-ebooks.dev/books/data-science-and-ai/introduction-to-data-science-using-python
# chapter 13. NetworkX  fig 13.1
#
# Description: 
# NetworkX is a Python package for the creation, manipulation, 
# and study of the structure, dynamics, and functions of complex networks.
#############################################################################################


import networkx as nx
import matplotlib.pyplot as plt

G = nx.krackhardt_kite_graph()
nx.draw_networkx(G)
plt.show() 
