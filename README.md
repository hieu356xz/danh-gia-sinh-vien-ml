# Dự án phân tích và dự đoán điểm cuối kì của sinh viên dựa trên dữ liệu học thuật và xã hội

Dự án này sử dụng các thuật toán Machine Learning để phân tích và dự đoán kết quả học tập cuối kỳ (điểm G3) của học sinh dựa trên dữ liệu về học thuật, xã hội và nhân khẩu học.

## Mục tiêu

-   Xây dựng một mô hình hồi quy (regression) để dự đoán điểm cuối kỳ (`G3`) của học sinh.
-   Phân tích mức độ quan trọng của các yếu tố khác nhau (ví dụ: thời gian học, điểm kỳ trước, hoạt động xã hội) ảnh hưởng đến kết quả học tập.
-   Xây dựng một giao diện web đơn giản để người dùng có thể tương tác và thực hiện dự đoán.

## Bộ dữ liệu

-   **Nguồn**: [UCI Student Performance](https://archive.ics.uci.edu/ml/datasets/Student+Performance)
-   **Mô tả**: Dữ liệu được thu thập từ hai trường học ở Bồ Đào Nha, bao gồm điểm số, thông tin nhân khẩu học, xã hội và các yếu tố liên quan đến trường học.

## Công nghệ sử dụng

-   **Ngôn ngữ**: Python
-   **Thư viện**: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Streamlit
-   **Mô hình**: `RandomForestRegressor`
-   **Phân tích**: Jupyter Notebook (`DuDoanDiemSinhVien.ipynb`)

## Cách chạy dự án

1.  **Tạo và kích hoạt môi trường ảo:**
    > **Chỉ cần chạy lần đầu tiên**

    Lệnh để tạo một môi trường ảo có tên là ".venv"
    ```bash
    python -m venv .venv
    ```
    Sau khi tạo, bạn cần kích hoạt nó mỗi khi làm việc với dự án.
    ### Đối với Windows (PowerShell):
    ```bash
    .venv\Scripts\Activate.ps1
    ```

    ### Đối với macOS/Linux (bash/zsh):
    ```bash
    source .venv/bin/activate
    ```
    Sau khi kích hoạt, bạn sẽ thấy `(.venv)` ở đầu dòng lệnh trong terminal.

2.  **Cài đặt các thư viện cần thiết:**
    (Đảm bảo môi trường ảo đã được kích hoạt)
    ```bash
    pip install -r requirements.txt
    ```

3.  **Xem quá trình phân tích và huấn luyện model:**
    Mở và chạy các cell trong file `DuDoanDiemSinhVien.ipynb`.

4.  **Chạy giao diện web dự đoán:**
    > **Lưu ý:** Cần chạy notebook ở **Bước 3** ít nhất một lần để export ra file model (`student_performance_regressor.joblib`).

    Chạy lệnh sau trong terminal:
    ```bash
    streamlit run app.py
    ```
    Một tab mới sẽ mở ra trong trình duyệt của bạn, hiển thị giao diện ứng dụng.
