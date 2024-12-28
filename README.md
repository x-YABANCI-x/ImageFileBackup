# Image File Backup

Bu Python scripti, `C:\\` sürücüsündeki tüm dizinleri tarar ve görüntü dosyalarını (`.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif` gibi uzantılarla) belirttiğiniz yedekleme klasörüne kopyalar. Orijinal klasör yapısı yedekleme konumunda korunur.

## Temel Özellikler

- `C:\\` sürücüsündeki görüntü dosyalarını otomatik olarak tarar.
- Görüntüleri hedef yedekleme dizinine kopyalar ve klasör yapısını korur.
- Gerekli durumlarda yedekleme konumunda eksik klasörleri oluşturur.

## Kullanım
1. `target_dir` değişkenini istediğiniz yedekleme konumuna ayarlayın.
2. Scripti çalıştırın:
    
    ```bash
    python image_backup.py

3. Script, tüm görüntü dosyalarını hedef klasöre kopyalar ve ilerlemeyi ekranda gösterir.
