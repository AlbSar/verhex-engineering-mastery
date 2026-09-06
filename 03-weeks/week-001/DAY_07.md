---
status: ready
day: 7
date: 2026-09-12
estimated_hours: 2
---

# Day 07 — Kanıt değerlendirmesi ve sonraki öncelik

## Oturum sözleşmesi
Öğretmen önce [concept-state](../../01-skill-matrix/concept-state.yaml) kaydını okur; kaydı olmayan ön koşulu UNKNOWN sayar. Today → Teach → Mechanism → Example → Predict → Lab → Observe → Review → Teach Back → Evidence sırası uygulanır. Her yeni komut/API/flag açıklanır; tek seferde yalnızca bir görev verilir. Kaynak okuma, açıklama, test ve kayıt aşağıdaki sürelere dahildir. Süre dolunca kalan required konu sonraki oturuma taşınır; tarihe göre atlanmaz. OPTIONAL/STRETCH ek süreleri ayrı kaydedilir ve geçiş koşulu değildir.

Kaynak bölümü, deney ve artefact: [Week 001 kaynak kartları](../../12-resources/WEEK_001.md). Komutlar için [ilk kullanım kartları](../../12-resources/COMMAND_PRIMER.md); kartı sadece linklemek öğretim yerine geçmez.

## Today
REQUIRED hedef: öğretilen konulardaki bağımsızlığı değerlendirmek. Ön koşullar: yalnızca önceki günlerde öğretilmiş veya açık ön bilgiyle kurulmuş kavramlar. UNKNOWN konu sınav sorusu yapılamaz; yeni öğretim sonraki oturum planına yazılır.

## 1. Kapsam ve mini assessment — 45 dakika
İlk 10 dakika concept-state ve required evidence ile sınav kapsamını belirle. Sonraki 20 dakika kullanıcı daha önce öğrendiği duplicate analizinin küçük bir varyantını ve bir normal/bir edge-case testini bağımsız yazar. Hazır olmadığı syntax/API kullanılmaz; prerequisite eksikse sınav yerine öğretim ve `repeat-critical-sections` kaydı. Son 15 dakika reviewer doğruluk ve açıklamayı inceler; çözümü devralmaz.

## 2. Teach-back — 25 dakika
Öğretilmiş konulardan seç: name→object, mutation/rebinding, scope, shell→program, exit status, stdin/stdout/pipe, process→socket→HTTP. Closure veya graph STRETCH tamamlama koşulu değildir. Kullanıcı bir soruya bilmiyorum derse bilgi açığı olarak kaydet; bilinmeyeni tahmin ettirme.

## 3. Evidence ve karar — 30 dakika
[Assessment](ASSESSMENT.md), [baseline](../../01-skill-matrix/baseline-assessment.md) ve [concept-state](../../01-skill-matrix/concept-state.yaml) güncellenir; aynı kanıtı linkle, yeniden üretme. Puan yalnızca kanıtlıysa, aksi `null`. AI notu ve kullanıcı açıklaması ayrılır. Faz 0 ayrı ek sınav değildir.

## 4. Retrospective — 15 dakika
[Retrospective](RETROSPECTIVE.md): öğretimden önce soru soruldu mu, bilinmeyen araç varsayıldı mı, 19 saat aşıldı mı, hangi prerequisite güçlendirilecek? Required/optional sürelerini ayrı tut.

## 5. Git kapanışı — 5 dakika
Day 01 Git kartlarını hatırlat; önce status ve diff. Seçilen kanıt dosyalarını kullanıcı stage/review/commit eder. Süre yetmezse ayrıca planla; blanket add veya kullanıcı geçmişini değiştirme yok.

## REQUIRED evidence
Mini bağımsız varyant ve iki test, kaynaklı teach-back, assessment/baseline/concept-state bağlantıları, retrospective ve sonraki öncelik.

## OPTIONAL / STRETCH / REFERENCE
OPTIONAL: İngilizce writing/speaking baseline, en fazla 20 dakika ek süre; Week 001 geçiş koşulu değil. REFERENCE: uzun vadeli mastery scale. Day 07 sonunda [Assessment Standard](../../00-governance/ASSESSMENT_STANDARD.md) ile proceed / proceed-with-reinforcement / repeat-critical-sections kararı verilir.
