class Symbol:
    def __init__(self, name, type_name=None):
        self.name = name
        self.type = type_name

    def __repr__(self):
        return f"<{self.name}:{self.type}>"

class SymbolTable:
    def __init__(self):
        self.scopes = [{}]  # Stack of scopes (dictionaries)

    def enter_scope(self):
        self.scopes.append({})

    def exit_scope(self):
        self.scopes.pop()

    def define(self, name, type_name):
        self.scopes[-1][name] = Symbol(name, type_name)

    def resolve(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None

    def __repr__(self):
        return str(self.scopes)
