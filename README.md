# Python Code Obfuscator 🔒

**Công cụ obfuscate mã Python bằng cách chuyển đổi thành state machine với ký tự Hàn Quốc**

## ✨ Tính năng

- 🇰🇷 **Ký tự Hàn Quốc**: Sử dụng ký tự Hàn Quốc làm tên biến để tăng độ khó đọc
- 🔄 **State Machine**: Chuyển đổi luồng thực thi thành while loop với match-case
- 🎲 **Xáo trộn**: Shuffle thứ tự các case để làm rối logic
- ⚙️ **Linh hoạt**: Nhiều tùy chọn để customize quá trình obfuscate
- 🚀 **Dễ sử dụng**: Giao diện command line thân thiện

## 🔧 Cài đặt

1. **Yêu cầu**: Python 3.10+ (do sử dụng match-case statement)
2. **Clone hoặc download** file `skibidi.py`
3. **Chạy trực tiếp** - không cần cài đặt thêm thư viện

```bash
# Kiểm tra phiên bản Python
python --version  # Cần >= 3.10

# Download file
curl -O https://raw.githubusercontent.com/your-repo/skibidi.py
# hoặc download trực tiếp từ GitHub
```

## 🚀 Cách sử dụng

### Cú pháp cơ bản

```bash
python skibidi.py <input_file> [options]
```

### Các tùy chọn

| Tùy chọn | Mô tả |
|----------|-------|
| `-o, --output FILE` | Lưu kết quả vào file (mặc định: in ra màn hình) |
| `-r, --run` | Chạy code đã obfuscate sau khi tạo |
| `--no-korean` | Không sử dụng ký tự Hàn Quốc (dùng ký tự Latin) |
| `--seed NUMBER` | Seed cho random generator (để có kết quả nhất quán) |
| `-v, --verbose` | In thông tin chi tiết |
| `-h, --help` | Hiển thị help |

### 📋 Ví dụ sử dụng

#### 1. Obfuscate và in ra màn hình
```bash
python skibidi.py example.py
```

#### 2. Obfuscate và lưu vào file
```bash
python skibidi.py example.py -o obfuscated.py
```

#### 3. Obfuscate và chạy luôn
```bash
python skibidi.py example.py -r
```

#### 4. Không dùng ký tự Hàn Quốc
```bash
python skibidi.py example.py --no-korean -o output.py
```

#### 5. Sử dụng seed cố định (để có kết quả nhất quán)
```bash
python skibidi.py example.py --seed 123 -o consistent.py
```

#### 6. Mode verbose (xem thông tin chi tiết)
```bash
python skibidi.py example.py -v -o output.py
```

## 🧪 Demo với file mẫu

Thử ngay với file `example.py` có sẵn:

```bash
# Chạy file gốc
python example.py

# Obfuscate và so sánh
python skibidi.py example.py -r
```

### Code gốc:
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(f"Fibonacci(10) = {fibonacci(10)}")
```

### Sau khi obfuscate:
```python
뻱ꎅ뇹뫬궶훝죚ꂮ뺻늵뵹숉붧껻닸ꌍ뾲 = 445834713894
while True:
    match 뻱ꎅ뇹뫬궶훝죚ꂮ뺻늵뵹숉붧껻닸ꌍ뾲:
        case 445834713895:
            뻱ꎅ뇹뫬궶훝죚ꂮ뺻늵뵹숉붧껻닸ꌍ뾲 = 445834713896
        case 445834713894:
            def fibonacci(n):
                if n <= 1:
                    return n
                return fibonacci(n - 1) + fibonacci(n - 2)
            뻱ꎅ뇹뫬궶훝죚ꂮ뺻늵뵹숉붧껻닸ꌍ뾲 = 445834713895
        case 445834713896:
            break
        case _:
            break
```

## 🎯 Cách hoạt động

1. **Parse AST**: Phân tích mã Python thành Abstract Syntax Tree
2. **Tạo labels**: Tạo các nhãn số ngẫu nhiên cho từng statement
3. **Xây dựng state machine**: Chuyển đổi thành while loop với match-case
4. **Shuffle cases**: Xáo trộn thứ tự để làm rối logic
5. **Generate code**: Tạo lại mã Python từ AST đã được modify

## ⚠️ Lưu ý

- **Python 3.10+**: Bắt buộc do sử dụng match-case statement
- **Performance**: Code sau khi obfuscate sẽ chạy chậm hơn do overhead của state machine
- **Debugging**: Rất khó debug code đã obfuscate
- **Chỉ là obfuscation**: Không phải là encryption thực sự, vẫn có thể reverse engineer

## 🛡️ Bảo mật

- Code obfuscate **KHÔNG** cung cấp bảo mật thực sự
- Chỉ làm khó đọc, không mã hóa
- Có thể bị reverse engineer bởi các công cụ chuyên dụng
- Nên kết hợp với các biện pháp bảo mật khác

## 🚫 Hạn chế

- Chỉ hoạt động với Python 3.10+
- Không hỗ trợ một số cấu trúc Python phức tạp
- Performance giảm đáng kể
- Kích thước file tăng lên

## 🤝 Đóng góp

Mọi đóng góp đều được hoan nghênh! Hãy:

1. Fork project
2. Tạo feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Mở Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📧 Liên hệ

**NGUYEN XUAN TRINH** - [GitHub Profile](https://github.com/your-username)

Project Link: [https://github.com/nguyenxuantrinhnotpd/Python-Obfuscator](https://github.com/nguyenxuantrinhnotpd/Python-Obfuscator)

---

## 🎉 Credits

- Inspired by các kỹ thuật obfuscation trong lĩnh vực cybersecurity
- Sử dụng Unicode Hàn Quốc ranges: 44032-55203 (Hangul Syllables)
- Built with ❤️ và Python AST

**Happy Obfuscating! 🔒✨**

