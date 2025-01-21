import networkx as nx

portfolio_dag = nx.DiGraph()

portfolio_dag.add_node('portfolio_connect')
portfolio_dag.add_node('portfolio_update')
portfolio_dag.add_node('view_portfolio')
portfolio_dag.add_node('make_investment')
portfolio_dag.add_node('view_recommendations')
portfolio_dag.add_node('make_recommendation_changes')

portfolio_dag.add_edge('portfolio_connect', 'portfolio_update')
portfolio_dag.add_edge('portfolio_connect', 'view_portfolio')
portfolio_dag.add_edge('portfolio_connect', 'view_recommendations')
portfolio_dag.add_edge('view_recommendations', 'make_recommendation_changes')
