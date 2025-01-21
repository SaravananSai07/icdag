from core.function_registry import function_registry

def portfolio_connect(params):
    print("Portfolio connect trigger: ", params)

def portfolio_update(params):
    print("Portfolio update trigger: ", params)

def view_portfolio(params):
    print("Get portfolio details: ", params)

def make_investment(params):
    print("Build investment trigger: ", params)

def register():
    function_registry.register("portfolio_connect", portfolio_connect)
    function_registry.register("portfolio_update", portfolio_update)
    function_registry.register("view_portfolio", view_portfolio)
    function_registry.register("make_investment", make_investment)
    print("Portfolio functions registered: ", function_registry.registry)
