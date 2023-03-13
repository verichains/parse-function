import json
from eth_abi import decode_abi
import re


# Example: input: 0xa9059cbb000000000000000000000000c663b28080e514662b469600bb3e69597fa1197400000000000000000000000000000000000000000000000000000000071596d2
# Example: output: 0x0000000000000000000000000000000000000000000000000000000000000001
# Return: transfer((address)(0xc663b28080e514662b469600bb3e69597fa11974), (uint256)(118855378)):0x1
def main(input_data, output_data):
    decoded_function = decode_function(input_data, output_data)
    return decoded_function


def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def print_arg(type_, value):
    if type_.startswith('int') or type_.startswith('uint'):
        return f'({type_})({value})'
    if type_ == 'address':
        return f'({type_})({value})'
    if type_.startswith('bytes'):
        return f'({type_})(0x{value.hex()})'
    if type_.startswith('string'):
        return f'({type_})("{value}")'
    return f'({type_})({value})'


# Example: input_data: 0xa9059cbb000000000000000000000000c663b28080e514662b469600bb3e69597fa1197400000000000000000000000000000000000000000000000000000000071596d2
# Example: output_data: 0x0000000000000000000000000000000000000000000000000000000000000001
def decode_function(input_data, output_data):
    """
    Decode function from input and output transaction data
    :param input_data
    :param output_data
    :return: decoded function
    """

    # Load the list of encoded methods from the "4bytes.json" file
    methods = json.loads(read_file("4bytes.json"))

    # Parse the first 10 characters of the input data to identify the method being called
    # method_id_ : 0xa9059cbb
    method_id_ = input_data[:10] if input_data else ''

    # Look up the method in the list of known methods, using the parsed method ID
    method = methods.get(method_id_, method_id_)
    # method : transfer(address,uint256)

    # Construct a string representation of the method call, including the parsed arguments
    method_str = f"{method}(0x{input_data[10:]})"
    # method_str: transfer(address,uint256)(0x000000000000000000000000c663b28080e514662b469600bb3e69597fa1197400000000000000000000000000000000000000000000000000000000071596d2)

    print(method_str)
    # If the method ID is recognized, split the input data to handle remaining data
    if method.endswith(')'):
        # Extract the remaining string from the input data
        input_ = (input_data or '')[10:]
        # input_: 000000000000000000000000c663b28080e514662b469600bb3e69597fa1197400000000000000000000000000000000000000000000000000000000071596d2
        method_name = method.split('(')[0]
        # method_name: 'transfer'

        # get list params in method
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
                elif letter == ',':
                    iter_.append("")
                elif letter == ')':
                    continue
                else:
                    if not iter_ or not isinstance(iter_[-1], str):
                        iter_.append("")
                    iter_[-1] += letter
        # in_types: ['address', 'uint256']

        # decode to get value for each param
        if input_:
            in_decoded = decode_abi(in_types, bytes.fromhex(input_))
            # in_decoded: ('0xc663b28080e514662b469600bb3e69597fa11974', 118855378)
            # Construct a string representation of the method call with the given arguments,
            # by iterating over each parameter and its corresponding value and combining them
            # into a comma-separated list enclosed in parentheses.
            method_str = f'{method_name}({", ".join(print_arg(type_, value) for type_, value in zip(in_types, in_decoded))})'
        # method_str: transfer((address)(0xc663b28080e514662b469600bb3e69597fa11974), (uint256)(0x118855378))

    # combine output_data
    if output_data:
        short_result = re.sub(r'0x0+', '0x', output_data)
        method_str += ':' + ('0x0' if short_result == '0x' else short_result)

    # method_str: transfer((address)(0xc663b28080e514662b469600bb3e69597fa11974), (uint256)(118855378)):0x1
    return method_str
