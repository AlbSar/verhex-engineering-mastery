# Resource flow — kaynak → öğrenme → kanıt

Kanonik akış:

developer-roadmap → official / primary documentation → explanation → structured practice when useful → small experiment → build-your-own when high leverage → production implementation → own lab → real project transfer → evidence → reflection

Her kaynak için hedef, belirli bölüm, prerequisite, deney ve beklenen artefact kaydedilir. Sadece link listesi ders değildir. İlk açıklama ve okuma süreleri Day bütçesinin içindedir. OPTIONAL adım seçilmezse nedenini yaz; tüm repo/kursu bitirmek zorunlu değildir. Aktif seçimler: [Week 001 cards](WEEK_001.md), [command primer](COMMAND_PRIMER.md).

## Kanonik altı referans

Aşağıdaki roller müfredat tasarım kararıdır. Repository erişimleri 2026-09-07 web denetiminde doğrulandı; içerik değişebilir, bir lab açılırken bölüm ve sürüm yeniden doğrulanır.

| Kaynak | Rol ve seçilmiş bölüm | Deney / evidence bağlantısı |
|---|---|---|
| [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | Direction: README Python/Linux/Git/Backend roadmap girişleri; kapsam ve prerequisite sırası | Öğretmen aktif haftanın prerequisite haritasını çıkarır; çıktı Week plan'dır. Harita kopyalanmaz |
| [freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | Structured learning: README Certifications → Python; aktif hedef için list/loop alt dersi seçimi | Öğretilen list/loop için tek ek pratik; çıktı kullanıcı lab/test. OPTIONAL; bölüm/sürüm bulunmadan egzersiz atanmaz |
| [awesome](https://github.com/sindresorhus/awesome) | Discovery: README Programming Languages / Python bölümü | Öğretmen bir primary kaynak adayını uygunluk ve alternatifle karşılaştırır; kaynak kartı. Öğrenciye liste tüketme ödevi yok |
| [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | Construction: README Build your own Web Server / Shell / Database / Neural Network kategorileri | Phase A TCP/HTTP veya shell, Phase B KV, Phase F neural mini lab. Her açılışta tek tutorial yolu/commit seçilir, kullanıcı implementasyonu + production farkı kaydedilir |
| [system-design-primer](https://github.com/donnemartin/system-design-primer) | Trade-offs: README Performance vs scalability, Latency vs throughput, Availability vs consistency; sonra caching/queues/replication | Day 06 hafif request path; Phase E capacity/failure vakaları. Diagram + ADR; teknoloji listesini ezberletme |
| [Linux](https://github.com/torvalds/linux) | Production internals: `Documentation/filesystems/proc.rst`, `fs/proc/base.c`; sonra ilgili subsystem | Önce /proc kavramı ve resmî doküman, sonra bir PID sorgusu yolu; source note + lab karşılaştırması. Week 001 kod okuma REFERENCE |

## Problemden teknolojiye

Everything is a trade-off.

requirement → constraints → workload → failure model → consistency → latency → scale → architecture → technology selection

Kafka/Redis/Kubernetes bir başlangıç cevabı değildir. Seçimden önce problem, ölçü, failure ve maliyet gerekçesi gerekir.

## Build-your-own ve source reading

High-leverage adaylar: CLI, shell, HTTP server, TCP service, key-value store, database, Git subset, Redis subset, container, interpreter, neural network, küçük transformer/LLM. Bunlar opsiyon havuzu; her biri otomatik görev değildir. Önce production karşılığını ve gereken bilgiyi açıkla, sonra küçük lab; correctness/concurrency/durability/security/observability/performance/recovery farklarını yaz.

Source reading: soru → kavram → resmî documentation → subsystem/entry point → tek execution/data path → ilgili test → architecture özeti → lab'a dönüş. Linux ana production laboratuvarıdır. Scheduler için scheduler dokümanı, TCP için network dokümanı, containers için namespaces/cgroups ön koşuldur. İlgili test bulunamazsa bulunamadığını kaydet; varmış gibi gösterme.

CPython/PostgreSQL/Redis/Git/Kubernetes/nginx/LLVM ileri ihtiyaç adaylarıdır; aktif soru yokken yeni zorunlu kaynak eklenmez. Source kartına commit/tag ve satır değil fonksiyon/path kaydet; değişken upstream line numarasını kanonik yapma.

## Kaynak kartı sözleşmesi

ID; REQUIRED/OPTIONAL/STRETCH/REFERENCE; phase/day; learning outcome; prior knowledge state; URL + section + version/date; teacher explanation; tiny experiment; expected evidence path; production comparison; transfer constraint; validation status. `templates/RESOURCE_CARD_TEMPLATE.md` kullanılabilir. Erişim hatası dead link kanıtı değildir; pending yaz ve primary alternatif sun.

## Üretime transfer

Lab → açıklama → kontrollü real project → failure/trade-off → teoriye dönüş. Production'a deney kodu otomatik yazılmaz. Notebook/AI özetleri referanstır; primary kaynağın veya kullanıcının açıklamasının yerine geçmez.
