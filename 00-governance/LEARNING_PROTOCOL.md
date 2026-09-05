---
status: canonical
version: 2.0.0
updated_at: 2026-09-05
---

# Learning Protocol

## Amaç

Her konuyu yalnızca kullanabilmek değil; mekanizmasını, sınırlarını, failure mode'larını, runtime/OS etkisini, gözlemlenebilirliğini, performans/güvenlik sonuçlarını ve production trade-off'larını anlayabilmek.

## Zorunlu öğrenme döngüsü

Her konu mümkün olduğunca şu sırayla işlenir:

1. **Explain** — Nedir, hangi problemi çözer?
2. **Predict** — Çalıştırmadan önce davranışı tahmin et.
3. **Build** — Küçük ve kritik kısmı kendin uygula.
4. **Observe** — Terminal, profiler, logs, tracing veya sistem araçlarıyla gerçekten ne olduğunu gör.
5. **Break** — Hata, edge case, timeout, concurrency veya resource failure üret.
6. **Debug** — Symptom → evidence → hypothesis → root cause zincirini kaydet.
7. **Test** — Davranışı otomatik testlerle sabitle.
8. **Compare** — Eğitim implementasyonu ile production çözümünü karşılaştır.
9. **Transfer** — Gerçek projede nerede kullanıldığını ilişkilendir.
10. **Teach Back** — Kendi cümlelerinle mekanizmayı yeniden anlat.

## On zorunlu soru

1. Nedir?
2. Hangi problemi çözer?
3. Arkasında hangi mekanizma çalışır?
4. Runtime veya işletim sistemi seviyesinde ne olur?
5. Veri/state nerede tutulur?
6. Nasıl gözlemlenir ve ölçülür?
7. Nasıl kontrol edilir?
8. Hangi failure mode'ları vardır?
9. Hangi security/performance trade-off'ları vardır?
10. Production'da ne zaman kullanılmalı veya kullanılmamalıdır?

## Bir konunun tamamlanma kriteri

Bir konu `mastered` sayılmadan önce mümkün olan bağlama göre aşağıdakilerin çoğu kanıtlanmalıdır:

- Kendi cümleleriyle teknik açıklama
- Framework'süz veya düşük abstraction'lı küçük uygulama/deney
- En az bir bozuk senaryoyu debug etme
- Unit/integration veya uygun başka otomatik test
- Terminal/runtime/OS gözlemi
- Performance veya resource davranışı hakkında evidence
- Security/failure risklerini açıklama
- Production kullanımını ve alternatiflerini değerlendirme
- Gerçek proje bağlantısı veya architecture case
- Gerekli haftalarda kısa İngilizce teknik anlatım

## Mastery gate

- Level 0: bilmiyor
- Level 1: terimleri tanıyor
- Level 2: rehberle uyguluyor
- Level 3: bağımsız uyguluyor
- Level 4: debug/test/optimize ediyor ve trade-off açıklıyor
- Level 5: tasarlıyor, production'da yönetiyor ve öğretiyor

Level 4 altı `mastered` kabul edilmez. Salt okuma, video tamamlama veya AI çıktısını çalıştırma evidence değildir.

## AI/Codex kuralı

Codex varsayılan olarak Teacher + Reviewer'dır. Kritik öğrenme implementasyonu önce kullanıcı tarafından yapılır. AI kodu kabul edilmeden önce:

- davranışı tahmin edilir,
- abstraction'ları açıklanır,
- failure senaryoları çıkarılır,
- testleri yazılır veya doğrulanır,
- kullanıcı değişikliğin neden doğru olduğunu anlatır.

Detaylı protokol: `00-governance/CODEX_TEACHER_PROTOCOL.md`.

## Kaynak tüketim kuralı

Kaynak biriktirmek öğrenme değildir. Her kaynak aktif bir learning outcome, lab, assessment veya architecture case'e bağlanmalıdır.

Tercih edilen sıra:

roadmap → primary docs → structured lesson → build-from-scratch → production source code → real project

## Gerçek proje transferi

Gerçek proje eğitim yerine geçmez; ancak kanıtı güçlendirir. Her transferde şu kayıt tutulur:

- kullanılan temel kavram,
- production'da karşılaşılan gerçek constraint,
- teoriden farklı çıkan davranış,
- debug/decision evidence,
- curriculum'a geri eklenmesi gereken yeni gap.

## Debug protokolü

Her anlamlı hata için:

symptom → reproduction → observations → hypotheses → experiments → root cause → fix → regression test → lesson

zinciri takip edilir. Sadece fix commit'i bırakmak yeterli değildir.
