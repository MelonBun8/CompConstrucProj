class Symbol:
    def __init__(self, name, type_name=None, mangled_name=None):
        self.name = name
        self.type = type_name
        self.mangled_name = mangled_name

    def __repr__(self):
        return f"<{self.name}:{self.type}:{self.mangled_name}>"

class SymbolTable:
    def __init__(self):
        self.scopes = [{}]  # Stack of scopes (dictionaries)
        self.counter = 0    # Global counter for unique names

    def enter_scope(self):
        self.scopes.append({})

    def exit_scope(self):
        self.scopes.pop()

    def define(self, name, type_name):
        # If already defined in current scope, reuse the existing symbol (mutable variable)
        # This prevents creating a new SSA-like version which breaks loops without Phi nodes
        if name in self.scopes[-1]:
            # Update type if needed, or keep existing
            symbol = self.scopes[-1][name]
            # If type was unknown and now we know it, could update, but for IR it's fine.
            return symbol.mangled_name

        # Generate a unique mangled name
        self.counter += 1
        mangled_name = f"{name}_{self.counter}"
        symbol = Symbol(name, type_name, mangled_name)
        self.scopes[-1][name] = symbol
        return mangled_name

    def resolve(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None

    def __repr__(self):
        return str(self.scopes)
