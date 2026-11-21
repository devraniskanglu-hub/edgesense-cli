# EdgeSense CLI - Gömülü Sistemler İçin Sensör Veri İzleme ve Eşik Uyarı Aracı

## Proje Tanımı
Mikrodenetleyici ve IoT prototipleme süreçlerinde, donanımdan veya test simülatörlerinden akan ham sıcaklık ve nem verilerinin terminal üzerinden anlık olarak takip edilmesi ve kritik eşik değerler aşıldığında geliştiricinin hızlıca uyarılması gerekir. **EdgeSense CLI**, fiziksel donanım bağlı olmadığı durumlarda dahi sensör verilerini simüle etmeyi, eşik değer kontrolü yapmayı ve kritik durumları raporlamayı sağlayan hafif bir komut satırı aracıdır. Bu proje; gömülü sistem geliştiricileri, IoT prototipleme yapan mühendislik öğrencileri ve donanım test süreçlerini otomatize etmek isteyen mühendisler için geliştirilmiştir.

## İş Takip Panosu (GitHub Projects)
Proje kapsamındaki tüm görevlerin, kabul kriterlerinin ve geliştirme aşamalarının takip edildiği panoya aşağıdaki bağlantıdan ulaşabilirsiniz:
* **Proje Panosu:** (https://github.com/users/devraniskanglu-hub/projects/1)

## Kurulum ve Çalıştırma Adımları
Proje yalnızca Python standart kütüphanelerini (`argparse`, `random`, `time`, `datetime`) kullanır; harici bir paket kurulumu gerektirmez.

1. Depoyu bilgisayarınıza klonlayın:
   ```bash
   git clone [https://github.com/devraniskanglu-hub/edgesense-cli.git](https://github.com/devraniskanglu-hub/edgesense-cli.git)
   cd edgesense-cli
