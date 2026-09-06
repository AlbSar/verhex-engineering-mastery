---
status: ready
day: 2
date: 2026-09-07
estimated_hours: 2.5
---

# Day 02 — Object, Identity, Equality ve Reference Semantics

## Günün amacı
Python'da isimlerin nesnelere nasıl bağlandığını; identity, equality ve aliasing farkını deneyle açıklamak.

Codex öğretmen ve reviewer'dır. Önce kullanıcı tahmin eder ve kodu yazar; Codex daha sonra mental model ve test boşluklarını inceler.

## 1. Teori — 35 dakika
Kendi cümlelerinle tanımla: object, name binding, identity, equality, type, aliasing.

Cevapla:
> `a = b` nesne kopyalar mı, yoksa yeni bir name binding mi oluşturur?

## 2. Çekirdek deneyler — 60 dakika
`object_identity.py` içinde en az üç deney yap:

1. Equal ama identical olmayan iki liste.
2. Aynı nesneye bağlanan iki isim ve mutation etkisi.
3. Immutable bir değerin rebinding sonrası identity davranışı.

Her deney için çalıştırmadan önce tahmin yaz; sonra sonucu ve farkın nedenini kaydet.

Not: interning veya CPython optimizasyonu görürsen bunu Python dil garantisi olarak genelleme.

## 3. Test — 35 dakika
En az 4 pytest testi yaz:
- equal / not identical
- same-object alias
- immutable rebinding
- custom `__eq__` veya mutable side effect

## 4. Teach-back ve log — 20 dakika
Kendi cümlelerinle şu cümleyi açıkla:
> Two names can refer to the same object; two different objects can still be equal.

Daily log'a yanlış tahminlerini ve düzeltilen zihinsel modeli ekle.

## Teslimatlar
- [ ] `object_identity.py`
- [ ] Tahmin/sonuç kaydı
- [ ] En az 4 test
- [ ] Teach-back notu
- [ ] Daily log

## Geçiş kontrolü
`is` ile `==` farkını implementation detail'e yaslanmadan açıklayabilmelisin.
