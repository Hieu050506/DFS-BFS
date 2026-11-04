

# Duyệt BFS và DFS trên đồ thị do người dùng nhập danh sách kề.
# ví dụ
# 1-2-5
# | |/
# 3-4-6
from collections import deque


def bfs(graph, start):
    visited = set()  # Tập hợp các đỉnh đã được thăm
    queue = deque()  # Hàng đợi để lưu trữ các đỉnh cần thăm

    # Thêm đỉnh bắt đầu vào hàng đợi và đánh dấu là đã thăm
    queue.append(start)
    visited.add(start)

    while queue:
        # Lấy đỉnh đầu tiên trong hàng đợi
        vertex = queue.popleft()
        print(vertex, end=" ")  # In ra đỉnh hiện tại

        # Duyệt qua các đỉnh kề của đỉnh hiện tại
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)  # Thêm đỉnh kề vào hàng đợi
                visited.add(neighbor)  # Đánh dấu là đã thăm

def dfs(graph, start):
    visited = set()
    stack = [start]  # Ngăn xếp: đỉnh vào sau được lấy ra trước.

    while stack:
        vertex = stack.pop()
        if vertex in visited:
            continue

        visited.add(vertex)
        print(vertex, end=" ")

        # Thêm theo thứ tự ngược để duyệt đỉnh kề nhập trước trước tiên.
        for neighbor in reversed(graph[vertex]):
            if neighbor not in visited:
                stack.append(neighbor)


# Ví dụ sử dụng
if __name__ == "__main__":
    # Nhập số lượng đỉnh
    while True:
        try:
            num_vertices = int(input("Nhập số lượng đỉnh: "))
            if num_vertices > 0:
                break
        except ValueError:
            pass
        print("Số lượng đỉnh phải là số nguyên dương.")
    graph = {}

    # Nhập các cạnh của đồ thị
    for i in range(num_vertices):
        while True:
            vertex = input(f"Nhập tên đỉnh {i + 1}: ").strip()
            if vertex and vertex not in graph:
                break
            print("Tên đỉnh phải khác rỗng và không trùng đỉnh đã nhập.")
        edges = input(f"Nhập các đỉnh kề của {vertex} (cách nhau bằng dấu cách): ").split()
        graph[vertex] = edges

    # Một đỉnh xuất hiện trong danh sách kề cũng cần được khai báo.
    # Hỏi bổ sung thay vì bỏ qua đỉnh đó hoặc để BFS báo KeyError.
    while True:
        missing = sorted({neighbor for edges in graph.values()
                          for neighbor in edges if neighbor not in graph})
        if not missing:
            break
        for vertex in missing:
            print(f"Đỉnh '{vertex}' có trong danh sách kề nhưng chưa được khai báo.")
            graph[vertex] = input(
                f"Nhập các đỉnh kề của {vertex} (cách nhau bằng dấu cách, Enter nếu không có): "
            ).split()

    # Nhập đồ thị một lần, sau đó chọn thuật toán cho từng lượt duyệt.
    while True:
        print("\n1. Duyệt BFS")
        print("2. Duyệt DFS")
        print("0. Thoát")
        choice = input("Chọn thuật toán (1/2/0): ").strip()

        if choice == "0":
            print("Đã thoát chương trình.")
            break
        if choice not in ("1", "2"):
            print("Vui lòng chọn 1, 2 hoặc 0.")
            continue

        while True:
            start_vertex = input("Nhập đỉnh bắt đầu: ").strip()
            if start_vertex in graph:
                break
            print("Đỉnh bắt đầu chưa được khai báo. Các đỉnh hiện có:", " ".join(graph))

        if choice == "1":
            print("Kết quả BFS:")
            bfs(graph, start_vertex)
        else:
            print("Kết quả DFS:")
            dfs(graph, start_vertex)
        print()
