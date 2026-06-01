# ROS 2 ve Gazebo ile Otonom Kurtarma Robotu Simülasyonu

Bu proje, **ROS 2 Humble** ve **Gazebo** simülasyon ortamı kullanılarak geliştirilmiş, engellerden otonom olarak kaçabilen bir kurtarma robotu (Burger modeli) uygulamasıdır. Proje, arama-kurtarma ve afet simülasyonları senaryolarında haritalandırılmamış alanlarda otonom keşif faaliyetlerine temel oluşturması amacıyla tasarlanmıştır.

## 🚀 Proje Özellikleri

- **Otonom Engel Kaçma:** 2D LiDAR (LaserScan) sensöründen gelen verileri anlık olarak işleyerek engelleri tespit eder.
- **Dinamik Karar Mekanizması:** Önündeki engelleri güvenli bir mesafeden algıladığında doğrusal hareketi durdurur ve güvenli yöne doğru kendi ekseninde dönerek rotasını düzeltir.
- **Gerçek Zamanlı Loglama:** Robotun anlık durumunu (Hız, Engel Tespiti, Dönüş Bilgisi) ROS 2 logger altyapısı üzerinden terminale yazdırır.

## 🛠️ Kullanılan Teknolojiler

- **İşletim Sistemi:** Ubuntu 22.04 LTS (Sanal Makine / VMware)
- **Robot İşletim Sistemi:** ROS 2 Humble Hawksbill
- **Simülasyon Ortamı:** Gazebo Simulator
- **Programlama Dili:** Python 3 (rclpy, sensor_msgs, geometry_msgs)
- **Robot Modeli:** TurtleBot3 (Burger)

## 📁 Proje Yapısı

```text
kurtarma-robotu-ros-2/
│
├── kurtarma_robotu.py    # Robotun otonom karar ve engelden kaçma mantığını içeren Python kodu
└── README.md             # Proje açıklama ve kullanım dokümanı
