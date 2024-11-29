# Hệ thống quản lý sự kiện hiến máu cho hội chữ thập đỏ

## Mô Tả

**Hệ Thống Quản Lý Sự Kiện Hiến Máu** Dự án này là một ứng dụng backend được xây dựng bằng DJANGO. Dự án cung cấp các API để xử lý các yêu cầu từ phía frontend hoặc các ứng dụng khác thông qua HTTP..

---

## Cài Đặt

Để cài đặt dự án, bạn có thể tuân theo các bước sau:

1. **Clone Repository**: Sao chép repository từ GitHub về máy tính của bạn bằng cách chạy lệnh sau trong terminal:

   ```bash
   git clone https://github.com/longhoang123123/volunteer-be.git
   ```

2. **Cài đặt Poetry (nếu chưa có)**:

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

   hoặc

   ```bash
   pip install poetry
   ```

3. **Cài đặt venv: Window**:

   ```bash
   python -m venv venv
   cd venv/Scripts
   activate
   cd ../../
   ```

   linux

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

4. **Cài đặt PostgreSQL**:

5. **Cài đặt thư viện kết nối PostgreSQL**:

   ```bash
   pip install psycopg2-binary
   ```

6. **Cấu hình settings.py trong Django**:

   ```bash
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tên_cơ_sở_dữ_liệu',
        'USER': 'tên_người_dùng',
        'PASSWORD': 'mật_khẩu',
        'HOST': 'localhost',  # Hoặc địa chỉ IP của máy chủ PostgreSQL
        'PORT': '5432',       # Cổng mặc định của PostgreSQL
    }
   }
   ```

7. **Tạo cơ sở dữ liệu trên pgAdmin 4**:
8. **Kết nối Django với cơ sở dữ liệu**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

9. **Lệnh tạo siêu người dùng để truy cập Django Admin**:

   ```bash
   python manage.py createsuperuser
   ```

10. **Lệnh chạy Django**:

    ```bash
    python manage.py runserver
    ```
