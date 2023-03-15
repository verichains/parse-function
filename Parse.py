import json
from eth_abi import decode_abi, decode, decode_single
import re


def main():
    input = "0xa9059cbb000000000000000000000000c663b28080e514662b469600bb3e69597fa1197400000000000000000000000000000000000000000000000000000000071596d2"
    output = "0x0000000000000000000000000000000000000000000000000000000000000001"
    print("input: ", input)
    print("output: ", output)
    decoded_function = decode_function(input, output)
    print("result: ", decoded_function.get("data"))
    print("\n")

    input = "0xc7ba24bc00000000000000000000000000000000000000000000000000000000000000600000000000000000000000000000000000000000000000007e73ecbb24d58763000000000000000000000000000000000000000000000000000117824da7be6c0000000000000000000000000000000000000000000000000000000000000005000000000000000000000000d0a4b8946cb52f0661273bfbc6fd0e0c75fc6433000000000000000000000000cad4da66e00fdecabec137a24e12af8edf303a1d0000000000000000000000001f573d6fb3f13d689ff844b4ce37794d79a7ff1c0000000000000000000000001f573d6fb3f13d689ff844b4ce37794d79a7ff1c000000000000000000000000c0829421c1d260bd3cb3e0f06cfe2d52db2ce31500000000000000000000000000000000000000000000000000000000"
    output = "0x0"
    print("input: ", input)
    print("output: ", output)
    decoded_function = decode_function(input, output)
    print("result: ", decoded_function.get("data"))
    print("\n")

    input = "0xa9059cbb00000000000000000000000012863901098aa24fa81f1ab952a449f6c8211afc000000000000000000000000000000000000000000000000a3306518fc65fc5e"
    output = "0x0"
    print("input: ", input)
    print("output: ", output)
    decoded_function = decode_function(input, output)
    print("result: ", decoded_function.get("data"))
    print("\n")

    input = "0x54bc0cf10000000000000000000000000000000000000000000000000000000000000060000000000000000000000000b59fce73e3b56330b84b91eb24130e723c04a2fa00000000000000000000000078e883ab727770cce222b0799f77a157caeaabf5000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000011cdfaa4000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000002e0000000000000000000000000072f45a506df2002e480a9ad40f728f297f024ca0000000000000000000000000000000000000000000000000000000000000040b59fce73e3b56330b84b91eb24130e723c04a2fa0000000000000185e7f7d60800000000000000000000000000000000000000000000000000000000000000c000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000120000000000000000000000000000000000000000000000000000000000000018000000000000000000000000000000000000000000000000000000000000001e0000000000000000000000000000000000000000000000000000000000000002e516d50766874666635515a6f464337457a525842614577414e35324a446a614e71427350536e3342316d6e6969500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000b59fce73e3b56330b84b91eb24130e723c04a2fa00000000000000000000000000000000000000000000000000000000000027100000000000000000000000000000000000000000000000000000000000000001000000000000000000000000b59fce73e3b56330b84b91eb24130e723c04a2fa00000000000000000000000000000000000000000000000000000000000003e800000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000004186c83c1e5597bfbaca589bcc535b087c10bb68722bbe5e500e0f9a14d2f4536a37995e07d9acd1efbbaebf1d8676afd8dedbf91b318d3c69658746c74d4c80881b00000000000000000000000000000000000000000000000000000000000000"
    output = "0x0"
    print("input: ", input)
    print("output: ", output)
    decoded_function = decode_function(input, output)
    print("result: ", decoded_function.get("data"))
    print("\n")

    input = "0x54cf2aeb"
    output = "0x0"
    print("input: ", input)
    print("output: ", output)
    decoded_function = decode_function(input, output)
    print("result: ", decoded_function.get("data"))
    print("\n")

def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def print_arg(type_, value):
    if type(type_) == list:
        return f'({",".join(print_arg(type1_, value1) for type1_, value1 in zip(type_, value))})'
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

    try:
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
                        if len(backs) > 0:
                            iter_ = backs.pop()
                        else:
                            continue
                    else:
                        if not iter_ or not isinstance(iter_[-1], str):
                            iter_.append("")
                        iter_[-1] += letter
            # in_types: ['address', 'uint256']
            parse_types = str(in_types)
            parse_types = parse_types.replace("[", "(").replace("]", ")").replace("'", "").replace(" ", "").replace(
                "()", "[]")

            # parse_in_types = "(((bytes4,bytes),uint256),address,address)"

            # decode to get value for each param
            if input_:
                in_decoded = decode_single(parse_types, bytes.fromhex(input_))
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
    except Exception as ex:
        print(ex)
        data = {
            "success": False,
            "msg": "Something wrong with input data"
        }
    else:
        data = {
            'success': True,
            "data": method_str
        }

    return data


if __name__ == '__main__':
    main()
