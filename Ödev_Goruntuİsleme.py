import cv2
import matplotlib.pyplot as plt

def calculate_histogram(image_path):
    # Görüntüyü gri seviyeye çevir
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    height, width = image.shape

    # Histogram için dizi oluştur
    histogram = [0] * 256

    # Görüntüdeki her pikselin değerine göre histogramı güncelle
    for i in range(height):
        for j in range(width):
            pixel_value = image[i, j]
            histogram[pixel_value] += 1

    return histogram

# Görüntüyü yükle
image_path = 'manzara.jpg'

# Histogramı hesapla
histogram = calculate_histogram(image_path)

# Histogramı görselleştir
plt.bar(range(256), histogram, color='gray')
plt.title('Gri Seviyeli Görüntü Histogramı')
plt.xlabel('Piksel Değeri')
plt.ylabel('Piksel Sayısı')
plt.show()