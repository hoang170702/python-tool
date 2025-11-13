import shlex


def parse_curl_command(curl_cmd: str):
    """
    Parse curl command thành dict config.
    Hỗ trợ: -X, --request, -H, --header, -d, --data, -L/--location, URL
    """
    if not curl_cmd.strip().startswith('curl '):
        raise ValueError("Lệnh phải bắt đầu bằng 'curl '")

    cmd = curl_cmd[4:].strip()
    try:
        tokens = shlex.split(cmd)
    except ValueError as e:
        raise ValueError(f"Lỗi định dạng dấu nháy: {e}")

    config = {
        'method': 'GET',
        'headers': {},
        'data': '',
        'cookies': {},
        'url': ''
    }

    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token in ('-X', '--request'):
            if i + 1 >= len(tokens):
                raise ValueError("Thiếu method sau -X")
            config['method'] = tokens[i + 1].upper()
            i += 2
        elif token in ('-H', '--header'):
            if i + 1 >= len(tokens):
                raise ValueError("Thiếu header sau -H")
            header = tokens[i + 1]
            if ':' in header:
                key, val = header.split(':', 1)
                config['headers'][key.strip()] = val.strip()
            i += 2
        elif token in ('-d', '--data', '--data-raw'):
            if i + 1 >= len(tokens):
                raise ValueError("Thiếu data sau -d")
            config['data'] = tokens[i + 1]
            if config['method'] == 'GET':
                config['method'] = 'POST'
            i += 2
        elif token in ('-L', '--location'):
            i += 1
        elif token in ('-k', '--insecure'):
            i += 1
        elif token.startswith('-'):
            i += 1
        elif token.startswith('http://') or token.startswith('https://'):
            config['url'] = token
            i += 1
        else:
            i += 1

    if not config['url']:
        raise ValueError("Không tìm thấy URL hợp lệ trong lệnh curl")
    return config