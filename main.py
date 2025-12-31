# Compiler Project - Main Driver
import sys
from antlr4 import *
from CalcScriptLexer import CalcScriptLexer
from CalcScriptParser import CalcScriptParser
from semantic_analyzer import SemanticAnalyzer
from ir_generator import IRGenerator
from optimizer import Optimizer
from interpreter import Interpreter

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file>")
        return

    input_file = sys.argv[1]
    input_stream = FileStream(input_file)
    
    # 1. Lexical Analysis
    lexer = CalcScriptLexer(input_stream)
    stream = CommonTokenStream(lexer)
    stream.fill() # Load all tokens

    print("--- Phase 1: Lexical Analysis (Tokens) ---")
    # Chart 2: Lexeme Stream
    for token in stream.tokens:
        if token.type == Token.EOF: break
        # Get symbolic name
        type_name = lexer.symbolicNames[token.type]
        print(f"Token: {type_name:<15} Lexeme: '{token.text}'")

    parser = CalcScriptParser(stream)
    tree = parser.prog()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("Syntax Errors found. Aborting.")
        return

    print("--- Phase 1 & 2: Parse Tree generated ---")
    print(tree.toStringTree(recog=parser))
    
    # 2. Semantic Analysis
    print("\n--- Phase 3: Semantic Analysis ---")
    semantic_analyzer = SemanticAnalyzer()
    symbol_table, errors = semantic_analyzer.visit(tree)
    if errors:
        for e in errors:
            print(e)
        return
    print("Symbol Table:")
    print(symbol_table)
    
    # 3. Intermediate Code Generation
    print("\n--- Phase 4: Intermediate Code Generation ---")
    ir_gen = IRGenerator()
    ir_code = ir_gen.visit(tree)
    for q in ir_code:
        print(q)

    # 4. Optimization
    print("\n--- Phase 5: Optimization (Constant Folding) ---")
    optimizer = Optimizer()
    optimized_ir = optimizer.optimize(ir_code)
    for q in optimized_ir:
        print(q)

    # 5. Code Generation / Execution
    print("\n--- Phase 6: Execution ---")
    interpreter = Interpreter()
    interpreter.execute(optimized_ir)

if __name__ == '__main__':
    main()
