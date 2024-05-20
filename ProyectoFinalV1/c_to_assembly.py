def translate_to_assembler(c_code):
    assembly_code = []
    c_to_assembler = {
        'int': '',  # 'int' keyword will be handled separately
        '+': 'add',
        '-': 'sub',
        '*': 'mul',
        '/': 'div',
        '=': 'mov',
        'return': 'mov eax,',
        'printf': 'call printf',
        'scanf': 'call scanf'
        # Add more mappings as needed
    }

    lines = c_code.strip().split('\n')
    variable_declarations = {}
    label_counter = 0

    for line in lines:
        line = line.strip().strip(';')
        if not line:
            continue
        tokens = line.split()

        # Handle main function
        if line.startswith('int main'):
            assembly_code.append('section .text')
            assembly_code.append('global main')
            assembly_code.append('main:')

        # Handle variable declarations
        elif tokens[0] == 'int':
            var_name = tokens[1]
            if len(tokens) > 3 and tokens[2] == '=':
                var_value = tokens[3]
                assembly_code.append(f'mov dword [{var_name}], {var_value}')
            else:
                assembly_code.append(f'mov dword [{var_name}], 0')
            variable_declarations[var_name] = 0

        # Handle arithmetic operations
        elif '=' in tokens:
            dest = tokens[0]
            src = tokens[2:]
            if len(src) == 1:
                src = src[0]
                assembly_code.append(f'mov eax, {src}')
                assembly_code.append(f'mov [{dest}], eax')
            else:
                operand1 = src[0]
                operator = src[1]
                operand2 = src[2]
                assembly_code.append(f'mov eax, {operand1}')
                assembly_code.append(f'{c_to_assembler[operator]} eax, {operand2}')
                assembly_code.append(f'mov [{dest}], eax')

        # Handle return statement
        elif tokens[0] == 'return':
            ret_value = tokens[1]
            assembly_code.append(f'mov eax, {ret_value}')
            assembly_code.append('ret')

    return '\n'.join(assembly_code)

def generate_intermediate_code(parser):
    # Generate intermediate code from the parser
    intermediate_code = []
    # Implementation here
    return intermediate_code

def optimize_code(intermediate_code):
    # Optimize the intermediate code
    optimized_code = intermediate_code
    # Implementation here
    return optimized_code

def generate_machine_code(intermediate_code):
    # Generate machine code from the intermediate code
    machine_code = []
    # Implementation here
    return machine_code

# Example usage:
c_code = """
int main() {
    int a = 10;
    int b = 20;
    int c = a + b;
    return 0;
}
"""

assembly_code = translate_to_assembler(c_code)
print(assembly_code)
