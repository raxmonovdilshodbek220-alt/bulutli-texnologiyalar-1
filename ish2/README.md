# 2-mustaqil ish: konteyner va avtomatik yetkazib berish

`app.py` — mahsulot narxi va miqdorini qabul qilib jami summani qaytaradigan Flask API. `Dockerfile` Python, kutubxonalar va ilova ishga tushirish buyrug‘ini bir xil tasvirga yig‘adi. `compose.yaml` lokal ishga tushirishni soddalashtiradi. `render.yaml` Render’da Docker servis yaratish uchun sozlama beradi.

GitHub Actions jarayoni image’ni quradi, konteynerni ishga tushiradi, `/health` va `/hisobla` javoblarini tekshiradi, so‘ng tasvirni GitHub Container Registry’ga yuboradi. Render `checksPass` rejimida sozlanganda, shu branch’dagi tekshiruvlar o‘tgach yangi versiyani joylashtiradi.

## Lokal ishga tushirish

```bash
cd ish2
docker compose up --build
```

Brauzerda `http://localhost:8080` ni oching. `/health` manzili xizmat holatini JSON’da qaytaradi. `/hisobla` manziliga JSON so‘rovi yuborilganda jami summa hisoblanadi.

## Muhitlar bir xilligini ta’minlash

Docker image ilovani ishga tushirish uchun kerakli Python versiyasi va kutubxonalarni o‘z ichiga oladi. Shu sababli dasturchi kompyuteri va bulutdagi Docker muhitida bir xil image ishlatiladi. Render bepul servislarida bo‘sh turganda servis vaqtincha to‘xtashi mumkin; bu o‘quv namunasiga mos, doimiy ishlab chiqarish tizimiga emas.

