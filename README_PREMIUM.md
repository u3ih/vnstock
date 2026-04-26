# Hướng dẫn sử dụng Vnstock Premium (Bypass & Sponsor Mode)

Phiên bản này đã được tối ưu hóa để loại bỏ quảng cáo, tự động vượt giới hạn (Rate Limit) và kích hoạt chế độ Sponsor.

## Cách cài đặt tự động cho Project khác

Bạn không cần copy thư mục thủ công. Hãy sử dụng một trong hai cách sau để tích hợp vào project mới:

### Cách 1: Thêm vào `requirements.txt` (Khuyên dùng)
Thêm dòng sau vào file `requirements.txt` của project bạn:

```text
git+https://github.com/u3ih/vnstock.git#egg=vnstock
```

Sau đó chạy lệnh: `pip install -r requirements.txt`

### Cách 2: Cài đặt trực tiếp qua Terminal
Chạy lệnh sau để cài đặt bản Premium từ GitHub:

```bash
pip install git+https://github.com/u3ih/vnstock.git#egg=vnstock
```

## Cách sử dụng trong Code
Sau khi cài đặt, bạn chỉ cần import như bình thường. Hệ thống sẽ tự động kích hoạt cơ chế **Auto-Bypass Rate Limit** và **Sponsor Mode**.

```python
from vnstock import Quote, Trading, Finance

# Khởi tạo và sử dụng (Tự động bypass nếu bị chặn IP)
q = Quote(symbol='VCI', source='vci')
df = q.history(start='2024-01-01', end='2024-12-31')
print(df)
```

## Các tính năng Premium nổi bật:
- **Auto Rate-Limit Bypass**: Tự động phát hiện lỗi 429 và xoay vòng Proxy để tiếp tục lấy dữ liệu.
- **Sponsor Mode Unlocked**: Loại bỏ hoàn toàn các thông báo yêu cầu nâng cấp hoặc quảng cáo.
- **High Availability**: Giảm thiểu tối đa tình trạng gián đoạn do bị phía Server chặn IP.

---
*Repo: [https://github.com/u3ih/vnstock](https://github.com/u3ih/vnstock)*
