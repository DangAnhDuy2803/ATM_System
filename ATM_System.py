# ==============================
# PRACTICE ATM SYSTEM
# ==============================

# Khởi tạo dữ liệu
account_name = ""
balance = 0
transactions = []

# ---------- Chức năng ----------
def tao_tai_khoan():
    global account_name, balance
    account_name = input("Nhập tên chủ tài khoản: ")
    while True:
        try:
            balance = float(input("Nhập số dư ban đầu: "))
            if balance < 0:
                print("❌ Số dư không hợp lệ")
            else:
                break
        except ValueError:
            print("❌ Vui lòng nhập số")
    print("✅ Tạo tài khoản thành công!\n")

def gui_tien():
    global balance
    try:
        amount = float(input("Nhập số tiền cần gửi: "))
        if amount <= 0:
            print("❌ Số tiền không hợp lệ")
            return
        balance += amount
        transactions.append(f"Gửi tiền: +{amount}")
        print("✅ Gửi tiền thành công!")
    except ValueError:
        print("❌ Vui lòng nhập số")

def rut_tien():
    global balance
    try:
        amount = float(input("Nhập số tiền cần rút: "))
        if amount <= 0:
            print("❌ Số tiền không hợp lệ")
        elif amount > balance:
            print("❌ Số dư không đủ")
        else:
            balance -= amount
            transactions.append(f"Rút tiền: -{amount}")
            print("✅ Rút tiền thành công!")
    except ValueError:
        print("❌ Vui lòng nhập số")

def xem_so_du():
    print(f"💰 Số dư hiện tại: {balance}")

def xem_lich_su():
    if not transactions:
        print("📭 Chưa có giao dịch nào")
    else:
        print("📜 Lịch sử giao dịch:")
        for i, t in enumerate(transactions, 1):
            print(f"{i}. {t}")

# ---------- Menu giao dịch ----------
def menu_giao_dich():
    while True:
        print("""
--- MENU GIAO DỊCH ---
a. Gửi tiền
b. Rút tiền
c. Xem số dư
d. Xem lịch sử giao dịch
e. Quay về menu chính
""")
        choice = input("Chọn chức năng: ").lower()

        if choice == "a":
            gui_tien()
        elif choice == "b":
            rut_tien()
        elif choice == "c":
            xem_so_du()
        elif choice == "d":
            xem_lich_su()
        elif choice == "e":
            break
        else:
            print("❌ Lựa chọn không hợp lệ")

# ---------- Menu chính ----------
def menu_chinh():
    while True:
        print("""
=== ATM SYSTEM ===
1. Tạo tài khoản
2. Giao dịch
3. Kết thúc
""")
        choice = input("Chọn chức năng: ")

        if choice == "1":
            tao_tai_khoan()
        elif choice == "2":
            if account_name == "":
                print("❌ Vui lòng tạo tài khoản trước")
            else:
                menu_giao_dich()
        elif choice == "3":
            print("👋 Cảm ơn đã sử dụng ATM!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ")

# ---------- Chạy chương trình ----------
menu_chinh()
