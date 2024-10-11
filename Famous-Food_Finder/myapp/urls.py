# urls.py
from django.urls import path
from myapp import views  # นำเข้าฟังก์ชัน view จากไฟล์ views.py

urlpatterns = [ #เพิ่มลิงค์ไปเพิ่ม ต้อง + urls.py ลงไปใน sub ย่อยด้วย
    path('',views.index), #,อย่าลืมใส่นะ
    path('about',views.about),
    path('date',views.date),
]
