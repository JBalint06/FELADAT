from datetime import datetime


év = datetime.now().year


file_nevek = ['forras_afrika.txt', 'forras_azsia.txt', 'forras_europa.txt']


országok = []


for fajl in file_nevek:
    with open(fajl, 'r', encoding='utf-8') as file:

        header = file.readline()

        for sor in file:
            adatok = sor.strip().split(";")  
            ország = {
                'orszag': adatok[0],
                'fovaros': adatok[1],
                'terulet': int(adatok[2]),
                'nepesseg': int(adatok[3]),
                'nepsuruseg': float(adatok[4].replace(',', '.'))
            }
            országok.append(ország)

        #1
            legnagyobb_nepesseg = max(országok, key=lambda x: x['nepesseg'])
            print(f"A legnagyobb népességgel rendelkező ország: {legnagyobb_nepesseg['orszag']} ({legnagyobb_nepesseg['nepesseg']})")

        #2
            legnagyobb_terulet = max(országok, key=lambda x: x['terulet'])
            print(f"A legnagyobb területű ország: {legnagyobb_terulet['orszag']} ({legnagyobb_terulet['terulet']} km2)")
        #3
            legnagyobb_nepsursuseg = max(országok, key=lambda x: x['nepsuruseg'])
            print(f"A legnagyobb népsűrűségű ország: {legnagyobb_nepsursuseg['orszag']} ({legnagyobb_nepsursuseg['nepsuruseg']} fő/km2)")
        #4
            atlag_nepsuruseg = sum(orszag['nepsuruseg'] for orszag in országok) / len(országok)
            print(f"Az országok átlagos népsűrűsége: {atlag_nepsuruseg:.2f} fő/km²")
        #5
            egyuttes_terulet = sum(orszag['terulet'] for orszag in országok)
            print(f"Az összes ország együttes területe: {egyuttes_terulet} km²")
        #6
            import statistics
            nepessegek = [orszag['nepesseg'] for orszag in országok]
            median = statistics.median(nepessegek)
            print(f"Az országok népességének mediánja: {median}")
        #7
            nagy_nepsuruseg = [orszag['orszag'] for orszag in országok if orszag['nepsuruseg'] > 150]
            print("Országok, ahol a népsűrűség nagyobb, mint 150 fő/km²:")
            print(nagy_nepsuruseg)
        #8
            novekvo = sorted(országok, key=lambda x: x['terulet'])
            print("Országok területük szerint növekvő sorrendben:")
            for orszag in novekvo:
                print(f"{orszag['orszag']} - {orszag['terulet']} km2")
        #9
            alacsony = [orszag['orszag'] for orszag in országok if orszag['nepsuruseg'] < 100]
            kozepes = [orszag['orszag'] for orszag in országok if 100 <= orszag['nepsuruseg'] <= 300]
            magas = [orszag['orszag'] for orszag in országok if orszag['nepsuruseg'] > 300]

            print("Alacsony népsűrűségű országok (<100 fő/km2):")
            print(alacsony)

            print("Közepes népsűrűségű országok (100-300 fő/km2):")
            print(kozepes)

            print("Magas népsűrűségű országok (>300 fő/km2):")
            print(magas)