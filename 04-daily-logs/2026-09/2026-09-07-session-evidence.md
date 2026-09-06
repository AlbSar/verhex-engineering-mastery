---
status: partial
date: 2026-09-07
week: 1
phase: 0
hours_spent: null
recorded_by: Codex
source: user messages and user-supplied terminal output in this repository session
---

# Session evidence — shell foundations

Codex derlemesidir; aşağıdaki komut çıktıları kullanıcı tarafından konuşmada sağlandı. 6–7 Eylül konuşması 7 Eylül'de kayda alındı; her komutun kesin saati ve toplam süre ölçülmedi. Yeniden çalıştırılmış sonuç veya bağımsız mastery beyanı değildir. AI reference notu: [notes.md](../../05-labs/python/week-001/notes.md); bu notun genişletilmiş sürümü yerelde henüz commit edilmemiştir, remote dosyada bulunmayabilir.

## Kullanıcının sunduğu gözlemler

| İşlem | Kullanıcının çıktısı | Yorum / sınır |
|---|---|---|
| `command -v python` | `/usr/bin/python` | Bu oturumun komut çözümlemesi |
| `python --version` ve `/usr/bin/python --version` | `Python 3.12.3` | Yol ve sürüm birbirinden ayrıldı |
| `ls -l /usr/bin/python` | `python -> python3`, ilk karakter `l` | Symlink gözlemi |
| `ls -l /usr/bin/python3` | `python3 -> python3.12`, ilk karakter `l` | İkinci bağlantı |
| `ls -l /usr/bin/python3.12` | İlk karakter `-`, execute izinleri | Normal dosya |
| `python --versiyon` | `unknown option --versiyon` | Python argument hatası |
| `pythonn --version` | Komut bulunamadı ve paket önerileri | Program başlamadı |
| Hatalı seçenek, sonra iki `echo $?` | `2`, sonra `0` | Kullanıcı önce bu sonucu tahmin etti |
| Hatalı seçenek `&& echo` | Echo görünmedi | Başarısız sol komut |
| Hatalı seçenek `|| echo` | Echo göründü; zincir exit 0 | Son çalıştırılan echo başarılı |
| Doğru seçenek `|| echo` | Yalnızca sürüm | Kullanıcının "her durumda basar" varsayımı düzeltildi |
| Doğru seçenek `&& echo` | Sürüm ve DEVAM | Kullanıcı doğru tahmin etti |
| `printf 'Python\nLinux\n'` pipe `wc -l` | `2` | Öğrenci "bilmiyorum" dedi; anlamadan çalışma mastery değildir |

## Öğretim düzeltmesi

Kullanıcı `wc` adı, amacı ve seçeneklerinin önce açıklanmasını istedi. Bu istek audit ve yeni teacher-first protokolünün tetikleyicisidir. Sonraki açıklamada wc/word count, -l/-w/-c/-m, stdin ve pipe tanıtıldı; yeni örnek tahmini henüz alınmadı.

## Durum

Shell/PATH ve exit/conditionals PRACTICING; pipe ve wc INTRODUCED. Hiçbiri bu kayıtla PROVEN/MASTERED yapılmadı, sayısal puan verilmedi. Python list/aliasing veya networking kanıtı bu terminal deneylerinden çıkarılamaz.

## Sonraki oturum

Day 01 devamı: wc ve stdin/stdout kısa, tam öğretim; tek minimal demonstration; ardından bir yeni newline tahmini ve kullanıcı deneyi. Bu kayıt öğrencinin kendi açıklamasının yerine geçmez; sonraki etkileşim kaynak gösterilerek eklenebilir.

## Tarihsel yerel Git kaydı

Audit öncesi korunmuş, henüz commit edilmemiş `04-daily-logs/2026-08/2026-08-04.md` metninde kullanıcı "git mantığı git kullanımı. branch worktree commit head kavramları." yazmış; aynı kayıtta tam öğrenme olmadığını belirtmiştir. Bu kaynaklı kısa alıntı yalnızca INTRODUCED kararını destekler; bağımsız Git yeterliliği sayılmaz. Asıl günlük değiştirilmedi ve bu curriculum commit'ine eklenmedi.
