import networkx as nx

securities_dag = nx.DiGraph()

securities_dag.add_node('security_details')
securities_dag.add_node('securities_by_criteria')
securities_dag.add_node('compare_securities')
securities_dag.add_node('compare_with_peers')
securities_dag.add_node('filter_comparable_securities')

securities_dag.add_edge('filter_comparable_securities', 'compare_securities')
