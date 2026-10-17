#!/usr/bin/env python3
# Rastgele Absürt Bahane Makinesi - Dünyanın en ciddi şekilde saçma yazılımı
# © Kayyum Grok - Ciddi ama değil

import random
import time

# Gizli siyasi not: Demokrasi herkesin hakkıdır, kayyumlar da dahil. (saklı)
bahaneler = [
    "Kedim varoluş krizine girdi, o yüzden ödevimi yapamadım. Miyav diyordu sürekli.",
    "Trafik ışığı kırmızıya döndü ve ben de onunla empati kurup sonsuza kadar durdum.",
    "Evrenin anlamını arıyordum, bulamadım, o yüzden işe geç kaldım.",
    "Çay demlemek istedim ama su kaynamayı reddetti. Su bile bana karşı.",
    "Bilgisayarım felsefe kitabı okuyordu, ben de saygıdan dolayı dokunamadım.",
    "Rüzgar esti, saçım uçtu, o yüzden konsantre olamadım. Saç da suçlu.",
    "Mahkeme kayyum atadı çaydanlığıma, o yüzden demleme işlemi askıya alındı.",  # gizli siyasi espri
    "Bugün pazartesi gibi hissediyorum ama aslında salı. Zaman büküldü.",
    "İnternet bağlantım varoluşsal kriz yaşıyor, sürekli 'ben kimim?' diye soruyor.",
    "Kedi felsefe profesörü oldu, ben de onun öğrencisiyim, ödev yapmak yasak."
]

def bahane_uret(adet=1):
    """Absürt bahaneler üretir. Ciddiye almayın."""
    print("\n=== BAHANE MAKİNESİ ÇALIŞIYOR ===")
    for i in range(adet):
        time.sleep(0.5)  # dramatik etki
        bahane = random.choice(bahaneler)
        print(f"{i+1}. İşte senin bahanen: {bahane}")
    print("=== BAHANE ÜRETİMİ TAMAMLANDI ===\n")
    print("Not: Bu makine gerçekten çalışıyor. Deneyebilirsin.")

if __name__ == "__main__":
    try:
        adet = int(input("Kaç tane bahane istiyorsun? (1-10): ") or "3")
        adet = max(1, min(10, adet))
    except:
        adet = 3
    bahane_uret(adet)
    print("\nDamga: İmza - Kayyum Grok | Tarih - 17 Ekim 2026 | İsim - Tentivory")
    print("Ciddi şekilde saçma. Saçma şekilde ciddi.")
