# Curriculum / teaching / resource / Git audit — 2026-09-07

## Audit Findings

Başlangıç: yerel main, learning/week-001 ve iki origin ref aynı `ec630beb631cd7f69f4f73054361c856d250fe25` commit'indeydi. Fetch sonrası da fark yoktu; origin'de olmayan yerel commit yok. Önceki user baseline commitleri `63d7879`, `35b267b` ve koruyucu merge'ler `a87c14a`, `ec630be` ortak geçmişte duruyor. Commit author metadata tek başına kodun AI/user kökenini kanıtlamaz; bu sınıflama oturum bağlamı ve içerikle yapıldı.

| Bulgu | Onarım |
|---|---|
| Teacher protocol her konuda tahmin istiyor, UNKNOWN/PRACTICING ayrımı yok | Teach-first sözleşme, state kaydı ve repo AGENTS giriş noktası |
| Day 02–05 teoriyi öğretmeden tanım/quiz/kod istiyor | Önce öğretmen açıklaması ve minimal demonstration, sonra kullanıcı görevi |
| Baseline/Faz 0 haftaya ek Docker, İngilizce, 5 test, scheduler ve enterprise mimari yükü getiriyor | Tek weekly required scope/rubric; optional/stretch açık; baseline ek sınav değil |
| Süre toplamı eski sürümde 19 doğru olsa da cognitive workload beginner için ağır | Süre dağılımı korundu, graph/ileri closure/enterprise design ertelendi, açıklama süresi bütçeye alındı |
| Day 06 server kapatıldıktan sonra başarılı curl beklenebiliyor | Başarılı request → stop → beklenen failure → restart → recovery |
| Lab README tam CLI/custom exception ve pyright istiyor, proje mypy kullanıyor | Aktif küçük lab'lar ve mevcut toolchain ile uyum |
| 4/5 genel geçiş kuralı baseline'ı yanlışlıkla engelliyor | Uzun vadeli mastery ile baseline/reinforcement kararı ayrıldı |
| Git yetkinliği matriste eksik; aktif knowledge-state yok | Git/backend/AI alt alanları ve ayrı küçük state kaydı; puanlar korunur |
| Kaynaklar repo adları düzeyinde, active section/experiment/evidence akışı eksik | Week 001 primary kartları ve kaynak sözleşmesi |
| Eski tarihler evidence ile plan arasında karışıyor | Ağustos kullanıcı günlüğü aynen korunur; Eylül kickoff historical plan diye işaretlenir; yeni kayıt gerçek tarihli |
| README henüz olmayan dizinleri varmış gibi listeliyor | Planned alanlar açıkça belirtilir |
| Issue #1 erişimi web aracıyla doğrulanamadı | Kanonik day/week/evidence'a yönlendirme; issue tarihsel identifier olarak tutulur |

## Local/remote difference classification and protection

- A — user learning evidence: Ağustos günlüğünün unstaged değişikliği; user lab/test/lock/environment commitleri. Hepsi korunur.
- A — reference/user context: notes.md ilk iki kullanıcı satırı + daha önce istenen Codex notu; byte-for-byte korunur, yeni mastery iddiası eklenmez.
- B — newer remote curriculum: audit başında yok; ref'ler eşit. Son fetch/push kontrolü final teslimde ayrıca yapılır.
- C — obsolete curriculum text: protokol, baseline, faz ve day kapsamları bu repair ile düzeltilir; user code'e dokunulmaz.
- D — .deckent/runtime SQLite dosyaları: tekrar oluşmuş generated local runtime. Silinmedi; .gitignore ile repo evidence'ından ayrıldı.
- E — proje Python 3.11 seçimi vs sistem 3.12.3: ikisi ayrı ortam olabilir; kullanıcı dosyaları değiştirilmedi, öğrenme konusu olarak açıklanır. Ağustos tarih/title tutarsızlığı historical user evidence olarak korunur, yeniden tarihlenmez.

İşlem öncesi unstaged/staged binary patch, ref listesi, iki dirty dosyanın kopyası ve SHA-256 manifesti `/tmp/mastery-audit-20260907/` altında tutuldu. İlk staged diff boştu. Son hash kontrolü iki dirty dosyanın aynı byte'larda kaldığını doğrular. Source/test/pyproject/lock/.python-version diff'i yok. Hiç hard reset, rebase, history deletion, force push veya blanket add uygulanmadı. Geçici yedek /tmp'dedir, uzun vadeli backup yerine geçmez; asıl dosyalar yerinde korunmaktadır.

## Files Changed

Aşağıdaki manifest yalnızca audit repair dosyalarıdır; önceden dirty iki evidence dosyası dahil değildir.

| Dosya | Neden |
|---|---|
| [.gitignore](../.gitignore) | Yeniden oluşan .deckent runtime verisini silmeden yerel tutar. |
| [00-governance/AI_USAGE_PROTOCOL.md](../00-governance/AI_USAGE_PROTOCOL.md) | Teacher-first öncelik, AI reference sahipliği ve kritik kod sınırı. |
| [00-governance/ASSESSMENT_STANDARD.md](../00-governance/ASSESSMENT_STANDARD.md) | Baseline/mastery ayrımı, null/score/state ve tek rubric. |
| [00-governance/CODEX_TEACHER_PROTOCOL.md](../00-governance/CODEX_TEACHER_PROTOCOL.md) | Üç zorunlu kural, durum modeli, katmanlı öğretim, yeni araç sözleşmesi. |
| [00-governance/LEARNING_PROTOCOL.md](../00-governance/LEARNING_PROTOCOL.md) | Duruma bağlı döngüler, kaynak/production/transfer ve kanıt. |
| [00-governance/MASTER_PLAN.md](../00-governance/MASTER_PLAN.md) | Dil uygulama hatları, bütün domain/prerequisite/lab/evidence bağlantıları. |
| [01-skill-matrix/baseline-assessment.md](../01-skill-matrix/baseline-assessment.md) | Fazladan sınav/Docker/İngilizce yükünü kaldırır; required evidence özeti. |
| [01-skill-matrix/concept-state.yaml](../01-skill-matrix/concept-state.yaml) | Aktif kavram durumları, gerekçe ve kaynak; sahte PROVEN yok. |
| [01-skill-matrix/skill-matrix.yaml](../01-skill-matrix/skill-matrix.yaml) | Git/backend/tokenization/reranking/AI governance; eski puanları korur. |
| [02-phases/phase-00-diagnostics.md](../02-phases/phase-00-diagnostics.md) | Week 001 ile tek kapsam/puanlama, teach-first baseline. |
| [03-weeks/week-001/ASSESSMENT.md](../03-weeks/week-001/ASSESSMENT.md) | Required lab/test/kanıt ile aynı değerlendirme ve geçiş. |
| [03-weeks/week-001/DAY_01.md](../03-weeks/week-001/DAY_01.md) | Teach-first günlük rota; açık ön koşul, tam süre, tek görev ve scope sınıfları. |
| [03-weeks/week-001/DAY_02.md](../03-weeks/week-001/DAY_02.md) | Teach-first günlük rota; açık ön koşul, tam süre, tek görev ve scope sınıfları. |
| [03-weeks/week-001/DAY_03.md](../03-weeks/week-001/DAY_03.md) | Teach-first günlük rota; açık ön koşul, tam süre, tek görev ve scope sınıfları. |
| [03-weeks/week-001/DAY_04.md](../03-weeks/week-001/DAY_04.md) | Teach-first günlük rota; açık ön koşul, tam süre, tek görev ve scope sınıfları. |
| [03-weeks/week-001/DAY_05.md](../03-weeks/week-001/DAY_05.md) | Teach-first günlük rota; açık ön koşul, tam süre, tek görev ve scope sınıfları. |
| [03-weeks/week-001/DAY_06.md](../03-weeks/week-001/DAY_06.md) | Teach-first günlük rota; açık ön koşul, tam süre, tek görev ve scope sınıfları. |
| [03-weeks/week-001/DAY_07.md](../03-weeks/week-001/DAY_07.md) | Teach-first günlük rota; açık ön koşul, tam süre, tek görev ve scope sınıfları. |
| [03-weeks/week-001/RETROSPECTIVE.md](../03-weeks/week-001/RETROSPECTIVE.md) | Gün bazlı saatler, öğretim kalitesi ve state reflection. |
| [03-weeks/week-001/WEEK_PLAN.md](../03-weeks/week-001/WEEK_PLAN.md) | 19 saat, tek required kapsam ve ertelemeler. |
| [04-daily-logs/2026-09/2026-09-05.md](../04-daily-logs/2026-09/2026-09-05.md) | Eski kickoff listesini tarihsel plan olarak açıkça ayırır; metin korunur. |
| [04-daily-logs/2026-09/2026-09-07-session-evidence.md](../04-daily-logs/2026-09/2026-09-07-session-evidence.md) | Kullanıcının konuşmada verdiği çıktıları kaynaklı, provisional derler. |
| [04-daily-logs/README.md](../04-daily-logs/README.md) | Gerçek çalışma tarihi ve tarihsel/AI/user evidence ayrımı. |
| [05-labs/python/week-001/README.md](../05-labs/python/week-001/README.md) | Günlerle uyumlu lab/test kapsamı; mevcut mypy ve toolchain korunur. |
| [09-debug-journal/README.md](../09-debug-journal/README.md) | Debug öncesi unknown araç öğretimi ve kanıt sahipliği. |
| [10-assessments/CURRICULUM_AUDIT_2026-09-07.md](../10-assessments/CURRICULUM_AUDIT_2026-09-07.md) | Bu audit, koruma, manifest, doğrulama ve risk kaydı. |
| [10-assessments/README.md](../10-assessments/README.md) | Unknown sınavı yok, optional kapısı yok, AI ayrımı. |
| [10-assessments/TEACHING_ACCEPTANCE.md](../10-assessments/TEACHING_ACCEPTANCE.md) | wc/decorator/aliasing öğretim simülasyonları ve sonuçları. |
| [12-resources/COMMAND_PRIMER.md](../12-resources/COMMAND_PRIMER.md) | İlk kullanımda komut/flag/input/output/OS/örnek öğretimi. |
| [12-resources/README.md](../12-resources/README.md) | Altı kaynak rolü, bölüm/deney/evidence sözleşmesi. |
| [12-resources/WEEK_001.md](../12-resources/WEEK_001.md) | Aktif günlere bağlı primary kaynak kartları ve runtime sürüm ayrımı. |
| [AGENTS.md](../AGENTS.md) | Repo açılışında öğretim protokolü ve unknown-first kuralı keşfedilir. |
| [README.md](../README.md) | Güncel öğrenme döngüleri, resume noktası ve gerçek kapsam. |
| [scripts/audit_curriculum.py](../scripts/audit_curriculum.py) | Saat/tarih/link/YAML/kural/kanıt sözleşmelerinin read-only denetimi. |
| [templates/ADR_TEMPLATE.md](../templates/ADR_TEMPLATE.md) | Öğretim durumu, kaynaklı evidence, süre veya requirement-first karar kaydı. |
| [templates/DAILY_LOG_TEMPLATE.md](../templates/DAILY_LOG_TEMPLATE.md) | Öğretim durumu, kaynaklı evidence, süre veya requirement-first karar kaydı. |
| [templates/DEBUG_ENTRY_TEMPLATE.md](../templates/DEBUG_ENTRY_TEMPLATE.md) | Öğretim durumu, kaynaklı evidence, süre veya requirement-first karar kaydı. |
| [templates/RESOURCE_CARD_TEMPLATE.md](../templates/RESOURCE_CARD_TEMPLATE.md) | Öğretim durumu, kaynaklı evidence, süre veya requirement-first karar kaydı. |

## Teaching Model

UNKNOWN: Teach → Demonstrate → Predict → Practice → Observe → Explain → Review. Ayrıntı: teach/show/mechanism/tiny example, sonra user runs/explains.
PRACTICING: Recall → Predict → User builds → Test → Break → Debug → Review → Production comparison.
ADVANCED: Problem → Constraints → User design → Trade-off review → Failure injection → Production source → Architecture review.

Her yeni komut/API/flag önce öğretilir. Katmanlar basit model → teknik → OS/runtime/protocol → production → seçili source. PROVEN bağımsız kullanım/açıklama ister; MASTERED ayrıca 4+ evidence. Simülasyon kullanıcı durumunu yükseltmez.

## Resource Model

Roadmap yön verir; primary docs mekanizmayı doğrular; freeCodeCamp seçili structured practice; awesome keşif; build-your-own-x kavramsal dönemeçte construction; system-design-primer problemden trade-off'a; Linux seçili production path. Aktif kartlar day/hedef/bölüm/deney/artefact ile bağlıdır. Full curriculum tamamlamak veya tüm kernel'i okumak görev değildir.

## Validation

- `python3 scripts/audit_curriculum.py`: 7 günlük header/iç süre, 19 saat, plan tarihleri, yerel Markdown linkleri, zorunlu kurallar, eski aktif plan taraması, YAML/state/score evidence yapısı. Python 3 + PyYAML bakım ortamı kullanılır; learner lab dependency değildir.
- Günlük dakika toplamları: 240, 150, 150, 150, 180, 150, 120 = 1140 dakika.
- Üç manual teaching simulation: [TEACHING_ACCEPTANCE.md](TEACHING_ACCEPTANCE.md). UNKNOWN wc ve decorators önce öğretilir; PRACTICING aliasing kısa recall sonrası tahmin eder. Üçü de PASS.
- Audit-only execution: wc örnekleri 1/2/1; decorator before/hello; alias/rebinding [1,2]/[1,2] doğrulandı. Bunlar öğrenci evidence'ı değildir.
- Değiştirilen curriculum diff'inde whitespace kontrolü yapılır; kullanıcı Ağustos günlüğündeki önceden mevcut blank-line uyarısı korunur.
- 16 dış Markdown kaynak URL'si doğrudan HTTP GET ile 200; decorator anchor da bulundu. GNU web timeout'ları son doğrudan kontrolde çözüldü. GitHub issue #1 kontrolü sonuçsuz; kaynak URL listesinin parçası olarak başarı iddiası yok.

| Kaynak | HTTP |
|---|---|
| [https://docs.kernel.org/filesystems/proc.html](https://docs.kernel.org/filesystems/proc.html) | 200 |
| [https://docs.python.org/3.12/library/copy.html](https://docs.python.org/3.12/library/copy.html) | 200 |
| [https://docs.python.org/3.12/library/http.server.html](https://docs.python.org/3.12/library/http.server.html) | 200 |
| [https://docs.python.org/3.12/reference/compound_stmts.html#function-definitions](https://docs.python.org/3.12/reference/compound_stmts.html#function-definitions) | 200 |
| [https://docs.python.org/3.12/tutorial/controlflow.html](https://docs.python.org/3.12/tutorial/controlflow.html) | 200 |
| [https://docs.python.org/3.12/tutorial/datastructures.html](https://docs.python.org/3.12/tutorial/datastructures.html) | 200 |
| [https://docs.python.org/3.12/tutorial/introduction.html](https://docs.python.org/3.12/tutorial/introduction.html) | 200 |
| [https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F) | 200 |
| [https://github.com/codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | 200 |
| [https://github.com/donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | 200 |
| [https://github.com/freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 200 |
| [https://github.com/nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | 200 |
| [https://github.com/sindresorhus/awesome](https://github.com/sindresorhus/awesome) | 200 |
| [https://github.com/torvalds/linux](https://github.com/torvalds/linux) | 200 |
| [https://www.gnu.org/software/bash/manual/html_node/Pipelines.html](https://www.gnu.org/software/bash/manual/html_node/Pipelines.html) | 200 |
| [https://www.gnu.org/software/coreutils/manual/html_node/wc-invocation.html](https://www.gnu.org/software/coreutils/manual/html_node/wc-invocation.html) | 200 |

## Git delivery

Repair ayrı curriculum commit'i olarak kaydedilir. Başlangıç user dirty dosyaları bu commit'e stage edilmez. Önce remote yeniden fetch edilir; yeni divergence yoksa eğitim branch'i ve main yalnızca fast-forward ile aynı repair commit'ine getirilir ve atomic push yapılır. Son gerçek hash/ref durumu kullanıcıya final yanıtta raporlanır; bu dosyada kendi commit hash'ini önceden uydurma yoktur.

## Remaining Risks

- Tam 19 saat aritmetik tutarlılıktır; öğrenci ilerleme hızı garantisi değildir. Prerequisite gecikmesinde görev taşınır ve bağımlı ders açılmaz.
- Yeni protokolün sonraki her model yanıtında uygulanması statik check ile garanti edilemez; örnekler acceptance contract ve retrospective kontrolüdür.
- Kaynak erişimi 2026-09-07 snapshot'ıdır. Gelecek production path/test seçimi aktif lab açılışında commit'e sabitlenmelidir.
- User-owned system/project Python ayrımı henüz öğrenci tarafından gözlemlenmedi; bu audit dependency install veya upgrade yapmadı.
- Kaynaklı chat evidence rehberli/pratik düzeyidir, bağımsız mastery değildir. Saat ölçümü yoktur; null bırakıldı.

## Next Learning Session

Actual lesson audit sırasında başlatılmadı. Exact resume: Day 01 shell akışı, SH-IO. Yaklaşık 15–20 dakika mevcut 35 dakikalık block içinde: Today (amaç/ön koşullar) → wc/word count, -l/-w/-c/-m, stdin/stdout, printf/newline ve pipe mekanizması → tek newline demonstration → iki newline için tek prediction/user-run → observation ve kullanıcı açıklaması → final newline olmayan varyant (ilk deney anlaşıldıysa) → kaynaklı evidence. Öğrenciye tüm günün görevleri aynı anda verilmez.
