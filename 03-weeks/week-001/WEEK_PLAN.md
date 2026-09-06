---
status: active
week: 1
phase: 0
start_date: 2026-09-05
end_date: 2026-09-12
owner: Alperen
required_hours: 19
---

# Week 001 — Tanılama ve Python + Linux + Networking Baseline

## Haftanın ana yeterliliği
Python object/reference/mutability/scope davranışlarını deneyle açıklamak; Linux process ve temel networking davranışını terminalden gözlemlemek; ilk system-design mental modelini oluşturmak.

Bu hafta hız değil doğruluk ölçülür. İlk tahmin ve kritik uygulamalar kullanıcı tarafından yapılır. Codex yalnızca `CODEX_TEACHER_PROTOCOL.md` ve `AI_USAGE_PROTOCOL.md` doğrultusunda Teacher + Socratic Guide + Reviewer rolündedir.

## Zaman bütçesi
Zorunlu haftalık toplam **19 saattir**. Günlük dosyalardaki `estimated_hours` değerleri bu bütçenin kanonik dağılımıdır:

| Gün | Tarih | Zorunlu süre | Odak |
|---:|---|---:|---|
| Day 01 | 5 Eylül | 4 saat | kickoff, environment, Git, Python/Linux/network baseline |
| 6 Eylül | Pazar | 0 | dinlenme / opsiyonel hafif tekrar |
| Day 02 | 7 Eylül | 2.5 saat | object, identity, equality |
| Day 03 | 8 Eylül | 2.5 saat | mutability, copy, argument binding |
| Day 04 | 9 Eylül | 2.5 saat | scope, namespace, closure |
| Day 05 | 10 Eylül | 3 saat | data structures, dependency graph |
| Day 06 | 11 Eylül | 2.5 saat | Linux, networking, first system context |
| Day 07 | 12 Eylül | 2 saat | assessment, teach-back, retrospective |
| **Toplam** | | **19 saat** | |

Docker çalışması bu hafta **opsiyonel bonus diagnostic**tir ve 19 saate dahil değildir. Docker teslimatı veya container bilgisi Week 001 geçiş koşulu değildir.

## Ana çalışma döngüsü
Her ana konu şu sırayla işlenir:

**Explain → Predict → Build → Observe → Break → Debug → Test → Compare → Transfer → Teach Back**

Bir görev yalnızca kod çalıştığı için tamamlanmış sayılmaz.

## Haftanın zorunlu teorik konuları
- Python object / name binding / identity / equality
- mutability, rebinding, shallow/deep copy
- function argument binding
- namespace, LEGB, closure, late binding
- list/dict/set/deque ve temel Big-O sezgisi
- dependency graph, in-degree ve cycle detection
- Linux process, PID, signal, `/proc`, file descriptor
- loopback, socket, port, TCP ve HTTP ilişkisi
- trust boundary ve temel failure-mode düşüncesi

## Zorunlu laboratuvarlar
1. runtime/object identity deneyleri
2. mutability/copy debugging
3. closure/late-binding debugging
4. duplicate analyzer
5. dependency scheduler + cycle detection
6. Linux process/signal gözlemi
7. loopback TCP/HTTP gözlemi
8. ilk system context diagram
9. mini kapalı-kaynak değerlendirme

## Opsiyonel bonus
- Docker lifecycle diagnostic
- ek İngilizce teknik yazı/ses kaydı
- ekstra benchmark

Opsiyonel çalışmalar zorunlu teslimatların önüne geçmez.

## Zorunlu kanıtlar
- kullanıcı tarafından yazılmış kod commitleri
- test çıktıları
- terminal/system gözlemleri
- en az bir debug-journal kaydı
- tahmin → gerçek sonuç karşılaştırmaları
- kendi cümleleriyle teach-back
- baseline assessment
- güncellenmiş skill matrix
- Week 001 assessment
- retrospective

## Week 001 geçiş kriterleri
Week 002'ye geçiş için:

1. Python object/reference/mutability/scope temel mental modeli açıklanmalı.
2. Kritik lab'lar kullanıcı tarafından yazılmış olmalı.
3. En az bir yanlış varsayım debugging ile düzeltilmiş olmalı.
4. Dependency scheduler cycle tespit edebilmeli.
5. Linux process ve network gözlemleri belgelenmiş olmalı.
6. Process → socket → TCP → HTTP zinciri açıklanabilmeli.
7. İlk system context diagram ve en az üç failure mode üretilmiş olmalı.
8. Assessment + retrospective + skill-matrix kanıtla güncellenmiş olmalı.

**Docker bu kriterlerin parçası değildir.**

## Değerlendirme yaklaşımı
Geçiş otomatik değildir. Day 07 sonunda kanıta göre şu kararlardan biri verilir:

- `proceed`
- `proceed-with-reinforcement`
- `repeat-critical-sections`

Mastery seviyesi için uzun vadeli hedef 4/5'tir; Week 001 bir baseline haftasıdır ve her alanda 4/5 beklenmez.
