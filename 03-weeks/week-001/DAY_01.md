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

## 1. Ortam envanteri — 45 dakika

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

### Kaydet

- İşletim sistemi ve sürümü
- Python sürümü
- `uv`, Git, Docker, Node sürümleri
- CPU, RAM ve disk görünümü
- Eksik veya hatalı araçlar

## 2. Repository çalışma akışı — 30 dakika

Remote `learning/week-001` branch'i kickoff için hazırlanmıştır. Yerelde:

```bash
git clone https://github.com/AlbSar/verhex-engineering-mastery.git
cd verhex-engineering-mastery
git fetch origin
git switch --track origin/learning/week-001
git status
git log --oneline --decorate -10
```

Repository zaten klonluysa yeniden clone etme; mevcut çalışma ağacında `git fetch origin` ve ardından ilgili branch'e geç.

Kendi cümlelerinle açıkla:

- Working tree nedir?
- Staging area nedir?
- Commit neyi temsil eder?
- Branch gerçekte neyi işaret eder?

## 3. Python proje alanı — 45 dakika

`05-labs/python/week-001/` altında ilk çalışma alanını kendin kur:

```text
week-001/
├── README.md
├── pyproject.toml
├── src/
│   └── week001/
│       └── __init__.py
└── tests/
```

Araçları ekle:

- pytest
- Ruff
- Pyright veya mypy

Doğrulama:

```bash
uv sync
uv run pytest
uv run ruff check .
```

Codex'ten proje dosyalarını senin yerine üretmesini isteme. Önce kendin kur; daha sonra yapı, dependency ve config review iste.

## 4. Python + Linux + Network ilk üçlü baseline — 60 dakika

### Python — 20 dakika

`runtime_probe.py` dosyasını **kendin yaz**. Program şu davranışları göstermeli:

- Bir immutable nesne ve bir mutable nesne oluştur.
- İki ismin aynı nesneye bağlandığı bir örnek üret.
- `id()`, `type()`, `==` ve `is` sonuçlarını gözlemle.
- Çalıştırmadan önce en az üç sonucu tahmin et ve sonra gerçekle karşılaştır.

Codex'e ancak tahminlerini ve sonucu gösterdikten sonra mekanizma review'u yaptır.

### Linux — 20 dakika

```bash
echo $$
ps -fp $$
cat /proc/$$/status | head -40
ls -l /proc/$$/fd | head
```

Kendi cümlelerinle cevapla:

- Shell neden bir process'tir?
- `$$` neyi temsil eder?
- `/proc/<PID>` gerçek bir disk klasörü müdür, yoksa kernel görünümü müdür?
- File descriptor neden önemlidir?

### Network — 20 dakika

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

Kendi cümlelerinle cevapla:

- `127.0.0.1` neyi temsil ediyor?
- `8080` process midir, socket midir, port numarası mıdır?
- `curl` isteğinde client ve server rolleri hangileri?
- TCP bağlantısı kurulmadan HTTP request gönderilebilir mi?

Deney bitince server process'ini kontrollü biçimde sonlandır.

## 5. İlk daily log — 20 dakika

`04-daily-logs/2026-09/2026-09-05.md` dosyası kickoff kaydı olarak branch'e eklenmiştir. Gerçek terminal ve kod sonuçlarınla şu alanları doldur:

- Ortamda hazır olanlar
- Eksik olanlar
- Python tahmin/gerçek sonuçları
- Linux process gözlemleri
- Network gözlemleri
- Kurulum sırasında oluşan hatalar
- Bugünkü yanlış varsayımlar
- Sonraki oturum için açık sorular

## 6. İngilizce baseline başlangıcı — 30 dakika

Başlık:

> My Current Engineering Background and the Purpose of the Verhex Mastery Marathon

İlk 150–200 kelimeyi AI yardımı olmadan yaz. Tam metin Day 07'de 300–500 kelimeye çıkarılacak.

## 7. Commit — 10 dakika

```bash
git add .
git diff --cached
git commit -m "chore: record week 1 engineering baseline"
```

Commit öncesi diff'i satır satır oku. Codex'ten commit öncesinde diff review isteyebilirsin; değişiklikleri sen onayla.

## Teslimatlar

- [ ] Ortam envanteri
- [ ] Yerel repository ve `learning/week-001` branch'i
- [ ] Python çalışma alanı
- [ ] `runtime_probe.py` ve tahmin/sonuç kaydı
- [ ] Linux process gözlemi
- [ ] Loopback HTTP/network gözlemi
- [ ] Doldurulmuş daily log
- [ ] İngilizce tanıtım taslağı
- [ ] İlk anlamlı kullanıcı commit'i

## Gün sonu kontrol soruları

1. WSL içinde çalışan process'ler hangi kernel üzerinde çalışıyor?
2. `uv run pytest` komutunda `uv` hangi sorumluluğu üstleniyor?
3. Branch neden repository'nin tam kopyası değildir?
4. Bir tool sürümünü kaydetmek neden reproducibility için önemlidir?
5. `python -m http.server` başladığında process, socket, port ve HTTP katmanları nasıl birbirine bağlanır?
6. Python'da bir isim ile nesne arasındaki ilişkiyi “değişken kutudur” modeli neden eksik açıklar?
