# bulutli-texnologiyalar-1
Lokal dasturni bulutga joylaştiriş böyiça mustaqil iş
# Bulutli texnologiyalar bo‘yicha mustaqil ish

## 1-mustaqil ish

### Mavzu
An’anaviy lokal muhitda ishlayotgan dasturni bulutli infratuzilmaga joylashtirish va xizmat modellarini taqqoslash

### Ishning maqsadi
Ushbu ishning maqsadi lokal kompyuterda ishlaydigan dasturni bulutga ko‘chirishni o‘rganish va bulutli xizmatlarning IaaS, PaaS hamda SaaS modellarini taqqoslashdan iborat.

### Bulutli texnologiya haqida
Bulutli texnologiya internet orqali server, ma’lumot saqlash joyi, tarmoq va dasturiy xizmatlardan foydalanish imkonini beradi. Bunda foydalanuvchi serverni o‘zi sotib olishi shart emas. U kerakli hisoblash resurslarini bulut xizmati orqali tanlab, masofadan foydalanishi mumkin.

Lokal muhitda dastur odatda bitta kompyuterda yoki tashkilotning ichki serverida ishlaydi. Bunday holatda qurilmaning ishlashi, saqlash joyi va elektr ta’minoti muhim hisoblanadi. Dastur bulutga ko‘chirilganda esa unga internet orqali murojaat qilish, zarurat tug‘ilganda resurslarni oshirish yoki kamaytirish mumkin.

### Bulutli xizmat modellari

**IaaS (Infrastructure as a Service)** — infratuzilmani xizmat sifatida taqdim etish modeli. Foydalanuvchi virtual server, saqlash joyi va tarmoqdan foydalanadi. Operatsion tizimni sozlash, dasturiy muhitni tayyorlash va ilovani boshqarish ko‘pincha foydalanuvchining zimmasida bo‘ladi. Bu model infratuzilmani ko‘proq nazorat qilish kerak bo‘lganda qulay.

**PaaS (Platform as a Service)** — dastur yaratish va ishga tushirish uchun tayyor platformani taqdim etish modeli. Server va operatsion tizimni boshqarish ishlarining katta qismini xizmat ko‘rsatuvchi tomon bajaradi. Dasturchi asosan dastur kodi va uning sozlamalariga e’tibor qaratadi.

**SaaS (Software as a Service)** — internet orqali foydalaniladigan tayyor dasturiy xizmat modeli. Foydalanuvchi server yoki dasturni o‘zi o‘rnatib boshqarmaydi. U odatda brauzer yoki maxsus dastur orqali xizmatdan foydalanadi. Elektron pochta va onlayn hujjat xizmatlari bunga misol bo‘ladi.

| Model | Boshqaruv taqsimoti | Misol |
|---|---|---|
| IaaS | Foydalanuvchi virtual server va undagi dasturiy muhitni boshqaradi | Bulutdagi virtual mashina |
| PaaS | Provayder platformani, foydalanuvchi esa dastur va kodni boshqaradi | Ilovani joylashtirish platformasi |
| SaaS | Provayder tayyor dasturni boshqaradi, foydalanuvchi undan foydalanadi | Onlayn pochta xizmati |

### Modellarning farqi
IaaS foydalanuvchiga ko‘proq sozlash va nazorat imkonini beradi, lekin server hamda operatsion tizimni boshqarish uchun qo‘shimcha bilim talab etadi. PaaS dastur ishlab chiqish va ishga tushirishni yengillashtiradi, biroq foydalanuvchi tanlangan platformaning imkoniyatlariga moslashishi kerak. SaaS’dan foydalanish oson, ammo foydalanuvchi xizmatning ichki infratuzilmasini boshqara olmaydi.

Mavjud dasturni bulutga ko‘chirishda IaaS yoki PaaS modellari ko‘proq mos kelishi mumkin. SaaS esa, odatda, o‘zimiz yaratgan dasturni joylashtirish uchun emas, balki tayyor dasturiy xizmatdan foydalanish uchun tanlanadi.

### Bulutga ko‘chirishda e’tibor beriladigan jihatlar
Dasturni ko‘chirishdan avval uning qanday resurslardan foydalanishi va ma’lumotlarni qayerda saqlashi aniqlanadi. Shundan so‘ng mos bulut xizmati tanlanib, dastur sozlanadi va internet orqali ishlashi tekshiriladi. Maxfiy ma’lumotlarni dastur kodiga yozmaslik, kirishni zarur ruxsatlar bilan cheklash va ma’lumotlarning zaxira nusxalarini saqlash kerak.

### Xulosa
Ushbu nazariy qismda bulutli texnologiyaning mazmuni hamda IaaS, PaaS va SaaS xizmat modellari ko‘rib chiqildi. Ularning asosiy farqi server, platforma va tayyor dasturiy ta’minotni foydalanuvchi hamda xizmat ko‘rsatuvchi tomon qanday boshqarishidadir. Keyingi amaliy qismda lokal muhitda ishlaydigan namunaviy dasturni bulutga joylashtirish usuli ko‘rib chiqiladi.

### Foydalanilgan manba
NIST, *The NIST Definition of Cloud Computing, SP 800-145*: https://csrc.nist.gov/pubs/sp/800/145/final
## Amaliy qism

### Loyiha tavsifi
Amaliy ishda lokal muhitda ham, bulutda ham ochiladigan `index.html` sahifasi yaratildi. Sahifaning tuzilishi HTML’da, ko‘rinishi CSS’da, ishlayotgan muhitийг ялгах хэсэг нь JavaScript дээр хийгдсэн.

### Lokal muhitda tekshirish
Sahifani lokal шалгахын тулд `index.html` файлыг компьютерт татаж авч, браузераар нээнэ. Сайт локал файл хэлбэрээр нээгдэхэд **“Lokal muhit”** гэсэн тэмдэглэгээ гарах ёстой. JavaScript нь `window.location.hostname` утгыг шалгаж, `localhost`, `127.0.0.1` эсвэл хоосон host байвал локал гэж үзнэ.

### Bulutga joylashtirish
`index.html` fayli GitHub repository’ning asosiy papkasiga joylandi. **Settings → Pages** bo‘limida `main` branch va `/(root)` papkasi tanlandi. GitHub Pages faylni joylab, saytni internet orqali ochiladigan qildi.

### Olingan natija
Sayt quyidagi manzilda ishlamoqda:

https://raxmonovdilshodbek220-alt.github.io/bulutli-texnologiyalar-1/

Sayt ochilganda **“Bulutli muhit”** belgisi, GitHub domeni va HTTPS ulanishi ko‘rinadi. JavaScript domen nomini aniqlab, joriy muhit haqidagi ma’lumotni sahifaga chiqaradi.

### Cheklov
Ushbu loyiha HTML, CSS va JavaScript’dan tuzilgan statik saytdir. GitHub Pages bunday sahifalarni joylashtiradi, ammo Python yoki boshqa server tomonida ishlaydigan dasturni ishga tushirmaydi. Shu sababli ushbu amaliy misolda backend server ishlatilmagan.

### Amaliy qism bo‘yicha xulosa
Amaliy ish davomida sahifa GitHub Pages’ga joylashtirildi va uning bulut domeni orqali ochilishi tekshirildi. Natijada lokal fayl хэлбэрээр болон үүлэн хостинг дээр нээхэд орчны мэдээллийг ялгаж харуулах боломжтой боллоо.
