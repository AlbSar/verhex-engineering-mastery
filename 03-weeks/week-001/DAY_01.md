---
status: ready
day: 1
date: 2026-08-04
estimated_hours: 4.5
---

# Day 01 — Ortam Envanteri, Git ve Başlangıç Kaydı

## Günün amacı

Çalışma ortamını varsayımlarla değil sürüm, kaynak ve çalışma çıktılarıyla doğrulamak; repository'yi yerel geliştirme akışına bağlamak.

## 1. Ortam envanteri — 60 dakika

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

## 2. Repository çalışma akışı — 45 dakika

```bash
git clone https://github.com/AlbSar/verhex-engineering-mastery.git
cd verhex-engineering-mastery
git switch -c learning/week-001
git status
git log --oneline --decorate -10
```

Açıkla:

- Working tree nedir?
- Staging area nedir?
- Commit neyi temsil eder?
- Branch gerçekte neyi işaret eder?

## 3. Python proje alanı — 60 dakika

`05-labs/python/week-001/` altında ilk çalışma alanını kur:

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

## 4. İlk daily log — 30 dakika

`04-daily-logs/2026-08/2026-08-04.md` dosyasını günlük şablondan üret.

Şunları kaydet:

- Ortamda hazır olanlar
- Eksik olanlar
- Kurulum sırasında oluşan hatalar
- Çalışma ortamının riskleri
- Bugünkü teknik varsayımların

## 5. İngilizce baseline başlangıcı — 45 dakika

Başlık:

> My Current Engineering Background and the Purpose of the Verhex Mastery Marathon

İlk 150–200 kelimeyi AI yardımı olmadan yaz. Tam metin Day 07'de 300–500 kelimeye çıkarılacak.

## 6. Commit — 15 dakika

```bash
git add .
git diff --cached
git commit -m "chore: record week 1 environment baseline"
```

Commit öncesi diff'i satır satır oku.

## Teslimatlar

- [ ] Ortam envanteri
- [ ] Yerel repository ve `learning/week-001` branch'i
- [ ] Python çalışma alanı
- [ ] İlk daily log
- [ ] İngilizce tanıtım taslağı
- [ ] İlk anlamlı commit

## Gün sonu kontrol soruları

1. WSL içinde çalışan process'ler hangi kernel üzerinde çalışıyor?
2. `uv run pytest` komutunda `uv` hangi sorumluluğu üstleniyor?
3. Branch neden repository'nin tam kopyası değildir?
4. Bir tool sürümünü kaydetmek neden reproducibility için önemlidir?
