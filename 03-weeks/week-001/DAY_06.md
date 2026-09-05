---
status: ready
day: 6
date: 2026-09-11
estimated_hours: 2.5
---

# Day 06 — Linux, Network ve İlk Sistem Tasarımı Tanılaması

## Günün amacı
Bir uygulamanın process, port, signal ve network seviyesinde nasıl yaşadığını gözlemlemek; ilk sistem bağlamını çizmek.

Docker bu hafta **opsiyonel bonus diagnostic**tir. Week 001 geçiş koşulu değildir.

## 1. Linux process deneyi — 45 dakika
Bir Python HTTP server başlat ve başka terminalden gözlemle:

```bash
python -m http.server 8080
ps aux | grep http.server
pgrep -af http.server
ls -l /proc/<PID>/fd
cat /proc/<PID>/status
kill -TERM <PID>
```

Açıkla:
- PID
- file descriptor
- process environment
- SIGTERM vs SIGKILL

## 2. Network deneyi — 35 dakika
```bash
ss -lntp
curl -v http://127.0.0.1:8080
getent hosts localhost
ip addr
ip route
```

Açıkla:
- loopback
- bind address
- listening socket
- client connection
- DNS çözümleme
- host/WSL network sınırı

## 3. Sistem tasarımı — 55 dakika
İlk bağlam diyagramını hazırla:

> Müşteri ortamında IFS/Oracle ile cloud LLM arasında çalışan Verhex Enterprise AI Integration Node

Minimum bileşenler:
- ERP/Oracle trust boundary
- integration node
- connector/listener
- AuthN/AuthZ
- tool execution
- audit log
- model gateway
- secret store
- monitoring
- human approval

Cevapla:
1. Trust boundary nerede?
2. Credential nerede tutulmalı?
3. Hangi işlemler read-only başlamalı?
4. En kritik üç failure mode nedir?
5. Cloud model erişimi kesilirse nasıl degrade olmalı?

## 4. Teach-back ve log — 15 dakika
Process → socket → TCP → HTTP → application zincirini kendi cümlelerinle açıkla.

## Opsiyonel bonus — Docker diagnostic (en fazla 45 dakika, haftalık 19 saate dahil değil)
Vakit ve enerji varsa tek bir container çalıştırıp image/container, main process ve port publish ilişkisini gözlemle. Bu bölüm tamamlanmazsa Week 001 geçişini etkilemez.

## Zorunlu teslimatlar
- [ ] Process/signal gözlemi
- [ ] Network gözlemi
- [ ] İlk sistem bağlam diyagramı
- [ ] Üç failure mode
- [ ] Teach-back notu
- [ ] Daily log

## Opsiyonel teslimat
- [ ] Docker lifecycle kısa notu
