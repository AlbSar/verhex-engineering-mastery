---
status: ready
day: 6
date: 2026-09-11
estimated_hours: 2.5
---

# Day 06 — Process, socket ve HTTP bağlantısı

## Oturum sözleşmesi
Öğretmen önce [concept-state](../../01-skill-matrix/concept-state.yaml) kaydını okur; kaydı olmayan ön koşulu UNKNOWN sayar. Today → Teach → Mechanism → Example → Predict → Lab → Observe → Review → Teach Back → Evidence sırası uygulanır. Her yeni komut/API/flag açıklanır; tek seferde yalnızca bir görev verilir. Kaynak okuma, açıklama, test ve kayıt aşağıdaki sürelere dahildir. Süre dolunca kalan required konu sonraki oturuma taşınır; tarihe göre atlanmaz. OPTIONAL/STRETCH ek süreleri ayrı kaydedilir ve geçiş koşulu değildir.

Kaynak bölümü, deney ve artefact: [Week 001 kaynak kartları](../../12-resources/WEEK_001.md). Komutlar için [ilk kullanım kartları](../../12-resources/COMMAND_PRIMER.md); kartı sadece linklemek öğretim yerine geçmez.

## Today
REQUIRED hedef: bir local HTTP isteğinin process/socket/TCP/HTTP yolunu gözlemek. Ön koşullar: terminal/shell, program başlatma, argüman, stdout. Socket, PID, fd, HTTP, `ps`, `ss`, `curl`, `kill` bilgisi varsayılmaz.

## 1. Teach ve minimal model — 45 dakika
Process çalışan program örneğidir; PID kimliğidir. File descriptor process'in açık I/O kaynaklarına erişim numarasıdır. Socket ağ iletişimi uç noktasıdır; bind yerel adres/port seçer, listen bağlantı bekler, accept bağlı socket verir. TCP byte stream taşır; HTTP request/response bu byte'lara anlam verir. İlk olarak client → loopback → server çizimi göster.
Komut kartlarıyla `python -m http.server 8080 --bind 127.0.0.1`, `ps -p PID -o pid,comm`, `ss -lnt`, `curl -v`, `kill -TERM PID` ve gerekirse `ls -l /proc/PID/fd` tanıtılır. PID metni gerçek gözlemlenen kimlikle değiştirilir; tahmin edilmez.

## 2. Lab ve observation — 50 dakika
Kullanıcı yalnızca lab klasöründe bir terminalden loopback HTTP server başlatır; ikinci terminalden port ve HTTP isteğini gözler. Server çalışırken önce başarılı `curl` kanıtı alınır. PID bir kez öğretildikten sonra server'ın PID'si gözlemlenir; `/proc` fd gösterimi öğretmen eşliğinde yapılır.
Kaydet: dinleyen adres/port, HTTP status, server logu ve bir fd örneği. API çağrılarının gerçek implementation'ını yazma Phase A'nın sonraki lab'ıdır. Kaynak kartı NET-PROC.

## 3. Failure ve recovery — 25 dakika
Öğrenci yalnızca kendi lab server'ına SIGTERM gönderir, sonra aynı isteği tekrarlar. Önce beklenen bağlantı hatasını tahmin eder; çıkış kodu ve mesajı gözler. Yeniden server başlatıp aynı isteğin düzelmesini doğrular. Böylece sunucu kapalıyken yanlışlıkla başarı bekleyen eski sıra ortadan kalkar.

## 4. Hafif system context ve evidence — 30 dakika
Client → local service → response diyagramı; process ölümü, port çakışması ve bağlantı hatasından iki failure mode. Requirement → constraints → workload → failure model → consistency → latency → scale → architecture → technology selection sırasını küçük ölçekte tanıt. Henüz queue/Kubernetes/enterprise gateway seçtirme. Kaynak kartı DESIGN-INTRO. Log, diagram ve teach-back kaydet.

## REQUIRED evidence
Process/port/HTTP gözlemi, stop/restart failure ve recovery, küçük request-path diagramı, iki failure mode.

## OPTIONAL / STRETCH / REFERENCE
OPTIONAL: Docker diagnostic, en fazla 30 dakika ek süre; image/container/port publish önce öğretilir. Docker/container bilgisi geçiş koşulu değildir. STRETCH: DNS için `getent hosts localhost`, önce kartla öğretim, en fazla 10 dakika ek süre. REFERENCE: Linux `/proc` source path; henüz kernel kodu okuma ödevi yok.
