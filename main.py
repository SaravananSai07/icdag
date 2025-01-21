from functions.portfolio import portfolio
from functions.securities import security
from functions.securities import compare
from core.dag_manager import dag_manager
from dags.portfolio_dag import portfolio_dag
from dags.securities_dag import securities_dag

ic_output = [{"module": "portfolio", "intent": "view_portfolio", "user_id": 123}, {"module": "securities", "intent": "compare_securities", "user_id": 123}]
intents = []
args = {}
for intent in ic_output:
    intents.append(intent["intent"])
    for key, value in intent.items():
        if key not in ["intent", "module"]:
            args[key] = value

portfolio.register()
security.register()
compare.register()

dag_manager.register_module_dag("portfolio", portfolio_dag)
dag_manager.register_module_dag("securities", securities_dag)

dag_manager.execute_dynamic_dag(intents, **args)
