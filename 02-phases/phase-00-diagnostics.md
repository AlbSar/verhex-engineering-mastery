---
status: active
phase: 0
planned_duration: 1 week
start_date: 2026-08-04
end_date: 2026-08-10
owner: Alperen
---

# Faz 0 — Tanılama ve Çalışma Ortamı

## Amaç

Başlangıç seviyesini varsayımla değil, gözlemlenebilir kanıtlarla ölçmek; 36 haftalık program boyunca kullanılacak geliştirme, değerlendirme ve dokümantasyon sistemini kurmak.

Bu faz bir eleme sınavı değildir. Sonraki haftaların zorluk seviyesini doğru kalibre etmek için mevcut zihinsel modelleri, güçlü alanları ve teknik boşlukları görünür kılar.

## Faz sonunda cevaplanacak sorular

1. Python kodunu yalnızca yazabiliyor muyum, yoksa runtime davranışını açıklayabiliyor muyum?
2. Bir problemi veri yapısı, karmaşıklık ve failure mode açısından parçalayabiliyor muyum?
3. Linux, process, network ve container davranışını terminalden gözlemleyebiliyor muyum?
4. Bir hatayı rastgele değişikliklerle değil, hipotez ve kanıtla çözebiliyor muyum?
5. AI tarafından üretilen kodu denetleyebiliyor muyum?
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

Ölçülecek başlıklar:

- Problemi girdi, çıktı ve invariant olarak tanımlama
- Big O sezgisi
- List, set, dictionary, stack ve queue seçimi
- Edge case üretimi
- Basit dependency graph yaklaşımı

Kanıtlar:

- İki algoritma sorusu
- Bir veri yapısı seçimi savunması
- Karmaşıklık analizi

### C. Git ve mühendislik disiplini — 10 puan

- Repository klonlama
- Branch oluşturma
- Anlamlı commit üretme
- Diff okuma
- Revert ile reset farkını açıklama
- Küçük bir pull request açıklaması yazma

### D. Linux, network ve Docker — 20 puan

- Process, PID, signal ve environment
- File permission ve pipe
- Port, socket, localhost ve DNS
- Container ile sanal makine farkı
- Image, layer, volume ve network
- Temel gözlem komutları

Kanıtlar:

- Terminal komut çıktıları
- Bir process gözlem deneyi
- Bir port/network deneyi
- Bir container lifecycle deneyi

### E. Debugging ve sistem tasarımı — 15 puan

- Belirti ile kök nedeni ayırma
- Hipotez kurma
- Minimum reproducer oluşturma
- Log ve debugger kullanma
- Basit servis mimarisi çizme
- Failure mode ve gözlemlenebilirlik gereksinimi çıkarma

### F. Teknik İngilizce — 15 puan

- Reading: kısa resmî doküman parçası
- Writing: 300 kelimelik teknik tanıtım
- Speaking: 5 dakikalık teknik anlatım
- Vocabulary: terimleri bağlam içinde kullanma
- Comprehension: okunan kaynağı kendi cümleleriyle özetleme

## Ortam doğrulama kontrol listesi

Aşağıdaki bileşenler sürüm çıktılarıyla kanıtlanır:

```bash
wsl --status
python --version
uv --version
git --version
docker --version
docker compose version
node --version
npm --version
code --version
```

WSL içinde ayrıca:

```bash
uname -a
cat /etc/os-release
free -h
df -h
nproc
```

Python araç zinciri:

- Python 3.12 veya program boyunca seçilen kanonik sürüm
- `uv`
- Ruff
- Pyright veya mypy
- pytest
- debugpy veya IDE debugger

Servis bağımlılıkları:

- Docker
- PostgreSQL
- Redis

## Uygulama sırası

1. Ortam envanteri çıkarılır.
2. Python ve algoritma tanılaması AI yardımı olmadan tamamlanır.
3. Linux, network ve Docker deneyleri yürütülür.
4. Debugging senaryosu çözülür.
5. İngilizce yazılı ve sözlü teslimatlar hazırlanır.
6. Kanıtlar `baseline-assessment.md` içine bağlanır.
7. `skill-matrix.yaml` puanları kanıt bağlantılarıyla güncellenir.
8. Haftalık retrospektif hazırlanır.

## Geçiş kriterleri

Faz 0 tamamlanmış sayılmak için:

- Tüm tanılama alanlarında kanıt üretilmiş olmalı.
- Geliştirme ortamı tekrar kurulabilir biçimde belgelenmiş olmalı.
- İlk günlük log ve debug journal kaydı yazılmış olmalı.
- Skill matrix başlangıç puanları kanıtlarla doldurulmuş olmalı.
- Week 002 zorluk seviyesi ölçüm sonuçlarına göre belirlenmiş olmalı.

## Faz çıktıları

- `01-skill-matrix/baseline-assessment.md`
- Güncellenmiş `01-skill-matrix/skill-matrix.yaml`
- `03-weeks/week-001/` günlük teslimatları
- İlk Python CLI laboratuvarı
- İlk debug journal kaydı
- İngilizce teknik tanıtım
- Week 001 değerlendirmesi ve retrospektifi
