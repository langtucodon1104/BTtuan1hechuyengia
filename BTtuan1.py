# Hệ chuyên gia quyết định đi biển

thoi_tiet =  input("Nhập thời tiết (nắng/mưa/âm u): ")
nhiet_do =   int(input("Nhập nhiệt độ (°C): "))       
suc_khoe =   input("Tình trạng sức khỏe (tốt/không tốt): ")

if thoi_tiet == "mưa" or thoi_tiet == "Mưa":
    print("Không nên đi biển: do mưa")
elif suc_khoe == "không tốt" or suc_khoe == "Không tốt":
    print("Không nên đi biển: Sức khỏe không đảm bảo")
elif (thoi_tiet == "âm u" or thoi_tiet == "Âm u") and nhiet_do < 25:
    print("Không nên đi biển: Trời âm u và lạnh.")
elif (thoi_tiet == "nắng" or thoi_tiet == "Nắng") and 25 <= nhiet_do <= 35 and (suc_khoe == "tốt" or suc_khoe == "Tốt"):
    print("Nên đi biển: Thời tiết đẹp, nhiệt độ phù hợp, sức khỏe tốt.")
else:
    print("Cân nhắc: Điều kiện chưa hoàn hảo để đi biển.")