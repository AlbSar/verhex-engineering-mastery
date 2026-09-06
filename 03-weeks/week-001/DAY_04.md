---
status: ready
day: 4
date: 2026-09-09
estimated_hours: 2.5
---

# Day 04 — Scope, Namespace, Function Object ve Closure

## Günün amacı
Python'da isim çözümleme zincirini, function object davranışını ve closure mekanizmasını deneyle açıklamak.

## 1. Teori — 30 dakika
Kendi cümlelerinle açıkla: namespace, scope, LEGB, `global`, `nonlocal`, closure, free variable ve late binding.

## 2. LEGB deneyleri — 40 dakika
En az üç kontrollü deney yap:
- local shadowing
- `nonlocal` ile enclosing binding değişikliği
- built-in shadowing riski

`globals()` ve `locals()` çıktısını yalnızca gözlem amacıyla incele.

## 3. Closure laboratuvarı — 45 dakika
İki örnek yaz:
- state tutan sayaç closure
- konfigürasyon bağlayan validator factory

Serbest değişkenlerin nereden çözümlendiğini açıkla.

## 4. Late-binding debugging — 25 dakika
Loop içinde fonksiyon/lambda üret; beklenmeyen sonucu reproduce et. Factory function veya açık binding yaklaşımıyla düzelt ve regression testi yaz.

## 5. Teach-back ve log — 10 dakika
`global` ile `nonlocal` farkını bir kod örneği üzerinden açıkla ve daily log'a ekle.

## Teslimatlar
- [ ] LEGB deneyleri
- [ ] İki closure örneği
- [ ] Late-binding reproducer + fix
- [ ] Regression testi
- [ ] Teach-back notu
- [ ] Daily log
