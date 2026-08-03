---
status: canonical
version: 1.0.0
updated_at: 2026-08-04
program_duration_weeks: 36
---

# Verhex Engineering & English Mastery Marathon

## Amaç

Bu programın amacı yalnızca Python, TypeScript, Linux, Docker, Kubernetes veya AI araçlarını kullanmak değildir. Hedef; bir sistemin ne yaptığını, neden çalıştığını, hangi katmanlardan oluştuğunu, nasıl gözlemlendiğini, nasıl bozulduğunu, nasıl test edildiğini ve production ortamında nasıl kontrol altında tutulduğunu anlayan kurumsal AI ve platform mühendisi olmaktır.

Program sonunda aşağıdaki yetkinlikler kanıtlanacaktır:

- Production-grade Python servisleri geliştirmek
- AI tarafından yazılan kodu satır satır denetlemek
- Algoritma, veri yapısı ve yazılım tasarım kararlarını açıklamak
- Linux sunucuları terminal üzerinden yönetmek
- Process, thread, memory, filesystem ve network davranışını anlamak
- Docker container çalışma modelini kavramak
- CI/CD pipeline tasarlamak ve debug etmek
- JavaScript runtime ve TypeScript type sistemine hâkim olmak
- API, SDK, CLI, worker ve web uygulamaları geliştirmek
- Kubernetes'in hangi problemi neden çözdüğünü bilmek
- Kurumsal AI entegrasyonları, RAG, agent ve model servisleri kurmak
- Fine-tuning veri seti hazırlamak ve QLoRA tabanlı eğitim yapmak
- Teknik İngilizcede C1 seviyesine ulaşmak
- Verhex adına tekrar satılabilir ürün çekirdekleri üretmek

## Ana ilkeler

1. Ezber değil mekanizma.
2. Framework'ten önce temel sistem davranışı.
3. Her bilgi gerçek projede kullanılacak.
4. Her yeterlilik açıklama, uygulama, debug, test ve production değerlendirmesiyle kanıtlanacak.
5. AI düşünmenin yerine geçmeyecek.
6. Bir konu en az 4/5 seviyesine ulaşmadan tamamlanmış sayılmayacak.

## Çalışma modeli

- Süre: 36 hafta
- Tempo: haftada 6 gün
- Günlük çalışma: 4–5 saat
- Haftalık toplam: yaklaşık 25–30 saat
- İngilizce hattı mühendislik programıyla eş zamanlı yürütülür.

## Haftalık döngü

- Pazartesi: kavram ve temel mekanizma
- Salı: framework kullanmadan sıfırdan uygulama
- Çarşamba: framework ve production uygulaması
- Perşembe: test ve debugging
- Cuma: Verhex ürün geliştirme
- Cumartesi: değerlendirme ve İngilizce teknik sunum
- Pazar: dinlenme veya hafif tekrar

## Fazlar

### Faz 0 — Tanılama ve çalışma ortamı

Başlangıç seviyesini ölçmek; WSL2, Python, uv, Git, Ruff, Pyright/mypy, pytest, Docker, PostgreSQL ve Redis tabanlı çalışma ortamını doğrulamak.

### Faz 1 — Python çekirdeği ve bilgisayar bilimi

Python veri modeli, referans semantiği, scope, fonksiyonlar, iterator/generator, typing, exception sistemi, veri yapıları, Big O ve temel algoritmalar.

Faz ürünü: `verhex-python-core`.

### Faz 2 — İleri Python, concurrency ve backend

Process/thread, GIL, asyncio, socket, TCP, HTTP, FastAPI, PostgreSQL, transaction, isolation, connection pool, idempotency ve production servis davranışı.

Faz ürünü: `verhex-service-runtime`.

### Faz 3 — AI mühendisliği ve model özelleştirme

Tokenizasyon, transformer temelleri, structured output, tool calling, RAG, retrieval, reranking, evaluation, agent/workflow ayrımı, durable execution, SFT, LoRA ve QLoRA.

Faz ürünü: `verhex-model-lab`.

### Faz 4 — Linux, sunucu, Docker ve operasyon

Kernel/user space, process, signal, filesystem, permissions, file descriptor, `/proc`, memory, swap, OOM, systemd, SSH, routing, NAT, DNS, TLS, namespace, cgroup, image layer, volume ve container güvenliği.

Faz ürünü: `verhex-deployment-node`.

### Faz 5 — JavaScript ve TypeScript uzmanlığı

Execution context, call stack, closure, prototype chain, event loop, promise, microtask, stream, strict TypeScript, generics, discriminated union, conditional type, Node.js, CLI, SDK ve web uygulama katmanı.

Faz ürünü: `verhex-typescript-sdk`.

### Faz 6 — CI/CD, IaC ve Kubernetes

GitHub Actions, artifact, release, secret, rollback, supply-chain security, Terraform, Ansible, Kubernetes control plane, pod, deployment, service, ingress, RBAC, storage, autoscaling, Helm ve GitOps.

Faz ürünü: `verhex-platform-kit`.

### Faz 7 — Verhex Enterprise AI Integration Node

AI Gateway, enterprise connector layer, tool execution layer, RAG, model routing, audit, approval, idempotency, Docker/Kubernetes deployment, monitoring, backup ve security kontrollerini tek satılabilir üründe birleştirmek.

## İngilizce hattı

Her gün teknik okuma, dinleme, yazma ve konuşma çalışması yapılır. Commit, PR, issue, ADR, README, incident report, architecture document ve müşteri iletişimi İngilizce üretilir. Her hafta bir teknik metin, bir sesli anlatım, bir doküman özeti ve bir teknik toplantı simülasyonu teslim edilir.

## Ölçme sistemi

- 0: bilmiyor
- 1: terimleri tanıyor
- 2: yardımla kullanıyor
- 3: bağımsız uyguluyor
- 4: debug ve optimize ediyor
- 5: tasarlıyor, öğretiyor ve production'da yönetiyor

Geçiş eşiği 4/5'tir. Her puan commit, test, benchmark, laboratuvar, teknik metin veya sunum kanıtı içermelidir.

## Kanonik kayıtlar

- `00-governance`: ana plan ve protokoller
- `01-skill-matrix`: ölçüm ve kanıtlar
- `02-phases`: faz planları
- `03-weeks`: haftalık planlar ve retrospektifler
- `04-daily-logs`: günlük öğrenme kayıtları
- `05-labs`: kontrollü laboratuvarlar
- `06-verhex-products`: şirket ürün çekirdekleri
- `07-english`: İngilizce çıktıları
- `08-adr`: mimari kararlar
- `09-debug-journal`: hata ve kök neden kayıtları
- `10-assessments`: değerlendirmeler
- `11-portfolio`: tamamlanmış kanıtlar
- `12-resources`: doğrulanmış kaynaklar

## Nihai başarı tanımı

Program sonunda şu cümle teknik kanıtlarla savunulabilmelidir:

> Bir kurumsal sistemin verisini, yetkilerini ve iş akışlarını analiz eder; Python ve TypeScript ile güvenli AI servisleri geliştirir; bunları Linux, Docker, CI/CD ve Kubernetes üzerinde dağıtır; gözlemler, test eder, ölçeklendirir ve müşteriye sürdürülebilir bir ürün olarak teslim ederim.
