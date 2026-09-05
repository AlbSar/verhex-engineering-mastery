---
status: ready
day: 2
date: 2026-09-07
estimated_hours: 4.5
---

# Day 02 — Object, Identity, Equality ve Reference Semantics

## Günün amacı

Python'da değişkenlerin nesneleri “saklamadığını”, isimlerin nesnelere bağlandığını deneylerle göstermek.

## 1. Teori — 60 dakika

Kendi cümlelerinle tanımla:

- Object
- Name binding
- Identity
- Equality
- Type
- Reference semantics
- Aliasing
- Garbage collection

Aşağıdaki soruya yazılı cevap ver:

> `a = b` ifadesi nesne kopyalar mı, yoksa isim bağlaması mı oluşturur?

## 2. Deney seti — 90 dakika

`object_identity.py` dosyasında en az şu deneyleri yap:

### Deney A — Identity ve equality

```python
a = [1, 2]
b = [1, 2]
c = a
```

Her çift için `==`, `is` ve `id()` sonuçlarını tahmin et; sonra çalıştır.

### Deney B — Immutable yeniden bağlama

Integer ve string üzerinde değişiklik sonrası `id()` davranışını gözlemle.

### Deney C — Aliasing

Aynı listeyi iki isim üzerinden değiştir ve yan etkiyi açıkla.

### Deney D — Küçük integer/string interning

Sonuçları genellemeden gözlemle. CPython optimizasyonunu dil garantisi gibi yorumlama.

### Deney E — Nesne yaşam döngüsü

`sys.getrefcount()` kullanarak referans sayımı hakkında kontrollü gözlem yap; fonksiyonun kendi geçici referans etkisini not et.

## 3. Tahmin tablosu — 30 dakika

Her deney için:

| Deney | Çalıştırmadan önce tahmin | Gerçek sonuç | Farkın nedeni |
|---|---|---|---|

En az iki yanlış tahmin bulmak hedeflenir. Yanlış tahmin başarısızlık değil, görünür hâle gelen zihinsel modeldir.

## 4. Test — 45 dakika

En az 5 pytest testi yaz:

- Equal ama identical olmayan iki liste
- Aynı nesneyi gösteren iki isim
- Immutable yeniden bağlama
- Mutable yan etki
- Custom sınıfta `__eq__` davranışı

## 5. İngilizce — 30 dakika

İngilizce 150–200 kelime:

> Explain the difference between identity and equality in Python.

Şu ifadeleri kullan:

- refers to
- evaluates to
- object identity
- semantic equality
- implementation detail

## Teslimatlar

- [ ] `object_identity.py`
- [ ] Tahmin/sonuç tablosu
- [ ] En az 5 test
- [ ] İngilizce açıklama
- [ ] Daily log

## Geçiş kontrolü

Aşağıdaki cümleyi hatasız açıklayabilmelisin:

> Two names can refer to the same object; two different objects can still be equal.
