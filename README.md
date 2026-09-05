# Verhex Engineering Mastery Program

Bu repository Alperen'in sürekli mühendislik gelişim sisteminin kanonik deposudur. Amaç yalnızca teknoloji öğrenmek değil; koddan kernel'e, network'ten distributed system'e, AI katmanından enterprise solution architecture'a kadar abstraction seviyeleri arasında güvenilir biçimde hareket edebilen bir mühendislik profili oluşturmaktır.

## Programın yönü

Ana eksenler:

- Python — primary language, backend, automation, AI engineering
- Go — second language, systems/networking/cloud-native/distributed systems
- TypeScript — product/web/SDK/Node.js katmanı
- Java — ileri enterprise/JVM specialization
- Linux + Networking — temel sistem davranışı
- PostgreSQL + Data — state, transactions, indexes, MVCC, query behavior
- Docker + Kubernetes — container ve platform engineering
- System Design + Distributed Systems — scale, failure, consistency, queues, caching, replication
- AI Engineering — transformers, inference, RAG, eval, agents, fine-tuning, MLOps
- Software/System/Solution Architecture — teknik bileşenden iş çözümüne kadar tasarım

## Çalışma modeli

Program 5 Eylül 2026'da başlar. 12 aylık çekirdek yol vardır ancak eğitim süreklidir ve mastery gate'leri takvimden daha önemlidir.

Sürdürülebilir hedef:

- hafta içi yaklaşık 3 saat/gün
- hafta sonu 4–5 saat derin çalışma
- haftalık yaklaşık 18–20 saat

Her konu için temel döngü:

**Explain → Predict → Build → Observe → Break → Debug → Test → Compare → Transfer → Teach Back**

## Codex'in rolü

Codex bu repo içinde varsayılan olarak **Teacher + Socratic Guide + Reviewer**'dır.

Codex kritik öğrenme kodunu kullanıcının yerine yazmaz; mekanizmayı açıklar, ipucu verir, yanlış mental modeli arar, kullanıcının kodunu review eder, test/failure senaryoları üretir ve production implementation ile farkları gösterir.

Detay: [`00-governance/CODEX_TEACHER_PROTOCOL.md`](00-governance/CODEX_TEACHER_PROTOCOL.md)

## Çekirdek kaynak sistemi

- `nilbuild/developer-roadmap` — neyi hangi sırayla öğrenmeli?
- `freeCodeCamp/freeCodeCamp` — structured lesson + exercise + project
- `sindresorhus/awesome` — kaliteli ecosystem/resource discovery
- `codecrafters-io/build-your-own-x` — mekanizmayı sıfırdan inşa ederek öğrenme
- `donnemartin/system-design-primer` — scalable/distributed system design
- `torvalds/linux` — gerçek production kernel internals

Kaynak haritası: [`12-resources/README.md`](12-resources/README.md)

## Kanonik plan

- Ana program: [`00-governance/MASTER_PLAN.md`](00-governance/MASTER_PLAN.md)
- Learning protocol: [`00-governance/LEARNING_PROTOCOL.md`](00-governance/LEARNING_PROTOCOL.md)
- Codex teacher protocol: [`00-governance/CODEX_TEACHER_PROTOCOL.md`](00-governance/CODEX_TEACHER_PROTOCOL.md)
- AI usage: [`00-governance/AI_USAGE_PROTOCOL.md`](00-governance/AI_USAGE_PROTOCOL.md)
- Assessment standard: [`00-governance/ASSESSMENT_STANDARD.md`](00-governance/ASSESSMENT_STANDARD.md)
- Skill matrix: [`01-skill-matrix/skill-matrix.yaml`](01-skill-matrix/skill-matrix.yaml)

## 12 aylık çekirdek fazlar

1. Foundations — Python + Linux + Networking + Git
2. Data + Backend + PostgreSQL
3. Linux Deep Dive + Containers + Operations
4. Go + Systems Programming
5. System Design + Distributed Systems
6. AI Engineering Foundations
7. Agents + AI Systems + MLOps
8. Platform Engineering — CI/CD + IaC + Kubernetes
9. Software + System + Solution Architecture
10. Capstone ve gerçek proje transferi

Fazlar kesin tarihli kurs modülleri değildir. Evidence yetersizse uzar; güçlü real-world evidence varsa hızlanabilir.

## Aktif çalışma döngüsü

**Week 001 — 5–12 Eylül 2026**  
**Odak: Python + Linux + Networking baseline**

- Takip issue'su: [#1 — Week 001 Tanılama ve Python Çalışma Modeli](https://github.com/AlbSar/verhex-engineering-mastery/issues/1)
- Haftalık plan: [`03-weeks/week-001/WEEK_PLAN.md`](03-weeks/week-001/WEEK_PLAN.md)
- Günlük görevler: [`DAY_01`](03-weeks/week-001/DAY_01.md) · [`DAY_02`](03-weeks/week-001/DAY_02.md) · [`DAY_03`](03-weeks/week-001/DAY_03.md) · [`DAY_04`](03-weeks/week-001/DAY_04.md) · [`DAY_05`](03-weeks/week-001/DAY_05.md) · [`DAY_06`](03-weeks/week-001/DAY_06.md) · [`DAY_07`](03-weeks/week-001/DAY_07.md)
- Baseline: [`01-skill-matrix/baseline-assessment.md`](01-skill-matrix/baseline-assessment.md)
- Assessment: [`03-weeks/week-001/ASSESSMENT.md`](03-weeks/week-001/ASSESSMENT.md)

## Repository kayıt yapısı

- `00-governance` — plan ve protokoller
- `01-skill-matrix` — mastery seviyeleri/evidence
- `02-phases` — phase detayları
- `03-weeks` — haftalık execution planları
- `04-daily-logs` — günlük öğrenme kayıtları
- `05-labs` — kontrollü deneyler
- `06-verhex-products` — gerçek proje transferleri
- `07-english` — teknik İngilizce çıktıları
- `08-adr` — mimari kararlar
- `09-debug-journal` — root-cause kayıtları
- `10-assessments` — değerlendirmeler
- `11-portfolio` — kanıtlanmış çıktılar
- `12-resources` — doğrulanmış kaynak haritası

## Başarı standardı

Bir konu salt okunarak veya AI çıktısı çalıştırılarak tamamlanmış sayılmaz. `mastered` olmak için en az Level 4 evidence gerekir:

> bağımsız uygula + gözlemle + boz + debug et + test et + trade-off açıkla.

Programın temel amacı Codex'in daha çok kod yazması değil, kullanıcının Codex olmadan açıklayabildiği, uygulayabildiği, debug edebildiği ve tasarlayabildiği alanın sürekli büyümesidir.

## Durum

`active / foundations / week-001` — program 5 Eylül 2026 itibarıyla yürürlüktedir.
