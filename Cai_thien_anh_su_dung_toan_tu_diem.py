# # Cải thiện ảnh sử dụng toán tử điểm
# # Bước 1: Đặt số mức xám của ảnh cân bằng là k
# # Bước 2: Tính số điểm ảnh trung bình của mỗi mức xám ảnh cân bằng. b = (m*n)/k
# # Bước 3: Tính số điểm ảnh có mức xám <= g:
# # Bước 4: Xác định hàm f(g): 

import numpy as np
from collections import Counter

def main():
    # Nhập số mức xám của ảnh
    K = int(input("Nhập số mức xám của ảnh (K): "))

    # Nhập các giá trị của ma trận
    values = list(map(int, input("Nhập tất cả các giá trị của ma trận (các giá trị cách nhau bởi dấu cách): ").split()))
    
    # Xác định số hàng và số cột
    total_elements = len(values)
    rows = int(input("Nhập số hàng của ma trận: "))
    cols = total_elements // rows
    if total_elements % rows != 0:
        print("Số phần tử không khớp với số hàng. Vui lòng nhập lại.")
        return

    # Tạo ma trận
    matrix = np.array(values).reshape((rows, cols))

    # In ma trận và kích thước
    print("\nMa trận vừa nhập:")
    print(matrix)
    print(f"\nĐộ dài của ma trận: {rows}")
    print(f"Độ rộng của ma trận: {cols}")
    b = (rows * cols) / K
    print(f"\nSố điểm trung bình mỗi điểm ảnh: {b}")

    # Chuyển ma trận thành danh sách các phần tử
    flat_list = matrix.flatten()
    
    # Đếm số lần xuất hiện của từng phần tử
    counts = Counter(flat_list)
    
    # Tạo danh sách g chứa các giá trị phần tử từ ma trận
    g = np.array(list(counts.keys()))
    
    # Tạo danh sách h chứa số lần xuất hiện tương ứng của từng giá trị trong g
    h = np.array(list(counts.values()))
    
    # Tạo danh sách các số và số lần xuất hiện của chúng
    result_list = list(zip(g, h))
    
    # Sắp xếp danh sách kết quả theo thứ tự từ bé đến lớn theo giá trị phần tử
    sorted_result_list = sorted(result_list, key=lambda x: x[0])
    
    # Tách danh sách g và h sau khi sắp xếp
    g_sorted, h_sorted = zip(*sorted_result_list)
    
    # Chuyển đổi kết quả thành numpy arrays
    g_sorted = np.array(g_sorted)
    h_sorted = np.array(h_sorted)
    
    # In danh sách g chứa các giá trị phần tử đã sắp xếp
    print("\nDanh sách g chứa các giá trị phần tử từ ma trận (đã sắp xếp):")
    print(g_sorted)
    
    # In danh sách h chứa số lần xuất hiện tương ứng (đã sắp xếp)
    print("\nDanh sách h chứa số lần xuất hiện tương ứng (đã sắp xếp):")
    print(h_sorted)
    
    # Tạo mảng t theo công thức tính toán
    t = np.zeros_like(h_sorted, dtype=int)
    t[0] = h_sorted[0]
    for i in range(1, len(h_sorted)):
        t[i] = t[i - 1] + h_sorted[i]
    
    # In danh sách t chứa các giá trị tính toán
    print("\nDanh sách t chứa các giá trị tính toán:")
    print(t)
    
    # Tạo mảng f theo công thức tính toán
    f = np.round((t / b) - 1).astype(int)
    
    # In danh sách f chứa các giá trị tính toán
    print("\nDanh sách f chứa các giá trị tính toán:")
    print(f)
    
    # Thay thế giá trị của g bằng các giá trị từ f
    g_replaced = np.copy(g_sorted)
    for i in range(len(g_sorted)):
        if i < len(f):
            g_replaced[i] = f[i]

    # Sắp xếp lại danh sách g và h theo các giá trị mới trong g
    result_list_replaced = list(zip(g_replaced, h_sorted))
    sorted_result_list_replaced = sorted(result_list_replaced, key=lambda x: x[0])
    g_sorted_replaced, h_sorted_replaced = zip(*sorted_result_list_replaced)
    
    # Chuyển đổi kết quả thành numpy arrays
    g_sorted_replaced = np.array(g_sorted_replaced)
    h_sorted_replaced = np.array(h_sorted_replaced)

    
    # Tạo bản sao của mảng values
    values_replaced = np.copy(values)
    
    # Thay thế các giá trị trong mảng values bằng các giá trị từ g_sorted_replaced
    value_map = dict(zip(g_sorted, g_sorted_replaced))
    values_replaced = np.array([value_map.get(val, val) for val in values])
    
    # In mảng values sau khi thay thế
    print("\nMảng values sau khi thay thế các giá trị:")
    print(values_replaced.reshape((rows, cols)))

if __name__ == "__main__":
    main()



 
