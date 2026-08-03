---
status: ready
day: 6
date: 2026-08-09
estimated_hours: 5
---

# Day 06 — Linux, Network, Docker ve Sistem Tasarımı Tanılaması

## Günün amacı

Bir uygulamanın process, port, signal ve container seviyesinde nasıl yaşadığını gözlemlemek; Verhex AI Integration Node için ilk sistem bağlamını çizmek.

## 1. Linux process deneyi — 60 dakika

Bir Python process başlat:

```bash
python -m http.server 8080
```

Başka terminalde:

```bash
ps aux | grep http.server
pgrep -af http.server
ls -l /proc/<PID>/fd
cat /proc/<PID>/status
tr '\0' '\n' < /proc/<PID>/environ
```

Ardından:

```bash
kill -TERM <PID>
```

Açıkla:

- PID nedir?
- File descriptor neyi temsil eder?
- Environment process'e nasıl taşınır?
- SIGTERM ile SIGKILL arasındaki operasyonel fark nedir?

## 2. Network deneyi — 45 dakika

```bash
ss -lntp
curl -v http://127.0.0.1:8080
getent hosts localhost
ip addr
ip route
```

Açıkla:

- `0.0.0.0`, `127.0.0.1` ve belirli interface IP'sine bind etmek
- Listening socket
- Client connection
- DNS çözümleme
- Host ile WSL network sınırı

## 3. Docker lifecycle deneyi — 75 dakika

Basit container çalıştır:

```bash
docker run --name week1-nginx -d -p 8081:80 nginx:alpine
docker ps
docker inspect week1-nginx
docker top week1-nginx
curl -v http://localhost:8081
docker stop week1-nginx
docker rm week1-nginx
```

İncele:

- Image ve container farkı
- Ana process
- Port publish
- Container IP'si
- Stop sırasında signal davranışı
- Writable layer

Ek deney:

- Bind mount
- Named volume
- Read-only filesystem
- Memory limiti

## 4. Sistem tasarımı — 90 dakika

İlk bağlam diyagramını hazırla:

> Müşteri ortamında IFS/Oracle ile cloud LLM arasında çalışan Verhex Enterprise AI Integration Node

Zorunlu bileşenler:

- ERP/Oracle trust boundary
- Integration node
- Connector/listener
- AuthN/AuthZ
- Queue/worker
- Tool registry
- Audit log
- Model gateway
- Secret store
- Monitoring
- Human approval

Zorunlu sorular:

1. Integration node neden ana ERP sunucusundan ayrıştırılmalı?
2. Database credential nerede tutulmalı?
3. Hangi işlemler read-only başlamalı?
4. Tool execution için idempotency nasıl sağlanmalı?
5. Cloud model erişimi kesilirse sistem nasıl degrade olmalı?

## 5. İngilizce — 30 dakika

İngilizce 200 kelime:

> Explain why a container is not a virtual machine.

## Teslimatlar

- [ ] Process ve signal gözlem notları
- [ ] Network komut çıktıları
- [ ] Docker lifecycle notu
- [ ] İlk sistem bağlam diyagramı
- [ ] En kritik beş failure mode
- [ ] İngilizce container açıklaması

## Geçiş kontrolü

Container içindeki `localhost` ile host üzerindeki `localhost` neden her zaman aynı network namespace'i göstermez, açıklayabilmelisin.
