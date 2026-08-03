# Debug Journal

Bu klasör önemli teknik hataların belirti–hipotez–kanıt–kök neden zinciriyle kaydedildiği kurumsal öğrenme alanıdır.

## Dosya adı

```text
YYYY-MM-DD-kisa-hata-basligi.md
```

## Yeni kayıt

`templates/DEBUG_ENTRY_TEMPLATE.md` dosyasını kopyala.

## Kayıt açma eşiği

Aşağıdaki durumlardan biri varsa debug journal kaydı açılır:

- Kök neden ilk bakışta açık değilse
- Aynı hata tekrar ediyorsa
- Production veya müşteri etkisi varsa
- Veri, güvenlik veya maliyet riski varsa
- Önemli bir zihinsel model hatası ortaya çıktıysa
- Regression testi gerektiriyorsa

## Temel kural

Çözüm olarak yalnızca değiştirilen kodu yazmak yeterli değildir. Mekanizma, kök neden ve önleyici kontrol açıklanmalıdır.
