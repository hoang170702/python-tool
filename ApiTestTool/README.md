# HƯỚNG DẪN SỬ DỤNG

## HƯỚNG DẪN TEST CURL
```` 
Dán curl vào file ApiTestTool\file\raw.txt
````
```` 
chạy cmd: python api_tool.py
````
```` 
Chọn option: 

=== TOOL GENERATE PYTHON COMMAND ===
Mode (single/stress) [default: stress]: (single - chạy 1 request, stress - chạy nhiều request đồng thời)
Method (POST/GET) [default: POST]: (chọn phương thức post, get)
Requests (-r) [default:100]: 10 (tổng số lượng request muốn bắn)
Concurrency (-c) [default:1]: 1 (tổng số lượng luồng, thường sẽ stress test trên một luồng)
````
```` 
Nếu request có một field đặc biệt, cần khác nhau mỗi lần bắn request, có thể custom ở file gen_uuid.py
````
