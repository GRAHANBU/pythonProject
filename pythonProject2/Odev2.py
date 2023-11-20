import cv2
import numpy as np

# Kamera bağlantısını başlat
cap = cv2.VideoCapture(0)

while True:
    # Kameradan bir frame al
    ret, frame = cap.read()

    # HSV renk uzayına dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Kırmızı renk aralığı (HSV formatında)
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # Belirtilen renk aralığındaki pikselleri beyaz, diğerlerini siyah yap
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Görüntüdeki sadece kırmızı nesneleri göster
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Görüntüleri göster
    cv2.imshow('Original', frame)
    cv2.imshow('Result', result)

    # Çıkış için 'q' tuşuna basın
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera bağlantısını kapat
cap.release()
cv2.destroyAllWindows()
