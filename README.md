### README: Basit Tahmin Oyunu

#### Genel Bilgi
Bu program, kullanıcının 1 ile 100 arasında rastgele seçilmiş bir sayıyı tahmin etmeye çalıştığı bir "Tahmin Oyunu"dur. Oyuncunun toplamda 5 tahmin hakkı bulunmaktadır. Program, kullanıcıya tahminlerini yönlendirmek için daha büyük veya daha küçük bir sayı denemesi gerektiğini belirtir.

---

#### Kurulum ve Çalıştırma
1. **Python Kurulumu:**  
   Programı çalıştırmadan önce Python'ın bilgisayarınıza yüklü olduğundan emin olun. [Python İndir](https://www.python.org/downloads/)  

2. **Kodun Çalıştırılması:**  
   - `guessing_game.py` adında bir dosya oluşturun ve aşağıdaki kodu yapıştırın.
   - Terminal veya bir IDE üzerinden çalıştırmak için şu adımları izleyin:  
     ```bash
     python guessing_game.py
     ```

---

#### Nasıl Oynanır?
1. Program açıldığında, oyuncuya oyunun başladığına dair bir mesaj gösterilir:  
   **"Welcome to the Simple Guessing Game!"**

2. Oyuncu, klavyeden tahmin yapmak için bir sayı girer.

3. Program şu durumlara göre yanıt verir:
   - **Doğru Tahmin:** Oyuncu doğru sayıyı tahmin ettiğinde, "Congratulations! You guessed it right." mesajı gösterilir ve oyun sona erer.
   - **Yanlış Tahmin:** Oyuncu yanlış bir tahminde bulunduğunda, sayının daha büyük mü yoksa daha küçük mü olduğunu bildirir:
     - **Daha büyük:** "Enter a larger number."
     - **Daha küçük:** "Enter a smaller number."

4. Her tahminden sonra kalan hak bir azaltılır. Kalan tahmin hakkı 0 olduğunda oyun sona erer ve doğru sayı açıklanır:
   **"Your right to guess is over! Correct answer X idi."**

---

#### Örnek Kullanım
```bash
Welcome to the Simple Guessing Game!
Enter your prediction: 50
Enter a larger number.
Enter your prediction: 75
Enter a smaller number.
Enter your prediction: 60
Congratulations! You guessed it right.
```

---

#### İyileştirme Önerileri
- Kullanıcıya her tahminden sonra kaç tahmin hakkı kaldığını göstermek.
- Oyunu kazanma veya kaybetme durumunda yeniden başlatma seçeneği eklemek.
- Kullanıcının tahmin geçmişini listeleyerek, önceki tahminleri görmesini sağlamak.
- Zorluk seviyesi ekleyerek (kolay, orta, zor) tahmin hakkını veya sayı aralığını değiştirmek.

---

#### Gereksinimler
- Python 3.6 veya üzeri sürüm

Keyifli oyunlar! 
