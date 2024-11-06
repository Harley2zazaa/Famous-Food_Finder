# urls.py
from django.urls import path
from myapp import views  # นำเข้าฟังก์ชัน view จากไฟล์ views.py
from . import views

urlpatterns = [ #เพิ่มลิงค์ไปเพิ่ม ต้อง + urls.py ลงไปใน sub ย่อยด้วย
    path('', views.index, name='index'),  # ชื่อ URL ต้องเป็น 'index'
    path('about/', views.about, name='about'),  # หน้าข้อมูลเกี่ยวกับ
    path('search/', views.search_recipes, name='search_recipes'),  # หน้า search_recipes
    path('random/', views.random_recipes, name='random_recipes'), #ระบบสุ่ม
    path('about/', views.about, name='about'),
]
