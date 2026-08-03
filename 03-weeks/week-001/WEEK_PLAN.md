---
status: active
week: 1
phase: 0
start_date: 2026-08-04
end_date: 2026-08-10
owner: Alperen
---

# Week 001 — Tanılama ve Python Çalışma Modeli

## Haftanın ana yeterliliği

Python'da object, identity, reference, mutability, scope ve function davranışlarını deneylerle açıklamak; mevcut Linux, Git, Docker, debugging ve teknik İngilizce seviyesini kanıtlarla ölçmek.

## Haftanın çalışma prensibi

Bu hafta hız değil doğruluk ölçülecek. İlk denemeler AI yardımı olmadan yapılır. AI daha sonra açıklama, code review, test boşluğu ve kavramsal doğrulama için kullanılır.

## Haftalık zaman bütçesi

| Alan | Hedef süre |
|---|---:|
| Teknik teori | 6 saat |
| Kodlama ve laboratuvar | 9 saat |
| Debugging ve test | 4 saat |
| Linux/Git/Docker tanılama | 3 saat |
| Teknik İngilizce | 4,5 saat |
| Dokümantasyon ve retrospektif | 2,5 saat |
| **Toplam** | **29 saat** |

## Günlük akış

| Gün | Odak | Ana teslimat |
|---:|---|---|
| 1 | Ortam envanteri ve Git | Doğrulanmış toolchain, ilk branch ve daily log |
| 2 | Object, identity, equality | Deney dosyası ve kavram açıklaması |
| 3 | Mutability, copy, parameter passing | Hata örnekleri, testler ve debug kaydı |
| 4 | Scope, namespace, function, closure | Closure laboratuvarı ve late-binding analizi |
| 5 | Veri yapıları ve algoritmik tanılama | Duplicate analizi ve dependency scheduler |
| 6 | Linux, network, Docker ve sistem tasarımı | Terminal deneyleri ve ilk mimari diyagram |
| 7 | İngilizce, sınav ve retrospektif | Baseline puanları, sunum ve Week 002 kararı |

Ayrıntılı görevler aynı klasördeki `DAY_01.md`–`DAY_07.md` dosyalarındadır.

## Haftanın teorik konuları

- Python object modeli
- Name binding ve reference semantics
- Identity ve equality
- Mutable ve immutable nesneler
- Hashability
- Shallow copy ve deep copy
- Scope, namespace ve LEGB
- Function object
- Default argument evaluation
- Closure ve late binding
- List, tuple, dictionary ve set seçimleri
- Big O başlangıç sezgisi
- Process, PID, signal, port ve container lifecycle

## Haftanın laboratuvarları

1. Object identity deney seti
2. Mutable default argument debugging
3. Shallow/deep copy analizi
4. Closure ve late binding laboratuvarı
5. Typed record normalization fonksiyonu
6. Duplicate customer analyzer
7. Dependency graph ve cycle detection
8. Linux process/signal deneyi
9. Docker lifecycle deneyi
10. Küçük Python CLI uygulaması

## Verhex bağlantısı

Hafta sonunda geliştirilecek küçük CLI, ileride `verhex-python-core` içinde kullanılabilecek şu davranışları taşımalıdır:

- Typed input modeli
- Validation
- Structured error
- Deterministic output
- Unit test
- Temel structured logging

Önerilen CLI konusu:

> JSON veya CSV müşteri kayıtlarını okuyup doğrulayan, duplicate kayıtları raporlayan ve hatalı satırları ayrı çıktıya yazan `verhex-record-audit` aracı.

## İngilizce teslimatları

- 300–500 kelimelik teknik tanıtım
- Resmî Python dokümanından 150 kelimelik özet
- 10 teknik ifade ve örnek cümle
- 5 dakikalık sesli anlatım
- Kısa İngilizce pull request açıklaması

## Zorunlu kanıtlar

- Kod commitleri
- pytest sonucu
- Ruff/type-check sonucu
- Terminal çıktıları
- En az bir debug journal kaydı
- Baseline assessment
- Güncellenmiş skill matrix
- Week assessment
- Retrospective

## Geçiş kriterleri

Week 001 tamamlanmış sayılmak için:

- Object/reference/mutability kavramları kendi cümleleriyle doğru açıklanmalı.
- En az 5 Python deneyi ve 8 unit test tamamlanmalı.
- En az 3 hatalı varsayım debugging yoluyla düzeltilmeli.
- Dependency graph çözümü cycle tespit etmeli.
- Linux process ve Docker lifecycle deneyleri belgelenmeli.
- İngilizce yazılı ve sözlü baseline teslim edilmeli.
- Skill matrix kanıta dayalı başlangıç puanlarıyla güncellenmeli.

## Haftalık değerlendirme ağırlıkları

| Alan | Ağırlık |
|---|---:|
| Kavramsal doğruluk | %25 |
| Kod kalitesi | %20 |
| Test ve debugging | %20 |
| Sistem gözlemi | %15 |
| Teknik dokümantasyon | %10 |
| Teknik İngilizce | %10 |

## Başarı eşiği

Bu hafta için geçme notu bir “başarı/başarısızlık” kararı değildir. Ama Week 002'ye geçmek için tüm zorunlu teslimatlar tamamlanmalı ve kritik kavramsal yanlışlar listelenmiş olmalıdır.
