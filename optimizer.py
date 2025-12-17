from ir_generator import Quadruple

class Optimizer:
    def optimize(self, ir_code):
        optimized_code = []
        constants = {} # Map temp vars to constant values if known

        for quad in ir_code:
            op, arg1, arg2, result = quad.op, quad.arg1, quad.arg2, quad.result
            
            # Resolve arguments if they are temps that hold constants
            val1 = constants.get(arg1, arg1)
            val2 = constants.get(arg2, arg2)

            if self.is_number(val1) and self.is_number(val2) and op in ['+', '-', '*', '/', '^']:
                # Perform the operation
                res_val = self.evaluate(op, val1, val2)
                constants[result] = str(res_val) # Store result as constant
                # We can either emit an assignment or skip. 
                # If we skip, we must ensure 'result' is replaced by 'res_val' in future uses.
                # However, our simple IR structure assumes 'result' is a destination.
                # To be safe and simple: convert to assignment: result = const
                optimized_code.append(Quadruple('=', str(res_val), None, result))
            else:
                # Update args if we found they were constants, for propagation
                # But don't change original quad if not folding completely?
                # Actually, constant propagation is good.
                new_arg1 = val1 if val1 != arg1 else arg1
                new_arg2 = val2 if val2 != arg2 else arg2
                optimized_code.append(Quadruple(op, new_arg1, new_arg2, result))
        
        return optimized_code

    def is_number(self, s):
        if not s: return False
        try:
            float(s)
            return True
        except ValueError:
            return False

    def evaluate(self, op, v1, v2):
        f1 = float(v1)
        f2 = float(v2)
        if op == '+': return f1 + f2
        if op == '-': return f1 - f2
        if op == '*': return f1 * f2
        if op == '/': return f1 / f2
        if op == '^': return f1 ** f2
        return 0
