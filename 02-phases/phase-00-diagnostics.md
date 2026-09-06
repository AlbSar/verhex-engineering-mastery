---
status: active
phase: 0
planned_duration: 1 week
start_date: 2026-09-05
end_date: 2026-09-12
owner: Alperen
---

# Faz 0 — Tanılama ve Çalışma Ortamı

## Amaç

Başlangıç seviyesini varsayımla değil, gözlemlenebilir kanıtlarla ölçmek; 5 Eylül 2026'da başlayan 12 aylık çekirdek mastery programı ve sonrasında devam edecek sürekli mühendislik eğitimi boyunca kullanılacak geliştirme, değerlendirme ve dokümantasyon sistemini kurmak.

Bu faz bir eleme sınavı değildir. Sonraki haftaların zorluk seviyesini doğru kalibre etmek için mevcut zihinsel modelleri, güçlü alanları ve teknik boşlukları görünür kılar.

## Faz sonunda cevaplanacak sorular

1. Python kodunu yalnızca yazabiliyor muyum, yoksa runtime davranışını açıklayabiliyor muyum?
2. Bir problemi veri yapısı, karmaşıklık ve failure mode açısından parçalayabiliyor muyum?
3. Linux, process ve network davranışını terminalden gözlemleyebiliyor muyum?
4. Bir hatayı rastgele değişikliklerle değil, hipotez ve kanıtla çözebiliyor muyum?
5. AI tarafından üretilen kodu denetleyebiliyor muyum ve Codex'i öğretmen/reviewer rolünde tutabiliyor muyum?
6. Teknik bir konuyu yazılı ve sözlü İngilizceyle aktarabiliyor muyum?

## Değerlendirme standardı

Her alan 0–5 ölçeğinde puanlanır:

| Seviye | Kanıt standardı |
|---:|---|
| 0 | Konuya dair kullanılabilir bilgi yok |
| 1 | Terimleri tanıyor ancak bağımsız uygulayamıyor |
| 2 | Rehberle uyguluyor; açıklama ve debugging zayıf |
| 3 | Bağımsız uyguluyor ve temel test yazıyor |
| 4 | Debug, test, trade-off ve production risklerini açıklıyor |
| 5 | Tasarlıyor, optimize ediyor, öğretiyor ve operasyonel olarak yönetiyor |

Başlangıç puanının düşük olması problem değildir. Kanıtsız yüksek puan verilmez.

## Teknik tanılama paketleri

### A. Python çalışma modeli — 25 puan

Ölçülecek başlıklar:

- Object, identity, equality ve reference semantics
- Mutable ve immutable nesneler
- Scope, namespace ve LEGB
- Function object, parameter passing ve closure
- Exception davranışı
- Temel type hints
- Unit test yazımı

Kanıtlar:

- Kısa kavram açıklaması
- Beş küçük kod deneyi
- Bir bozuk kod debugging görevi
- En az üç pytest testi

### B. Algoritmik düşünme — 15 puan

- Problemi girdi, çıktı ve invariant olarak tanımlama
- Big O sezgisi
- List, set, dictionary, stack ve queue seçimi
- Edge case üretimi
- Basit dependency graph yaklaşımı

### C. Git ve mühendislik disiplini — 10 puan

- Repository klonlama
- Branch kullanımı
- Anlamlı commit üretme
- Diff okuma
- Revert ile reset farkını açıklama
- Küçük bir pull request açıklaması yazma

### D. Linux ve networking — 20 puan

- Process, PID, signal ve environment
- File permission, file descriptor, pipe ve redirect
- `/proc` üzerinden process gözlemi
- Port, socket, localhost ve DNS
- Basit TCP/HTTP bağlantısı
- Temel gözlem komutları

Docker bu haftada yalnızca mevcut baseline'ı görmek için opsiyonel gözlem alanıdır; container internals ve production containerization sonraki mastery fazlarında Linux temeli üzerine işlenecektir.

### E. Debugging ve sistem tasarımı — 15 puan

- Belirti ile kök nedeni ayırma
- Hipotez kurma
- Minimum reproducer oluşturma
- Log ve debugger kullanma
- Basit servis mimarisi çizme
- Failure mode ve gözlemlenebilirlik gereksinimi çıkarma

### F. Teknik İngilizce — 15 puan

- Reading: kısa resmî doküman parçası
- Writing: teknik açıklama
- Speaking: teknik anlatım
- Vocabulary: terimleri bağlam içinde kullanma
- Comprehension: kaynağı kendi cümleleriyle özetleme

## Ortam doğrulama kontrol listesi

```bash
wsl --status
python --version
git --version
code --version
```

WSL içinde:

```bash
uname -a
cat /etc/os-release
free -h
df -h
nproc
```

Python araç zinciri:

- Program için seçilen kanonik Python 3.x sürümü
- `uv`
- Ruff
- Pyright veya mypy
- pytest
- debugger/debugpy

Sonraki fazlarda eklenecek ana toolchain:

- Go
- PostgreSQL
- Docker
- Kubernetes
- Node.js/TypeScript
- Java/JVM (enterprise specialization fazında)

## Uygulama sırası

1. Ortam envanteri çıkarılır.
2. Python ve algoritma tanılaması ilk denemede kritik çözüm AI'ya devredilmeden tamamlanır.
3. Linux ve network deneyleri yürütülür.
4. Debugging senaryosu çözülür.
5. İlk küçük system-design değerlendirmesi yapılır.
6. İngilizce yazılı ve sözlü baseline hazırlanır.
7. Kanıtlar `baseline-assessment.md` içine bağlanır.
8. `skill-matrix.yaml` puanları kanıt bağlantılarıyla güncellenir.
9. Haftalık retrospektif hazırlanır.

## Geçiş kriterleri

Faz 0 tamamlanmış sayılmak için:

- Tüm aktif tanılama alanlarında kanıt üretilmiş olmalı.
- Geliştirme ortamı tekrar kurulabilir biçimde belgelenmiş olmalı.
- İlk günlük log ve debug journal kaydı yazılmış olmalı.
- Skill matrix başlangıç puanları kanıtlarla doldurulmuş olmalı.
- Week 002 zorluk seviyesi ölçüm sonuçlarına göre belirlenmiş olmalı.

## Faz çıktıları

- `01-skill-matrix/baseline-assessment.md`
- Güncellenmiş `01-skill-matrix/skill-matrix.yaml`
- `03-weeks/week-001/` günlük teslimatları
- İlk Python/Linux/network laboratuvarları
- İlk debug journal kaydı
- İlk system-design notu
- İngilizce teknik baseline
- Week 001 değerlendirmesi ve retrospektifi
