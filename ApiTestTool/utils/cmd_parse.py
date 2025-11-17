import json
import re


def escape_json_for_curl(raw_json: str) -> str:
    obj = json.loads(raw_json)
    compact = json.dumps(obj, separators=(',', ':'))
    escaped = compact.replace('"', r'\\\"')
    return escaped

def parse_curl_full(raw: str):
    curl = raw.replace("\\\n", " ")
    curl = curl.replace("\\", "")
    curl = curl.replace("\n", " ")
    curl = re.sub(r"\s+", " ", curl).strip()

    url = ""
    m = re.search(r"curl.*?'([^']+)'", curl)
    if m:
        url = m.group(1)

    headers = dict(re.findall(r"--header '([^:]+):\s*([^']+)'", curl))

    data = ""
    m2 = re.search(r"--data '(.+?)'", curl)
    if m2:
        data = m2.group(1).strip()

    return url, headers, data

def generate_context(raw: str):
    print("=== TOOL GENERATE PYTHON COMMAND ===")

    mode = input("Mode (single/stress) [default: stress]: ").strip()
    if not mode:
        mode = "stress"

    method = input("Method (POST/GET) [default: POST]: ").upper().strip()
    if not method:
        method = "POST"

    r = input("Requests (-r) [default:100]: ").strip()
    if not r:
        r = "100"

    c = input("Concurrency (-c) [default:1]: ").strip()
    if not c:
        c = "1"

    url, headers, data_json = parse_curl_full(raw)

    if not url.startswith("http"):
        raise ValueError("Không lấy được URL từ curl!")

    context = {
        "url": url,
        "method": method,
        "headers": headers,
        "data": data_json,
        "mode": mode,
        "requests": int(r),
        "concurrency": int(c)
    }
    return context
