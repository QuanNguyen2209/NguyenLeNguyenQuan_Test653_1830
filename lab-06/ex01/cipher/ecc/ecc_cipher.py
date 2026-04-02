try:
    from ecies import encrypt, decrypt
    from ecies.utils import generate_key
    ECIES_AVAILABLE = True
    
    # Đưa phần tạo khóa ra ngoài để nó tự động in ra khi Server vừa khởi động
    print("\n" + "="*70)
    print("🔑 BỘ KHÓA ECC (DÙNG ĐỂ TEST GIAO DIỆN)")
    k = generate_key()
    print(f"[1] Public Key (Khóa Công khai - Dùng để Mã hóa): \n{k.public_key.format(True).hex()}")
    print("-" * 70)
    print(f"[2] Private Key (Khóa Bí mật - Dùng để Giải mã): \n{k.to_hex()}")
    print("="*70 + "\n")

except ImportError:
    ECIES_AVAILABLE = False
    print("\n[CẢNH BÁO] Chưa cài thư viện eciespy. Hãy mở Terminal chạy lệnh: pip install eciespy\n")

class ECCCipher:
    def __init__(self):
        pass

    def encrypt_text(self, text, public_key_hex):
        """
        Hàm xử lý mã hóa ECC thật.
        Biến đổi text thành bytes -> Mã hóa bằng Public Key -> Trả về chuỗi Hex.
        """
        if not ECIES_AVAILABLE:
            return "[LỖI] Chưa cài thư viện! Vui lòng mở Terminal chạy lệnh: pip install eciespy"
            
        if not text or not public_key_hex:
            return "[LỖI] Vui lòng nhập bản rõ và Public Key!"
            
        try:
            # Mã hóa bản rõ
            encrypted_bytes = encrypt(public_key_hex, text.encode('utf-8'))
            return encrypted_bytes.hex()
        except Exception as e:
            return f"[LỖI MÃ HÓA] Public Key không hợp lệ! Chi tiết: {str(e)}"

    def decrypt_text(self, hex_ciphertext, private_key_hex):
        """
        Hàm xử lý giải mã ECC thật.
        Lấy chuỗi Hex -> Biến đổi về bytes -> Giải mã bằng Private Key -> Trả về text gốc.
        """
        if not ECIES_AVAILABLE:
            return "[LỖI] Chưa cài thư viện! Vui lòng mở Terminal chạy lệnh: pip install eciespy"
            
        if not hex_ciphertext or not private_key_hex:
            return "[LỖI] Vui lòng nhập bản mã và Private Key!"
            
        try:
            # Chuyển bản mã từ dạng Hex về dạng Bytes
            encrypted_bytes = bytes.fromhex(hex_ciphertext)
            # Giải mã
            decrypted_bytes = decrypt(private_key_hex, encrypted_bytes)
            return decrypted_bytes.decode('utf-8')
        except Exception as e:
            return f"[LỖI GIẢI MÃ] Sai Private Key hoặc bản mã bị hỏng! Chi tiết: {str(e)}"