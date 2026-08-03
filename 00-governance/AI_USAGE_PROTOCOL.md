---
status: canonical
version: 1.0.0
updated_at: 2026-08-04
---

# AI Usage Protocol

## Kod üretmeden önce

- Problem tanımlanır.
- Girdi ve çıktı belirlenir.
- Invariant ve failure senaryoları çıkarılır.
- Tasarım kararı kullanıcı tarafından verilir.

## AI kodu üretildikten sonra

1. Çalıştırmadan önce davranışı tahmin et.
2. Her fonksiyonun sorumluluğunu açıkla.
3. Kullanılan abstraction'ları belirle.
4. Edge-case ve failure senaryoları üret.
5. Testleri yaz.
6. Debugger ile yürüt.
7. En az bir bölümü yeniden yaz.
8. Alternatif tasarımı değerlendir.
9. Production risklerini kaydet.

## Kabul edilmeyen davranışlar

- Anlamadan kopyalama
- Test etmeden kabul etme
- Framework davranışını sorgulamama
- Hata mesajını körlemesine modele devretme
- Mimari kararı bütünüyle modele bırakma
