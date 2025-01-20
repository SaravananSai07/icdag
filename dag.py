import networkx as nx
from functions import portfolio_connect, portfolio_update, view_portfolio, make_investment, view_recommendations, make_recommendation_changes

dag = nx.DiGraph()

dag.add_node('portfolio_connect')
dag.add_node('portfolio_update')
dag.add_node('view_portfolio')
dag.add_node('make_investment')
dag.add_node('view_recommendations')
dag.add_node('make_recommendation_changes')

dag.add_edge('portfolio_connect', 'portfolio_update')
dag.add_edge('portfolio_connect', 'view_portfolio')
dag.add_edge('portfolio_connect', 'view_recommendations')
dag.add_edge('view_recommendations', 'make_recommendation_changes')

function_registry = {
    'portfolio_connect': portfolio_connect,
    'portfolio_update': portfolio_update,
    'view_portfolio': view_portfolio,
    'make_investment': make_investment,
    'view_recommendations': view_recommendations,
    'make_recommendation_changes': make_recommendation_changes
}

def execute_dag(dag, params):
    target_node = params["intent"]
    if target_node not in function_registry:
        print("Intent not found in registry: ", target_node)
        return

    relevant_nodes = set()
    relevant_nodes.add(target_node)
    relevant_nodes.update(dag.predecessors(target_node))

    sorted_nodes = list(nx.topological_sort(dag.subgraph(relevant_nodes)))
    print("Sorted nodes: ", sorted_nodes)

    for node in sorted_nodes:
        if node not in function_registry:
            print("Node not found in registry: ", node)
            continue
        print("Executing node: ", node)
        function_registry[node](params)
