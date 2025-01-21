from core.function_registry import function_registry

def get_security_details(params):
    print("Get security details: ", params)

def get_securities_by_criteria(params):
    print("Get securities by criteria: ", params)

def register():
    function_registry.register("get_security_details", get_security_details)
    function_registry.register("get_securities_by_criteria", get_securities_by_criteria)
