ev_dict = {
    "pen": "bút",
    "pencil": "bút chì",
    "eraser": "cục tẩy",
    "notebook": "sổ tay",
    "ruler": "thước kẻ",
    "marker": "bút đánh dấu",
    "highlighter": "bút dạ quang",
    "backpack": "ba lô",
    "calculator": "máy tính",
    "stapler": "dập ghim",
    "paperclip": "kẹp giấy",
    "scissors": "kéo",
    "glue": "keo dán",
    "sharpener": "gọt bút chì",
    "folder": "bìa hồ sơ",
    "chalk": "phấn",
    "whiteboard": "bảng trắng",
    "notepad": "giấy ghi chú",
    "compass": "com-pa",
    "protractor": "thước đo góc"
}
def translate_to_VN(data_dic,word):
  if word in ev_dict:
    return ev_dict[word]
  else:
    return None

#kiểm thử
print("Từ điển Anh - Việt này có 20 từ về dụng cụ học tập.")
input_word=input("Mời bạn nhập vào 1 từ tiếng Anh:").lower()
translated_word=translate_to_VN(ev_dict,input_word)
if translated_word is None:
  print("Chưa có từ này trong từ điển.")
else:
  print(f"{input_word.capitalize()} nghĩa là {translated_word}.")
