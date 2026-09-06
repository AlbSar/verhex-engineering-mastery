---
status: ready
day: 5
date: 2026-09-10
estimated_hours: 3
---

# Day 05 — Veri yapısı seçimi ve küçük construction

## Oturum sözleşmesi
Öğretmen önce [concept-state](../../01-skill-matrix/concept-state.yaml) kaydını okur; kaydı olmayan ön koşulu UNKNOWN sayar. Today → Teach → Mechanism → Example → Predict → Lab → Observe → Review → Teach Back → Evidence sırası uygulanır. Her yeni komut/API/flag açıklanır; tek seferde yalnızca bir görev verilir. Kaynak okuma, açıklama, test ve kayıt aşağıdaki sürelere dahildir. Süre dolunca kalan required konu sonraki oturuma taşınır; tarihe göre atlanmaz. OPTIONAL/STRETCH ek süreleri ayrı kaydedilir ve geçiş koşulu değildir.

Kaynak bölümü, deney ve artefact: [Week 001 kaynak kartları](../../12-resources/WEEK_001.md). Komutlar için [ilk kullanım kartları](../../12-resources/COMMAND_PRIMER.md); kartı sadece linklemek öğretim yerine geçmez.

## Today
REQUIRED hedef: küçük bir duplicate analyzer yazmak ve seçilen veri yapısını gerekçelendirmek. Ön koşullar: list/dict, loop, condition, function, test. UNKNOWN konular ilk blokta öğretilir. Dependency scheduler ileri extension'dır.

## 1. Teach ve demonstration — 45 dakika
List sırası, dict key/value ve set membership'i küçük örneklerle öğret. Boş input, duplicate, deterministic output ve temel Big-O sezgisini tanıt. Hashing derinliği gerekmez; tool/API ne yapar önce açıklanır. Production karşılığı: kayıt işleme servisindeki duplicate kontrolünün küçük modeli.

## 2. Kullanıcı construction — 70 dakika
Kullanıcı `src/week001/duplicate_analyzer.py` içinde basit kayıt listesindeki tekrar eden kimlikleri bulur. Önce input/output sözleşmesini seçer. Kapsam: boş liste, tekrar yok, tekrar var. Veri kaynağı küçük ve kontrollüdür; JSON parser, CLI framework, custom exception hierarchy aynı anda zorunlu değildir.

## 3. Test ve debugging — 40 dakika
Üç durum için en az üç test. Öğrenci bir yanlış veri yapısı/koşul varsayımını gözlem ve testle düzeltir. Yeni pytest API'leri tanıtılır. Eksik kimlik davranışı öğretildiyse dördüncü test eklenebilir; süreyi aşma.

## 4. Compare ve evidence — 25 dakika
Naive tekrar taraması ile seçilen yaklaşımın maliyetini niteliksel açıkla. Production daha büyük veri, concurrency, durability, security, observability ve recovery ister; bu lab bunları sağlamaz. Kaynak kartı PY-DATA; kod, test ve trade-off notu kaydet.

## REQUIRED evidence
Duplicate analyzer, üç test, veri yapısı gerekçesi, bir production farkı ve günlük.

## OPTIONAL / STRETCH / REFERENCE
STRETCH: dependency scheduler + cycle detection, en fazla 60 dakika ayrı oturum. Önce graph/node/edge, queue, in-degree ve Kahn algoritması öğretilir; sonra kullanıcı yazar. Zorunlu haftanın dışındadır, gelecek Phase A haftasına taşınabilir. REFERENCE: build-your-own-x construction adayları; listeyi bitirme ödevi yok.
