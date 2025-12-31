class Symbol:
    def __init__(self, name, type_name=None, kind="var", params=None, mangled_name=None):
        self.name = name
        self.type = type_name
        self.kind = kind  # "var", "func", "param"
        self.params = params or [] # List of parameter types for functions, or empty
        self.mangled_name = mangled_name

    def __repr__(self):
        if self.kind == "func":
             params_str = ",".join(self.params)
             return f"<{self.name}:{self.kind}:{self.type}({params_str})>"
        return f"<{self.name}:{self.kind}:{self.type}:{self.mangled_name}>"

class SymbolTable:
    def __init__(self):
        self.scopes = [{}]  # Stack of scopes (dictionaries)
        self.counter = 0    # Global counter for unique names
        
        # Initialize Pre-defined functions if any (e.g. print?)
        # For now, empty. 
        # But we could add: self.define("print", "void", "func", ["any"])

    def enter_scope(self):
        self.scopes.append({})

    def exit_scope(self):
        self.scopes.pop()

    def define(self, name, type_name, kind="var", params=None):
        # Allow redeclaration check here if needed?
        # For now, we overwrite if same scope, or shadow if different scope.
        
        # Unique Name Generation for vars
        if kind in ["var", "param"]:
            self.counter += 1
            mangled_name = f"{name}_{self.counter}"
        else:
            mangled_name = name # Functions usually global/static names
            
        symbol = Symbol(name, type_name, kind, params, mangled_name)
        self.scopes[-1][name] = symbol
        return mangled_name

    def resolve(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None

    def __repr__(self):
        return str(self.scopes)
