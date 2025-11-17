import argparse
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

from utils.cmd_parse import  generate_context
from utils.json_parse import try_json_parse


def send_request(context, timeout=10):
    start_time = time.time()
    # dùng khi request có filed unique
    # inject_unique_id(context)
    try:
        response = requests.request(
            method=context['method'],
            url=context['url'],
            headers=context.get('headers', {}),
            data=context.get('data', ''),
            cookies=context.get('cookies', {}),
            timeout=timeout,
            verify=False
        )
        duration = time.time() - start_time
        return {
            'success': True,
            'json': try_json_parse(response.text),
            'duration': duration
        }
    except Exception as e:
        duration = time.time() - start_time
        return {
            'success': False,
            'error': str(e),
            'duration': duration
        }


def run_stress_test(context, total_req, concurrency):
    print(f"\033[94mBắt đầu stress test: {total_req} requests với {concurrency} luồng đồng thời\033[0m")
    print(f"URL: {context['url']} | Phương thức: {context['method']}\n")

    results = []
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = [executor.submit(send_request, context, timeout=10) for _ in range(total_req)]

        for i, future in enumerate(as_completed(futures)) :
            result = future.result()
            results.append(result)
            progress = (i+1) / total_req * 100
            bar = f"[{'#' * int(progress / 5)}{'.' * (20 - int(progress / 5))}]"
            sys.stdout.write(f"\rĐang xử lý: {progress:.1f}% {bar}")
            sys.stdout.flush()

    total_time = time.time() - start_time
    successful = [r for r in results if r['success']]
    failed = [r for r in results if not r['success']]


    print("\n\n\033[92m===== KẾT QUẢ STRESS TEST =====\033[0m")
    print(f"Tổng thời gian: {total_time:.2f}s")
    print(f"Tổng requests: {total_req} | Thành công: \033[92m{len(successful)}\033[0m | Thất bại: \033[91m{len(failed)}\033[0m")
    print(f"Tỷ lệ thành công: {len(successful) / total_req * 100:.1f}%")
    print(f"Requests/giây: {total_req / total_time:.2f}")

    if failed:
        print("\n\033[91mChi tiết lỗi:\033[0m")
        for err in failed[:5]:
            print(f"- {err['error']}")



def print_result(result):
    if not result['success']:
        print(f"\033[91m❌ Lỗi kết nối: {result['error']}\033[0m")
        return

    if 'respCode' in result['json']:
        code = result['json']['respCode'].get('code', '???')
        message = result['json']['respCode'].get('message', 'No message')

        if code == "00":
            print(f"\033[92mResponse Code: [{code}] {message}\033[0m")
        else:
            print(f"\033[91m⚠️  Error Code: [{code}] {message}\033[0m")
    print(f"\033[94mDuration: {result['duration']:.2f}s\033[0m")
    print("\n\033[93mResponse:\033[0m")
    if 'data' in result['json']:
        print(json.dumps(result['json']['data'], indent=2, ensure_ascii=False))
    else:
        print(result['content'])



def main():
    context = generate_context()

    if context['mode'] == 'single':
        result = send_request(context)
        print_result(result)
    else:
        run_stress_test(context, context['requests'], context['concurrency'])


if __name__ == "__main__":
    main()






