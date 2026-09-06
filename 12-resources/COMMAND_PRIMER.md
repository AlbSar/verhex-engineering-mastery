# First-use command cards

Öğretmen için REFERENCE. Kartların tümünü öğrenciye aynı anda verme. Her ilk kullanımda adı, amacı, syntax/options, input/output, minimal örnek ve OS konumunu anlat; sonra farklı küçük örnekte tahmin al. PROVEN olmayan yeni flag için kartı genişlet. Yer tutucu PATH/PID gerçek gözlemle değiştirilir. Liste dışındaki grep/sed/awk/strace/lsof/find/xargs/chmod/systemctl/journalctl vb. için de aynı sözleşme zorunludur.

## wc — word count
Amaç: dosya veya stream içeriğini elle saymadan ölçmek; Unix araçlarını metin akışıyla birleştirmek. Syntax: `wc [OPTION] [FILE]`; FILE yoksa stdin okur. `-l` newline, `-w` whitespace ile ayrılan kelimeler, `-c` bytes, `-m` locale'e göre karakterler. Seçeneksiz newline/word/byte sayıları verir. stdout'a sayılar (dosya adı verilirse adı da) yazılır; hata stderr/başarısız status ile bildirilir. User-space dış programdır; stdin'den veya dosyadan okur, kernel I/O sağlar. UTF-8 byte/character aynı değildir; newline olmayan son parça `-l` sayısını artırmaz.

Önce öğretmen demonstration: `printf 'x\n' | wc -l` bir newline ürettiğinden 1 verir. Burada Bash printf builtin'i metin üretir, pipe stdout'u wc stdin'ine bağlar, wc sayıyı stdout'a yazar. Ancak bu açıklamadan sonra farklı örnek `printf 'a\nb\n' | wc -l` için prediction alınır. Kaynak: SH-IO kartı.

## printf, echo ve shell operatörleri
`printf FORMAT ARG...`: formatlı çıktı, Bash builtin; `%s` string, `\n` newline. `printf '%s\n' 'hello'` hello ve newline yazar; girdisi argüman, çıktısı stdout. `echo TEXT`: Bash builtin, metni genellikle newline ile yazar; bu derste seçenek kullanmadan `echo 'hello'` gösterilir.

`$PATH` arama dizinleri değişkeni; `$$` shell PID; `$?` son komut status'u. Çift tırnak değişken değerini tek argüman tutar. `echo $?` status'u okur fakat kendisi de yeni status bırakır. `&&` sol status 0 ise, `||` sol status nonzero ise sağ komutu yürütür; `;` sırayla yürütür. `|` standart çıktıyı standart girdiye bağlar, hata çıktısını otomatik taşımaz. Bunlar program adları değil Bash syntax'ıdır. Basit demonstration: `printf 'ok\n' && echo 'done'`; başarılı printf sonrası done. Pipeline süreçleri eşzamanlı çalışabilir; kernel pipe buffer'ı sınırlıdır. FD 0 stdin, 1 stdout, 2 stderr daha sonra çizimle gösterilir; ilk derste pipefail detayı zorunlu değil.

## command, python, uv ve Git sürümü
`command -v NAME`: Bash builtin; NAME'in nasıl çözümleneceğini bildirir, programı çalıştırmaz. `-v` bilgi ister. `command -v python` bir yol/karşılık veya bulunamama verir. Program adı `PATH` çözümlemesine, tam yol doğrudan dosyaya gider; symlink yine takip edilir.

`python --version`: dış runtime; argümandan sürüm isteğini alır, sürümü yazıp kapanır; `--version` Python seçeneğidir. `python FILE` dosyayı yürütür; file syntax'ı önce tanıtılır. `-m MODULE` modülü program olarak yürütür. `uv --version`, `git --version` kendi dış araçlarının sürümünü bildirir; hiçbiri Python mastery değildir.

`uv run COMMAND`: projenin ortamında COMMAND çalıştırır, gerektiğinde environment/dependency hazırlayabilir. stdout/stderr/status alt komuttan gelir. Minimal demonstration ancak uv öğretildikten sonra `uv run python --version`; sistem ve proje Python'u farklı olabilir. `.python-version` ve lock dosyaları açıklanmadan değiştirilmez.

## Git working state ve kayıt
Git snapshot/version-control dış programıdır. Girdisi subcommand/path, çıktısı repository durumudur. `git status` working tree/index farkının özetini gösterir. `git diff` unstaged, `git diff --cached` staged patch'i gösterir; read-only örnek önce öğretmen tarafından açıklanır.

`git log --oneline` her commit'i tek satır özetler; `--decorate` ref adları, `--graph` graph, `--all` tüm ref'ler, `-10` en çok on commit. `git branch -vv` branch/upstream bilgisi. `git fetch origin` remote ref'lerini günceller, working tree dosyalarını merge etmez.

Kayıt demonstration modeli: `git add -- PATH` seçilen dosyayı index'e alır; `--` seçeneklerin sonu. `git diff --cached` incelemesi sonrası `git commit -m 'message'` staged snapshot'ı kaydeder; `-m` mesajdır. Öğrenci PATH yerine kendi evidence dosyasını seçer. Toplu `git add .` varsayılanı yoktur.

## ls ve /proc
`ls -l PATH`: dış dosya listeleme aracı; `-l` uzun format. Girdi path, stdout dosya türü/izin/sahip/boyut/ad. Demonstration: `ls -l /usr/bin/python` → varsa symlink için `l` ve `->`; normal dosyada `-`. Kernel filesystem metadata sağlar. `/proc/PID/fd`, process'in fd görünümüdür; PID bulunmadan rastgele numara verilmez.

## ps — process status
`ps -p PID -o pid,comm`: process tablosu görünümü; `-p` PID seçer, `-o` alan seçer. Dış user-space araç Linux process bilgisini (çoğunlukla /proc) okur. Minimal demo: `ps -p $$ -o pid,comm`, kendi shell kimliği ve komut adı. Çıktı o anki snapshot'tır; canlı process sonradan kapanabilir. Server PID için öğretmen `ps -eo pid,args` kartını genişletir: `-e` tüm process'ler, `args` komut satırı; lab komutunu gözle bul. Üstüne açıklamasız grep ekleme.

## ss — socket statistics
`ss -lnt`: socket görünümü; `-l` listening, `-n` sayısal adres/port, `-t` TCP. Girdi kernel socket bilgisi, stdout socket/adres tablosu; ağ isteği üretmek zorunda değildir. Dış user-space araç kernel arayüzleriyle sorgular. Önce server yokken tabloyu öğretmen açıklar; sonra lab server ile 127.0.0.1:8080 satırı aranır. `-p` eklenecekse process bilgisi ve izin sınırı ayrıca öğretilir.

## curl — URL ile veri aktarımı
`curl -v URL`: URL'ye istek yapar; `-v` bağlantı/protocol ayrıntılarını stderr'e, response body'yi stdout'a yazar. Dış client process, socket/TCP üzerinden HTTP konuşur. Minimal örnek: çalışan local server'a `curl -v http://127.0.0.1:8080/`. Body ile status/header ayrı açıklanır. HTTP hata status'u her zaman curl nonzero değildir; bağlantı reddi ile HTTP yanıtını karıştırma.

## HTTP server ve kill
`python -m http.server 8080 --bind 127.0.0.1`: Python standart modülü; 8080 port, `--bind` dinlenecek adres. Çalışılan lab dizinini HTTP üzerinden sunar, request alır ve log/response üretir. Loopback dışına açmak gerekmiyor; production server değildir. Önce process/socket/bind/listen/accept kavramları öğretilir.

`kill -TERM PID`: adı kill olsa da signal gönderir; Bash builtin veya dış araç olabilir. `-TERM` SIGTERM seçer, PID hedef process. Normal başarıda stdout boş olabilir; status sinyalin gönderilebildiğini gösterir, process'in kesin kapandığını tek başına kanıtlamaz. Kernel sinyali iletir; uygulama nasıl ele alacağını belirleyebilir. Yalnızca kullanıcının lab server PID'sine gönder, sonra port/process gözlemiyle doğrula. SIGKILL farkı öğretilmeden seçenek değiştirme.

## OPTIONAL getent
`getent hosts localhost`: sistem name-service yapılandırmasından hosts kaydını sorgular. Database adı hosts, anahtar localhost; stdout adres/ad satırları. Dış program resolver/NSS katmanını kullanır; sonuç mutlaka DNS ağ isteği yapıldığı anlamına gelmez. DNS/hosts ayrımı sonra derinleşir.

## Test/lint/type araçları
`pytest` Python test runner; test discovery, `assert` ve hata raporu önce tanıtılır. `uv run pytest` aktif projedeki testleri yürütür; test sayısı/başarısızlıklar stdout ve status'ta görülür.
`ruff check .`: Ruff lint, `.` mevcut dizin, check inceleme; `ruff format --check .` dosya değiştirmeyen format doğrulaması. `mypy src`: src altındaki Python için statik type analizi; programı çalıştırmaz. Her birine küçük kasıtlı örnek ve açıklama, sonra öğrenci kendi lab'ında kullanır. Bunlar birbirinin veya kullanıcı açıklamasının yerine geçmez.
