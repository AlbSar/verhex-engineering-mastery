---
status: active
phase: 0
planned_duration: 1 week
start_date: 2026-09-05
end_date: 2026-09-12
---

# Faz 0 — Öğretilen temeller ve başlangıç kanıtı

5 Eylül 2026'da başlayan 12 aylık çekirdek + sürekli eğitim programının girişidir. Phase A foundations içinde Week 001'i kalibre eder; ek bir sınav veya tool kurulum maratonu değildir.

Kanonik kapsam, saat ve geçiş: [Week 001](../03-weeks/week-001/WEEK_PLAN.md). Tek rubric: [Assessment](../03-weeks/week-001/ASSESSMENT.md); puan standardı: [Assessment Standard](../00-governance/ASSESSMENT_STANDARD.md).

UNKNOWN önce öğretilir; INTRODUCED rehberli denenir; PRACTICING için recall/predict/build; PROVEN ve MASTERED yalnızca kaynaklı kanıtla. [Concept state](../01-skill-matrix/concept-state.yaml) dersin seviyesini belirler. Unix, pytest, uv veya Git komutları bildiği varsayılmaz.

## Girişten çıkışa
1. Shell/program ve mevcut ortam; PATH derinliği hedefe yetecek kadar.
2. Python object, mutation, function/scope ve küçük testler.
3. Basit veri yapısı construction ve debugging.
4. Process/socket/HTTP gözlemi, küçük failure/recovery.
5. Git ve gerçek tarihli evidence kaydı; mevcut kullanıcı çalışması korunur.
6. Öğretilen konuların assessment'i ve sonraki hafta kararı.

19 required saat içindeki tekrar kullanılan kanıtlar: lab, test, debug journal, terminal çıktısı, kendi açıklaması, küçük context diagramı ve retrospective. Ek İngilizce/Docker zorunlu değildir. Graph scheduler/enterprise design ileri fazlara ertelenebilir. Her alanda mastery 4 beklenmez. Eksik prerequisite varsa aynı faz öğretimle sürer.

## Sonraki bağlantı
Phase A devamı: functions/closures/iterators, algoritma ve TCP/HTTP construction. Phase B veri/SQL/backend, Phase C kernel/container, Phase D Go. Toolchain ve production-source derinliği aktif kavrama göre eklenir; şimdi Kubernetes/Java kurmak gerekmiyor.
