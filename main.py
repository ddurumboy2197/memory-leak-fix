import threading
import time

class KeyboardExtension:
    def __init__(self):
        self.lock = threading.Lock()
        self.running = False

    def start(self):
        with self.lock:
            if not self.running:
                self.running = True
                threading.Thread(target=self.run).start()

    def stop(self):
        with self.lock:
            if self.running:
                self.running = False

    def run(self):
        while self.running:
            # Keyboard extension logic here
            print("Keyboard extension is running...")
            time.sleep(1)

    def cleanup(self):
        self.stop()
        while threading.active_count() > 1:
            time.sleep(0.1)

def main():
    extension = KeyboardExtension()
    extension.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        extension.cleanup()

if __name__ == "__main__":
    main()
```

Kodda quyidagilar qilindi:

1. `KeyboardExtension` klassi yaratildi, unda `lock` obyekti va `running` boolean atributi mavjud.
2. `start` metodi `lock` obyekti bilan muvofaqatlanib, agar `running` atributi `False` bo'lsa, uni `True` ga o'zgartiradi va `run` metodi orqali yangi threadni boshlaydi.
3. `stop` metodi `lock` obyekti bilan muvofaqatlanib, agar `running` atributi `True` bo'lsa, uni `False` ga o'zgartiradi.
4. `run` metodi `while` tsikli orqali `running` atributi `True` bo'lganda ishlaydi.
5. `cleanup` metodi `stop` metodi orqali `running` atributi `False` ga o'zgartiradi va `while` tsikli orqali faol bo'lgan threadlar sonini 1 ga teng bo'lgunga qadar `time.sleep(0.1)` tsikli orqali o'tkazadi.
6. `main` funksiyasi `KeyboardExtension` obyekti yaratib, `start` metodi orqali yangi threadni boshlaydi va `try-except` tsikli orqali `KeyboardInterrupt` istisno bo'lishiga qadar `time.sleep(1)` tsikli orqali o'tkazadi. Agar `KeyboardInterrupt` istisno bo'lsa, `cleanup` metodi orqali threadni tozalaydi.
