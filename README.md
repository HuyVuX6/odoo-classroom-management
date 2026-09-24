# Hệ Thống Quản Lý Lớp Học Odoo
## Đào Tạo Lái Máy Bay Mô Phỏng Tích Hợp Phân Tích AI

**Trạng thái:** Tuần 1 - Nền tảng (Đang thực hiện)
**Hạn chót:** 27/09/2026
**Quản lý dự án:** HuyVu
**Mục tiêu:** Ứng tuyển vị trí Business Analyst tại Google

---

## 🎯 Tổng quan & Bài toán (Project Overview)

Dự án này giải quyết bài toán số hóa và tối ưu hóa quy trình quản lý hệ thống đào tạo phi công thông qua buồng lái máy bay mô phỏng (Flight Simulator). Trong thực tế, quá trình huấn luyện thường sinh ra lượng lớn dữ liệu thô phân tán, thiếu sự liên kết để đánh giá năng lực tổng thể. 

Lý do lựa chọn phát triển hệ thống này là nhằm kết hợp sức mạnh của nền tảng quản trị doanh nghiệp (ERP - Odoo) với phân tích dữ liệu AI để tự động hóa việc theo dõi học viên và đo lường hiệu suất giảng viên. Dự án được thiết kế để minh chứng tư duy hệ thống và năng lực giải quyết trọn vẹn một bài toán nghiệp vụ phức tạp từ đầu đến cuối:
* **Xây dựng luồng dữ liệu (Data Pipeline):** Tự động chuyển hóa dữ liệu thô (CSV) thành chuẩn định dạng hệ thống (JSON) để phân tích chuyên sâu.
* **Quản trị rủi ro dữ liệu:** Xây dựng cơ chế phát hiện và ngăn chặn dữ liệu trùng lặp khi nạp vào hệ thống.
* **Hỗ trợ ra quyết định:** Sử dụng mô hình Odoo và phân tích AI để xây dựng các biểu đồ (Dashboards) báo cáo năng suất thực tế của thiết bị, giảng viên và học viên.

---

## 📊 Trạng thái hiện tại: Tuần 1

* ✅ **Đã hoàn thành:** Khởi tạo Git repository, phát triển các kịch bản xử lý dữ liệu (Python scripts), thiết lập luồng chuyển đổi CSV sang JSON, hoàn thiện phân tích dữ liệu bằng `groupby`, và tạo dữ liệu mẫu (10 phiên bay, 5 học viên).

---

## 🚀 Hướng dẫn Cài đặt Nhanh

**Yêu cầu hệ thống:** Python 3.8+ và Git.

1. **Sao chép mã nguồn dự án:**
   ```bash
   git clone [https://github.com/HuyVux6/odoo-classroom-management.git](https://github.com/HuyVux6/odoo-classroom-management.git)
   cd odoo-classroom-management
Cài đặt thư viện phụ thuộc (pandas, openpyxl):

Bash
pip install -r requirements.txt
Kiểm tra môi trường:

Bash
python scripts/read_csv.py
📁 Cấu trúc Dự án Cốt lõi
data/: Thư mục lưu trữ dữ liệu đầu vào (tệp mẫu sample_flights.csv) và dữ liệu đầu ra định dạng hệ thống (.json).

scripts/: Chứa 3 kịch bản mã nguồn Python chịu trách nhiệm xử lý luồng dữ liệu.

output/: Chứa tệp analysis_results.json lưu trữ toàn bộ thông tin thống kê sau khi phân tích.

🐍 Kịch bản xử lý dữ liệu (Python Scripts)
Dự án tự động hóa việc xử lý thông qua 3 tệp kịch bản chính, sử dụng thư viện pandas:

read_csv.py: Tải dữ liệu, phân tích tổng quan các cột, kiểu dữ liệu, các giá trị duy nhất (học viên, giảng viên) và cung cấp thống kê cơ bản.

export_json.py: Chuyển đổi dữ liệu bảng (CSV) sang cấu trúc JSON thu gọn và JSON định dạng đẹp (pretty-printed), đồng thời đính kèm siêu dữ liệu (metadata) quản lý file.

analyze_data.py: Thực hiện các truy vấn nhóm (groupby) phức tạp nhằm bóc tách dữ liệu: hiệu suất theo từng cá nhân học viên, tỷ lệ đỗ, cường độ làm việc của giảng viên và tần suất khai thác máy bay mô phỏng.

🎓 Mô hình Dữ liệu (Data Model)
Hệ thống được vận hành dựa trên một mô hình dữ liệu quy mô với 12 thực thể cốt lõi (Bao gồm: Học viên, Phiên bay, Giảng viên, Máy mô phỏng, Đánh giá kỹ năng...).

Tối ưu hóa kiến trúc: Hệ thống đã được chuẩn hóa để giảm 41% số lượng trường dữ liệu dư thừa (từ 195 xuống còn 115 trường).

💡 Đề xuất Giải pháp Nghiệp vụ (Key BA Proposals)
External_Session_ID: Sử dụng mã định danh duy nhất từ phần mềm bay bên ngoài để đối chiếu, chặn triệt để tình trạng nhập trùng lặp phiên bay vào ERP.

File_Hash Verification: Quét mã băm (MD5/SHA256) của tệp dữ liệu để hệ thống nhận diện và từ chối các tệp đã từng được nạp trước đó.

Tách biệt cột điểm số AI: Lưu trữ độc lập từng loại kỹ năng (điều hướng, an toàn, giao tiếp) thành các trường dữ liệu riêng biệt để tăng tốc độ truy xuất khi vẽ biểu đồ.

📚 Lộ trình Phát triển & Công nghệ
Lộ trình 8 tuần: Dự án bắt đầu từ việc chuẩn hóa dữ liệu (Tuần 1), xây dựng bộ xác thực logic (Tuần 2), thiết kế các Form/Model trên Odoo (Tuần 3-8), tích hợp AI dự báo và hoàn thiện Dashboards.

Công nghệ sử dụng: Ngôn ngữ Python (Pandas, JSON), hệ quản trị Odoo 15+, cơ sở dữ liệu PostgreSQL, mã nguồn mở Git/GitHub.

📈 Giá trị Thể hiện (Portfolio Value)
Dự án cung cấp cái nhìn thực tế về các kỹ năng của một Business Analyst:

Năng lực phân tích và thiết kế mô hình dữ liệu tối ưu.

Khả năng viết mã (Python) để tự động hóa quy trình nghiệp vụ.

Kỹ năng cấu trúc hệ thống có tính mở rộng (Scalable architecture) và chú trọng vào chất lượng dữ liệu.

Quy trình làm việc chuyên nghiệp, hệ thống tài liệu rõ ràng.

📞 Thông tin Liên hệ
Quản lý dự án: HuyVu

Email: shadow20053301@gmail.com

GitHub: @HuyVux6