---
status: ready
day: 4
date: 2026-09-09
estimated_hours: 2.5
---

# Day 04 — Scope, function ve closure temeli

## Oturum sözleşmesi
Öğretmen önce [concept-state](../../01-skill-matrix/concept-state.yaml) kaydını okur; kaydı olmayan ön koşulu UNKNOWN sayar. Today → Teach → Mechanism → Example → Predict → Lab → Observe → Review → Teach Back → Evidence sırası uygulanır. Her yeni komut/API/flag açıklanır; tek seferde yalnızca bir görev verilir. Kaynak okuma, açıklama, test ve kayıt aşağıdaki sürelere dahildir. Süre dolunca kalan required konu sonraki oturuma taşınır; tarihe göre atlanmaz. OPTIONAL/STRETCH ek süreleri ayrı kaydedilir ve geçiş koşulu değildir.

Kaynak bölümü, deney ve artefact: [Week 001 kaynak kartları](../../12-resources/WEEK_001.md). Komutlar için [ilk kullanım kartları](../../12-resources/COMMAND_PRIMER.md); kartı sadece linklemek öğretim yerine geçmez.

## Today
REQUIRED hedef: local/global isim çözümlemesini ve fonksiyonun değer olarak taşınmasını açıklamak. Ön koşullar: assignment, function çağrısı, argument/return. UNKNOWN ise önce öğret. Closure derinleşmesi temel scope'un yerine geçmez.

## 1. Teach ve demonstration — 45 dakika
Namespace isim→nesne eşlemesidir; scope ismin aranabildiği bağlamdır. LEGB'yi local/enclosing/global/builtins olarak tanıt. Function object, argument ve return ile küçük scope örneğini öğretmen açıklar. `global`/`nonlocal` kullanılacaksa farklarını önce öğret.

## 2. Scope lab — 45 dakika
Kullanıcı `src/week001/closures.py` içinde local shadowing ve bir fonksiyonun başka fonksiyona verilmesini deneyler. Tahmin ve observation sonrası isimlerin nerede çözümlendiğini çizdir. En az iki küçük davranış testi.

## 3. Closure bağlantısı ve debug — 40 dakika
Öğretmen bir iç fonksiyonun enclosing binding'e erişimini çizim ve küçük demonstration ile tanıtır. Kullanıcı tek basit closure örneği yazar; function object prerequisite zayıfsa önce onu pekiştir ve closure'ı INTRODUCED olarak bırak. Yanlış scope varsayımını testle göster. İki farklı factory ve late-binding çözümü zorunlu değildir.

## 4. Review ve evidence — 20 dakika
Scope çizimi, kullanıcı lab'ı, iki test ve closure'ın hangi noktada kaldığı. Kaynak kartı PY-SCOPE. PROVEN yazmak için bağımsız açıklama/kullanım gerekir.

## REQUIRED evidence
Scope/function lab, iki test, isim çözümleme açıklaması; closure için öğretim/gözlem kaydı yeterli, mastery gate değil.

## OPTIONAL / STRETCH / REFERENCE
STRETCH: `nonlocal` sayaç ve late-binding debugging, en fazla 25 dakika ek süre, önce öğret. REFERENCE: decorators; bu hafta sınavı yok.
