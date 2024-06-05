def get_product_info(products, prod_id):
    """Lấy thông tin sản phẩm bằng ID sản phẩm"""
    if prod_id in products:
        return products[prod_id]
    return None

def update_product_list(products, prod_id, prod_name):
    """Cập nhật danh sách sản phẩm"""
    products[prod_id] = prod_name

def display_products(products):
    """Hiển thị danh sách sản phẩm hiện tại"""
    if not products:
        print("Danh sách sản phẩm trống.")
    else:
        print("Danh sách sản phẩm hiện tại:")
        for prod_id, prod_name in products.items():
            print(f"ID: {prod_id}, Tên: {prod_name}")

def main():
    products = {}

    while True:
        print("\nQuản lý sản phẩm:")
        print("1. Thêm sản phẩm mới")
        print("2. Cập nhật sản phẩm")
        print("3. Xoá sản phẩm")
        print("4. Hiển thị danh sách sản phẩm")
        print("5. Thoát")

        try:
            option = int(input("Chọn một tuỳ chọn (1-5): "))
        except ValueError:
            print("Vui lòng nhập một số nguyên.")
            continue

        if option == 1:
            product_id = int(input("Nhập ID sản phẩm: "))
            if get_product_info(products, product_id):
                print(f"Sản phẩm với ID {product_id} đã tồn tại.")
            else:
                product_name = input("Nhập tên sản phẩm: ")
                update_product_list(products, product_id, product_name)
                print(f"Đã thêm sản phẩm: ID {product_id}, Tên {product_name}")

        elif option == 2:
            product_id = int(input("Nhập ID sản phẩm cần cập nhật: "))
            if get_product_info(products, product_id):
                product_name = input("Nhập tên mới của sản phẩm: ")
                update_product_list(products, product_id, product_name)
                print(f"Đã cập nhật sản phẩm: ID {product_id}, Tên {product_name}")
            else:
                print(f"Sản phẩm với ID {product_id} không tồn tại.")

        elif option == 3:
            product_id = int(input("Nhập ID sản phẩm cần xoá: "))
            if get_product_info(products, product_id):
                del products[product_id]
                print(f"Đã xoá sản phẩm với ID {product_id}.")
            else:
                print(f"Sản phẩm với ID {product_id} không tồn tại.")

        elif option == 4:
            display_products(products)

        elif option == 5:
            print("Thoát khỏi ứng dụng.")
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 5.")

        display_products(products)

if __name__ == "__main__":
    main()
