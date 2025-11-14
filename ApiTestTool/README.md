# HƯỚNG DẪN SỬ DỤNG

## HƯỚNG DẪN TEST CURL
```` 
python api_tool.py --mode single --curl "curl --location \"{url}\"" --> api không tham số
````

```` 
python api_tool.py --mode single --curl "curl --location \"{url}\" --header \"Content-Type: application/json\" --data \"{\\\"task\\\": \\\"task 4\\\", \\\"done\\\": true}\"" --> api có tham số
````
## Đưa prompt cho GPT
```` 
-r -> số lượng request
-c -> số lượng luồng
````
````
Dán CURL của bạn xuống phần "curl cung cấp"
````
```` 
dưới đây là mẫu python bắn api stress test, hãy dùng curl tôi cung cấp để thêm vào mẫu python api, lưu ý chỉ cần cung cấp mẫu mới cho tôi là đc, không cần dài dòng thêm


mẫu :
python api_tool.py --mode single --curl "curl --location \"{url}\" --header \"Content-Type: application/json\" --data \"{\\\"task\\\": \\\"task 4\\\", \\\"done\\\": true}\""  -r 100 -c 1

curl cung cấp:
curl --location 'http://localhost:8058/merchant/get-all-mcc' \
--header 'Content-Type: application/json' \
--data '{
    "id":"1212-12121-12121-12121",
    "time":"1111111",
    "channel":"123123",
    "data": {}
}'
````