import subprocess
import os

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"Lệnh: {command}\nKết quả: {result.stdout}")
    except subprocess.CalledProcessError as e:
        if "is not recognized" in e.stderr or "not found" in e.stderr.lower():
            print(f"\n[!] LOI: Khong tim thay lenh 'git' tren may tinh cua ban.")
            print("Vui long tai va cai dat Git tai: https://git-scm.com/")
            print("Sau khi cai dat, hay khoi dong lai VS Code va thu lai.\n")
        else:
            print(f"Lỗi khi chạy lệnh: {command}\nLỗi: {e.stderr}")
        return False
    return True

def check_git_identity():
    # Kiểm tra email
    res_email = subprocess.run("git config user.email", shell=True, capture_output=True, text=True)
    res_name = subprocess.run("git config user.name", shell=True, capture_output=True, text=True)
    
    if not res_email.stdout.strip() or not res_name.stdout.strip():
        print("\n--- CAI DAT THONG TIN GIT (CHI CAN LAM 1 LAN) ---")
        if not res_email.stdout.strip():
            email = input("Nhap Email GitHub cua ban: ")
            run_command(f'git config --global user.email "{email}"')
        if not res_name.stdout.strip():
            name = input("Nhap Ten GitHub cua ban: ")
            run_command(f'git config --global user.name "{name}"')
        print("--------------------------------------------------\n")

def push_to_github(commit_message="Add new exercises"):
    # Kiểm tra danh tính trước
    check_git_identity()
    
    # Kiểm tra thư mục hiện tại có phải repo Git không
    if not os.path.exists(".git"):
        print("Khởi tạo kho lưu trữ Git...")
        if not run_command("git init"):
            return

    # Thêm tất cả các tệp
    print("Đang thêm các tệp...")
    if not run_command("git add ."):
        return

    # Commit
    print(f"Đang commit với thông điệp: {commit_message}")
    if not run_command(f'git commit -m "{commit_message}"'):
        # Nếu commit thất bại (có thể do chưa có thay đổi), ta cứ tiếp tục thử push
        print("Lưu ý: Không thể tạo commit mới (có thể do không có thay đổi).")

    # Kiểm tra remote
    result = subprocess.run("git remote", shell=True, capture_output=True, text=True)
    if not result.stdout.strip():
        print("\nĐang thiết lập Remote cho GitHub...")
        repo_url = "https://github.com/pham-ngoc-khanh/Chuong-2.git"
        if run_command(f"git remote add origin {repo_url}"):
            print(f"Đã thêm remote: {repo_url}")
        else:
            return

    # Đẩy lên GitHub
    print("Đang đẩy code lên GitHub...")
    # Đảm bảo nhánh hiện tại là 'main'
    run_command("git branch -M main")
    run_command("git push -u origin main") 

if __name__ == "__main__":
    push_to_github()
