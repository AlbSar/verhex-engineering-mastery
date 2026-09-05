---
status: active
week: 1
phase: foundations
start_date: 2026-09-05
end_date: 2026-09-12
owner: Alperen
---

# Week 001 — Baseline: Python + Linux + Networking

## Haftanın ana yeterliliği

İlk hafta amaç hız değil, gerçek başlangıç seviyesini kanıtla görmek ve üç temel katmanı birbirine bağlamaktır:

- Python'da object/reference/mutability davranışı
- Linux'ta process/PID/file descriptor/`/proc` gözlemi
- Network'te process → socket → TCP → HTTP zinciri

Git çalışma modeli ve toolchain de baseline olarak doğrulanır.

## Codex çalışma prensibi

Codex Teacher + Reviewer'dır. Kritik öğrenme kodunu kullanıcı yazar. Codex:

- mekanizmayı açıklar,
- küçük ipuçları verir,
- yanlış mental modeli arar,
- kodu review eder,
- test ve failure senaryosu önerir,
- production farklarını gösterir.

Tam kurallar: `00-governance/CODEX_TEACHER_PROTOCOL.md`.

## Haftalık zaman bütçesi

Sürdürülebilir hedef 18–20 saattir. Şirket veya sağlık gibi olağanüstü yüklerde minimum ritim korunur; plan başarısız sayılmaz, evidence bir sonraki güne taşınır.

| Alan | Hedef süre |
|---|---:|
| Kavram / kaynak okuma | 4 saat |
| Kodlama ve laboratuvar | 7 saat |
| Linux/network gözlemi | 3 saat |
| Test + debugging | 3 saat |
| Dokümantasyon / retrospektif | 2 saat |
| **Toplam** | **19 saat** |

Teknik İngilizce günlük çıktılara doğal biçimde eklenir; ayrı saat kotası ilk haftada zorunlu değildir.

## Takvim

- 5 Eylül Cumartesi: Day 01 — kickoff, environment ve system baseline
- 6 Eylül Pazar: hafif tekrar / eksik evidence tamamlama
- 7–12 Eylül: temel Python + Linux + networking lab'ları ve assessment

## Günlük akış

| Gün | Odak | Ana teslimat |
|---:|---|---|
| 1 | Ortam, Git, process/socket baseline | Toolchain inventory, `runtime_probe.py`, terminal evidence |
| 2 | Object, identity, equality | Python deney seti + kendi açıklaması |
| 3 | Mutability, copy, parameter passing | Hatalı varsayım + test + debug journal |
| 4 | Scope, namespace, function, closure | Closure lab + explanation |
| 5 | Veri yapıları, Big O, küçük CLI | Typed/deterministic Python CLI |
| 6 | Linux process + networking | `/proc`, fd, socket, TCP/HTTP gözlemleri |
| 7 | Assessment + system-design giriş | Baseline score, ilk architecture case, retrospective |

## Haftanın teorik konuları

### Python
- object ve name binding
- identity vs equality
- mutable/immutable
- hashability
- shallow/deep copy
- parameter passing modeli
- scope/namespace/LEGB
- functions/closures
- temel collections ve Big O sezgisi

### Linux
- user space / kernel space giriş
- process ve PID
- parent/child ilişkisi
- file descriptor
- stdin/stdout/stderr
- `/proc`
- signal giriş

### Networking
- IP ve loopback
- port
- socket
- TCP connection
- client/server
- HTTP request/response'un TCP üzerinde taşınması
- DNS'in zincirdeki yeri

### Git
- commit object ve DAG zihinsel modeli
- working tree / index / repository
- branch pointer
- merge/rebase kavramsal farkı

## Haftanın zorunlu laboratuvarları

1. `runtime_probe.py` — PID/PPID/runtime bilgisi
2. Object identity/mutability deneyleri
3. Mutable default argument veya benzeri gerçek Python bug'ını debug etme
4. `/proc/<pid>` ve file descriptor gözlemi
5. Python TCP echo server/client
6. Minimal HTTP server veya raw HTTP gözlemi
7. Küçük typed CLI
8. İlk system-design mini case: tek servisli uygulamanın request path diyagramı

Docker bu hafta ana öğrenme hedefi değildir. Sadece mevcut kurulum ve temel lifecycle tanılaması yapılabilir; namespaces/cgroups ilerleyen Linux/Container fazında derinleştirilir.

## Zorunlu evidence

- kendi yazdığı kritik kod
- terminal çıktıları
- pytest veya uygun test çıktısı
- en az 1 debug journal
- en az 1 "çalıştırmadan önce tahmin / sonra gözlem" kaydı
- kendi cümleleriyle Python + process + socket açıklaması
- skill-matrix baseline
- week retrospective

## Geçiş kriterleri

Week 002'ye geçiş için öğrenci:

1. Python'da name → object/reference ilişkisini doğru açıklayabilmeli.
2. Mutable ve immutable davranışı kodla gösterebilmeli.
3. Çalışan bir Python process'ini Linux terminalinden PID, `/proc` ve fd perspektifinden gözlemleyebilmeli.
4. Bir server process'inin socket açıp TCP üzerinden request aldığını açıklayabilmeli ve lab ile göstermeli.
5. En az bir gerçek bug için symptom → hypothesis → evidence → root cause → regression test zinciri üretmeli.
6. Git commit/branch modelini dosya kopyası gibi değil graph/pointer modeliyle anlatabilmeli.
7. Eksiklerini dürüstçe `partial/not-proven` olarak kaydetmeli.

## İlk system-design soruları

Hafta sonunda şu sorular cevaplanmalıdır:

- Client'tan Python servisine request hangi katmanlardan geçiyor?
- Process ölürse ne kaybolur, ne kalır?
- Aynı porta neden iki process normalde bind edemez?
- Database eklendiğinde state nerede yaşamaya başlar?
- Latency'nin hangi parçaları network, application ve data katmanından gelir?

## Başarı tanımı

Week 001'in amacı "çok konu bitirmek" değildir. Başarılı hafta şu durumda oluşur:

> Öğrenci ilk kez Python kodunu yalnızca dil olarak değil; Linux process'i ve network participant'ı olarak gözlemlemeye başlamış, yanlış mental modellerini kaydetmiş ve sonraki haftalar için güvenilir baseline üretmiştir.
