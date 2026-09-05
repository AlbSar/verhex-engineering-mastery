---
status: active
day: 1
date: 2026-09-05
estimated_hours: 4
---

# Day 01 — Ortam Envanteri, Git ve Başlangıç Kaydı

## Günün amacı
Çalışma ortamını varsayımlarla değil sürüm, kaynak ve çalışma çıktılarıyla doğrulamak; repository'yi yerel geliştirme akışına bağlamak ve Python + Linux + network için ilk gözlemlenebilir baseline'ı üretmek.

Codex bu oturumda öğretmen ve reviewer'dır. Kritik kodu kullanıcı yazar; Codex mekanizmayı açıklar, hipotezleri sorgular, diff/test review yapar ve yanlış zihinsel modelleri görünür kılar.

> **Zaman bütçesi:** Bu günün toplam zorunlu bütçesi 4 saattir. Alt bölüm süreleri üst sınırdır; kurulum hızlı biterse kalan süre derinleşme veya notlara aktarılır. 4 saat aşıldığında ek işler ertesi güne taşınır.

## 1. Ortam envanteri — en fazla 40 dakika

Windows PowerShell:
```powershell
wsl --status
wsl --version
```

WSL Ubuntu:
```bash
uname -a
cat /etc/os-release
python --version
uv --version
git --version
docker --version
docker compose version
node --version
npm --version
free -h
df -h
nproc
```

Kaydet: işletim sistemi, Python/uv/Git/Node sürümleri, CPU/RAM/disk görünümü ve eksik araçlar. Docker mevcutsa sürümü kaydet; yoksa Week 001 için zorunlu değildir.

## 2. Repository çalışma akışı — en fazla 30 dakika
Repository zaten klonluysa yeniden clone etme. Önce:

```bash
git fetch origin
git status
git branch -vv
git log --oneline --decorate --graph --all -12
```

Yerel branch remote'dan ayrışmışsa körlemesine reset/rebase yapma. Commit grafiğini incele ve kullanıcı çalışmalarını koruyan entegrasyon planı çıkar.

Kendi cümlelerinle açıkla: working tree, staging area, commit ve branch pointer.

## 3. Python proje alanı — en fazla 40 dakika
`05-labs/python/week-001/` altında çalışma alanını kendin kur. Minimum:

```text
week-001/
├── README.md
├── pyproject.toml
├── src/
└── tests/
```

pytest + Ruff ve seçilen type checker'ı doğrula. Codex proje dosyalarını senin yerine üretmez; yapı review yapar.

## 4. Python + Linux + Network baseline — 75 dakika

### Python
`runtime_probe.py` dosyasını **kendin yaz**:
- immutable + mutable örnek
- iki ismin aynı nesneye bağlanması
- `id()`, `type()`, `==`, `is`
- çalıştırmadan önce en az üç tahmin

### Linux
```bash
echo $$
ps -fp $$
cat /proc/$$/status | head -40
ls -l /proc/$$/fd | head
```

Açıkla: shell neden process, `$$`, `/proc/<PID>` ve file descriptor.

### Network
Bir terminalde:
```bash
python -m http.server 8080 --bind 127.0.0.1
```
Başka terminalde:
```bash
ss -lntp | grep 8080
curl -v http://127.0.0.1:8080/
getent hosts localhost
```

Açıkla: loopback, port, listening socket, client/server ve TCP → HTTP ilişkisi.

## 5. Daily log + teach-back — 45 dakika
`04-daily-logs/2026-09/2026-09-05.md` içine gerçek sonuçları kaydet:
- ortam
- tahmin/gerçek farkları
- Linux/network gözlemleri
- hatalar
- yanlış varsayımlar
- açık sorular

Kısa teach-back:
> Process → socket → TCP → HTTP → application zinciri nasıl bağlanır?

## 6. Commit — en fazla 10 dakika
```bash
git add .
git diff --cached
git commit -m "chore: record week 1 engineering baseline"
```

## Zorunlu teslimatlar
- [ ] Ortam envanteri
- [ ] Güvenli local/remote Git durum analizi
- [ ] Python çalışma alanı
- [ ] `runtime_probe.py` + tahmin/sonuç
- [ ] Linux process gözlemi
- [ ] Loopback HTTP/network gözlemi
- [ ] Daily log
- [ ] İlk anlamlı kullanıcı commit'i

## Opsiyonel
- [ ] Docker sürüm/kurulum kontrolü
- [ ] Teknik İngilizce kısa notu

## Gün sonu kontrolü
1. Branch neden repository'nin tam kopyası değildir?
2. `/proc` hangi bilgiyi nereden üretir?
3. `python -m http.server` başladığında process, socket, port ve HTTP nasıl bağlanır?
4. Python'da name → object modelini açıklayabilir misin?
