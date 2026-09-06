---
status: canonical
version: 3.0.0
updated_at: 2026-09-07
---

# Learning Protocol

## Önce öğretim

> Never ask the learner to interpret, predict, debug, or use a concept, command, API, tool, flag, protocol, or abstraction that has not first been taught or explicitly established as prior knowledge.

> Socratic questioning is a reinforcement technique, not a substitute for instruction.

> For unknown concepts the correct order is Teach → Demonstrate → Predict → Practice → Observe → Explain → Review.

Davranış otoritesi [Codex Teacher Protocol](CODEX_TEACHER_PROTOCOL.md); aktif durum kaydı [concept-state.yaml](../01-skill-matrix/concept-state.yaml).

## Öğrenme döngüleri

UNKNOWN: TEACH → SHOW → EXPLAIN MECHANISM → TINY EXAMPLE → PREDICT → USER RUNS → OBSERVE → USER EXPLAINS → REVIEW.

PRACTICING: RECALL → PREDICT → USER BUILDS → TEST → BREAK → DEBUG → REVIEW → PRODUCTION COMPARISON.

ADVANCED: PROBLEM → CONSTRAINTS → USER DESIGN → TRADE-OFF REVIEW → FAILURE INJECTION → PRODUCTION SOURCE → ARCHITECTURE REVIEW.

INTRODUCED rehberli deneyi sürdürür; PROVEN ön koşul olarak kullanılabilir; MASTERED 4+ çok yönlü kanıt gerektirir. Yeni alt kavram UNKNOWN ise ileri oturumda bile öğretime dönülür. Durum geçişleri kanıtla yapılır; kalıcı puan yalnızca [Assessment Standard](ASSESSMENT_STANDARD.md) ile verilir.

## Mekanizma derinliği

Önce basit model, sonra teknik mekanizma, OS/runtime/protocol, production sonucu ve gerektiğinde seçilmiş kaynak yolu. Konu ilerledikçe şu soruları yanıtla: nedir, hangi sorun için yaratıldı, altında ne olur, hangi veri yapıları vardır, nasıl gözlenir, bozulur ve debug edilir, trade-off ve production farkı nedir, gerçek sistemde nerede görülür? İlk oturuma tüm derinlikleri sıkıştırma.

## Kaynak akışı

 developer-roadmap → official / primary documentation → explanation → structured practice when useful → small experiment → build-your-own when high leverage → production implementation → own lab → real project transfer → evidence → reflection

Her atlanan opsiyonel adım gerekçelendirilir; kaynak okuma ders süresine dahildir. Ayrıntı ve aktif kartlar: [Resources](../12-resources/README.md). Kaynak listesini bitirmek başarı ölçüsü değildir.

## Construction ve production reading

Build-your-own öncesi hangi production mekanizmasının küçük modelini kurduğunu açıkla. CLI/shell/HTTP/TCP/KV/database/Redis/Git/container/interpreter/neural network/transformer adaydır; hepsini yapma. Ön koşullar ve fayda seçim nedenidir.

Production kaynak okuma: soru → kavram → resmî doküman → seçilmiş subsystem/entry point → tek call/data path → ilgili test → mimari özet → kendi lab'ına dönüş. Linux ana referanstır. CPython/PostgreSQL/Redis/Git/Kubernetes/nginx/LLVM ancak aktif ihtiyaçta eklenir. Binlerce satır dökme; sürüm/commit ve incelenen yolu kaydet.

Karşılaştırma: correctness, concurrency, durability, security, observability, performance, recovery. Lab'da olmayan garantileri açıkça yaz.

## Gerçek proje transferi

LEARN → LAB → EXPLAIN → REAL PROJECT → FAILURE / TRADE-OFF → RETURN TO THEORY → DEEPEN.

Kontrollü lab önce gelir. Verhex/Deckent production reposuna deney kodu otomatik taşınmaz. Transfer kaydı: iş problemi, temel kavram, constraint, karar, risk, rollback ve geri dönen öğrenme boşluğu.

## Kanıt ve reflection

Kod, test, terminal çıktısı, debug journal, benchmark, diagram, ADR, incident analizi ve kendi açıklaması kanıt olabilir. AI reference notu tek başına kanıt değildir. Kullanıcının kaynaklı etkileşimi ayrıca belirtilir. Kanıt yoksa `null`/not-proven; UNKNOWN konuya sınav veya otomatik sıfır puan yoktur.

Debug zinciri: symptom → reproduction → observations → hypotheses → experiments → root cause → fix → regression test → lesson. Yeni araç önce öğretilir. Week 001'de tüm konu başına production benchmark zorunlu değildir; uygun derinlik zaman bütçesi içinde seçilir.
