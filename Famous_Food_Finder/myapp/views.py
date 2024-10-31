from django.shortcuts import render  # สำคัญ ไอนี้ไว้ใช้เรียกไฟล์
from django.http import HttpResponse  # สำคัญ อันนี้ตอบสนอง

# Create your views here.
# ฟังก์ชัน ให้มันทำ
def index(request):
    return render(request,"index.html") #ใส่ tag html ได้

def about(request):
    return render(request,"about.html")