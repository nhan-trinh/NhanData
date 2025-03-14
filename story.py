from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Khởi tạo trình duyệt Chrome
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Chạy ẩn trình duyệt (tùy chọn)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Truy cập NetTruyen
url = "https://nettruyenrr.com/"
driver.get(url)

try:
    # Chờ danh sách truyện xuất hiện
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "item")))

    # Lấy danh sách truyện
    stories = driver.find_elements(By.CLASS_NAME, "item")

    for story in stories:
        try:
            # Lấy tên truyện
            name = story.find_element(By.CLASS_NAME, "jtip").text.strip()

            # Lấy chapter mới nhất
            chapter = story.find_element(By.CLASS_NAME, "chapter").text.strip()

            print(f"Tên Truyện: {name} - Chapter: {chapter}")
        except:
            continue

except Exception as e:
    print("Không tìm thấy dữ liệu:", e)

# Đóng trình duyệt
driver.quit()