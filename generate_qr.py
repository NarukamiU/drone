import qrcode

# 変数の値
v = "4"
range_val = "5"
takeoff_val = "1"
land_val = "0"

# データをデリミタで結合
data = f"v={v},range={range_val},takeoff={takeoff_val},land={land_val}"

# QRコードを生成
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# ファイル名を構築
file_name = f"v{v}_range{range_val}_takeoff{takeoff_val}_land{land_val}.png"

# ファイルパスを指定
file_path = f"C:\\DATA\\program\\drone\\img_qr\\{file_name}"

# 生成したQRコードを指定したファイルパスに保存
img = qr.make_image(fill_color="black", back_color="white")
img.save(file_path)

print(f"QRコードを {file_path} に保存しました。")
