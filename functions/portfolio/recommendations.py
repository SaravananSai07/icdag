from core.function_registry import function_registry

def view_recommendations(params):
    print("Get recommendations: ", params)

def make_recommendation_changes(params):
    print("Update portfolio with recommendation changes: ", params)

def register():
    function_registry.register("view_recommendations", view_recommendations)
    function_registry.register("make_recommendation_changes", make_recommendation_changes)
    print("Portfolio functions registered: ", function_registry.registry)
