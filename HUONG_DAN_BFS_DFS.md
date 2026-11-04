# Hướng dẫn BFS và DFS từng bước

Tài liệu giải thích chương trình trong [BFS.py](BFS.py): ý nghĩa các biến, cách hàng đợi và ngăn xếp hoạt động, quá trình duyệt đồ thị và cách nhập dữ liệu.

## 1. Đồ thị dùng trong ví dụ

```text
1-2-5
| |/
3-4-6
```

Đây là đồ thị vô hướng. Nét chéo `/` biểu diễn cạnh nối đỉnh `4` với đỉnh `5`.

Trong Python, lưu đồ thị bằng một dictionary chứa các danh sách kề:

```python
graph = {
    "1": ["2", "3"],
    "2": ["1", "4", "5"],
    "3": ["1", "4"],
    "4": ["2", "3", "5", "6"],
    "5": ["2", "4"],
    "6": ["4"]
}

start = "1"
```

- Khóa `"1"` là tên một đỉnh.
- Giá trị `["2", "3"]` là danh sách các đỉnh kề với đỉnh `1`.
- `graph["1"]` trả về `["2", "3"]`.
- `start = "1"` nghĩa là bắt đầu duyệt từ đỉnh `1`.

Tên đỉnh trong chương trình là chuỗi vì được đọc bằng `input()`. Vì vậy, `graph["1"]` và `graph[1]` là hai cách truy cập khác nhau; ví dụ trên chỉ có khóa `"1"`.

## 2. Ý nghĩa các biến và câu lệnh

| Thành phần | Ý nghĩa |
|---|---|
| `graph` | Toàn bộ đồ thị, lưu dưới dạng danh sách kề |
| `start` | Đỉnh bắt đầu duyệt |
| `vertex` | Đỉnh vừa lấy ra để xử lý |
| `neighbor` | Một đỉnh kề của `vertex` |
| `visited` | Tập hợp ghi nhớ các đỉnh đã được đánh dấu |
| `queue` | Hàng đợi dùng trong BFS |
| `stack` | Ngăn xếp dùng trong DFS |
| `append(x)` | Thêm `x` vào cuối hàng đợi hoặc danh sách |
| `popleft()` | Lấy và xóa phần tử đầu hàng đợi |
| `pop()` | Lấy và xóa phần tử cuối danh sách |
| `visited.add(x)` | Thêm `x` vào tập hợp đã đánh dấu |
| `x not in visited` | Kiểm tra `x` chưa có trong tập hợp |

### Hiểu dòng `for neighbor in graph[vertex]`

Giả sử `vertex = "1"`. Khi đó, `graph[vertex]` chính là `["2", "3"]`.

Vòng lặp lấy lần lượt từng phần tử trong danh sách này:

```text
Lượt 1: neighbor = "2" → chạy phần thân vòng lặp với đỉnh 2.
Lượt 2: neighbor = "3" → chạy phần thân vòng lặp với đỉnh 3.
Hết danh sách → kết thúc vòng for.
```

Từ khóa `in` có hai vai trò trong đoạn chương trình:

- Trong `for neighbor in graph[vertex]`: lấy lần lượt từng đỉnh kề.
- Trong `neighbor not in visited`: kiểm tra đỉnh kề chưa có trong tập hợp đã đánh dấu.

## 3. BFS — duyệt theo chiều rộng

BFS xét các đỉnh theo từng lớp tính từ đỉnh bắt đầu: lớp gần trước, lớp xa sau. BFS sử dụng hàng đợi theo nguyên tắc **vào trước, ra trước**.

Ví dụ hàng đợi là `[2, 3, 4]`: `popleft()` lấy `2` ra trước, còn lại `[3, 4]`.

### Mã chương trình

```python
from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque()

    queue.append(start)
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
```

### Các bước thực hiện

1. `visited = set()`: tạo tập hợp rỗng để ghi nhớ các đỉnh đã phát hiện.
2. `queue = deque()`: tạo hàng đợi rỗng.
3. `queue.append(start)`: đưa đỉnh bắt đầu vào hàng đợi.
4. `visited.add(start)`: đánh dấu đỉnh bắt đầu.
5. `while queue`: tiếp tục lặp khi hàng đợi còn phần tử.
6. `vertex = queue.popleft()`: lấy đỉnh ở đầu hàng đợi ra xử lý.
7. `print(vertex, end=" ")`: in tên đỉnh, thêm dấu cách và chưa xuống dòng.
8. `for neighbor in graph[vertex]`: xét lần lượt các đỉnh kề.
9. Nếu `neighbor` chưa được đánh dấu, đưa nó vào cuối hàng đợi và đánh dấu ngay.
10. Quay lại bước 5. Khi hàng đợi rỗng, hàm kết thúc.

### Vì sao cần đánh dấu ngay khi thêm vào hàng đợi?

Ví dụ đỉnh `4` kề cả đỉnh `2` và `3`. Khi xử lý đỉnh `2`, chương trình đưa `4` vào hàng đợi và thêm `4` vào `visited`. Sau đó, khi xử lý đỉnh `3`, chương trình thấy `4` đã có trong `visited` nên không thêm lần nữa.

Trong hàm BFS này, có mặt trong `visited` nghĩa là **đã được phát hiện và đưa vào hàng đợi**. Đỉnh đó có thể vẫn đang chờ, chưa được lấy ra in.

### Chạy BFS từ đỉnh 1

Để bảng dễ đọc, các tên đỉnh được viết không có dấu nháy. Trong chương trình, chúng vẫn là chuỗi. Thứ tự các phần tử trong `visited` không có ý nghĩa vì đây là tập hợp.

Ban đầu: `queue = [1]`, `visited = {1}`.

| Bước | Đỉnh lấy ra và in | Đỉnh mới thêm | Hàng đợi sau khi xét các đỉnh kề | `visited` sau bước này |
|---|---|---|---|---|
| 1 | `1` | `2, 3` | `[2, 3]` | `{1, 2, 3}` |
| 2 | `2` | `4, 5` | `[3, 4, 5]` | `{1, 2, 3, 4, 5}` |
| 3 | `3` | Không có | `[4, 5]` | `{1, 2, 3, 4, 5}` |
| 4 | `4` | `6` | `[5, 6]` | `{1, 2, 3, 4, 5, 6}` |
| 5 | `5` | Không có | `[6]` | `{1, 2, 3, 4, 5, 6}` |
| 6 | `6` | Không có | `[]` | `{1, 2, 3, 4, 5, 6}` |

Kết quả:

```text
1 2 3 4 5 6
```

Các lớp tính từ đỉnh `1` là: lớp 0 gồm `1`, lớp 1 gồm `2, 3`, lớp 2 gồm `4, 5`, lớp 3 gồm `6`.

## 4. DFS — duyệt theo chiều sâu

DFS đi sâu theo một nhánh trước, sau đó tiếp tục các nhánh còn lại. Hàm trong `BFS.py` dùng ngăn xếp theo nguyên tắc **vào sau, ra trước**.

Ví dụ ngăn xếp là `[2, 3, 4]`: `pop()` lấy `4` ra trước, còn lại `[2, 3]`.

### Mã chương trình

```python
def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex in visited:
            continue

        visited.add(vertex)
        print(vertex, end=" ")

        for neighbor in reversed(graph[vertex]):
            if neighbor not in visited:
                stack.append(neighbor)
```

### Các bước thực hiện

1. `visited = set()`: tạo tập hợp rỗng để ghi nhớ các đỉnh đã xử lý.
2. `stack = [start]`: tạo ngăn xếp chứa đỉnh bắt đầu.
3. `while stack`: tiếp tục lặp khi ngăn xếp còn phần tử.
4. `vertex = stack.pop()`: lấy đỉnh cuối ngăn xếp ra.
5. Nếu đỉnh đã có trong `visited`, `continue` bỏ qua phần còn lại của lượt này và chuyển sang lượt tiếp theo.
6. Nếu chưa được thăm, thêm đỉnh vào `visited` rồi in ra.
7. Duyệt ngược danh sách kề bằng `reversed(graph[vertex])`.
8. Thêm các đỉnh kề chưa thăm vào cuối ngăn xếp.
9. Quay lại bước 3. Khi ngăn xếp rỗng, hàm kết thúc.

### Vì sao có `reversed()`?

Đỉnh `1` có các đỉnh kề theo thứ tự `[2, 3]`. Chương trình thêm `3` trước, rồi thêm `2`, tạo ngăn xếp `[3, 2]`. Vì lấy phần tử cuối bằng `pop()`, đỉnh `2` được xử lý trước.

Như vậy, DFS ưu tiên đỉnh kề được nhập trước. Nếu bỏ `reversed()`, thứ tự ưu tiên sẽ thay đổi.

### Chạy DFS từ đỉnh 1

Trong bảng, phần tử bên phải cùng là đỉnh sẽ được lấy ra tiếp theo. Ban đầu: `stack = [1]`, `visited = {}` (tập rỗng, được tạo bằng `set()` trong Python).

| Bước | Đỉnh lấy ra | Hành động | Ngăn xếp sau bước này | Kết quả đã in |
|---|---|---|---|---|
| 1 | `1` | Đánh dấu, in; thêm `3`, rồi `2` | `[3, 2]` | `1` |
| 2 | `2` | Đánh dấu, in; thêm `5`, rồi `4` | `[3, 5, 4]` | `1 2` |
| 3 | `4` | Đánh dấu, in; thêm `6`, `5`, rồi `3` | `[3, 5, 6, 5, 3]` | `1 2 4` |
| 4 | `3` | Đánh dấu, in; không thêm đỉnh nào | `[3, 5, 6, 5]` | `1 2 4 3` |
| 5 | `5` | Đánh dấu, in; không thêm đỉnh nào | `[3, 5, 6]` | `1 2 4 3 5` |
| 6 | `6` | Đánh dấu, in; không thêm đỉnh nào | `[3, 5]` | `1 2 4 3 5 6` |
| 7 | `5` | Đã thăm, bỏ qua bằng `continue` | `[3]` | `1 2 4 3 5 6` |
| 8 | `3` | Đã thăm, bỏ qua bằng `continue` | `[]` | `1 2 4 3 5 6` |

Kết quả:

```text
1 2 4 3 5 6
```

Hàm DFS này đánh dấu khi lấy đỉnh ra khỏi ngăn xếp. Vì vậy, một đỉnh chưa được xử lý có thể được thêm vào ngăn xếp nhiều lần. Câu lệnh `if vertex in visited: continue` bảo đảm mỗi đỉnh chỉ được in và xét danh sách kề một lần.

Dãy kết quả là thứ tự thăm đỉnh. Hai đỉnh đứng liên tiếp trong dãy không nhất thiết nối trực tiếp với nhau; DFS có thể đã kết thúc một nhánh rồi chuyển sang nhánh khác.

## 5. So sánh BFS và DFS trong chương trình

| Đặc điểm | BFS | DFS |
|---|---|---|
| Cách duyệt | Theo từng lớp | Đi sâu từng nhánh |
| Cấu trúc lưu đỉnh chờ | Hàng đợi `deque` | Ngăn xếp `list` |
| Nguyên tắc lấy đỉnh | Vào trước, ra trước | Vào sau, ra trước |
| Lệnh lấy đỉnh | `queue.popleft()` | `stack.pop()` |
| Thời điểm đánh dấu trong mã này | Khi đưa vào hàng đợi | Khi lấy ra xử lý lần đầu |
| Kết quả ví dụ từ `1` | `1 2 3 4 5 6` | `1 2 4 3 5 6` |

Cả hai chỉ duyệt các đỉnh đi tới được từ `start`. Thứ tự kết quả còn phụ thuộc vào thứ tự các đỉnh trong danh sách kề.

## 6. Nhập đồ thị và chọn BFS hoặc DFS

Chạy chương trình:

```bash
python BFS.py
```

Nhập số lượng đỉnh là `6`, sau đó nhập lần lượt:

| Tên đỉnh | Các đỉnh kề cần nhập |
|---|---|
| `1` | `2 3` |
| `2` | `1 4 5` |
| `3` | `1 4` |
| `4` | `2 3 5 6` |
| `5` | `2 4` |
| `6` | `4` |

Với đồ thị vô hướng, cần nhập đủ hai chiều: nếu danh sách của `1` chứa `2`, danh sách của `2` cũng cần chứa `1`. Chương trình hiện tại sử dụng đúng các danh sách bạn nhập, không tự thêm chiều ngược lại.

Sau khi nhập xong, chương trình hiển thị:

```text
1. Duyệt BFS
2. Duyệt DFS
0. Thoát
```

1. Nhập `1` để chọn BFS hoặc `2` để chọn DFS.
2. Nhập đỉnh bắt đầu, ví dụ `1`.
3. Chương trình in kết quả rồi quay lại menu.
4. Tiếp tục chọn thuật toán và đỉnh bắt đầu cho lượt mới, hoặc nhập `0` để thoát.

Mỗi lần gọi BFS hoặc DFS, hàm tạo một `visited` mới. Vì vậy, có thể duyệt lại cùng đồ thị nhiều lần mà không cần nhập lại dữ liệu.

## 7. Hiểu các lỗi thường gặp

### Chương trình chỉ in đỉnh 1

Nếu đỉnh bắt đầu là `1`, kết quả chỉ có `1` nghĩa là danh sách kề của `1` không chứa đỉnh nào khác để duyệt tiếp. Hãy kiểm tra đã nhập `2 3` cho đỉnh `1` chưa. Hình vẽ trong các dòng chú thích bắt đầu bằng `#` không tự tạo ra dữ liệu đồ thị.

### Lỗi `KeyError: '5'`

Lỗi này xuất hiện khi truy cập `graph["5"]` nhưng dictionary chưa có khóa `"5"`. Ví dụ, bạn đã nhắc tới `5` trong danh sách kề của `2`, nhưng chưa khai báo đỉnh `5`.

Bản `BFS.py` hiện tại kiểm tra các tên đỉnh còn thiếu và hỏi bổ sung danh sách kề trước khi chạy thuật toán. Chương trình cũng loại bỏ khoảng trắng ở hai đầu tên đỉnh, ngăn nhập trùng tên và kiểm tra đỉnh bắt đầu.

### Kết quả khác ví dụ

Kiểm tra đỉnh bắt đầu, các cạnh đã nhập và thứ tự đỉnh kề. Ví dụ, nhập `3 2` cho đỉnh `1` có thể tạo thứ tự duyệt khác với nhập `2 3`, dù các cạnh vẫn giống nhau.
