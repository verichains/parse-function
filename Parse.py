import json
from eth_abi import decode_single
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

    input = "0x0eaead67000000000000000000000000000000000000000000000000000000000000006000000000000000000000000078e883ab727770cce222b0799f77a157caeaabf50000000000000000000000000000000000000000000000000000000000000001b59fce73e3b56330b84b91eb24130e723c04a2fa0000000000000185e7f7d60800000000000000000000000000000000000000000000000000000000000000c000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000120000000000000000000000000000000000000000000000000000000000000018000000000000000000000000000000000000000000000000000000000000001e0000000000000000000000000000000000000000000000000000000000000002e516d50766874666635515a6f464337457a525842614577414e35324a446a614e71427350536e3342316d6e6969500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000b59fce73e3b56330b84b91eb24130e723c04a2fa00000000000000000000000000000000000000000000000000000000000027100000000000000000000000000000000000000000000000000000000000000001000000000000000000000000b59fce73e3b56330b84b91eb24130e723c04a2fa00000000000000000000000000000000000000000000000000000000000003e800000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000004186c83c1e5597bfbaca589bcc535b087c10bb68722bbe5e500e0f9a14d2f4536a37995e07d9acd1efbbaebf1d8676afd8dedbf91b318d3c69658746c74d4c80881b00000000000000000000000000000000000000000000000000000000000000"
    output = "0x0"
    print("input: ", input)
    print("output: ", output)
    decoded_function = decode_function(input, output)
    print("result: ", decoded_function.get("data"))
    print("\n")


def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def parse_arg(val_, type_, params_):
    if isinstance(val_, tuple):
        params_data = []
        typeChild = [type(elem) for elem in val_]
        for typeChildEl, valChild_ in zip(typeChild, val_):
            parse_arg(valChild_, typeChildEl, params_data)
        # print('tuple',params_data)
        params_.append(params_data)
    if type(val_) == bytes:
        # print(val_)
        params_.append(val_.hex())

    if type(val_) == str or type(val_) == int:
        params_.append(val_)


# Example: input_data: 0xa9059cbb000000000000000000000000c663b28080e514662b469600bb3e69597fa1197400000000000000000000000
# 000000000000000000000000000000000071596d2
# Example: output_data: 0x0000000000000000000000000000000000000000000000000000000000000001
def decode_function(input_data, output_data):
    """
    Decode function from input and output transaction data
    :param input_data
    :param output_data
    :return: decoded function
    """

    global params, short_result
    try:
        # Load the list of encoded methods from the "4bytes.json" file
        methods = json.loads(read_file("4bytes.json"))

        # Parse the first 10 characters of the input data to identify the method being called
        # method_id_ : 0xa9059cbb
        method_id_ = input_data[:10] if input_data else ''

        # Look up the method in the list of known methods, using the parsed method ID
        method = methods.get(method_id_, method_id_)
        # method : transfer(address,uint256)

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

            # generate parse type for decode input params
            parse_types = str(in_types).replace("[", "(").replace("]", ")").replace("'", "").replace(" ", "").replace(
                "()", "[]").replace(",[]", "[]").replace(",,", ",")

            # decode to get value for each param
            if input_:
                in_decoded = decode_single(parse_types, bytes.fromhex(input_))
                params = []
                types = [type(elem) for elem in in_decoded]
                for val_, type_ in zip(in_decoded, types):
                    parse_arg(val_, type_, params)
                # params: ['0xc663b28080e514662b469600bb3e69597fa11974', 118855378]

        # combine output_data
        if output_data:
            short_result = re.sub(r'0x0+', '0x', output_data)

    except:
        data = {
            "success": False,
            "msg": "Something wrong with input data"
        }
    else:
        data = {
            'success': True,
            "data": {
                "function": method,
                "params": params,
                "output": short_result
            }
        }

    # data:
    # 	{
    # 	    "success": true,
    # 	    "data":
    # 	    {
    # 	        "function": "transfer(address,uint256)",
    # 	        "params":
    # 	        [
    # 	            "0xc663b28080e514662b469600bb3e69597fa11974",
    # 	            118855378
    # 	        ],
    # 	        "output": "0x1"
    # 	    }
    # 	}
    return data


if __name__ == '__main__':
    main()
