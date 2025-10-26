# Dự án Phân tích và Dự đoán Kết quả Học tập của Sinh viên

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

1.  **Cài đặt các thư viện cần thiết:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Xem quá trình phân tích và huấn luyện model:**
    Mở và chạy các cell trong file `DuDoanDiemSinhVien.ipynb`.

3.  **Chạy giao diện web dự đoán:**
    > **Lưu ý:** Cần chạy notebook ở **Bước 2** ít nhất một lần để export ra file model (`student_performance_regressor.joblib`).

    Chạy lệnh sau trong terminal:
    ```bash
    streamlit run app.py
    ```
    Một tab mới sẽ mở ra trong trình duyệt của bạn, hiển thị giao diện ứng dụng.
