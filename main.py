import argparse
import random
import time
from datetime import datetime

def generate_sensor_data():
    temp = round(random.uniform(22.0, 38.0), 2)
    humidity = round(random.uniform(35.0, 75.0), 1)
    return temp, humidity

def run_monitor(count: int, interval: float, threshold: float | None):
    print(f"[BİLGİ] Sensör simülasyonu başlatıldı ({count} okuma yapılacak)...")
    if threshold is not None:
        print(f"[BİLGİ] Aktif Sıcaklık Eşiği: {threshold}°C\n")
    else:
        print()

    alert_count = 0

    for i in range(1, count + 1):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        temp, humidity = generate_sensor_data()
        
        alert_tag = ""
        if threshold is not None and temp > threshold:
            alert_tag = "  --> [UYARI: KRİTİK SICAKLIK]"
            alert_count += 1

        print(f"[{timestamp}] Okuma #{i} | Sıcaklık: {temp}°C | Nem: %{humidity}{alert_tag}")
        
        if i < count:
            time.sleep(interval)

    print("\n--- İzleme Özeti ---")
    print(f"Toplam Okuma: {count}")
    if threshold is not None:
        print(f"Eşik Aşımı ({threshold}°C üzeri): {alert_count} adet")

def main():
    parser = argparse.ArgumentParser(
        description="EdgeSense CLI - Gömülü Sistemler İçin Sensör İzleme ve Uyarı Aracı"
    )
    subparsers = parser.add_subparsers(dest="command", help="Kullanılabilir komutlar")

    monitor_parser = subparsers.add_parser("monitor", help="Sensör verilerini canlı izle")
    monitor_parser.add_argument("--count", type=int, default=5, help="Okunacak veri sayısı")
    monitor_parser.add_argument("--interval", type=float, default=1.0, help="Okuma aralığı (saniye)")
    monitor_parser.add_argument("--threshold", type=float, default=None, help="Kritik sıcaklık eşiği (°C)")

    args = parser.parse_args()

    if args.command == "monitor":
        run_monitor(args.count, args.interval, args.threshold)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()