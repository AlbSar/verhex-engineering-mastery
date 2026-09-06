---
status: ready
day: 3
date: 2026-09-08
estimated_hours: 2.5
---

# Day 03 — Mutability, Copy ve Parameter Passing

## Günün amacı
Mutable nesnelerde yan etkileri, shallow/deep copy farkını ve Python function argument davranışını deneyle kanıtlamak.

## 1. Teori — 30 dakika
Kendi cümlelerinle açıkla: mutable/immutable, mutation vs rebinding, shallow copy, deep copy, object sharing ve argument binding.

Şunu değerlendir:
> “Python is pass-by-reference.”

Neden eksik olduğunu yaz.

## 2. Copy laboratuvarı — 45 dakika
İç içe bir dict/list yapısında şu dört yaklaşımı karşılaştır:
- direct assignment
- `dict.copy()` veya `copy.copy()`
- `copy.deepcopy()`

En az bir nested mutation ile hangi referansların paylaşıldığını göster.

## 3. Mutable default debugging — 45 dakika
Hatalı mutable default argument örneği üret.

Yap:
1. reproducer
2. root cause açıklaması
3. güvenli düzeltme
4. regression test
5. debug journal kaydı

## 4. Side-effect karşılaştırması — 20 dakika
Bir input'u yerinde değiştiren fonksiyon ile yeni değer döndüren sürümü karşılaştır. Okunabilirlik, performans ve API contract açısından kısa trade-off yaz.

## 5. Teach-back ve log — 10 dakika
Şu soruya cevap ver:
> Bir tuple içinde mutable nesne varsa tuple'ın immutability özelliği tam olarak neyi garanti eder?

## Teslimatlar
- [ ] Copy deneyi
- [ ] Mutable default reproducer + fix
- [ ] Regression testi
- [ ] Debug journal
- [ ] Side-effect trade-off notu
- [ ] Daily log
