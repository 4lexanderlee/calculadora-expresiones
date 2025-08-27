def evaluar_expresion(expresion: str):
    # This is the code for the REFACTOR phase.
    # It replaces the simple eval() function with a more secure and robust solution.
    import re

    # A simple tokenizer to separate numbers, operators, and parentheses
    tokens = re.findall(r"(\d+\.?\d*|[\+\-\*\/\(\)])", expresion.replace(" ", ""))

    # Shunting-yard algorithm implementation
    def shunting_yard(tokens):
        output_queue = []
        operator_stack = []
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

        for token in tokens:
            if re.match(r"^\d+\.?\d*$", token):
                output_queue.append(token)
            elif token in precedence:
                while (operator_stack and operator_stack[-1] != '(' and
                       precedence.get(operator_stack[-1], 0) >= precedence.get(token, 0)):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                if operator_stack and operator_stack[-1] == '(':
                    operator_stack.pop()

        while operator_stack:
            output_queue.append(operator_stack.pop())
        
        return output_queue

    # Postfix evaluation
    def evaluate_postfix(tokens):
        operand_stack = []
        for token in tokens:
            if re.match(r"^\d+\.?\d*$", token):
                operand_stack.append(float(token))
            else:
                right = operand_stack.pop()
                left = operand_stack.pop()
                if token == '+':
                    operand_stack.append(left + right)
                elif token == '-':
                    operand_stack.append(left - right)
                elif token == '*':
                    operand_stack.append(left * right)
                elif token == '/':
                    if right == 0:
                        raise ZeroDivisionError("Division by zero is not allowed")
                    operand_stack.append(left / right)
        return operand_stack[0]

    try:
        postfix_tokens = shunting_yard(tokens)
        return evaluate_postfix(postfix_tokens)
    except IndexError:
        return "Invalid expression"