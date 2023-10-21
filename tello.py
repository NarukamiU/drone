import cv2
from pyzbar.pyzbar import decode

# カメラを起動
cap = cv2.VideoCapture(4)  # カメラデバイスの番号を指定

# ウィンドウの初期サイズを設定
cv2.namedWindow('QR Code Detection', cv2.WINDOW_NORMAL)
cv2.resizeWindow('QR Code Detection', 990, 510)  # 640x480 のサイズに変更

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # QRコードを読み取り
    decoded_objects = decode(frame)

    for obj in decoded_objects:
        data = obj.data.decode('utf-8')
        cv2.putText(frame, data, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # 画面に映像を表示
    cv2.imshow('QR Code Detection', frame)

    # 'q' キーを押すとプログラムが終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
