import math

class TranspositionCipher:
    def __init__(self):
        # Hàm khởi tạo, bạn có thể để trống hoặc thiết lập các biến mặc định nếu cần
        pass

    def encrypt_text(self, text, key):
        """
        Hàm mã hóa Transposition Cipher
        :param text: Chuỗi văn bản gốc (Plaintext)
        :param key: Số lượng cột (Integer)
        :return: Chuỗi đã được mã hóa (Ciphertext)
        """
        # Nếu số cột <= 1, không cần hoán vị
        if key <= 1 or not text:
            return text

        # Tạo một mảng chứa các cột, mỗi phần tử là 1 chuỗi rỗng
        ciphertext_columns = [""] * key

        # Duyệt qua từng cột
        for col in range(key):
            pointer = col
            # Lấy các ký tự cách nhau một khoảng bằng đúng số cột (key)
            while pointer < len(text):
                ciphertext_columns[col] += text[pointer]
                pointer += key

        # Nối các cột lại với nhau để tạo thành bản mã
        return "".join(ciphertext_columns)

    def decrypt_text(self, text, key):
        """
        Hàm giải mã Transposition Cipher
        :param text: Chuỗi bản mã (Ciphertext)
        :param key: Số lượng cột lúc mã hóa (Integer)
        :return: Chuỗi văn bản gốc (Plaintext)
        """
        if key <= 1 or not text:
            return text

        # Tính toán hình dáng của lưới giải mã
        # Số cột của lưới giải mã chính là độ dài của một phần chuỗi được chia
        num_cols = int(math.ceil(len(text) / float(key)))
        
        # Số hàng của lưới giải mã (tương ứng với key lúc mã hóa)
        num_rows = key
        
        # Tính số lượng ô trống (shaded boxes) ở góc dưới cùng bên phải của lưới
        num_shaded_boxes = (num_cols * num_rows) - len(text)

        # Mảng chứa bản rõ, mỗi phần tử đại diện cho 1 cột của LƯỚI GIẢI MÃ
        plaintext_columns = [""] * num_cols
        
        col = 0
        row = 0
        
        # Duyệt qua từng ký tự trong bản mã
        for symbol in text:
            plaintext_columns[col] += symbol
            col += 1
            
            # Chuyển sang hàng tiếp theo nếu đã đi hết cột hiện tại 
            # HOẶC chạm vào ô trống (shaded box) ở những hàng cuối
            if (col == num_cols) or (col == num_cols - 1 and row >= num_rows - num_shaded_boxes):
                col = 0
                row += 1
                
        # Nối lại để được bản rõ ban đầu
        return "".join(plaintext_columns)