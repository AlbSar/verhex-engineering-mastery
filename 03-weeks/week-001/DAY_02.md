---
status: ready
day: 2
date: 2026-09-07
estimated_hours: 2.5
---

# Day 02 — Python object, identity ve equality

## Oturum sözleşmesi
Öğretmen önce [concept-state](../../01-skill-matrix/concept-state.yaml) kaydını okur; kaydı olmayan ön koşulu UNKNOWN sayar. Today → Teach → Mechanism → Example → Predict → Lab → Observe → Review → Teach Back → Evidence sırası uygulanır. Her yeni komut/API/flag açıklanır; tek seferde yalnızca bir görev verilir. Kaynak okuma, açıklama, test ve kayıt aşağıdaki sürelere dahildir. Süre dolunca kalan required konu sonraki oturuma taşınır; tarihe göre atlanmaz. OPTIONAL/STRETCH ek süreleri ayrı kaydedilir ve geçiş koşulu değildir.

Kaynak bölümü, deney ve artefact: [Week 001 kaynak kartları](../../12-resources/WEEK_001.md). Komutlar için [ilk kullanım kartları](../../12-resources/COMMAND_PRIMER.md); kartı sadece linklemek öğretim yerine geçmez.

## Today
REQUIRED hedef: isim ile nesneyi, aynı nesne ile eşit değeri ayırmak. Ön koşullar: Day 01 Python çalıştırma, literal, liste, assignment, print. UNKNOWN varsa önce öğret; tarih Day 02'yi otomatik açmaz.

## 1. Teach ve demonstration — 40 dakika
Object/type/value, name binding, identity ve equality modelini öğret. `=` isim bağlar; kopyalama garantisi vermez. `is` identity, `==` equality karşılaştırır. `id()` ve `type()` sonuçlarının neyi gösterdiğini açıkla. Önce küçük bir liste çizimi ve sonucu açıklanan örnek göster. CPython interning davranışını dil garantisi olarak öğretme.

## 2. Guided lab — 55 dakika
Kullanıcı `src/week001/object_identity.py` içinde eşit ayrı listeler ve aynı listeye bağlı iki isim kurar. PRACTICING aliasing için kısa recall sonrası tahmin uygundur; UNKNOWN ise önce gösterim. Her seferinde tek değişiklik ve gözlem.

## 3. Test ve failure — 35 dakika
`assert` ve pytest önceden kurulmamışsa tanıt. Ayrı ama eşit listeler, aynı nesne ve rebinding için üç küçük test. Yanlış `is`/`==` seçiminin bir testte yarattığı hatayı açıklat. Kritik test/kod kullanıcı tarafından yazılır.

## 4. Review ve evidence — 20 dakika
İsim→nesne çizimi, bir tahmin farkı, test çıktısı ve kendi açıklaması. Kaynak kartı PY-OBJECT.

## REQUIRED evidence
Object identity lab, üç test, alias/rebinding açıklaması ve günlük bağlantısı.

## OPTIONAL / STRETCH / REFERENCE
STRETCH: custom `__eq__` yalnızca class/method ön koşulları öğretildiyse, en fazla 20 dakika ek süre. REFERENCE: CPython object implementation, henüz zorunlu değil.
