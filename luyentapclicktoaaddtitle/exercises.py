import os

# B1: Viết một chương trình Python để đọc n dòng đầu tiên của một tập tin cho trước. 
# Với n là số được nhập từ bàn phím.
def exercise_b1():
    file_path = "demo_file1.txt" # Giả sử dùng file này để test
    if not os.path.exists(file_path):
        # Tạo file tạm nếu chưa có để demo
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("Dòng 1\nDòng 2\nDòng 3\nDòng 4\nDòng 5")
            
    try:
        n = int(input("Nhập số dòng n cần đọc: "))
        with open(file_path, 'r', encoding='utf-8') as f:
            for i in range(n):
                line = f.readline()
                if not line:
                    break
                print(line.strip())
    except ValueError:
        print("Vui lòng nhập một số nguyên.")

# B2: Viết một chương trình Python để ghi đoạn văn bản vào một tập tin và hiển thị văn bản đó.
def exercise_b2():
    file_path = "exercise_b2.txt"
    content = input("Nhập đoạn văn bản muốn ghi vào file: ")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Nội dung văn bản trong file là:")
    with open(file_path, 'r', encoding='utf-8') as f:
        print(f.read())

# B3: Tạo file 'demo_file1.txt' trong thư mục source code.
# Nội dung: 'Thuc \n hanh \n voi \n file\n IO\n'
def exercise_b3():
    content = "Thuc \n hanh \n voi \n file\n IO\n"
    file_path = "demo_file1.txt"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # a) In ra màn hình nội dung file đó trên một dòng
    print("a) Nội dung trên một dòng:")
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().replace('\n', ' ')
        print(text)
        
    # b) In ra màn hình nội dung file đó theo từng dòng
    print("\nb) Nội dung theo từng dòng:")
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())

# B4: Nhập thông tin cá nhân và lưu vào file 'setInfo.txt'
def exercise_b4():
    # Nhập từ bàn phím
    print("Nhập thông tin cá nhân:")
    ten = input("Tên: ")
    tuoi = input("Tuổi: ")
    email = input("Email: ")
    skype = input("Skype: ")
    dia_chi = input("Địa chỉ: ")
    noi_lam_viec = input("Nơi làm việc: ")
    
    info = f"Tên: {ten}\nTuổi: {tuoi}\nEmail: {email}\nSkype: {skype}\nĐịa chỉ: {dia_chi}\nNơi làm việc: {noi_lam_viec}"
    
    # a) Lưu vào file 'setInfo.txt'
    with open('setInfo.txt', 'w', encoding='utf-8') as f:
        f.write(info)
        
    # b) Đọc và hiển thị kết quả
    print("\nKết quả từ file setInfo.txt:")
    with open('setInfo.txt', 'r', encoding='utf-8') as f:
        print(f.read())

# B5: Đếm số lượng xuất hiện của các từ trong file 'demo_file2.txt'
def exercise_b5():
    content = 'Dem so luong tu xuat hien abc abc abc 12 12 it it eaut'
    file_path = 'demo_file2.txt'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    word_count = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        # Tách từ và chuyển về chữ thường để đếm chính xác (nếu cần)
        # Ở đây theo đề bài thì có vẻ giữ nguyên hoặc không quan trọng hoa thường
        text = f.read()
        words = text.split()
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
            
    print("\nKết quả đếm từ:")
    print(word_count)

if __name__ == "__main__":
    while True:
        print("\n--- CHỌN BÀI TẬP ---")
        print("1. Bài B1: Đọc n dòng đầu file")
        print("2. Bài B2: Ghi và hiển thị văn bản")
        print("3. Bài B3: Tạo file demo_file1.txt và in")
        print("4. Bài B4: Nhập thông tin cá nhân và lưu file")
        print("5. Bài B5: Đếm từ trong file demo_file2.txt")
        print("0. Thoát")
        
        choice = input("Nhập lựa chọn của bạn: ")
        
        if choice == '1':
            exercise_b1()
        elif choice == '2':
            exercise_b2()
        elif choice == '3':
            exercise_b3()
        elif choice == '4':
            exercise_b4()
        elif choice == '5':
            exercise_b5()
        elif choice == '0':
            break
        else:
            print("Lựa chọn không hợp lệ.")
