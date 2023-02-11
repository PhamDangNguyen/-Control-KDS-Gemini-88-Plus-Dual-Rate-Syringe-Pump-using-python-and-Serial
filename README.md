# RUN CODE ĐIỀU KHIỂN VI BƠM KDS GEMINI 88 TRONG MÔI TRƯỜNG PYTHON
## Overview
- Vi bơm Gemini 88 được dùng chủ yếu trong các phòng thí nghiệm được phát triểm bởi đội ngũ kỹ thuật viên của KD Scientific, vì sản phẩm này không được FDA chấp thuận cho sử dụng lâm sàn ở người nên nó không phổ biến, tài liệu để sử dụng phần mềm điều khển vi bơm ở trên mạng gần như là không có. Vậy nên ở dự án này sẽ hướng dẫn dùng code Serial COM kết hợp môi trường python để truyền lệnh giúp kiểm soát, điều khiển vi bơm KDS Gemini 88.
## PUMP
- Máy bơm ống tiêm tốc độ kép này có thể truyền đồng thời ở các tốc độ khác nhau hoặc truyền bằng một ống tiêm và rút ra bằng ống tiêm kia, độ chính xác cao có thể kết hợp với nhiều kiểu Syringe
- Chi tiết sản phẩm: [LINK](https://www.kdscientific.com/gemini-88-plus-dual-rate-syringe-pump-1804.html)
### Hình ảnh minh họa Pump Gemini 88
![example](File_anh\pump.jpg)
## Method Used and Technologies
- python
- Serial COM
- Command Pump Code
## Main python libraries
- Python 
- Serial
- Driver of pump
## Code
### Create virtual environment:
- Sử dụng lệnh: 'python -m venv <tên fiel môi trường>'
### Requirement:
- pyserial==3.5
- python==3.9.10
## Run code:
- B1: Run file 'realSerial.py'
- B2: Run file 'InfuseCode.py'

###  **Note**: 
- Ta hoàn toàn có thể truyền các lệnh khác nhau như trong bản PDF trong file 'File_tutorial' đã hướng dẫn ở phần 'Pump Chain Commands', muốn chạy lệnh nào ta chỉ việc gán câu lệnh đó cho biến input trong file 'InfuseCode.py' và màn hình hiển thị của máy bơm không nhất thiết phải thay đổi khi ta tác động tới máy bơm bằng phần mềm.
## Result: 
- Máy vi bơm chạy đúng theo lệnh