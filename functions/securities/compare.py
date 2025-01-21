from core.function_registry import function_registry

def compare_securities(params):
    print("Compare specified securities: ", params)

def compare_with_peers(params):
    print("Compare with peers: ", params)

def filter_comparable_securities(params):
    print("Filter comparable securities: ", params)

def register():
    function_registry.register("compare_securities", compare_securities)
    function_registry.register("compare_with_peers", compare_with_peers)
    function_registry.register("filter_comparable_securities", filter_comparable_securities)
