from django.shortcuts import render  # สำคัญ ไอนี้ไว้ใช้เรียกไฟล์
from django.http import HttpResponse  # สำคัญ อันนี้ตอบสนอง
from django.conf import settings# นำเข้า settings สำหรับดึง API key
import requests  # ใช้สำหรับเรียก API ภายนอก
import random # สำหรับสุ่มอาหารที่เลือก

# Create your views here.
# ฟังก์ชัน ให้มันทำ
def index(request):
    return render(request,"index.html") #ใส่ tag html ได้

def about(request):
    return render(request,"about.html")

# ฟังก์ชันค้นหา recipes จาก API
def search_recipes(request):
    query = request.GET.get('query')  # ดึงคีย์เวิร์ดที่ผู้ใช้ค้นหาจาก query parameter
    api_key = settings.SPOONACULAR_API_KEY  # ดึง API key จาก settings

    # เรียก API ของ Spoonacular ด้วย query
    url = f"https://api.spoonacular.com/recipes/complexSearch?query={query}&number=200&apiKey={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        all_recipes = response.json().get('results', [])
        # Randomly select 6 recipes
        recipes = random.sample(all_recipes, min(6, len(all_recipes)))
    else:
        recipes = []

    return render(request, "search_results.html", {'recipes': recipes})

# ฟังก์ชันสุ่ม recipes จาก API
def random_recipes(request):
    api_key = settings.SPOONACULAR_API_KEY  # ดึง API key จาก settings

    # เรียก API ของ Spoonacular โดยไม่ระบุ query เพื่อดึงอาหารแบบสุ่ม
    url = f"https://api.spoonacular.com/recipes/random?number=200&apiKey={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        all_recipes = response.json().get('recipes', [])
        # Randomly select 6 recipes
        recipes = random.sample(all_recipes, min(6, len(all_recipes)))
    else:
        recipes = []

    return render(request, "search_results.html", {'recipes': recipes})
