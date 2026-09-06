---
status: ready
day: 5
date: 2026-09-10
estimated_hours: 3
---

# Day 05 — Veri Yapıları ve Algoritmik Tanılama

## Günün amacı
Problemi doğru veri yapısıyla çözmek, karmaşıklığı açıklamak ve küçük bir dependency graph üzerinde cycle tespit etmek.

## 1. Veri yapısı seçimi — 35 dakika
List, tuple, dict, set ve deque için şu soruları cevapla:
- temel kullanım
- membership maliyeti
- sıra davranışı
- hash gereksinimi
- bir production örneği

Heap bu hafta yalnızca kavramsal not seviyesindedir; zorunlu implementasyon yoktur.

## 2. Duplicate customer analyzer — 55 dakika
Typed bir çözüm yaz. Şunları ele al:
- boş input
- eksik `customer_id`
- duplicate yok / birden fazla duplicate
- deterministic output
- büyük veri için memory değerlendirmesi

En az 4 test yaz.

## 3. Dependency scheduler — 70 dakika
Kahn algoritmasıyla küçük görev-bağımlılık grafiği için çalışma sırası üret.

Zorunlu özellikler:
- in-degree
- deterministic queue order
- unknown dependency validation
- cycle detection
- özel cycle hatası

Açıkla:
- queue neden var?
- cycle nasıl anlaşılır?
- zaman/alan karmaşıklığı nedir?

## 4. Kısa ölçüm ve teach-back — 20 dakika
Küçük ve daha büyük iki sentetik input üzerinde süreyi gözlemle. Benchmark sonucu diye genelleme yapma; yalnızca gözlem kaydı tut.

Şunu açıkla:
> Veri yapısı seçimi neden hem performansı hem kodun açıklanabilirliğini değiştirir?

## Teslimatlar
- [ ] Veri yapısı karşılaştırma notu
- [ ] Duplicate analyzer
- [ ] En az 4 test
- [ ] Dependency scheduler
- [ ] Cycle testi
- [ ] Karmaşıklık açıklaması
- [ ] Daily log
