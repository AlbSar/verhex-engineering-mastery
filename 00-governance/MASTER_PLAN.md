---
status: canonical
version: 2.0.0
updated_at: 2026-09-05
program_start: 2026-09-05
program_horizon: 12-month-core-plus-continuous
---

# Verhex Engineering Mastery Program

## Misyon

Bu repository bir kurs arşivi değil, yaşayan bir mühendislik laboratuvarıdır. Amaç yalnızca teknoloji kullanabilmek değil; bir sistemi en alt katmandan iş problemine kadar açıklayabilmek, tasarlayabilmek, debug edebilmek, test edebilmek, gözlemleyebilmek ve production ortamında sürdürülebilir biçimde yönetebilmektir.

Hedef profil tek bir rol değildir. Program aşağıdaki bakış açılarını aynı kişide birleştirir:

- Software Engineer — bileşeni doğru ve test edilebilir biçimde uygular.
- AI Engineer — model, retrieval, tool, evaluation, inference ve agent katmanlarını mühendislik disipliniyle kurar.
- Platform / Infrastructure Engineer — Linux, network, container, CI/CD, Kubernetes ve gözlemlenebilirlik katmanlarını yönetir.
- System Architect — bileşenler, veri akışları, failure domain'leri ve ölçek trade-off'larını tasarlar.
- Solution Architect — iş problemi, risk, maliyet, güvenlik, entegrasyon ve operasyon gereksinimlerinden teknik çözüme iner.

Nihai hedef abstraction seviyeleri arasında iki yönlü hareket edebilmektir:

hardware/kernel → process/runtime → network/data → service → distributed system → AI layer → platform → enterprise architecture → business solution

ve gerektiğinde aynı zinciri tersine takip ederek kök nedene inebilmek.

## Çekirdek ilkeler

1. Ezber değil mekanizma.
2. Framework'ten önce temel davranış.
3. API kullanımından önce mümkün olduğunca alt katmanı anlamak.
4. Bir teknoloji adı mimari gerekçe değildir; seçim requirement, constraint ve trade-off'tan doğar.
5. Her bilgi açıklama + uygulama + test + debug + production bağlantısı ile kanıtlanır.
6. AI düşünmenin yerine geçmez; öğretmen, reviewer ve hızlandırıcıdır.
7. Kritik öğrenme kodunu öğrenci yazar.
8. Gerçek projeler ileri seviye laboratuvardır; eğitim ve production birbirini besler.
9. Süre değil mastery gate geçişi belirler.
10. Program 12 aylık çekirdek yol içerir ama eğitim sistemi süreklidir ve bitmez.

## Çalışma temposu

Hedef sürdürülebilir tempo:

- Hafta içi: yaklaşık 3 saat/gün
- Hafta sonu: 4–5 saatlik derin çalışma bloğu
- Haftalık hedef: 18–20 saat
- Yoğun dönemlerde minimum korunacak ritim: haftada 10 saat

Saat tek başına başarı metriği değildir. Her hafta kod, terminal çıktısı, test, debug kaydı, teknik açıklama veya mimari artefact üretmelidir.

## Haftalık çalışma döngüsü

1. Mekanizma: kavram, neden, alt katman.
2. Lab: framework kullanmadan küçük uygulama veya deney.
3. Production bağlantısı: gerçek araç/framework/servis ile karşılaştırma.
4. Failure injection: boz, gözlemle, debug et.
5. Test ve ölçüm: correctness, latency, resource kullanımı, güvenlik varsayımları.
6. Gerçek proje transferi: uygun olduğunda Verhex/Deckent veya kişisel projeye bağla.
7. Retrospektif: kendi cümlelerinle öğrendiklerini, yanlış modelleri ve açık soruları kaydet.

## Dil stratejisi

### Primary — Python

Python; bilgisayar bilimi temelleri, automation, backend, AI engineering ve hızlı sistem prototipleme için ana dildir.

Beklenen derinlik:

- object/reference modeli ve mutability
- scope, functions, iterators, generators, decorators, context managers
- typing ve API design
- exceptions ve resource management
- testing, packaging, profiling
- threading, multiprocessing, GIL, asyncio
- sockets, HTTP, backend servisleri
- CPython internals'a giriş

### Second — Go

Go ikinci ana dil olarak; systems tooling, network programming, concurrency, backend, distributed systems ve cloud-native mühendislik için kullanılacaktır.

Beklenen derinlik:

- type system, interfaces, composition
- goroutine, channel, context, cancellation
- memory/escape davranışı
- network ve HTTP servisleri
- CLI/system tooling
- profiling ve concurrency debugging
- production-grade Go servisleri

### Product/Web — TypeScript

TypeScript; ürün arayüzleri, Node.js servisleri, SDK/CLI ve web katmanlarında kullanılır. JavaScript runtime mekanizmaları ayrıca öğrenilir.

### Enterprise specialization — Java

Java çekirdek yolun başında değil; JVM, GC, concurrency, Spring ve büyük kurumsal codebase'leri anlamak için ileri uzmanlaşma hattıdır.

## 12 aylık çekirdek roadmap

Takvim yönlendiricidir; mastery gate başarısızsa faz uzatılır.

### Phase A — Foundations: Python + Linux + Networking + Git
Yaklaşık Ay 1–2

Konular:
- Python fundamentals ve object model
- terminal-first çalışma
- Linux process, PID, signal, file descriptor, `/proc`, filesystem ve permissions
- shell, pipes, redirects, grep/sed/awk temelleri
- Git object/DAG modeli, branch, merge, rebase
- IP, TCP/UDP, socket, DNS, HTTP, TLS'e giriş
- temel veri yapıları, Big O ve algoritmik düşünme

Build-from-scratch:
- CLI
- TCP echo server/client
- minimal HTTP server
- minimal shell parçaları

Gate:
Bir Python programının process olarak nasıl çalıştığını, socket açıp TCP üzerinden nasıl HTTP mesajı taşıdığını Linux araçlarıyla gözlemleyebilmek.

### Phase B — Data + Backend + PostgreSQL
Yaklaşık Ay 2–3

Konular:
- relational model ve SQL
- indexes ve query plans
- transactions, ACID, isolation, MVCC
- locks, deadlocks, connection pools
- API design, REST, idempotency
- authentication/authorization fundamentals
- caching ve Redis mantığı
- structured logging, metrics, tracing'e giriş

Build-from-scratch:
- küçük KV store veya mini database bölümü
- Redis-benzeri küçük protocol/server
- production-grade Python API

Gate:
Bir API request'inin network'ten database transaction'ına ve response'a kadar yolunu, failure mode'ları ve gözlemlenebilirlik noktalarıyla açıklayabilmek.

### Phase C — Linux Deep Dive + Containers + Operations
Yaklaşık Ay 3–4

Konular:
- kernel/user space
- virtual memory, page, allocator kavramları
- scheduler ve concurrency temelleri
- namespaces, cgroups, capabilities, seccomp
- container image/layer, overlay filesystem
- Docker networking, volumes, resource limits
- systemd, SSH, process supervision
- DNS, routing, NAT, TLS derinleşme

Kaynak kod okuma:
- `torvalds/linux` ilgili subsystem dokümantasyonu ve seçilmiş kod yolları

Build-from-scratch:
- minimal container deneyi/runtime

Gate:
Container'ın neden VM olmadığını kernel primitive'leri seviyesinde açıklamak ve resource/network isolation davranışını terminalde göstermek.

### Phase D — Go + Systems Programming
Yaklaşık Ay 4–5

Konular:
- idiomatic Go
- interfaces ve composition
- goroutines/channels
- context/cancellation
- HTTP/network programming
- race conditions ve synchronization
- benchmarks/profiling

Ürün:
- Python'da yapılmış bir network/service lab'ının Go karşılığı
- production CLI veya daemon

Gate:
Python ve Go runtime/concurrency modellerinin trade-off'larını gerçek benchmark ve kod üzerinden açıklayabilmek.

### Phase E — System Design + Distributed Systems
Yaklaşık Ay 5–7

Ana kaynaklardan biri: `donnemartin/system-design-primer`.

Konular:
- latency vs throughput
- vertical/horizontal scaling
- availability, consistency, CAP bağlamı
- replication ve partitioning
- caching strategies
- queues, backpressure, async processing
- service discovery
- load balancing, reverse proxy, CDN
- distributed failure models
- retries, timeout, circuit breaker, idempotency
- consensus'a kavramsal giriş
- observability ve SLO/SLA
- cost/performance trade-off

Her vaka şu sırayla çözülür:
requirement → constraints → workload → failure model → consistency → architecture → bottleneck → technology selection → cost/operations

Gate:
En az üç farklı büyük sistem vakasını capacity estimate, diagram, trade-off ve failure analysis ile savunabilmek.

### Phase F — AI Engineering Foundations
Yaklaşık Ay 7–9

Konular:
- gerekli linear algebra/probability temelleri
- neural networks
- tokenization
- attention ve transformer
- embeddings
- model inference
- structured output ve tool use
- RAG: chunking, retrieval, reranking
- evaluation
- prompt/model/application ayrımı
- cost, latency, context ve reliability

Build-from-scratch:
- küçük neural network/transformer çalışması
- basit RAG pipeline
- eval harness

Gate:
Bir LLM uygulamasındaki hatayı model, retrieval, tool, orchestration veya evaluation katmanına doğru sınıflandırabilmek ve kanıtla debug edebilmek.

### Phase G — Agents + AI Systems + MLOps
Yaklaşık Ay 9–10

Konular:
- agent vs workflow
- planning ve tool selection
- state/memory
- durable execution
- approval/HITL
- audit/evidence
- model/provider routing
- retries/budgets/timeouts
- eval-driven development
- fine-tuning: dataset, SFT, LoRA/QLoRA
- model serving ve inference economics
- MLOps fundamentals

Failure modes:
- hallucination
- retrieval failure
- tool selection error
- context contamination
- state divergence
- planning failure
- nondeterminism
- cost/latency amplification

Gate:
Bir agentic sistemi feature listesiyle değil authority, state, failure, evidence, cost ve recovery modelleriyle tasarlayabilmek.

### Phase H — Platform Engineering: CI/CD + IaC + Kubernetes
Yaklaşık Ay 10–11

Konular:
- CI/CD design
- artifact/release/rollback
- secrets ve supply-chain security
- Terraform/IaC
- Kubernetes architecture: API server, scheduler, controller, etcd
- pod/deployment/service/ingress
- RBAC
- storage
- autoscaling
- health/readiness
- Helm/GitOps
- observability

Gate:
Bir servisi yalnızca deploy etmek değil; neden Kubernetes gerektiğini/gerekmediğini, failure ve operation modelini açıklayabilmek.

### Phase I — Software, System & Solution Architecture
Yaklaşık Ay 11–12

Software Architecture:
- modularity, boundaries, coupling/cohesion
- domain modeling
- API/contracts
- event-driven patterns
- ADR ve architecture fitness

System Architecture:
- distributed topology
- data ownership
- integration boundaries
- security zones
- resiliency
- observability
- capacity/cost

Solution Architecture:
- business goals ve constraints
- stakeholder requirements
- build/buy/integrate
- enterprise integration
- risk, compliance, security
- migration roadmap
- TCO/ROI
- operations/governance

Capstone:
Gerçek bir Verhex veya kişisel ürün problemi için business requirement'tan kod/infra/AI katmanına kadar tam çözüm tasarımı ve çalışan kanıt.

Gate:
Aynı çözümü software engineer, system architect ve solution architect perspektiflerinden ayrı ayrı savunabilmek.

## Sürekli Production Code Reading hattı

Gerçek repo okumak ayrı bir faz değil, tüm programa paralel bir disiplindir.

Öncelikli codebase türleri:
- Linux kernel
- CPython
- PostgreSQL
- Redis
- Git
- Docker/container ecosystem
- Kubernetes
- seçilmiş Go ve TypeScript production projeleri

Kural: repository baştan sona okunmaz. Aktif kavrama bağlı olarak documentation → call path → implementation → test → issue/commit zinciri takip edilir.

## Kaynak mimarisi

Ana kaynak rolleri:

- `nilbuild/developer-roadmap` — neyi hangi sırada öğrenmeli?
- `freeCodeCamp/freeCodeCamp` — structured learning, exercise ve project practice
- `sindresorhus/awesome` — ilgili ekosistemde kaliteli kaynak/araç keşfi
- `codecrafters-io/build-your-own-x` — kritik teknolojileri sıfırdan inşa etme
- `donnemartin/system-design-primer` — scalable/distributed system design
- `torvalds/linux` — gerçek production kernel internals

Kaynaklar müfredat değildir; aktif hedefe bağlanmadıkça tüketilmez.

## Codex rolü

Codex'in ana rolü Teacher + Socratic Guide + Reviewer'dır.

Codex:
- doğru soruları sorar,
- mekanizmayı açıklar,
- kaynakta ilgili bölümü bulur,
- egzersiz/lab tasarlar,
- kullanıcının kodunu review eder,
- test/failure senaryosu önerir,
- yanlış mental modeli tespit eder.

Codex kritik öğrenme implementasyonunu varsayılan olarak yazmaz. Kullanıcı önce tahmin eder, tasarlar ve kodlar. Ayrıntılı kurallar `00-governance/CODEX_TEACHER_PROTOCOL.md` içindedir.

## Mastery modeli

0 — bilmiyor
1 — terimleri tanıyor
2 — rehberle uyguluyor
3 — bağımsız uyguluyor
4 — debug/test/optimize ediyor ve trade-off açıklıyor
5 — tasarlıyor, production'da yönetiyor ve öğretebiliyor

Bir konu en az 4 seviyesinde kanıtlanmadan mastered kabul edilmez.

Zorunlu kanıt türleri:
- kendi açıklaması
- kod/lab
- otomatik test
- debug/failure kaydı
- gözlem veya benchmark
- production bağlantısı
- gerektiğinde architecture/ADR

## Gerçek projelerle pekiştirme

Deckent, Verhex işleri ve kişisel ürünler ileri seviye laboratuvar olarak kullanılabilir. Ancak production ihtiyacı eğitim hedefini ezmemelidir. Her gerçek proje transferinde şu üç soru kaydedilir:

1. Hangi temel kavram kullanıldı?
2. Production gerçeği eğitim modelinden nasıl farklıydı?
3. Bu deneyim curriculum'a hangi yeni lab veya knowledge gap'i ekledi?

## Kanonik kayıtlar

- `00-governance`: plan ve protokoller
- `01-skill-matrix`: mastery seviyeleri ve evidence
- `02-phases`: detaylı faz planları
- `03-weeks`: haftalık execution planı
- `04-daily-logs`: günlük kayıt
- `05-labs`: kontrollü deneyler
- `06-verhex-products`: gerçek proje transferleri
- `07-english`: teknik İngilizce çıktıları
- `08-adr`: mimari kararlar
- `09-debug-journal`: hata ve root-cause kayıtları
- `10-assessments`: sınav/review
- `11-portfolio`: tamamlanmış kanıtlar
- `12-resources`: kaynak haritası

## Nihai başarı tanımı

Programın çekirdek 12 aylık yolunun sonunda şu iddia teknik kanıtlarla savunulabilmelidir:

> Bir iş problemini ve constraint'lerini analiz eder; gerekli software, data, infrastructure ve AI katmanlarını seçer; Python, Go ve gerektiğinde TypeScript/Java ile güvenilir bileşenler geliştirir; Linux, PostgreSQL, container ve Kubernetes katmanlarını mekanizma seviyesinde anlayarak işletir; distributed system ve LLM/agent failure mode'larını debug eder; çözümü security, observability, cost ve operations boyutlarıyla System ve Solution Architecture seviyesinde tasarlar ve savunurum.
