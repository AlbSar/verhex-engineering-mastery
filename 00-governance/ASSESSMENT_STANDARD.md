---
status: canonical
version: 2.0.0
updated_at: 2026-09-07
---

# Assessment Standard

| Seviye | Kanıtla gösterilen yeterlilik |
|---:|---|
| 0 | Konuyu bilmiyor; yalnızca açık değerlendirme sonucu verilir |
| 1 | Terimleri tanıyor |
| 2 | Rehberlikle kullanıyor |
| 3 | Bağımsız uyguluyor ve açıklıyor |
| 4 | Debug, test, trade-off ve production etkisini açıklıyor |
| 5 | Tasarlıyor, optimize ediyor, öğretiyor ve işletiyor |

Her sayısal puan somut kanıt bağlantısı gerektirir. `null` değerlendirilmemiştir. Concept knowledge_state öğretim modunu seçer; sayıdan otomatik türetilmez. UNKNOWN ön bilgisi kurulmamıştır; otomatik 0 değildir. PROVEN bağımsız kullanım ve açıklama, MASTERED en az 4 puan ve debug/test/trade-off/production kanıtı gerektirir. Skill matrix'teki `target` uzun vadeli hedeftir, haftalık geçiş notu değildir.

## Baseline ile mastery ayrımı

Week 001 tanılama haftasıdır; her alanda 4/5 şartı yoktur. Yalnızca haftada öğretilen REQUIRED konular ve belgelenmiş ön bilgiler değerlendirilir. UNKNOWN kavram sınanmaz; önce öğretilir, kalan çalışma ertelenir. OPTIONAL, STRETCH ve REFERENCE geçişi engellemez. Eksik required kanıtla otomatik geçiş yoktur; tekrar veya hedefli reinforcement kararı gerekçelendirilir.

- `proceed`: REQUIRED kanıtlar mevcut, temel ilişkiyi bağımsız açıklayabiliyor; kritik prerequisite açığı yok.
- `proceed-with-reinforcement`: kanıtlar mevcut, rehberlik ihtiyacı veya sınırlı açık için sonraki hafta süreli telafi planı var; kritik konu eksikse ona bağımlı görev açılmaz.
- `repeat-critical-sections`: kritik required kanıt/ön koşul eksik; o bölüm öğretimle tekrar edilir.

Ağırlıklı not kararın yerine geçmez. Formül: sum(ağırlık × puan / 5), tüm değerlendirilen alanlar doluysa 0–100. Eksik alan varsa toplam `pending`; sıfırla doldurma. Faz 0 aynı Week 001 rubric'ini kullanır; ikinci bir sınav/puan tablosu yoktur.

## Kaynak ve sahiplik

Kanıt kaydı: konu, gerçek tarih, öğrenci/AI/reference kaynağı, yardım düzeyi, komut/kod/çıktı bağlantısı, açıklama, reviewer ve karar. Simülasyonlar kullanıcı kanıtı değildir. Doğru tahmin tek başına PROVEN değildir. AI tarafından yazılan tekrar notu kaynakça olabilir; bağımsız açıklama yerine geçmez. Sözlü/chat açıklaması kaynağıyla korunabilir, tekrar yazma bürokrasisi gerekmez.
