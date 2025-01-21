class FunctionRegistry:
    def __init__(self):
        self.registry = {}

    def register(self, name, func):
        """Register a function with a name."""
        self.registry[name] = func

    def get(self, name):
        """Retrieve a function by name."""
        return self.registry.get(name, None)

function_registry = FunctionRegistry()
