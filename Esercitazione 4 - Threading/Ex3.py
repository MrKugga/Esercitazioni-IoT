import requests
from threading import Thread, Lock

class Translator(Thread):
    Nucleotides = ['A', 'T', 'C', 'G']

    codonDict = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': 'STOP', 'TAG': 'STOP',
        'TGC': 'C', 'TGT': 'C', 'TGA': 'STOP', 'TGG': 'W',
    }

    translated = []

    def __init__(self, protein, threadLock):
        Thread.__init__(self)
        self.protein = protein
        self.threadLock = threadLock

    def run(self):
        codons = [self.protein[i:i+3] for i in range(0, len(self.protein), 3)]
        translated_protein = ""
        for codon in codons:
            translated_protein += Translator.codonDict[codon.upper()]

        self.threadLock.acquire()
        Translator.translated.append(translated_protein)
        self.threadLock.release()


def split(string, separators): # separa le proteine in base ai codoni di stop

    codons = [string[i:i+3] for i in range(0, len(string), 3)]
    for i, codon in enumerate(codons):
        if codon in separators:
            codons[i] = " "
    proteins = "".join(codons).split()

    return proteins


def translate(chromosome):

    endpoint = "https://api.genome.ucsc.edu/getData/sequence"
    payload = {
        "genome": "hg38",
        "chrom": "chrUn_KI270394v1"
    }

    r = requests.get(endpoint, params= payload)
    if r.status_code != 200:
        return "Errore nella comunicazione col server."
    else:
        content = r.json()
        dna = content["dna"]
        stop_codons = [key.casefold() for key, value in Translator.codonDict.items() if value == "STOP"]
        proteins = split(dna, stop_codons)

        threads = []
        translated = []
        threadLock = Lock()
        for protein in proteins:
            threads.append(Translator(protein, threadLock))
        # print(len(dna)) # 970/3 -> 323 + 1, quell'uno dà ovviamente errore, ma non ci posso fare niente
        # threads.append(Translator(proteins[21], threadLock)) # debugging
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        return Translator.translated

if __name__ == "__main__":
    chromosome = "chrUn_KI270394v1"
    print(translate(chromosome))
