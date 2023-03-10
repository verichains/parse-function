import json
from eth_abi import decode_abi
import re


def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def print_arg(type_, value):
    if type_.startswith('int') or type_.startswith('uint'):
        return f'({type_})(0x{value})'
    if type_ == 'address':
        return f'({type_})(0x{value})'
    if type_.startswith('bytes'):
        return f'({type_})(0x{value.hex()})'
    if type_.startswith('string'):
        return f'({type_})("{value}")'
    return f'({type_})({value})'


def decode_function(input_data, output_data):
    methods = json.loads(read_file("4bytes.json"))

    method_id_ = input_data[:10] if input_data else ''
    method = methods.get(method_id_, method_id_)
    method_str = f"{method}(0x{input_data[10:]})"

    if method.endswith(')'):
        input_ = (input_data or '')[10:]
        method_name = method.split('(')[0]

        if method.count('(') == 1:
            in_types = method.split('(')[1][:-1].split(',')
        else:
            in_types = []
            iter_ = in_types
            backs = []
            for letter in method[method.index('(') + 1:]:
                if letter == '(':
                    iter_.append([])
                    backs.append(iter_)
                    iter_ = iter_[-1]
                elif letter == ')':
                    iter_ = backs.pop()
                elif letter == ',':
                    iter_.append("")
                else:
                    if not iter_ or not isinstance(iter_[-1], str):
                        iter_.append("")
                    iter_[-1] += letter

        in_decoded = decode_abi(in_types, bytes.fromhex(input_))
        method_str = f'{method_name}({", ".join(print_arg(type_, value) for type_, value in zip(in_types, in_decoded))})'

    if output_data:
        short_result = re.sub(r'0x0+', '0x', output_data)
        method_str += ':' + ('0x0' if short_result == '0x' else short_result)

    return method_str
