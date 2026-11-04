# DFS-BFS

Chương trình Python duyệt đồ thị bằng BFS (chiều rộng) và DFS (chiều sâu).

## Chức năng

- Nhập tên đỉnh và danh sách các đỉnh kề.
- Kiểm tra tên đỉnh trùng, đỉnh còn thiếu và đỉnh bắt đầu.
- Nhập đồ thị một lần, chọn BFS hoặc DFS nhiều lần.
- Đổi đỉnh bắt đầu trong mỗi lượt duyệt.

## Chạy chương trình

Cần Python 3. Chương trình chỉ dùng thư viện chuẩn, không cần cài thêm gói.

```bash
python BFS.py
```

Nhập số lượng đỉnh, sau đó tên và các đỉnh kề của từng đỉnh, cách nhau bằng dấu cách. Nhấn Enter nếu một đỉnh không có đỉnh kề.

Với đồ thị vô hướng, nhập cạnh theo cả hai chiều.

## Ví dụ

```text
1-2-5
| |/
3-4-6
```

Nhập số lượng đỉnh là `6` và các danh sách kề:

| Đỉnh | Các đỉnh kề |
|---|---|
| 1 | `2 3` |
| 2 | `1 4 5` |
| 3 | `1 4` |
| 4 | `2 3 5 6` |
| 5 | `2 4` |
| 6 | `4` |

Sau khi nhập xong, chọn thuật toán:

```text
1. Duyệt BFS
2. Duyệt DFS
0. Thoát
```

Chọn đỉnh bắt đầu là `1`, kết quả:

```text
BFS: 1 2 3 4 5 6
DFS: 1 2 4 3 5 6
```

Thứ tự duyệt phụ thuộc vào thứ tự đỉnh kề được nhập.

## Tài liệu

Xem [hướng dẫn BFS và DFS từng bước](HUONG_DAN_BFS_DFS.md) để hiểu các biến, hàng đợi, ngăn xếp và quá trình thực hiện.
