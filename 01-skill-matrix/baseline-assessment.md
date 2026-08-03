---
status: active
assessment_date: 2026-08-04
assessor: ChatGPT + self-assessment
scoring_scale: 0-5
---

# Baseline Assessment

## Kullanım talimatı

Bu dosya tanılama sonuçlarının kanonik özetidir. Her puanın yanında gözlemlenebilir bir kanıt bulunmalıdır. Yalnızca öznel güven hissine dayanarak puan verilmez.

Her bölüm için:

1. AI yardımı olmadan ilk denemeyi yap.
2. Süreyi kaydet.
3. Kendi açıklamanı yaz.
4. Kod, test, terminal çıktısı veya ses kaydı bağlantısı ekle.
5. Son olarak 0–5 puan ver.

## Puan özeti

| Alan | Puan | Hedef | Kanıt durumu |
|---|---:|---:|---|
| Python çalışma modeli | — | 4 | Bekleniyor |
| Python kodlama | — | 4 | Bekleniyor |
| Test ve debugging | — | 4 | Bekleniyor |
| Algoritmik düşünme | — | 4 | Bekleniyor |
| Git | — | 4 | Bekleniyor |
| Linux | — | 4 | Bekleniyor |
| Network | — | 4 | Bekleniyor |
| Docker | — | 4 | Bekleniyor |
| Sistem tasarımı | — | 4 | Bekleniyor |
| Teknik İngilizce | — | C1 / seviye 4 | Bekleniyor |

# 1. Python

## 1.1 Kavramsal sorular

Kendi cümlelerinle cevapla:

1. Python'da değişken nedir; nesnenin kendisi midir, bir isim bağlaması mıdır?
2. `is` ile `==` arasındaki fark nedir?
3. Mutable bir nesnenin iki farklı isim üzerinden değiştirilmesi neden yan etki üretir?
4. Tuple her durumda tamamen immutable mıdır?
5. Function argument passing için “pass by reference” demek neden eksik veya yanıltıcı olabilir?
6. Local, enclosing, global ve built-in scope nasıl aranır?
7. Shallow copy ile deep copy arasındaki operasyonel fark nedir?
8. Hashable olmak ne anlama gelir ve dictionary key tasarımını nasıl etkiler?

## 1.2 Kodlama görevleri

- `normalize_customer_record(record)` fonksiyonunu type hint ve testlerle yaz.
- İç içe mutable veri üzerinde shallow/deep copy deneyini hazırla.
- Closure kullanan bir sayaç üret.
- Hatalı default mutable argument örneğini üret, açıkla ve düzelt.
- Custom exception hierarchy içeren küçük bir validation akışı yaz.

## 1.3 Debugging görevi

Aşağıdaki davranışı açıklayan minimum reproducer üret:

- Bir fonksiyona gönderilen liste beklenmedik biçimde değişiyor.
- İki “aynı görünen” nesnede `is` sonucu farklı.
- Bir loop içinde oluşturulan closure'ların tamamı aynı değeri döndürüyor.

## 1.4 Test kanıtı

- En az 5 unit test
- En az 2 edge case
- En az 1 beklenen exception testi

### Sonuç

- Puan:
- Süre:
- Kanıt bağlantıları:
- Yanlış varsayımlarım:
- Tekrar edilmesi gereken konular:

# 2. Algoritmik düşünme

## Görev A — Tekrarlı kayıt analizi

Bir müşteri kayıt listesinde tekrar eden `customer_id` değerlerini ve tekrar sayılarını döndüren bir çözüm yaz.

Açıkla:

- Neden seçtiğin veri yapısını kullandın?
- Zaman ve alan karmaşıklığı nedir?
- Veri çok büyürse ne değişir?

## Görev B — Dependency sıralaması

Basit bir görev-bağımlılık sözlüğü için geçerli çalışma sırası üret. Cycle varsa özel hata döndür.

Açıkla:

- In-degree nedir?
- Queue neden kullanılır?
- Cycle nasıl tespit edilir?

### Sonuç

- Puan:
- Süre:
- Kanıt bağlantıları:
- Edge case listesi:

# 3. Git

## Uygulama

- Repository'yi klonla.
- `learning/week-001` branch'i oluştur.
- Bir günlük log ekle.
- Anlamlı bir commit mesajı yaz.
- `git diff`, `git log --oneline`, `git status` çıktılarını yorumla.

## Kavramsal sorular

- Working tree, staging area ve commit arasındaki fark nedir?
- `revert`, `reset` ve `restore` hangi durumlarda kullanılır?
- Rebase hangi riski taşır?

### Sonuç

- Puan:
- Kanıt bağlantıları:

# 4. Linux

## Uygulama

- Çalışan shell'in PID bilgisini bul.
- Bir process başlat, gözlemle ve signal ile sonlandır.
- Pipe ve redirect farkını deneyle göster.
- Bir dosyanın permission bitlerini açıkla.
- `/proc/<pid>` altında en az üç kaynağı incele.

### Sonuç

- Puan:
- Komutlar:
- Gözlemler:
- Kanıt bağlantıları:

# 5. Network

## Uygulama

- `localhost`, `127.0.0.1` ve host IP arasındaki farkı açıkla.
- Dinleyen portları görüntüle.
- DNS çözümleme zincirini özetle.
- Basit bir TCP bağlantısını gözlemle.

### Sonuç

- Puan:
- Komutlar:
- Gözlemler:

# 6. Docker

## Uygulama

- Bir container çalıştır ve ana process'i bul.
- Container'ı `SIGTERM` ile durdur.
- Bind mount ile volume farkını deneyle göster.
- Container içindeki `localhost` davranışını açıkla.
- Memory limiti verilen bir container'ın sınırı aşması hâlinde ne olacağını tahmin et ve gözlemle.

### Sonuç

- Puan:
- Komutlar:
- Gözlemler:
- Failure mode açıklaması:

# 7. Debugging

Bir hata seç ve aşağıdaki formatla çöz:

- Belirti:
- Beklenen davranış:
- Minimum reproducer:
- İlk hipotezler:
- Toplanan kanıt:
- Kök neden:
- Düzeltme:
- Regression test:
- Önleyici aksiyon:

### Sonuç

- Puan:
- Debug journal bağlantısı:

# 8. Sistem tasarımı

## Senaryo

Müşteri ortamında çalışan, IFS/Oracle verisine kontrollü erişen ve cloud LLM çağrısı yapan bir AI integration node tasarla.

En az şu bileşenleri göster:

- API veya listener
- Authentication ve authorization
- Connector katmanı
- Tool execution
- Audit log
- Queue veya worker
- Model gateway
- Secret yönetimi
- Retry ve idempotency
- Monitoring

Açıkla:

- Trust boundary nerede?
- Hangi işlemler human approval gerektirir?
- En kritik üç failure mode nedir?
- Ana ERP sunucusundan neden ayrıştırılmalı veya hangi koşulda ayrıştırılmamalı?

### Sonuç

- Puan:
- Diyagram bağlantısı:
- Karar notları:

# 9. Teknik İngilizce

## Writing

300–500 kelime:

> Introduce your current engineering background, Verhex's technical focus, the systems you can already build, and the capabilities you want to develop during this program.

## Speaking

5 dakika:

> Explain the difference between using a framework and understanding the mechanism behind it.

## Reading

Seçilen resmî Python dokümanından kısa bir bölümü oku ve şu çıktıları üret:

- 150 kelimelik İngilizce özet
- 10 teknik ifade
- Anlamadığın 3 cümle
- Türkçe teknik açıklama

### Sonuç

- Reading puanı:
- Writing puanı:
- Speaking puanı:
- Vocabulary puanı:
- Kanıt bağlantıları:

# 10. Nihai değerlendirme

## Güçlü alanlar

- 

## Öncelikli gelişim alanları

- 

## Yanlış veya eksik zihinsel modeller

- 

## Week 002 için kalibrasyon kararları

- 

## Genel başlangıç seviyesi

- Teknik seviye:
- İngilizce seviyesi:
- Program riski:
- Önerilen tempo:
