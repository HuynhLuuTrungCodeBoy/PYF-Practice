def count_word_occurrences(text):
    # Bước 1: Khai báo biến num_words để lưu trữ số lần xuất hiện của mỗi từ
    num_words = {}
    
    # Sử dụng split() để tách các từ trong chuỗi truyền vào
    text_list = text.split()
    
    # Sử dụng for...in để lặp qua mảng text_list
    for word in text_list:
        # Chuyển các ký tự hoa thành ký tự thường và loại bỏ khoảng trắng
        word = word.lower().strip()
        
        # Lấy giá trị đếm hiện tại của từ lặp trong num_words, mặc định là 0 nếu không tìm thấy
        count = num_words.get(word, 0)
        
        # Cập nhật giá trị đếm của từ
        num_words[word] = count + 1
    
    # Trả biến num_words làm kết quả hàm
    return num_words

# Bước 2: Khai báo biến message mang giá trị là văn bản cần đếm
message = "This is a test. This test is only a test."

# Bước 3: Gọi hàm đếm từ và truyền message làm tham số
word_counts = count_word_occurrences(message)

# In kết quả
print(word_counts)
