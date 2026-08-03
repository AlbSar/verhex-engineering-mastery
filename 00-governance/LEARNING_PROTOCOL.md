---
status: canonical
version: 1.0.0
updated_at: 2026-08-04
---

# Learning Protocol

## Amaç

Her konuyu kullanabilmenin ötesinde; mekanizmasını, sınırlarını, failure mode'larını, gözlemlenebilirliğini ve production etkisini anlamak.

## Yedi zorunlu soru

Her konu aşağıdaki sorularla işlenir:

1. Nedir?
2. Hangi problemi çözer?
3. Arkasında hangi mekanizma çalışır?
4. İşletim sistemi veya runtime seviyesinde ne olur?
5. Nasıl gözlemlenir?
6. Nasıl kontrol edilir?
7. Hangi koşullarda bozulur?

## Bir konunun tamamlanma kriteri

- Kendi cümleleriyle açıklama
- Sıfırdan küçük uygulama
- Bozuk örneği debug etme
- Unit veya integration test yazma
- Performans ve güvenlik risklerini açıklama
- Production kullanımını değerlendirme
- En az beş dakika İngilizce teknik anlatım

## AI kullanım kuralı

AI düşünmenin yerine geçmez. AI kodu kabul edilmeden önce davranışı tahmin edilir, abstraction'lar açıklanır, failure senaryoları çıkarılır, testleri yazılır ve en az bir bölümü yeniden uygulanır.
