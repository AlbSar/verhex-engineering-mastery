---
status: ready
day: 4
date: 2026-08-07
estimated_hours: 4.5
---

# Day 04 — Scope, Namespace, Function Object ve Closure

## Günün amacı

Python'da isim çözümleme zincirini, function object davranışını ve closure mekanizmasını deneylerle açıklamak.

## 1. Teori — 60 dakika

Kendi cümlelerinle açıkla:

- Namespace
- Scope
- LEGB
- Local ve global binding
- `global`
- `nonlocal`
- Function object
- Closure
- Free variable
- Late binding

## 2. LEGB deneyleri — 60 dakika

Aynı isim için local, enclosing, global ve built-in katmanlarını ayrı ayrı gözlemle.

Yapılacaklar:

- Global ismi localde shadow et.
- Enclosing scope değerini `nonlocal` ile değiştir.
- Built-in bir ismi gölgele ve riskini açıkla.
- `globals()` ve `locals()` çıktılarını kontrollü biçimde incele.

## 3. Closure laboratuvarı — 75 dakika

Aşağıdaki yapıları geliştir:

- State tutan sayaç closure
- Belirli eşik üzerinde uyarı üreten closure
- Konfigürasyon bağlayan validator factory

Her biri için closure içindeki serbest değişkenleri açıkla.

## 4. Late-binding debugging — 45 dakika

Loop içinde lambda/function üret ve tüm fonksiyonların neden son loop değerini döndürdüğünü göster.

Ardından iki farklı düzeltme uygula:

- Default argument ile binding
- Factory function ile yeni scope

Regression testlerini yaz.

## 5. İngilizce — 30 dakika

İngilizce 150 kelime:

> Explain how a closure retains access to variables from its enclosing scope.

Şu ifadeleri kullan:

- enclosing scope
- free variable
- evaluated later
- binding time
- retained state

## Teslimatlar

- [ ] LEGB deney dosyası
- [ ] Üç closure örneği
- [ ] Late-binding reproducer
- [ ] İki alternatif düzeltme
- [ ] Regression testleri
- [ ] İngilizce açıklama

## Geçiş kontrolü

`global` ile `nonlocal` arasındaki farkı kod örneği üzerinden açıklayabilmelisin.
