---
status: active
week: 1
phase: 0
start_date: 2026-09-05
end_date: 2026-09-12
required_hours: 19
---

# Week 001 — Python + Linux + Networking + Git foundations

## Amaç ve başlangıç
5 Eylül 2026 kickoff. 6 Eylül dinlenme/isteğe bağlı tekrar; gün numaraları öğrenme sırasıdır. Gerçek çalışma tarihi günlükte kaydedilir. 7 Eylül olması Day 01'in kanıtsız tamamlandığı anlamına gelmez.

Hafta baseline'dır: bilinmeyeni sınamak yerine öğret, sonra gözlemle. [Teacher protocol](../../00-governance/CODEX_TEACHER_PROTOCOL.md) ve [concept-state](../../01-skill-matrix/concept-state.yaml) her oturum başında okunur. Kaydı olmayan konu UNKNOWN. Socratic sorgulama öğretimden sonra gelir. Kaynaklar: [aktif kartlar](../../12-resources/WEEK_001.md).

## Zaman bütçesi
| Gün | Plan tarihi | Required saat | Odak |
|---|---|---:|---|
| Day 01 | 2026-09-05 | 4 | Ortam, shell, Git, ilk Python |
| Day 02 | 2026-09-07 | 2.5 | Object/identity/equality |
| Day 03 | 2026-09-08 | 2.5 | Mutation/copy/debug |
| Day 04 | 2026-09-09 | 2.5 | Scope/function/closure introduction |
| Day 05 | 2026-09-10 | 3 | Veri yapısı ve küçük construction |
| Day 06 | 2026-09-11 | 2.5 | Process/socket/HTTP bağlantısı |
| Day 07 | 2026-09-12 | 2 | Assessment ve retrospective |
| Toplam | | 19 | |

İç bölüm süreleri günlük header ile tam eşittir. Açıklama, kaynak, test ve evidence bütçeye dahildir. Önemli öğrenme sonucu yetişmezse sonraki oturuma taşınır; aynı güne gizli ek yük yazılmaz. Yeni hafta bağımlı konular için prerequisite kapısını bekler.

## Kapsam sınıfları
- REQUIRED: günlerin zorunlu temel deneyleri ve evidence.
- OPTIONAL: seçilebilir diagnostic; ek süre ayrı, geçişi etkilemez.
- STRETCH: ön koşullu derinleşme; sonraki Phase A haftasına taşınabilir.
- REFERENCE: ihtiyaç halinde kaynak; bitirilecek ödev değildir.

## REQUIRED kanıt ve geçiş
1. Shell/program/PATH ve bir stdin/stdout/exit-status deneyi.
2. Güvenli Git diff/index/commit modeline ilişkin kanıt ve runtime_probe.
3. Identity/aliasing lab ve üç test.
4. Mutation/copy lab, iki test ve debug journal.
5. Scope/function lab, iki test; closure introduction kaydı (mastery şartı yok).
6. Duplicate analyzer, üç test ve veri yapısı gerekçesi.
7. Local HTTP process/port gözlemi, stop/restart ve recovery, küçük request-path diagramı ve iki failure mode.
8. Day 07 bağımsız küçük varyant/iki test, kaynaklı açıklama, baseline, concept-state, assessment ve retrospective.

Mevcut kanıt tekrar kullanılabilir; her tablo için yeniden deney yapılmaz. Unknown araçlar önce öğretilir. Puanlanmamış konular null kalır. [Assessment standard](../../00-governance/ASSESSMENT_STANDARD.md) kararı belirler; her alanda 4/5 Week 001 şartı değildir.

## Ertelenen derinlik
Docker, ayrı İngilizce kota, dependency scheduler/cycle detection, custom equality, deep-copy derinliği, late-binding ve tam enterprise integration mimarisi geçiş koşulu değildir. Bunlar ilgili Day dosyasında OPTIONAL/STRETCH/REFERENCE olarak sınırlandırılmıştır; ileride Phase A/B/E/I kapsamında tekrar açılır.

## Öğretmenin günlük sunumu
Today (hedef/neden/ön koşul durumları/çıktı) → Teach → Mechanism → Example → Predict → tek Lab → Observe → Review → Teach Back → Evidence. Öğretmen açıklama örneğinin sonucunu gösterebilir; kullanıcı deneyi için çözümü yazmaz. Takvim ve checklist öğretimin yerine geçmez.
