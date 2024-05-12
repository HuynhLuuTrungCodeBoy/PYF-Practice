#Kiểm tra số nhập vào là số chẳn hoặc lẻ, sử dụng toán tử điều kiện ba ngôi
so=int(input("Nhập 1 số nguyên dương: "))
thong_bao="Đây là số chẵn" if so % 2 == 0 else "Đây là số lẻ"
print(thong_bao)