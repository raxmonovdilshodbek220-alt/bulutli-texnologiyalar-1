# Bulutli texnologiyalar bo‘yicha uchta mustaqil ish

Ushbu loyihada topshiriq varag‘idagi uch mavzu bitta izchil misolda yoritiladi. Birinchi ishda lokal sahifa GitHub Pages’da joylashtiriladi. Ikkinchisida Flask ilovasi Docker konteynerga qadoqlanib, GitHub Actions orqali tekshiriladi va Render’ga yetkazishga tayyorlanadi. Uchinchisida hisob-kitob vazifasi Vercel Serverless Python funksiyasiga ajratiladi.

## 1-mustaqil ish. Lokal dasturni bulutga ko‘chirish

### Nazariy qism
Bulutli xizmatlar hisoblash resurslarini internet orqali talabga qarab taqdim etadi. IaaS’da foydalanuvchi virtual server va operatsion tizimni ko‘proq boshqaradi; PaaS’da provayder dastur ishga tushadigan platformani yuritadi; SaaS’da foydalanuvchi internet orqali tayyor dasturdan foydalanadi. Lokal serverda apparat va dastur muhitini tashkilotning o‘zi boshqarsa, bulutda ayrim vazifalar xizmat ko‘rsatuvchi tomonga o‘tadi.

| Model | Mas’uliyat taqsimoti | Mos foydalanish holati |
|---|---|---|
| IaaS | Foydalanuvchi operatsion tizim, runtime va ilovani boshqaradi | Server sozlamalari ustidan nazorat kerak bo‘lsa |
| PaaS | Provayder platformani, foydalanuvchi ilovani boshqaradi | Kodni tez joylashtirish muhim bo‘lsa |
| SaaS | Provayder tayyor dasturni taqdim etadi | Tayyor dasturiy xizmat kerak bo‘lsa |

### Amaliy qism
`index.html` sahifasi HTML, CSS va JavaScript’dan tuzilgan. JavaScript `window.location.hostname` orqali sahifa qayerda ochilganini aniqlab, lokal yoki bulutli muhit belgisini chiqaradi. GitHub Pages sozlamasida `main` branch va asosiy papka (`/(root)`) tanlandi.

**Ishlayotgan sahifa:** https://raxmonovdilshodbek220-alt.github.io/bulutli-texnologiyalar-1/

Bu loyiha statik saytdir. GitHub Pages HTML, CSS va JavaScript fayllarini joylaydi, lekin Python kabi server tomonida ishlaydigan kodni bajarmaydi. Shu sababli ushbu amaliy misolda backend server ishlatilmagan.

## 2-mustaqil ish. Bir xil muhit va avtomatik yetkazib berish

### Nazariy qism
Bir xil kod turli kompyuterlarda turlicha ishlashiga Python versiyasi, kutubxona versiyasi yoki tizim sozlamalari ta’sir qilishi mumkin. Docker ilova va kerakli kutubxonalarni konteyner tasviriga yig‘adi. Virtual mashinada alohida operatsion tizim ishlaydi; konteyner esa asosiy tizim yadrosidan foydalanadi va odatda yengilroq bo‘ladi.

CI/CD — koddagi o‘zgarishlarni avtomatik yig‘ish, tekshirish va joylashtirish jarayoni. CI bosqichida konteyner tasviri yaratiladi va xizmatning javobi tekshiriladi. CD bosqichida muvaffaqiyatli o‘zgarish bulut muhitiga yetkaziladi.

### Amaliy qism
`ish2/` papkasida Flask API, Dockerfile va Compose sozlamasi mavjud. API narx va miqdorni olib, jami summani hisoblaydi. GitHub Actions workflow mos commit kelganda konteyner tasvirini quradi, ishga tushiradi va `/health` hamda hisoblash javobini tekshiradi. Muvaffaqiyatli workflow tasvirni GitHub Container Registry’ga yuboradi. `render.yaml` Render’da Docker servis yaratish va CI tekshiruvlaridan so‘ng deploy qilish uchun sozlangan.

```bash
cd ish2
docker compose up --build
```

### Kod izohi
`Dockerfile` Python muhiti, kutubxonalar va ishga tushirish buyrug‘ini image’ga kiritadi. `compose.yaml` ilovani lokal kompyuterda bir buyruq bilan ishga tushiradi. GitHub Actions workflow esa image’ni qurib, `/health` va `/hisobla` manzillarini tekshiradi. Render Dockerfile asosida shu ilovani internetga chiqarishi mumkin.

## 3-mustaqil ish. Monolitni serverless xizmat bilan modernizatsiya qilish

### Nazariy qism
Monolit ilovada asosiy qismlar bitta dastur tarkibida ishlaydi. Ayrim vazifalarni alohida xizmatga chiqarish ularni mustaqil yangilash va masshtablash imkonini beradi, biroq tarmoq aloqasi, kuzatuv va xatolarni boshqarishni murakkablashtiradi. Serverless funksiyaning infratuzilmasini provayder boshqaradi; funksiya odatda HTTP so‘rovi yoki boshqa hodisa kelganda ishga tushadi.

### Amaliy qism
`ish3/index.html` summa kiritish uchun veb-sahifa. `ish3/api/calculate.py` mustaqil Python funksiyasi so‘rovni tekshiradi, o‘quv uchun belgilangan 12 foizlik qiymatni hisoblaydi va JSON javob qaytaradi. Vercel’da loyihani joylashtirishda root papka sifatida `ish3` tanlanadi; GitHub bilan ulansa, yangi commitlar avtomatik deploy qilinadi.

**Eslatma:** 12 foiz ushbu namunaning hisoblash uchun tanlangan qiymatidir. Bu amaldagi soliq bo‘yicha huquqiy yoki moliyaviy tavsiya emas.

## Xulosa
Uchta ish orqali lokal joylashtirish, konteyner yordamida muhitni bir xil qilish, avtomatik build va serverless funksiyaning vazifasi ko‘rib chiqildi. Birinchi loyiha GitHub Pages’da ishlayapti. Ikkinchi va uchinchi loyihalarning alohida hosting xizmatlarida ishga tushirilgan holati yakuniy hisobotda mavjud bo‘lsa, ularning manzillari bilan ko‘rsatiladi.

## Foydalanilgan manbalar
1. NIST SP 800-145, *The NIST Definition of Cloud Computing*: https://csrc.nist.gov/pubs/sp/800/145/final
2. GitHub Pages, *What is GitHub Pages?*: https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages
3. Docker Docs, *Use Compose in production*: https://docs.docker.com/compose/how-tos/production/
4. GitHub Docs, *Deploying your website automatically*: https://docs.github.com/en/get-started/start-your-journey/deploying-your-website-automatically
5. Render, *Blueprint YAML Reference*: https://render.com/docs/blueprint-spec
6. Vercel, *Python Runtime*: https://vercel.com/docs/functions/runtimes/python

