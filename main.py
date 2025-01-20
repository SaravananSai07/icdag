from dag import dag as portfolio_dag, execute_dag

ic_output = {"module": "portfolio", "intent": "view_portfolio", "user_id": 123}

dag_registry = {
    "portfolio": portfolio_dag
}

def process_intent(input):
    module = input["module"]
    if module not in dag_registry:
        print("Module not found in registry: ", module)
        return
    intent = input["intent"]
    print("Processing intent: ", intent)
    dag = dag_registry[module]
    if dag is None:
        print("Dag not found for intent: ", intent)
        return
    execute_dag(dag, input)

process_intent(ic_output)
