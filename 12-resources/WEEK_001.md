# Week 001 — aktif kaynak kartları

Öğretmen seçimi; bütün linkleri okuma ödevi değildir. Her Day yalnızca ilgili karttan kısa bir bölüm kullanır; süre o günün Teach/Lab bütçesi içindedir. Python web dokümanı gözlemlenen sistem 3.12 hattına sabitlenmiştir; proje `.python-version` ise 3.11 seçer. Proje çalıştırmasında farklı runtime çıkabilir; bunu Day 01'de öğret ve sürüme göre ilgili resmî dokümanı seç. Kullanıcının toolchain dosyaları audit sırasında değiştirilmedi.

## SH-IO — REQUIRED Day 01 / sonraki oturum
- Hedef: stdout/stdin ve pipe ile newline sayımını açıklamak.
- Ön koşul: shell/program PRACTICING; pipe/wc INTRODUCED, öğretim tekrarı gerekli.
- Primary: [GNU wc invocation](https://www.gnu.org/software/coreutils/manual/html_node/wc-invocation.html), `-l`, `-w`, `-c`, `-m` ve stdin paragrafı; [Bash Pipelines](https://www.gnu.org/software/bash/manual/html_node/Pipelines.html), bağlantı ve status bölümü.
- Erişim: web aracı önce timeout verdi; ardından salt okunur HTTP denetiminde her iki GNU sayfası da 200 döndü (2026-09-07). Gelecekte erişilemezse yerel GNU yardım/manual öğretmen tarafından doğrulanmış alternatif olabilir.
- Öğretim: [wc kartı](COMMAND_PRIMER.md); word count, seçenek, input/output, Unix process ve küçük gösterim.
- Deney: öğretmen tek newline gösterir; sonra kullanıcı iki satır ve sonda newline olmayan varyantı ayrı ayrı tahmin eder/çalıştırır.
- Evidence: gerçek tarihli `04-daily-logs/` kaydı; komut, tahmin, stdout, açıklama. Assistant çıktısı öğrenci kanıtı sayılmaz.
- Transfer: log işleme hattında satır sayımı, binary/encoding ve eksik final newline sınırı.

## GIT-STATE — REQUIRED Day 01/07
- Hedef: working tree/index/commit ayrımı ve kanıtı güvenle kaydetmek.
- Primary: [Pro Git — What is Git?](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F), Snapshots / The Three States.
- Deney: öğretilmiş status/diff ile tek evidence dosyasının staging öncesi/sonrasını karşılaştır; toplu stage yok.
- Evidence: günlük diff özeti ve kullanıcı commit'i; AI bakım commit'i kişisel Git mastery değildir.

## PY-OBJECT — REQUIRED Day 01/02
- Hedef: literal/name/list, object identity ve equality.
- Primary: [Python 3.12 introduction](https://docs.python.org/3.12/tutorial/introduction.html), Numbers/Lists; [Data Structures](https://docs.python.org/3.12/tutorial/datastructures.html), More on Lists (append/copy).
- Ön koşul: dosya çalıştırma, assignment ve print; UNKNOWN ise önce öğret.
- Deney: isim-nesne çizimi, ayrı eşit listeler ve alias; prediction sonra lab.
- Evidence: runtime_probe/object_identity ve testleri; interning optimizasyonunu dil garantisi yapma.

## PY-COPY — REQUIRED Day 03
- Primary: [copy](https://docs.python.org/3.12/library/copy.html), assignment/copy ve shallow/deep tanımları.
- Hedef: mutation/rebinding ve paylaşılan state. İlk kısım required; deepcopy derinliği STRETCH.
- Deney: assignment ve shallow copy karşılaştırması; kullanıcı mutation bug'ı ve regression.
- Evidence: mutability lab, iki test, `09-debug-journal/` kaydı.

## PY-SCOPE — REQUIRED Day 04
- Primary: [More Control Flow Tools](https://docs.python.org/3.12/tutorial/controlflow.html), Defining Functions; default evaluation yalnızca extension seçilirse.
- Hedef: function/local scope; closure girişinde enclosing binding modelini öğretmen ekler.
- Deney: local shadowing ve function-as-value; sonra tek closure demonstration ve kullanıcının küçük denemesi.
- Evidence: scope çizimi, closures lab ve iki test; late-binding STRETCH.

## PY-DATA — REQUIRED Day 05
- Primary: [Data Structures](https://docs.python.org/3.12/tutorial/datastructures.html), Sets ve Dictionaries.
- Hedef: membership/frequency için veri yapısı seçimi.
- Deney: küçük duplicate analyzer, empty/unique/duplicate testleri.
- Evidence: kullanıcı implementation, test çıktısı, maliyet gerekçesi. freeCodeCamp pratik ancak ilave açıklama yararlıysa OPTIONAL seçilir; required saat değiştirilmez.

## NET-PROC — REQUIRED Day 06
- Primary: [Python http.server](https://docs.python.org/3.12/library/http.server.html), command-line usage ve bind; [Linux /proc documentation](https://docs.kernel.org/filesystems/proc.html), process-specific subdirectories ve fd.
- Ön koşul: shell ve process; socket/fd/HTTP önce öğretilir.
- Deney: loopback local server, port/status/fd gözlemi, stop→failed request→restart→recovery.
- Evidence: terminal çıktısı ve iki failure mode; production server yerine geçmediğinin açıklaması.
- REFERENCE source: Linux `fs/proc/base.c`, ilgili PID/fd yolu ve `tools/testing/selftests/proc/`; kod okumadan önce upstream commit ve mevcut test adı doğrulanır. Bu hafta zorunlu source ödevi yok.

## DESIGN-INTRO — REQUIRED Day 06, hafif
- Reference: [system-design-primer](https://github.com/donnemartin/system-design-primer), Latency vs throughput; yalnızca bu ayrım öğretmen eşliğinde.
- Hedef: request path ve gözlemlenebilir failure; teknoloji adı seçmek değil.
- Deney/evidence: client/service/response diyagramı ve iki failure mode; enterprise integration Phase I'a ertelenir.

Python/Git/kernel ve altı çekirdek repo web erişimleri 2026-09-07 kontrol edildi. Aktif örneklerde yalnızca seçilen bölüm kullanılır; belgelerin tümü atanmamıştır.
