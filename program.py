class FA:
    def __init__(self, tokenValid):
        self.tokenValid = tokenValid

    def recognize(self, kata):
        return kata in self.tokenValid
    
class PDA:
    def __init__(self, s_recognizer, p_recognizer, o_recognizer, k_recognizer):
        self.s_recognizer = s_recognizer
        self.p_recognizer = p_recognizer
        self.o_recognizer = o_recognizer
        self.k_recognizer = k_recognizer

    def parse(self, tokens):
        state = 'S'
        struktur = []

        for token in tokens:
            if state == 'S':
                if self.s_recognizer.recognize(token):
                    struktur.append('S')
                    state = 'P'
                else:
                    return False, struktur
            elif state == 'P':
                if self.p_recognizer.recognize(token):
                    struktur.append('P')
                    state = 'O'
                else:
                    return False, struktur
            elif state == 'O':
                if self.o_recognizer.recognize(token):
                    struktur.append('O')
                    state = 'K'
                else:
                    if self.k_recognizer.recognize(token):
                        struktur.append('K')
                        state = 'END'
                    else:
                        return False, struktur
            elif state == 'K':
                if self.k_recognizer.recognize(token):
                    struktur.append('K')
                    state = 'END'
                else:
                    return False, struktur
            
        strukturValid = [['S', 'P', 'O', 'K'], ['S', 'P', 'K'], ['S', 'P', 'O'], ['S', 'P']]
        return struktur in strukturValid, struktur
    
def printToken(title, tokens):
    print("-" * 42)
    print(f"{title:^42}")
    print("-" * 42)
    rows = (len(tokens) + 3) // 3
    for i in range(rows):
        for j in range(3):
            idx = i + j * rows
            if idx < len(tokens):
                print(f"{tokens[idx]:<17}", end="")
            else:
                print(" " * 17, end="")
        print()
    print("\n")

def printStrukturValid():
    strukturValid = [
        "1. S - P - O - K",
        "2. S - P - O",
        "3. S - P - K",
        "4. S - P"
    ]
    print("="*42)
    print(f"{'POLA YANG VALID':^42}")
    print("\n")
    for struktur in strukturValid:
        print(f'{struktur:<37} [OK]')

def main():
    tokenSubjek = ["IBU", "RAJA", "KALIAN", "NONA", "KUCING"]
    tokenPredikat = ["MEMELIHARA", "MENGADAKAN", "MENJADWALKAN", "MEMANGGANG", "MENGEJAR"]
    tokenObjek = ["HAMSTER", "RAPAT", "KONSER", "KUE", "BOLA"]
    tokenKet = ["KECIL", "DI", "KERAJAAN", "BULAN", "DEPAN", "PAGI", "INI", "BESAR"]

    s_recognizer = FA(tokenSubjek)
    p_recognizer = FA(tokenPredikat)
    o_recognizer = FA(tokenObjek)
    k_recognizer = FA(tokenKet)

    parser = PDA(s_recognizer, p_recognizer, o_recognizer, k_recognizer)

    print("\n")
    print("="*42)
    print(f"{'TUBES TEORI BAHASA DAN AUTOMATA':^42}")

    print("\n")
    print(f"{'Anggota Kelompok':^42}")
    print("\n")
    print(f"{'Aulia Faradis Ishmah':<25} | {'1301220006':>14}")
    print(f"{'Imelia Dhevita Sari':<25} | {'1301220048':>14}")
    print(f"{'Rafelisha Ananfadya':<25} | {'1301223466':>14}")
    print("="*42)
    print("\n")

    print("="*42)
    print(f"{'KATA KUNCI':^42}")
    print("="*42)
    print("\n")
    printToken("SUBJEK", tokenSubjek)
    printToken("PREDIKAT", tokenPredikat)
    printToken("OBJEK", tokenObjek)
    printToken("KETERANGAN", tokenKet)
    print("="*42)
    print("\n")

    printStrukturValid()
    print("="*42)
    print("\n")

    kalimat = input("Masukkan Kalimat : ")
    tokens = kalimat.split()
    valid, struktur = parser.parse(tokens)

    print("\n")
    print("="*42)
    print(f"{'HASIL':^42}")
    print("\n")
    print(f"{'Kalimat':<10} {kalimat}")
    print(f"{'Struktur':<10} {' '.join(struktur)}")
    print(f"{'Validitas':<10} {valid}")
    print("="*42)

main()