---
status: ready
day: 3
date: 2026-08-06
estimated_hours: 4.5
---

# Day 03 — Mutability, Copy ve Parameter Passing

## Günün amacı

Mutable nesnelerde yan etkilerin nasıl oluştuğunu, shallow/deep copy farkını ve Python function argument davranışını deneylerle kanıtlamak.

## 1. Teori — 60 dakika

Kendi cümlelerinle açıkla:

- Mutable ve immutable
- In-place mutation
- Rebinding
- Shallow copy
- Deep copy
- Object sharing
- Function call sırasında argument binding

Şu ifadeyi değerlendir:

> Python is pass-by-reference.

Bu ifadenin neden eksik olduğunu ve “call by sharing” veya “object-reference passing” ifadelerinin neyi daha iyi açıkladığını yaz.

## 2. Copy laboratuvarı — 75 dakika

İç içe veri yapısı kullan:

```python
source = {
    "customer": {"id": 10, "tags": ["erp", "ai"]},
    "active": True,
}
```

Aşağıdakileri karşılaştır:

- Doğrudan assignment
- `dict.copy()`
- `copy.copy()`
- `copy.deepcopy()`

İç nesneleri değiştir; hangi katmanda paylaşım devam ediyor göster.

## 3. Mutable default argument debugging — 60 dakika

Hatalı örnek üret:

```python
def append_event(event, events=[]):
    events.append(event)
    return events
```

Yapılacaklar:

1. Beklenmeyen davranışı reproduce et.
2. Default değerin ne zaman değerlendirildiğini açıkla.
3. Güvenli tasarıma dönüştür.
4. Regression testi yaz.
5. Debug journal kaydı oluştur.

## 4. Function side-effect analizi — 45 dakika

İki fonksiyon yaz:

- Girdi listesini yerinde değiştiren sürüm
- Yeni liste üreten saflaştırılmış sürüm

Şu trade-off'ları değerlendir:

- Performans
- Okunabilirlik
- Tahmin edilebilirlik
- Büyük veri
- API contract

## 5. İngilizce — 30 dakika

İngilizce kısa incident açıklaması yaz:

> A shared mutable default argument caused data from previous requests to leak into later calls.

Şunları içersin:

- symptom
- root cause
- fix
- regression prevention

## Teslimatlar

- [ ] Copy deney dosyası
- [ ] Mutable default reproducer
- [ ] Düzeltme ve regression testi
- [ ] İlk debug journal kaydı
- [ ] Side-effect trade-off notu
- [ ] İngilizce incident özeti

## Geçiş kontrolü

Şu soruya net cevap ver:

> Bir tuple içinde liste varsa tuple tamamen immutable sayılır mı?
