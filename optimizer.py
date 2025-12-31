# Phase 5: Optimization - Constant Folding, Dead Code, Peephole
from ir_generator import Quadruple

class Optimizer:
    def optimize(self, ir_code):
        # Pass 1: Constant Folding
        folded_code = self.constant_folding(ir_code)
        
        # Pass 2: Peephole Optimization
        peephole_code = self.peephole_optimization(folded_code)
        
        # Pass 3: Dead Code Elimination (Basic: After Return/Goto)
        # Note: Full DCE requires flow graph, here we do local block DCE
        final_code = self.dead_code_elimination(peephole_code)
        
        return final_code

    def constant_folding(self, ir_code):
        optimized_code = []
        constants = {} 

        for quad in ir_code:
            op, arg1, arg2, result = quad.op, quad.arg1, quad.arg2, quad.result
            
            # SAFEGUARD: Control Flow Merge Points
            if op == 'LABEL':
                constants.clear()
                optimized_code.append(quad)
                continue
            
            val1 = constants.get(arg1, arg1)
            val2 = constants.get(arg2, arg2)

            if op == '=' and self.is_number(str(val1)):
                # If direct assignment of number: t1 = 5
                constants[result] = str(val1)
                optimized_code.append(Quadruple('=', str(val1), None, result))
            elif self.is_number(str(val1)) and self.is_number(str(val2)) and op in ['+', '-', '*', '/', '^']:
                res_val = self.evaluate(op, val1, val2)
                constants[result] = str(res_val) 
                optimized_code.append(Quadruple('=', str(res_val), None, result))
            else:
                # Propagate constants if possible
                new_arg1 = val1 if val1 != arg1 else arg1
                new_arg2 = val2 if val2 != arg2 else arg2
                optimized_code.append(Quadruple(op, new_arg1, new_arg2, result))
        
        return optimized_code

    def peephole_optimization(self, ir_code):
        optimized = []
        i = 0
        while i < len(ir_code):
            q = ir_code[i]
            # Rule 1: Remove x = x
            if q.op == '=' and q.arg1 == q.result:
                i += 1
                continue
            
            # Rule 2: Algebraic Identities (x + 0 = x, x * 1 = x)
            if q.op == '+' and str(q.arg2) == '0':
                # Convert to assignment: result = arg1
                optimized.append(Quadruple('=', q.arg1, None, q.result))
                i += 1
                continue
            if q.op == '*' and str(q.arg2) == '1':
                optimized.append(Quadruple('=', q.arg1, None, q.result))
                i += 1
                continue
                
            optimized.append(q)
            i += 1
        return optimized

    def dead_code_elimination(self, ir_code):
        optimized = []
        # Remove code immediately following a RETURN or UNCONDITIONAL GOTO until a LABEL
        reachable = True
        
        for q in ir_code:
            if q.op == 'LABEL':
                reachable = True
            
            if reachable:
                optimized.append(q)
            
            if q.op in ['RETURN', 'GOTO', 'END_FUNC']: # Unconditional jump breaks flow
                reachable = False
                
        return optimized

    def is_number(self, s):
        if not s: return False
        try:
            float(s)
            return True
        except ValueError:
            return False

    def evaluate(self, op, v1, v2):
        try:
            f1 = float(v1)
            f2 = float(v2)
            is_int = f1.is_integer() and f2.is_integer()
            
            res = 0
            if op == '+': res = f1 + f2
            elif op == '-': res = f1 - f2
            elif op == '*': res = f1 * f2
            elif op == '/': res = f1 / f2 
            elif op == '^': res = f1 ** f2
            
            if is_int and op != '/': 
                return int(res)
            return res
        except:
            return 0
