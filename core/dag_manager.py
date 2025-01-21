import networkx as nx
from core.function_registry import function_registry

class DAGManager:
    def __init__(self):
        self.module_dags = {}

    def register_module_dag(self, module_name, dag):
        """Register a DAG for a module."""
        self.module_dags[module_name] = dag

    def create_dynamic_dag(self, intents):
        """Create a dynamic DAG by merging relevant module DAGs."""
        dynamic_dag = nx.DiGraph()
        for module_dag in self.module_dags.values():
            for intent in intents:
                if intent in module_dag:
                    relevant_nodes = nx.ancestors(module_dag, intent)
                    relevant_nodes.add(intent)
                    subgraph = module_dag.subgraph(relevant_nodes)
                    # dynamic_dag.update(subgraph)
                    dynamic_dag.add_nodes_from(subgraph.nodes(data=True))
                    dynamic_dag.add_edges_from(subgraph.edges(data=True))
        print(f"Dynamic DAG: {dynamic_dag.nodes}")
        return dynamic_dag

    def execute_dynamic_dag(self, intents, **kwargs):
        """Execute the dynamic DAG."""
        dynamic_dag = self.create_dynamic_dag(intents)
        sorted_nodes = list(nx.topological_sort(dynamic_dag))
        print(f"Sorted nodes: {sorted_nodes}")
        for node in sorted_nodes:
            func = function_registry.get(node)
            print(f"Function to be executed: {func}")
            if func:
                print(f"Executing node: {node}")
                func(kwargs)

dag_manager = DAGManager()
