---
status: ready
day: 3
date: 2026-09-08
estimated_hours: 2.5
---

# Day 03 — Mutation, copy ve debugging

## Oturum sözleşmesi
Öğretmen önce [concept-state](../../01-skill-matrix/concept-state.yaml) kaydını okur; kaydı olmayan ön koşulu UNKNOWN sayar. Today → Teach → Mechanism → Example → Predict → Lab → Observe → Review → Teach Back → Evidence sırası uygulanır. Her yeni komut/API/flag açıklanır; tek seferde yalnızca bir görev verilir. Kaynak okuma, açıklama, test ve kayıt aşağıdaki sürelere dahildir. Süre dolunca kalan required konu sonraki oturuma taşınır; tarihe göre atlanmaz. OPTIONAL/STRETCH ek süreleri ayrı kaydedilir ve geçiş koşulu değildir.

Kaynak bölümü, deney ve artefact: [Week 001 kaynak kartları](../../12-resources/WEEK_001.md). Komutlar için [ilk kullanım kartları](../../12-resources/COMMAND_PRIMER.md); kartı sadece linklemek öğretim yerine geçmez.

## Today
REQUIRED hedef: iki ismin paylaştığı state'i ve mutation/rebinding farkını debug etmek. Ön koşullar: Day 02 identity/equality; function ve argument UNKNOWN ise bu oturumda öğretilir.

## 1. Teach ve demonstration — 40 dakika
Mutable/immutable, function argument binding ve shallow copy kavramlarını öğret. Küçük bir liste örneğinde assignment ile `list.copy()` farkını göster. Nested yapı öncesi listelerin başka nesnelere referans tuttuğunu çiz. API'nin input'u değiştirmesi neden önemlidir anlat.

## 2. Copy lab — 45 dakika
Kullanıcı `src/week001/mutability.py` içinde assignment ve shallow copy'yi karşılaştırır. Öğretim sonrası tahmin, tek mutation, observation. Nested copy hazır değilse düz listeyle öğrenme hedefine ulaş; nested örnek ertelenir.

## 3. Failure ve regression — 45 dakika
Kullanıcı beklenmeyen paylaşılan mutation'ı reproduce eder; symptom → hypothesis → evidence → root cause → fix → regression test. Kod kullanıcıya aittir. En az bir normal ve bir failure test. Default mutable argument konusu ancak function/default evaluation önce öğretildiyse bu hata yerine seçilebilir; ikisini birden zorunlu yapma.

## 4. Review ve evidence — 20 dakika
Input mutation ile yeni değer döndürmenin bir trade-off'unu açıkla. Bir debug journal ve test çıktısı; kaynak kartı PY-COPY. AI explanation bağımsız kullanıcı açıklaması sayılmaz.

## REQUIRED evidence
Copy karşılaştırması, paylaşılan mutation reproducer/fix, iki test ve bir debug journal.

## OPTIONAL / STRETCH / REFERENCE
STRETCH: `copy.deepcopy()` ve tuple içinde mutable nesne, önce öğretimle en fazla 25 dakika ek süre. REFERENCE: mutable default ve nesne grafı; Day 03 geçiş koşulu değil.
