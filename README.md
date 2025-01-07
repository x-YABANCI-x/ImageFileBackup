# Image File Backup (Turkish)

Bu Python scripti, `C:\\` sürücüsündeki tüm dizinleri tarar ve görüntü dosyalarını (`.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif` gibi uzantılarla) belirttiğiniz yedekleme klasörüne kopyalar. Orijinal klasör yapısı yedekleme konumunda korunur.

### Temel Özellikler
- `C:\\` sürücüsündeki görüntü dosyalarını otomatik olarak tarar.
- Görüntüleri hedef yedekleme dizinine kopyalar ve klasör yapısını korur.
- Gerekli durumlarda yedekleme konumunda eksik klasörleri oluşturur.

### Kullanım
**1.** `target_dir` değişkenini istediğiniz yedekleme konumuna ayarlayın.
**2.** Scripti çalıştırın:
    
```bash
python image_backup.py
```
**3.** Script, tüm görüntü dosyalarını hedef klasöre kopyalar ve ilerlemeyi ekranda gösterir.

<hr>

# Image File Backup (English)

This Python script scans all directories on the `C:\\` drive and copies image files (with extensions like `.jpg`, `.jpeg`, `.png`, `.bmp`, and `.gif`) to a specified backup directory. The original folder structure is preserved in the backup location.

### Key Features
- Automatically scans the `C:\\` drive for image files.
- Copies images to a specified target directory while maintaining the directory structure.
- Creates missing folders in the backup location as needed.

### Usage
**1.** Set the `target_dir` variable to your desired backup location.
**2.** Run the script: 

   ```bash
 python image_backup.py
```
**3.** The script will copy all image files to the target directory and display the progress.
