# Phase 6: Code Generation - Executable Output / Interpreter
class Interpreter:
    def execute(self, ir_code):
        pc = 0
        memory = {} # Variables and Temps
        labels = {} # Map label name to instruction index

        # First pass: find labels
        for i, quad in enumerate(ir_code):
            if quad.op == 'LABEL':
                labels[quad.result] = i

        while pc < len(ir_code):
            quad = ir_code[pc]
            op, arg1, arg2, res = quad.op, quad.arg1, quad.arg2, quad.result
            
            # Helper to get value
            def val(x):
                # If x is a string number, return float or int
                try:
                    f = float(x)
                    if f.is_integer():
                        return int(f)
                    return f
                except ValueError:
                    v = memory.get(x, 0)
                    if isinstance(v, float) and v.is_integer():
                        return int(v)
                    return v
                except TypeError:
                    return 0

            if op == '=':
                memory[res] = val(arg1)
            elif op == '+':
                memory[res] = val(arg1) + val(arg2)
            elif op == '-':
                memory[res] = val(arg1) - val(arg2)
            elif op == '*':
                memory[res] = val(arg1) * val(arg2)
            elif op == '/':
                memory[res] = val(arg1) / val(arg2)
            elif op == '^':
                memory[res] = val(arg1) ** val(arg2)
            elif op == '>':
                memory[res] = 1 if val(arg1) > val(arg2) else 0
            elif op == '<':
                memory[res] = 1 if val(arg1) < val(arg2) else 0
            elif op == '>=':
                memory[res] = 1 if val(arg1) >= val(arg2) else 0
            elif op == '<=':
                memory[res] = 1 if val(arg1) <= val(arg2) else 0
            elif op == '==':
                memory[res] = 1 if val(arg1) == val(arg2) else 0
            elif op == '!=':
                memory[res] = 1 if val(arg1) != val(arg2) else 0
            
            elif op == 'PRINT':
                print(val(arg1))

            elif op == 'GOTO':
                if res in labels:
                    pc = labels[res]
                    continue
                else:
                    raise Exception(f"Label {res} not found")

            elif op == 'IF_FALSE':
                # arg1 is condition
                if val(arg1) == 0:
                    if res in labels:
                        pc = labels[res]
                        continue
            
            # LABEL, etc. just continue
            pc += 1
