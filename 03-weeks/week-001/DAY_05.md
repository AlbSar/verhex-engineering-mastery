---
status: ready
day: 5
date: 2026-08-08
estimated_hours: 5
---

# Day 05 — Veri Yapıları ve Algoritmik Tanılama

## Günün amacı

Problemi doğru veri yapısıyla çözmek, çözüm karmaşıklığını açıklamak ve basit dependency graph üzerinde cycle tespit etmek.

## 1. Veri yapısı seçimi — 60 dakika

Aşağıdaki yapıların temel kullanımını ve maliyetlerini karşılaştır:

- list
- tuple
- dict
- set
- deque
- heap

Her biri için:

- Erişim
- Ekleme
- Silme
- Membership kontrolü
- Sıra garantisi
- Hash gereksinimi
- Production kullanım örneği

## 2. Duplicate customer analyzer — 75 dakika

Bir kayıt listesinde tekrar eden `customer_id` değerlerini, tekrar sayılarını ve kaynak satırlarını döndüren typed bir çözüm yaz.

Gereksinimler:

- Boş input
- Eksik `customer_id`
- `None` değer
- Farklı tipte kimlik
- Büyük veri için memory değerlendirmesi
- Deterministic output

Testler:

- Normal durum
- Duplicate yok
- Birden fazla duplicate
- Bozuk kayıt
- Büyük sentetik input

## 3. Dependency scheduler — 90 dakika

Bir görev-bağımlılık sözlüğünden çalışma sırası üret.

Örnek:

```python
dependencies = {
    "deploy": ["test", "build"],
    "test": ["build"],
    "build": [],
}
```

Gereksinimler:

- Kahn algoritması
- In-degree tablosu
- Deterministic queue sırası
- Bilinmeyen dependency doğrulaması
- Cycle detection
- Custom `DependencyCycleError`

Açıkla:

- Neden queue kullanılıyor?
- Cycle nasıl tespit ediliyor?
- Zaman ve alan karmaşıklığı nedir?
- Graph çok büyürse hangi gözlem metrikleri gerekir?

## 4. Benchmark — 30 dakika

Küçük, orta ve büyük sentetik graph üret. Süreyi ölç ancak tek koşumu kesin performans sonucu gibi yorumlama.

Kaydet:

- Input boyutu
- Node/edge sayısı
- Süre
- Bellek için yaklaşık değerlendirme

## 5. İngilizce — 30 dakika

Beş dakikalık İngilizce anlatım taslağı:

> Why data-structure selection changes the performance and clarity of a solution.

## Teslimatlar

- [ ] Veri yapısı karşılaştırma tablosu
- [ ] Duplicate analyzer
- [ ] Dependency scheduler
- [ ] Cycle regression testi
- [ ] Karmaşıklık analizi
- [ ] Benchmark notu
- [ ] İngilizce anlatım taslağı

## Geçiş kontrolü

Dictionary membership ile list membership arasındaki ortalama karmaşıklık farkını ve bunun hangi varsayımlara dayandığını açıklayabilmelisin.
