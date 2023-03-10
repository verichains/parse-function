import json


def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def decode_function(input_data, output_data):
    methods = json.loads(read_file("4bytes.json"))

    method_id_ = input_data[:10] if input_data else ''
    method = methods.get(method_id_, method_id_)
    method_str = f"{method}(0x{input_data[10:]})"

    if output_data:
        short_result = output_data.replace('0x0+', '0x')
        method_str += f":{'0x0' if short_result == '0x' else short_result}"

    return method_str
