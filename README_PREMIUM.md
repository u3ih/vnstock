# Hướng dẫn sử dụng Vnstock Premium

Phiên bản này đã được tối ưu để **xoá thông báo quảng cáo / yêu cầu nâng cấp** và **tối ưu hiệu năng** khi lấy dữ liệu.

---

## Cài đặt

> **Lưu ý quan trọng:** Nếu bạn đã cài `vnstock` trước đó, bắt buộc phải dùng `--force-reinstall` để ghi đè bản cũ. Sau khi cài xong, hãy **restart kernel** (Jupyter/IPython) hoặc **restart Python process** để load lại thư viện mới.

### Cách 1: Cài đặt trực tiếp qua Terminal

```bash
pip install --force-reinstall git+https://github.com/u3ih/vnstock.git#egg=vnstock
```

### Cách 2: Thêm vào `requirements.txt`

Nếu `requirements.txt` đang có khai báo `vnstock` (ví dụ `vnstock==3.x.x` hoặc `vnstock`), hãy **comment hoặc xoá dòng đó trước**, rồi thêm dòng bên dưới:

```text
# vnstock==3.x.x   <-- comment hoặc xoá dòng này nếu có
git+https://github.com/u3ih/vnstock.git#egg=vnstock
```

Sau đó chạy:

```bash
pip install --force-reinstall -r requirements.txt
```

### Sau khi cài đặt

- **Jupyter Notebook / JupyterLab**: Vào menu `Kernel` → `Restart Kernel`
- **IPython / Terminal**: Thoát và mở lại Python
- **Script thông thường**: Chạy lại script từ đầu

---

## Tính năng

### 1. Xoá thông báo quảng cáo & yêu cầu nâng cấp

Bản Premium loại bỏ hoàn toàn các thông báo nhắc nâng cấp lên `vnstock_data` (Sponsor package) xuất hiện khi import hoặc gọi một số hàm nhất định.

### 2. Tối ưu hiệu năng

Hệ thống tự động retry với **exponential backoff** khi gặp lỗi kết nối hoặc quá tải.

Cấu hình retry mặc định (có thể chỉnh trong `vnstock/config.py`):

| Tham số             | Giá trị mặc định | Mô tả                        |
|---------------------|-----------------|------------------------------|
| `RETRIES`           | `3`             | Số lần thử lại tối đa        |
| `BACKOFF_MULTIPLIER`| `1.0`           | Hệ số nhân thời gian chờ     |
| `BACKOFF_MIN`       | `2` giây        | Thời gian chờ tối thiểu      |
| `BACKOFF_MAX`       | `10` giây       | Thời gian chờ tối đa         |

---

## Cách sử dụng

Sau khi cài đặt và restart kernel, import bình thường — hệ thống tự kích hoạt:

```python
from vnstock import Quote, Trading, Finance

q = Quote(symbol='VCI', source='vci')
df = q.history(start='2024-01-01', end='2024-12-31')
print(df)
```

---

*Repo: [https://github.com/u3ih/vnstock](https://github.com/u3ih/vnstock)*
