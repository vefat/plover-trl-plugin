

# STBKRLMAİEIPRTNŞLKSMÇ
KEYS = (
    'S-', 'T-', 'B-', 'K-', 'R-', 'L-', 'M-', 'A-', 'İ-', '-E',
    '-I', '-P', '-R', '-T', '-N', '-Ş', '-L', '-K', '-S', '-M', '-Ç'
)

IMPLICIT_HYPHEN_KEYS = KEYS

SUFFIX_KEYS = ()

NUMBER_KEY = None

NUMBERS = {}

UNDO_STROKE_STENO = 'U'

ORTHOGRAPHY_RULES = [
    # == +ler, +lar ==
    #: kedi + ler = kediler
    #: soru + lar = sorular
    (r"^(.*[aıou]) \^ ler$", r"\1lar"),
    (r"^(.*[eiüö]) \^ ler$", r"\1ler"),
    (r"^(.*[aıou][bcçdfgğhjklmnprsştvyz]) \^ ler$", r"\1lar"),
    (r"^(.*[eiöü][bcçdfgğhjklmnprsştvyz]) \^ ler$", r"\1ler"),

    # == +e, +a, +ye, +ya ==
    #: ev + e = eve
    #: at + a = ata
    #: kedi + ye = kediye
    #: soru + ya = soruya
    (r"^(.*[aıou]) \^ e$", r"\1ya"),
    (r"^(.*[aıou][bcçdfgğhjklmnprsştvyz]) \^ e$", r"\1a"),
    (r"^(.*[eiüö]) \^ e$", r"\1ye"),
    (r"^(.*[eiüö][bcçdfgğhjklmnprsştvyz]) \^ e$", r"\1e"),

    # == +i, +ı, +ü, +u, +yi, +yı, +yü, +yu ==
    #: kedi + si = kediyi
    #: halı + sı = halıyı
    #: menü + sü = menüyü
    #: soru + yu = soruyu
    #: ev + i = evi
    #: at + ı = atı
    #: göl + ü = gölü
    #: ton + u = tonu
    (r"^(.*[ei][bcçdfgğhjklmnpqrsştvwxyz]) \^ i$", r"\1i"),
    (r"^(.*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ i$", r"\1ı"),
    (r"^(.*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ i$", r"\1ü"),
    (r"^(.*[ou][bcçdfgğhjklmnpqrsştvwxyz]) \^ i$", r"\1u"),
    (r"^(.*[ei][^aeıioöuü]*) \^ i$", r"\1yi"),
    (r"^(.*[aı][^aeıioöuü]*) \^ i$", r"\1yı"),
    (r"^(.*[öü][^aeıioöuü]*) \^ i$", r"\1yü"),
    (r"^(.*[ou][^aeıioöuü]*) \^ i$", r"\1yu"),

    # == +den, +dan, +ten, +tan ==
    #: kedi + den = kediden
    #: soru + dan = sorudan
    #: et + ten = etten
    #: at + tan = attan
    (r"^(.*[aıou][fstkçşhp]) \^ den$", r"\1tan"),
    (r"^(.*[eiüö][fstkçşhp]) \^ den$", r"\1ten"),
    (r"^(.*[aıou][bcdgğjlmnqrvwxyz]) \^ den$", r"\1dan"),
    (r"^(.*[eiüö][bcdgğjlmnqrvwxyz]) \^ den$", r"\1den"),

    # == +de, +da, +te, +te ==
    #: kedi + de = kedide
    #: soru + da = soruda
    #: et + te = ette
    #: at + ta = atta
    (r"^(.*[aıou][fstkçşhp]) \^ de$", r"\1ta"),
    (r"^(.*[eiüö][fstkçşhp]) \^ de$", r"\1te"),
    (r"^(.*[aıou][bcdgğjlmnqrvwxyz]) \^ de$", r"\1da"),
    (r"^(.*[eiüö][bcdgğjlmnqrvwxyz]) \^ de$", r"\1de"),

    # == +m, +im, +ım, +üm, +um ==
    #: kedi + m = kedim
    #: ev + im = evim
    #: at + ım = atım
    #: göl + üm = gölüm
    #: ton + um = tonum
    (r"^(.*[aeıioöuü]) \^ im$", r"\1m"),
    (r"^(.*[ei][bcçdfgğhjklmnpqrsştvwxyz]) \^ im$", r"\1im"),
    (r"^(.*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ im$", r"\1ım"),
    (r"^(.*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ im$", r"\1üm"),
    (r"^(.*[ou][bcçdfgğhjklmnpqrsştvwxyz]) \^ im$", r"\1um"),

    # == +n, +in, +ın, +ün, +un ==
    #: kedi + n = kedin
    #: ev + in = evin
    #: at + ın = halkın
    #: göl + ün = gölün
    #: ton + un = tonun
    (r"^(.*[aeıioöuü]) \^ in$", r"\1n"),
    (r"^(.*[ei][bcçdfgğhjklmnpqrsştvwxyz]) \^ in$", r"\1in"),
    (r"^(.*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ in$", r"\1ın"),
    (r"^(.*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ in$", r"\1ün"),
    (r"^(.*[ou][bcçdfgğhjklmnpqrsştvwxyz]) \^ in$", r"\1un"),

    # == +si, +sı, +sü, +su, +i, +ı, +ü, +u ==
    #: kedi + si = kedisi
    #: halı + sı = halısı
    #: menü + sü = menüsü
    #: soru + su = sorusu
    #: ev + i = evi
    #: at + ı = atı
    #: göl + ü = gölü
    #: ton + u = tonu
    (r"^(.*[ei][bcçdfgğhjklmnpqrsştvwxyz]) \^ si$", r"\1i"),
    (r"^(.*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ si$", r"\1ı"),
    (r"^(.*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ si$", r"\1ü"),
    (r"^(.*[ou][bcçdfgğhjklmnpqrsştvwxyz]) \^ si$", r"\1u"),
    (r"^(.*[ei][^aeıioöuü]*) \^ si$", r"\1si"),
    (r"^(.*[aı][^aeıioöuü]*) \^ si$", r"\1sı"),
    (r"^(.*[öü][^aeıioöuü]*) \^ si$", r"\1sü"),
    (r"^(.*[ou][^aeıioöuü]*) \^ si$", r"\1su"),


    # == +miz, +imiz, +ımız, +ümüz, +umuz ==
    #: kedi + miz = kedimiz
    #: ev + imiz = evimiz
    #: at + ımız = atımız
    #: göl + ümüz = gölümüz
    #: ton + umuz = tonumuz
    (r"^(.*[aeıioöuü]) \^ miz$", r"\1miz"),
    (r"^(.*[ei][bcçdfgğhjklmnpqrsştvwxyz]) \^ miz$", r"\1imiz"),
    (r"^(.*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ miz$", r"\1ımız"),
    (r"^(.*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ miz$", r"\1ümüz"),
    (r"^(.*[ou][bcçdfgğhjklmnpqrsştvwxyz]) \^ miz$", r"\1umuz"),


    # == +niz, +iniz, +ınız, +ünüz, +unuz ==
    #: kedi + niz = kediniz
    #: ev + iniz = eviniz
    #: at + ıniz = atınız
    #: göl + ünüz = gölünüz
    #: ton + unuz = tonunuz
    (r"^(.*[aeıioöuü]) \^ niz$", r"\1niz"),
    (r"^(.*[ei][bcçdfgğhjklmnpqrsştvwxyz]) \^ niz$", r"\1iniz"),
    (r"^(.*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ niz$", r"\1ınız"),
    (r"^(.*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ niz$", r"\1ünüz"),
    (r"^(.*[ou][bcçdfgğhjklmnpqrsştvwxyz]) \^ niz$", r"\1unuz"),

    # == +leri, +ları ==
    #: kedi + leri = kedileri
    #: soru + ları = soruları
    (r"^(.*[aıou]) \^ leri$", r"\1ları"),
    (r"^(.*[eiüö]) \^ leri$", r"\1leri"),

    # == +nin, +nın, +nun, +nün, +in, +ın, +un, +ün ==
    #: kedi + nin = kedinin
    #: halı + nın = halının
    #: menü + nün = menünün
    #: soru + nun = sorunun
    #: ev + in = evin
    #: at + ın = atın
    #: göl + ün = gölün
    #: ton + un = tonun
    (r"^(.*[ei][bcçdfgğhjklmnpqrsştvwxyz]) \^ in$", r"\1in"),
    (r"^(.*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ in$", r"\1ın"),
    (r"^(.*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ in$", r"\1ün"),
    (r"^(.*[ou][bcçdfgğhjklmnpqrsştvwxyz]) \^ in$", r"\1un"),
    (r"^(.*[ei][^aeıioöuü]*) \^ in$", r"\1nin"),
    (r"^(.*[aı][^aeıioöuü]*) \^ in$", r"\1nın"),
    (r"^(.*[öü][^aeıioöuü]*) \^ in$", r"\1nün"),
    (r"^(.*[ou][^aeıioöuü]*) \^ in$", r"\1nun"),
    
    # == +yorum, +iyorum, +ıyorum, +uyorum, +üyorum ==
    #: uyu + yorum = uyuyorum
    #: geç + iyorum = geçiyorum
    #: al + ıyorum = alıyorum
    #: kon + uyorum = konuyorum
    #: böl + üyorum = bölüyorum
    #: anla + ıyorum = anlıyorum
    #: de + iyorum = diyorum
    (r"^(.*[ei][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yorum)$", r"\1iyorum"),
    (r"^(.*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yorum)$", r"\1ıyorum"),
    (r"^(.*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yorum)$", r"\1üyorum"),
    (r"^(.*[ou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yorum)$", r"\1uyorum"),
    (r"^(.*)[ao] \^ (yorum)$", r"\1ıyorum"),
    (r"^(.*)[eö] \^ (yorum)$", r"\1iyorum"),
    (r"^(.*[aeiıöoüu]) \^ (yorum)$", r"\1yorum"),

    # == +yorsun, +iyorsun, +ıyorsun, +uyorsun, +üyorsun ==
    #: uyu + yorsun = uyuyorsun
    #: geç + iyorsun = geçiyorsun
    #: al + ıyorsun = alıyorsun
    #: kon + uyorsun = konuyorsun
    #: böl + üyorsun = bölüyorsun
    #: anla + ıyorsun = anlıyorsun
    #: de + iyorsun = diyorsun
    (r"^(.*[ei][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yorsun)$", r"\1iyorsun"),
    (r"^(.*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yorsun)$", r"\1ıyorsun"),
    (r"^(.*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yorsun)$", r"\1üyorsun"),
    (r"^(.*[ou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yorsun)$", r"\1uyorsun"),
    (r"^(.*)[ao] \^ (yorsun)$", r"\1ıyorsun"),
    (r"^(.*)[eö] \^ (yorsun)$", r"\1iyorsun"),
    (r"^(.*[aeiıöoüu]) \^ (yorsun)$", r"\1yorsun"),

    # == +yor, +iyor, +ıyor, +uyor, +üyor ==
    #: uyu + yor = uyuyor
    #: geç + iyor = geçiyor
    #: al + ıyor = alıyor
    #: kon + uyor = konuyor
    #: böl + üyor = bölüyor
    #: anla + yor = anlıyor
    #: de + iyor = diyor
    (r"^(.*[ei][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yor)$", r"\1iyor"),
    (r"^(.*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yor)$", r"\1ıyor"),
    (r"^(.*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yor)$", r"\1üyor"),
    (r"^(.*[ou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yor)$", r"\1uyor"),
    (r"^(.*)[ao] \^ (yor)$", r"\1ıyor"),
    (r"^(.*)[eö] \^ (yor)$", r"\1iyor"),
    (r"^(.*[aeiıöoüu]) \^ (yor)$", r"\1yor"),

    # == +yoruz, +iyoruz, +ıyoruz, +uyoruz, +üyoruz ==
    #: uyu + yoruz = uyuyoruz
    #: geç + iyoruz = geçiyoruz
    #: al + ıyoruz = alıyoruz
    #: kon + uyoruz = konuyoruz
    #: böl + üyoruz = bölüyoruz
    #: anla + yoruz = anlıyoruz
    #: de + iyoruz = diyoruz
    (r"^(.*[ei][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yoruz)$", r"\1iyoruz"),
    (r"^(.*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yoruz)$", r"\1ıyoruz"),
    (r"^(.*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yoruz)$", r"\1üyoruz"),
    (r"^(.*[ou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yoruz)$", r"\1uyoruz"),
    (r"^(.*)[ao] \^ (yoruz)$", r"\1ıyoruz"),
    (r"^(.*)[eö] \^ (yoruz)$", r"\1iyoruz"),
    (r"^(.*[aeiıöoüu]) \^ (yoruz)$", r"\1yoruz"),

     # == +yorsunuz, +iyorsunuz, +ıyorsunuz, +uyorsunuz, +üyorsunuz ==
    #: uyu + yorsunuz = uyuyorsunuz
    #: geç + iyorsunuz = geçiyorsunuz
    #: al + ıyorsunuz = alıyorsunuz
    #: kon + uyorsunuz = konuyorsunuz
    #: böl + üyorsunuz = bölüyorsunuz
    #: anla + yorsunuz = anlıyorsunuz
    #: de + iyorsunuz = diyorsunuz
    (r"^(.*[ei][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yorsunuz)$", r"\1iyorsunuz"),
    (r"^(.*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yorsunuz)$", r"\1ıyorsunuz"),
    (r"^(.*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yorsunuz)$", r"\1üyorsunuz"),
    (r"^(.*[ou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yorsunuz)$", r"\1uyorsunuz"),
    (r"^(.*)[ao] \^ (yorsunuz)$", r"\1ıyorsunuz"),
    (r"^(.*)[eö] \^ (yorsunuz)$", r"\1iyorsunuz"),
    (r"^(.*[aeiıöoüu]) \^ (yorsunuz)$", r"\1yorsunuz"),

    # == +yorlar, +iyorlar, +ıyorlar, +uyorlar, +üyorlar ==
    #: uyu + yorlar = uyuyorlar
    #: geç + iyor = geçiyorlar
    #: al + ıyorlar = alıyorlar
    #: kon + uyorlar = konuyorlar
    #: böl + üyorlar = bölüyorlar
    #: anla + yorlar = anlıyorlar
    #: de + iyorlar = diyorlar
    (r"^(.*[ei][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yorlar)$", r"\1iyorlar"),
    (r"^(.*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yorlar)$", r"\1ıyorlar"),
    (r"^(.*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yorlar)$", r"\1üyorlar"),
    (r"^(.*[ou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yorlar)$", r"\1uyorlar"),
    (r"^(.*)[ao] \^ (yorlar)$", r"\1ıyorlar"),
    (r"^(.*)[eö] \^ (yorlar)$", r"\1iyorlar"),
    (r"^(.*[aeiıöoüu]) \^ (yorlar)$", r"\1yorlar"),

    # == +rum, +rim, +rım, +rüm, +irim, +ırım, +erim, +arım, +urum, +ürüm ==
    #: uyu + rum = uyurum
    #: eri + rim = eririm
    #: ara + rım = ararım
    #: çürü + rüm = çürürüm
    #: geç + erim = geçerim
    #: kon + arım = konarım
    #: çalış + ırım = çalışırım
    #: gerek + irim = gerekirim
    #: düşün + ürüm = düşünürüm
    #: bulun + urum = bulunurum
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (rim)$", r"\1erim"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (rim)$", r"\1arım"),
    (r"^((.*)(.*).*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ (rim)$", r"\1ırım"),
    (r"^((.*)(.*).*[ei][[bcçdfgğhjklmnpqrsştvwxyz]) \^ (rim)$", r"\1irim"),
    (r"^((.*)(.*).*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (rim)$", r"\1ürüm"),
    (r"^((.*)(.*).*[ou][[bcçdfgğhjklmnpqrsştvwxyz]) \^ (rim)$", r"\1urum"),
    (r"^(.*[ei]) \^ (rim)$", r"\1rim"),
    (r"^(.*[aı]) \^ (rim)$", r"\1rım"),
    (r"^(.*[ou]) \^ (rim)$", r"\1rum"),
    (r"^(.*[öü]) \^ (rim)$", r"\1rüm"),

    # == +rsun, +rsin, +rsın, +rsün, +irsin, +ırsın, +ersin, +arsın, +ursun, +ürsün ==
    #: uyu + rsun = uyursun
    #: eri + rsin = erirsin
    #: ara + rsın = ararsın
    #: çürü + rsün = çürürsün
    #: geç + ersin = geçersin
    #: kon + arsın = konarsın
    #: çalış + ırsın = çalışırsın
    #: gerek + irsin = gerekirsin
    #: düşün + ürsün = düşünürsün
    #: bulun + ursun = bulunursun
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (rsin)$", r"\1ersin"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (rsin)$", r"\1arsın"),
    (r"^((.*)(.*).*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ (rsin)$", r"\1ırsın"),
    (r"^((.*)(.*).*[ei][[bcçdfgğhjklmnpqrsştvwxyz]) \^ (rsin)$", r"\1irsin"),
    (r"^((.*)(.*).*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (rsin)$", r"\1ürsün"),
    (r"^((.*)(.*).*[ou][[bcçdfgğhjklmnpqrsştvwxyz]) \^ (rsin)$", r"\1ursun"),
    (r"^(.*[ei]) \^ (rsin)$", r"\1rsin"),
    (r"^(.*[aı]) \^ (rsin)$", r"\1rsın"),
    (r"^(.*[ou]) \^ (rsin)$", r"\1rsun"),
    (r"^(.*[öü]) \^ (rsin)$", r"\1rsün"),

    # == +r, +ir, +ır, +er, +ar, +ur, +ür ==
    #: uyu + r = uyur
    #: geç + er = geçer
    #: kon + ar = konar
    #: çalış + ır = çalışır
    #: gerek + ir = gerekir
    #: düşün + ür = düşünür
    #: bulun + ur = bulunur
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (ir)$", r"\1er"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (ir)$", r"\1ar"),
    (r"^((.*)(.*).*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ (ir)$", r"\1ır"),
    (r"^((.*)(.*).*[ei][[bcçdfgğhjklmnpqrsştvwxyz]) \^ (ir)$", r"\1ir"),
    (r"^((.*)(.*).*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (ir)$", r"\1ür"),
    (r"^((.*)(.*).*[ou][[bcçdfgğhjklmnpqrsştvwxyz]) \^ (ir)$", r"\1ur"),
    (r"^(.*[aeıioöüu]) \^ (ir)$", r"\1r"),

    # == +ruz, +riz, +rız, +rüz, +iriz, +ırız, +eriz, +arız, +uruz, +ürüz ==
    #: uyu + rum = uyurum
    #: eri + rim = eririm
    #: ara + rım = ararım
    #: çürü + rüm = çürürüm
    #: geç + erim = geçerim
    #: kon + arım = konarım
    #: çalış + ırım = çalışırım
    #: gerek + irim = gerekirim
    #: düşün + ürüm = düşünürüm
    #: bulun + urum = bulunurum
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (riz)$", r"\1eriz"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (riz)$", r"\1arız"),
    (r"^((.*)(.*).*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ (riz)$", r"\1ırız"),
    (r"^((.*)(.*).*[ei][[bcçdfgğhjklmnpqrsştvwxyz]) \^ (riz)$", r"\1iriz"),
    (r"^((.*)(.*).*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (riz)$", r"\1ürüz"),
    (r"^((.*)(.*).*[ou][[bcçdfgğhjklmnpqrsştvwxyz]) \^ (riz)$", r"\1uruz"),
    (r"^(.*[ei]) \^ (riz)$", r"\1riz"),
    (r"^(.*[aı]) \^ (riz)$", r"\1rız"),
    (r"^(.*[ou]) \^ (riz)$", r"\1ruz"),
    (r"^(.*[öü]) \^ (riz)$", r"\1rüz"),

    # == +rsunuz, +rsiniz, +rsınız, +rsünüz, +irsiniz, +ırsınız, +ersiniz, +arsınız, +ursunuz, +ürsünüz ==
    #: uyu + rsunuz = uyursunuz
    #: eri + rsiniz = erirsiniz
    #: ara + rsınız = ararsınız
    #: çürü + rsünüz = çürürsünüz
    #: geç + ersiniz = geçersiniz
    #: kon + arsınız = konarsınız
    #: çalış + ırsınız = çalışırsınız
    #: gerek + irsiniz = gerekirsiniz
    #: düşün + ürsünüz = düşünürsünüz
    #: bulun + ursunuz = bulunursunuz
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (rsiniz)$", r"\1ersiniz"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (rsiniz)$", r"\1arsınız"),
    (r"^((.*)(.*).*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ (rsiniz)$", r"\1ırsınız"),
    (r"^((.*)(.*).*[ei][[bcçdfgğhjklmnpqrsştvwxyz]) \^ (rsiniz)$", r"\1irsiniz"),
    (r"^((.*)(.*).*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (rsiniz)$", r"\1ürsünüz"),
    (r"^((.*)(.*).*[ou][[bcçdfgğhjklmnpqrsştvwxyz]) \^ (rsiniz)$", r"\1ursunuz"),
    (r"^(.*[ei]) \^ (rsiniz)$", r"\1rsiniz"),
    (r"^(.*[aı]) \^ (rsiniz)$", r"\1rsınız"),
    (r"^(.*[ou]) \^ (rsiniz)$", r"\1rsunuz"),
    (r"^(.*[öü]) \^ (rsiniz)$", r"\1rsünüz"),

    # == +rlar, +rler, +irler, +ırlar, +erler, +arlar, +urlar, +ürler ==
    #: uyu + rlar = uyurlar
    #: eri + rler = erirler
    #: geç + erler = geçerler
    #: kon + arlar = konarlar
    #: çalış + ırlar = çalışırlar
    #: gerek + irler = gerekirler
    #: düşün + ürler = düşünürler
    #: bulun + urlar = bulunurlar
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (irler)$", r"\1erler"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (irler)$", r"\1arlar"),
    (r"^((.*)(.*).*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ (irler)$", r"\1ırlar"),
    (r"^((.*)(.*).*[ei][[bcçdfgğhjklmnpqrsştvwxyz]) \^ (irler)$", r"\1irler"),
    (r"^((.*)(.*).*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (irler)$", r"\1ürler"),
    (r"^((.*)(.*).*[ou][[bcçdfgğhjklmnpqrsştvwxyz]) \^ (irler)$", r"\1urlar"),
    (r"^(.*[eiöü]) \^ (irler)$", r"\1rler"),
    (r"^(.*[aıou]) \^ (irler)$", r"\1rlar"),

    # == +miyorum, +mıyorum, +muyorum, +müyorüm ==
    #: geç + miyorum = geçmiyorum
    #: al + mıyorum = almıyorum
    #: kon + muyorum = konmuyorum
    #: böl + müyorum = bölmüyorum
    (r"^(.*[ei][bcçdfgğhjklmnpqrsştvwxyz]) \^ (miyorum)$", r"\1miyorum"),
    (r"^(.*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ (miyorum)$", r"\1mıyorum"),
    (r"^(.*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (miyorum)$", r"\1müyorum"),
    (r"^(.*[ou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (miyorum)$", r"\1muyorum"),
    (r"^(.*[ei]) \^ (miyorum)$", r"\1miyorum"),
    (r"^(.*[aı]) \^ (miyorum)$", r"\1mıyorum"),
    (r"^(.*[öü]) \^ (miyorum)$", r"\1müyorum"),
    (r"^(.*[ou]) \^ (miyorum)$", r"\1muyorum"),

    # == +miyorsun, +mıyorsun, +muyorsun, +müyorsün ==
    #: geç + miyorsun = geçmiyorsun
    #: al + mıyorsun = almıyorsun
    #: kon + muyorsun = konmuyorsun
    #: böl + müyorsun = bölmüyorsun
    (r"^(.*[ei][bcçdfgğhjklmnpqrsştvwxyz]) \^ (miyorsun)$", r"\1miyorsun"),
    (r"^(.*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ (miyorsun)$", r"\1mıyorsun"),
    (r"^(.*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (miyorsun)$", r"\1müyorsun"),
    (r"^(.*[ou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (miyorsun)$", r"\1muyorsun"),
    (r"^(.*[ei]) \^ (miyorsun)$", r"\1miyorsun"),
    (r"^(.*[aı]) \^ (miyorsun)$", r"\1mıyorsun"),
    (r"^(.*[öü]) \^ (miyorsun)$", r"\1müyorsun"),
    (r"^(.*[ou]) \^ (miyorsun)$", r"\1muyorsun"),

    # == +miyor, +mıyor, +muyor, +müyor ==
    #: geç + miyor = geçmiyor
    #: al + mıyor = almıyor
    #: kon + muyor = konmuyor
    #: böl + müyor = bölmüyor
    (r"^(.*[ei][bcçdfgğhjklmnpqrsştvwxyz]) \^ (miyor)$", r"\1miyor"),
    (r"^(.*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ (miyor)$", r"\1mıyor"),
    (r"^(.*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (miyor)$", r"\1müyor"),
    (r"^(.*[ou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (miyor)$", r"\1muyor"),
    (r"^(.*[ei]) \^ (miyor)$", r"\1miyor"),
    (r"^(.*[aı]) \^ (miyor)$", r"\1mıyor"),
    (r"^(.*[öü]) \^ (miyor)$", r"\1müyor"),
    (r"^(.*[ou]) \^ (miyor)$", r"\1muyor"),

    # == +miyoruz, +mıyoruz, +muyoruz, +müyoruz ==
    #: geç + miyoruz = geçmiyoruz
    #: al + mıyoruz = almıyoruz
    #: kon + muyoruz = konmuyoruz
    #: böl + müyoruz = bölmüyoruz
    (r"^(.*[ei][bcçdfgğhjklmnpqrsştvwxyz]) \^ (miyoruz)$", r"\1miyoruz"),
    (r"^(.*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ (miyoruz)$", r"\1mıyoruz"),
    (r"^(.*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (miyoruz)$", r"\1müyoruz"),
    (r"^(.*[ou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (miyoruz)$", r"\1muyoruz"),
    (r"^(.*[ei]) \^ (miyoruz)$", r"\1miyoruz"),
    (r"^(.*[aı]) \^ (miyoruz)$", r"\1mıyoruz"),
    (r"^(.*[öü]) \^ (miyoruz)$", r"\1müyoruz"),
    (r"^(.*[ou]) \^ (miyoruz)$", r"\1muyoruz"),

    # == +miyorsunuz, +mıyorsunuz, +muyorsunuz, +müyorsunuz ==
    #: geç + miyorsunuz = geçmiyorsunuz
    #: al + mıyorsunuz = almıyorsunuz
    #: kon + muyorsunuz = konmuyorsunuz
    #: böl + müyorsunuz = bölmüyorsunuz
    (r"^(.*[ei][bcçdfgğhjklmnpqrsştvwxyz]) \^ (miyorsunuz)$", r"\1miyorsunuz"),
    (r"^(.*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ (miyorsunuz)$", r"\1mıyorsunuz"),
    (r"^(.*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (miyorsunuz)$", r"\1müyorsunuz"),
    (r"^(.*[ou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (miyorsunuz)$", r"\1muyorsunuz"),
    (r"^(.*[ei]) \^ (miyorsunuz)$", r"\1miyorsunuz"),
    (r"^(.*[aı]) \^ (miyorsunuz)$", r"\1mıyorsunuz"),
    (r"^(.*[öü]) \^ (miyorsunuz)$", r"\1müyorsunuz"),
    (r"^(.*[ou]) \^ (miyorsunuz)$", r"\1muyorsunuz"),

    # == +miyorlar, +mıyorlar, +muyorlar, +müyorlar ==
    #: geç + miyorlar = geçmiyorlar
    #: al + mıyorlar = almıyorlar
    #: kon + muyorlar = konmuyorlar
    #: böl + müyorlar = bölmüyorlar
    (r"^(.*[ei][bcçdfgğhjklmnpqrsştvwxyz]) \^ (miyorlar)$", r"\1miyorlar"),
    (r"^(.*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ (miyorlar)$", r"\1mıyorlar"),
    (r"^(.*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (miyorlar)$", r"\1müyorlar"),
    (r"^(.*[ou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (miyorlar)$", r"\1muyorlar"),
    (r"^(.*[ei]) \^ (miyorlar)$", r"\1miyorlar"),
    (r"^(.*[aı]) \^ (miyorlar)$", r"\1mıyorlar"),
    (r"^(.*[öü]) \^ (miyorlar)$", r"\1müyorlar"),
    (r"^(.*[ou]) \^ (miyorlar)$", r"\1muyorlar"),

    # == +mam, +mem ==
    #: uyu + mam = uyumam
    #: geç + mem = geçmem
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mem)$", r"\1mem"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mem)$", r"\1mam"),
    (r"^(.*[eiöü]) \^ (mem)$", r"\1mem"),
    (r"^(.*[aıou]) \^ (mem)$", r"\1mam"),

    # == +mazsın, +mezsin ==
    #: uyu + mazsın = uyumazsın
    #: geç + mezsin = geçmezin
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mezsin)$", r"\1mezsin"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mezsin)$", r"\1mazsın"),
    (r"^(.*[eiöü]) \^ (mezsin)$", r"\1mezsin"),
    (r"^(.*[aıou]) \^ (mezsin)$", r"\1mazsın"),

    # == +maz, +mez ==
    #: uyu + maz = uyumaz
    #: geç + mez = geçmez
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mez)$", r"\1mez"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mez)$", r"\1maz"),
    (r"^(.*[eiöü]) \^ (mez)$", r"\1mez"),
    (r"^(.*[aıou]) \^ (mez)$", r"\1maz"),

    # == +mayız, +meyiz ==
    #: uyu + mayız = uyumayız
    #: geç + meyiz = geçmeyiz
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (meyiz)$", r"\1meyiz"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (meyiz)$", r"\1mayız"),
    (r"^(.*[eiöü]) \^ (meyiz)$", r"\1meyiz"),
    (r"^(.*[aıou]) \^ (meyiz)$", r"\1mayız"),

    # == +mazsınız, +mezsiniz ==
    #: uyu + mazsınız = uyumazsınız
    #: geç + mezsiniz = geçmezsiniz
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mezsiniz)$", r"\1mezsiniz"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mezsiniz)$", r"\1mazsınız"),
    (r"^(.*[eiöü]) \^ (mezsiniz)$", r"\1mezsiniz"),
    (r"^(.*[aıou]) \^ (mezsiniz)$", r"\1mazsınız"),

    # == +mazlar, +mezler ==
    #: uyu + mazlar = uyumazlar
    #: geç + mezler = geçmezler
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mezler)$", r"\1mezler"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mezler)$", r"\1mazlar"),
    (r"^(.*[eiöü]) \^ (mezler)$", r"\1mezler"),
    (r"^(.*[aıou]) \^ (mezler)$", r"\1mazlar"),

    # == +maz, +mez ==
    #: uyu + maz = uyumazlar
    #: geç + mez = geçmezler
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mezler)$", r"\1mezler"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mezler)$", r"\1mazlar"),
    (r"^(.*[eiöü]) \^ (mezler)$", r"\1mezler"),
    (r"^(.*[aıou]) \^ (mezler)$", r"\1mazlar"),

    # == +sam, +sem ==
    #: uyu + sam = uyusam
    #: eri + sem = erisem
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ sem$", r"\1sam"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ sem$", r"\1sem"),
    (r"^(.*[aıou]) \^ sem$", r"\1sam"),
    (r"^(.*[eiöü]) \^ sem$", r"\1sem"),

    # == +san, +sen ==
    #: uyu + sa = uyusan
    #: eri + se = erisen
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ sen$", r"\1san"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ sen$", r"\1sen"),
    (r"^(.*[aıou]) \^ sen$", r"\1san"),
    (r"^(.*[eiöü]) \^ sen$", r"\1sen"),

    # == +sa, +se ==
    #: uyu + sa = uyusa
    #: eri + se = erise
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ se$", r"\1sa"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ se$", r"\1se"),
    (r"^(.*[aıou]) \^ se$", r"\1sa"),
    (r"^(.*[eiöü]) \^ se$", r"\1se"),

    # == +sak, +sek ==
    #: uyu + sak = uyusak
    #: eri + sek = erisek
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ sek$", r"\1sak"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ sek$", r"\1sek"),
    (r"^(.*[aıou]) \^ sek$", r"\1sa"),
    (r"^(.*[eiöü]) \^ sek$", r"\1se"),

    # == +sanız, +seniz ==
    #: uyu + sa = uyusanız
    #: eri + se = eriseniz
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ seniz$", r"\1sanız"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ seniz$", r"\1seniz"),
    (r"^(.*[aıou]) \^ senız$", r"\1sanız"),
    (r"^(.*[eiöü]) \^ seniz$", r"\1seniz"),

    # == +salar, +seler ==
    #: uyu + salar = uyusalar
    #: eri + seler = eriseler
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ seler$", r"\1salar"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ seler$", r"\1seler"),
    (r"^(.*[aıou]) \^ selar$", r"\1salar"),
    (r"^(.*[eiöü]) \^ seler$", r"\1seler"),

    # == +masam, +mesem ==
    #: uyu + masam = uyumasam
    #: eri + mesem = erimesem
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ mesem$", r"\1masam"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ mesem$", r"\1mesem"),
    (r"^(.*[aıou]) \^ mesem$", r"\1masam"),
    (r"^(.*[eiöü]) \^ mesem$", r"\1mesem"),

    # == +masan, +mesen ==
    #: uyu + masan = uyumasan
    #: eri + mesen = erimesen
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ mesen$", r"\1masan"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ mesen$", r"\1mesen"),
    (r"^(.*[aıou]) \^ mesen$", r"\1masan"),
    (r"^(.*[eiöü]) \^ mesen$", r"\1mesen"),

    # == +masa, +mese ==
    #: uyu + masa = uyumasa
    #: eri + mese = erimese
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ mese$", r"\1masa"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ mese$", r"\1mese"),
    (r"^(.*[aıou]) \^ mese$", r"\1masa"),
    (r"^(.*[eiöü]) \^ mese$", r"\1mese"),

    # == +masak, +mesek ==
    #: uyu + masak = uyumasak
    #: eri + mesek = erimesek
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ mesek$", r"\1masak"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ mesek$", r"\1mesek"),
    (r"^(.*[aıou]) \^ mesek$", r"\1masak"),
    (r"^(.*[eiöü]) \^ mesek$", r"\1mesek"),

    # == +masanız, +meseniz ==
    #: uyu + masanız = uyumasanız
    #: eri + meseniz = erimeseniz
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ meseniz$", r"\1masanız"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ meseniz$", r"\1meseniz"),
    (r"^(.*[aıou]) \^ meseniz$", r"\1masanız"),
    (r"^(.*[eiöü]) \^ meseniz$", r"\1meseniz"),

    # == +masalar, +meseler ==
    #: uyu + masalar = uyumasalar
    #: eri + meseler = erimeseler
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ meseler$", r"\1masalar"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ meseler$", r"\1meseler"),
    (r"^(.*[aıou]) \^ meseler$", r"\1masalar"),
    (r"^(.*[eiöü]) \^ meseler$", r"\1meseler"),

    # == +yacağım, +yeceğim, +acağım, +eceğim ==
    #: uyu + yacağım = uyuyacağım
    #: eri + yeceğim = eriyeceğim
    #: al + acağım = alacağım
    #: böl + eceğim = böleceğim
    (r"^(.*[eiöü]) \^ (yeceğim)$", r"\1yeceğim"),
    (r"^(.*[aıou]) \^ (yeceğim)$", r"\1yacağım"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yeceğim)$", r"\1eceğim"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yeceğim)$", r"\1acağım"),

    # == +yacaksın, +yeceksin, +acaksın, +eceksin ==
    #: uyu + yacaksın = uyuyacaksın
    #: eri + yeceksin = eriyeceksin
    #: al + acaksın = alacaksın
    #: böl + eceksin = böleceksin
    (r"^(.*[eiöü]) \^ (yeceksin)$", r"\1yeceksin"),
    (r"^(.*[aıou]) \^ (yeceksin)$", r"\1yacaksın"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yeceksin)$", r"\1eceksin"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yeceksin)$", r"\1acaksın"),

    # == +yacak, +yecek, +acak, +ecek ==
    #: uyu + yacak = uyuyacak
    #: eri + yecek = eriyecek
    #: al + acak = alacak
    #: böl + ecek = bölecek
    (r"^(.*[eiöü]) \^ (yecek)$", r"\1yecek"),
    (r"^(.*[aıou]) \^ (yecek)$", r"\1yacak"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yecek)$", r"\1ecek"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yecek)$", r"\1acak"),

    # == +yacağız, +yeceğiz, +acağız, +eceğiz ==
    #: uyu + yacağız = uyuyacağız
    #: eri + yeceğiz = eriyeceğiz
    #: al + acağız = alacağız
    #: böl + eceğiz = böleceğiz
    (r"^(.*[eiöü]) \^ (yeceğiz)$", r"\1yeceğiz"),
    (r"^(.*[aıou]) \^ (yeceğiz)$", r"\1yacağım"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yeceğiz)$", r"\1eceğiz"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yeceğiz)$", r"\1acağız"),
    
     # == +yacaksınız, +yeceksiniz, +acaksınız, +eceksiniz ==
    #: uyu + yacaksınız = uyuyacaksınız
    #: eri + yeceksiniz = eriyeceksiniz
    #: al + acaksınız = alacaksınız
    #: böl + eceksiniz = böleceksiniz
    (r"^(.*[eiöü]) \^ (yeceksiniz)$", r"\1yeceksiniz"),
    (r"^(.*[aıou]) \^ (yeceksiniz)$", r"\1yacaksınız"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yeceksiniz)$", r"\1eceksiniz"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yeceksiniz)$", r"\1acaksınız"),

    # == +yacaklar, +yecekler, +acaklar, +ecekler ==
    #: uyu + yacaklar = uyuyacaklar
    #: eri + yecek = eriyecekler
    #: al + acaklar = alacaklar
    #: böl + ecek = bölecekler
    (r"^(.*[eiöü]) \^ (yecekler)$", r"\1yecekler"),
    (r"^(.*[aıou]) \^ (yecekler)$", r"\1yacaklar"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yecekler)$", r"\1ecekler"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yecekler)$", r"\1acaklar"),

    # == +dim, +dım, +dum, +düm, +tim, +tım, +tum, +tüm ==
    #: uyu + dum = uyudum
    #: eri + dim = eridim
    #: al + dım = aldım
    #: böl + düm = böldüm
    #: geç + tim = geçtim
    #: çalış + tım = çalıştım
    #: tut + tum = tuttum
    #: öt + tüm = öttüm
    (r"^(.*[ou][fstkçşhp]) \^ dim$", r"\1tum"),
    (r"^(.*[aı][fstkçşhp]) \^ dim$", r"\1tım"),
    (r"^(.*[öü][fstkçşhp]) \^ dim$", r"\1tüm"),
    (r"^(.*[ei][fstkçşhp]) \^ dim$", r"\1tim"),
    (r"^(.*[ou][bcdgğjlmnqrvwxyz]) \^ dim$", r"\1dum"),
    (r"^(.*[aı][bcdgğjlmnqrvwxyz]) \^ dim$", r"\1dım"),
    (r"^(.*[öü][bcdgğjlmnqrvwxyz]) \^ dim$", r"\1düm"),
    (r"^(.*[ei][bcdgğjlmnqrvwxyz]) \^ dim$", r"\1dim"),
    (r"^(.*[ou]) \^ dim$", r"\1dum"),
    (r"^(.*[aı]) \^ dim$", r"\1dım"),
    (r"^(.*[öü]) \^ dim$", r"\1düm"),
    (r"^(.*[ei]) \^ dim$", r"\1dim"),
    (r"^(.*[se$mese$][e]) \^ dim$", r"\1ydim"),
    (r"^(.*[se$mese$][a]) \^ dim$", r"\1ydım"),

    # == +din, +dın, +dun, +dün, +tin, +tın, +tun, +tün ==
    #: uyu + dun = uyudun
    #: eri + din = eridin
    #: al + dın = aldın
    #: böl + dün = böldün
    #: geç + tin = geçtin
    #: çalış + tın = çalıştın
    #: tut + tun = tuttun
    #: öt + tün = öttün
    (r"^(.*[ou][fstkçşhp]) \^ din$", r"\1tun"),
    (r"^(.*[aı][fstkçşhp]) \^ din$", r"\1tın"),
    (r"^(.*[öü][fstkçşhp]) \^ din$", r"\1tün"),
    (r"^(.*[ei][fstkçşhp]) \^ din$", r"\1tin"),
    (r"^(.*[ou][bcdgğjlmnqrvwxyz]) \^ din$", r"\1dun"),
    (r"^(.*[aı][bcdgğjlmnqrvwxyz]) \^ din$", r"\1dın"),
    (r"^(.*[öü][bcdgğjlmnqrvwxyz]) \^ din$", r"\1dün"),
    (r"^(.*[ei][bcdgğjlmnqrvwxyz]) \^ din$", r"\1din"),
    (r"^(.*[ou]) \^ din$", r"\1dun"),
    (r"^(.*[aı]) \^ din$", r"\1dın"),
    (r"^(.*[öü]) \^ din$", r"\1dün"),
    (r"^(.*[ei]) \^ din$", r"\1din"),
    (r"^(.*[se$mese$][e]) \^ din$", r"\1ydin"),
    (r"^(.*[se$mese$][a]) \^ din$", r"\1ydın"),

    # == +di, +dı, +du, +dü, +ti, +tı, +tu, +tü ==
    #: uyu + du = uyudu
    #: eri + di = eridi
    #: al + dı = aldı
    #: böl + dü = böldü
    #: geç + ti = geçti
    #: çalış + tı = çalıştı
    #: tut + tu = tuttu
    #: öt + tü = öttü
    (r"^(.*[ou][fstkçşhp]) \^ di$", r"\1tu"),
    (r"^(.*[aı][fstkçşhp]) \^ di$", r"\1tı"),
    (r"^(.*[öü][fstkçşhp]) \^ di$", r"\1tü"),
    (r"^(.*[ei][fstkçşhp]) \^ di$", r"\1ti"),
    (r"^(.*[ou][bcdgğjlmnqrvwxyz]) \^ di$", r"\1du"),
    (r"^(.*[aı][bcdgğjlmnqrvwxyz]) \^ di$", r"\1dı"),
    (r"^(.*[öü][bcdgğjlmnqrvwxyz]) \^ di$", r"\1dü"),
    (r"^(.*[ei][bcdgğjlmnqrvwxyz]) \^ di$", r"\1di"),
    (r"^(.*[ou]) \^ di$", r"\1du"),
    (r"^(.*[aı]) \^ di$", r"\1dı"),
    (r"^(.*[öü]) \^ di$", r"\1dü"),
    (r"^(.*[se$mese$][e]) \^ di$", r"\1ydi"),
    (r"^(.*[se$mese$][a]) \^ di$", r"\1ydı"),

    # == +dik, +dık, +duk, +dük, +tik, +tık, +tuk, +tük ==
    #: uyu + duk = uyuduk
    #: eri + dik = eridik
    #: al + dık = aldık
    #: böl + dük = böldük
    #: geç + tik = geçtik
    #: çalış + tık = çalıştık
    #: tut + tuk = tuttuk
    #: öt + tük = öttük
    (r"^(.*[ou][fstkçşhp]) \^ dik$", r"\1tuk"),
    (r"^(.*[aı][fstkçşhp]) \^ dik$", r"\1tık"),
    (r"^(.*[öü][fstkçşhp]) \^ dik$", r"\1tük"),
    (r"^(.*[ei][fstkçşhp]) \^ dik$", r"\1tik"),
    (r"^(.*[ou][bcdgğjlmnqrvwxyz]) \^ dik$", r"\1duk"),
    (r"^(.*[aı][bcdgğjlmnqrvwxyz]) \^ dik$", r"\1dık"),
    (r"^(.*[öü][bcdgğjlmnqrvwxyz]) \^ dik$", r"\1dük"),
    (r"^(.*[ei][bcdgğjlmnqrvwxyz]) \^ dik$", r"\1dik"),
    (r"^(.*[ou]) \^ dik$", r"\1duk"),
    (r"^(.*[aı]) \^ dik$", r"\1dık"),
    (r"^(.*[öü]) \^ dik$", r"\1dük"),
    (r"^(.*[ei]) \^ dik$", r"\1dik"),
    (r"^(.*[se$mese$][e]) \^ dik$", r"\1ydik"),
    (r"^(.*[se$mese$][a]) \^ dik$", r"\1ydık"),


    # == +diniz, +dınız, +dunuz, +dünüz, +tiniz, +tınız, +tunuz, +tünüz ==
    #: uyu + dunuz = uyudunuz
    #: eri + diniz = eridiniz
    #: al + dınız = aldınız
    #: böl + dünüz = böldünüz
    #: geç + tiniz = geçtiniz
    #: çalış + tınız = çalıştınız
    #: tut + tunuz = tuttunuz
    #: öt + tünüz = öttünüz
    (r"^(.*[ou][fstkçşhp]) \^ diniz$", r"\1tunuz"),
    (r"^(.*[aı][fstkçşhp]) \^ diniz$", r"\1tınız"),
    (r"^(.*[öü][fstkçşhp]) \^ diniz$", r"\1tünüz"),
    (r"^(.*[ei][fstkçşhp]) \^ diniz$", r"\1tiniz"),
    (r"^(.*[ou][bcdgğjlmnqrvwxyz]) \^ diniz$", r"\1dunuz"),
    (r"^(.*[aı][bcdgğjlmnqrvwxyz]) \^ diniz$", r"\1dınız"),
    (r"^(.*[öü][bcdgğjlmnqrvwxyz]) \^ diniz$", r"\1dünüz"),
    (r"^(.*[ei][bcdgğjlmnqrvwxyz]) \^ diniz$", r"\1diniz"),
    (r"^(.*[ou]) \^ diniz$", r"\1dunuz"),
    (r"^(.*[aı]) \^ diniz$", r"\1dınız"),
    (r"^(.*[öü]) \^ diniz$", r"\1dünüz"),
    (r"^(.*[ei]) \^ diniz$", r"\1diniz"),
    (r"^(.*[se$mese$][e]) \^ diniz$", r"\1ydiniz"),
    (r"^(.*[se$mese$][a]) \^ diniz$", r"\1ydınız"),

    # == +diler, +dılar, +dular, +düler, +tiler, +tılar, +tular, +tüler ==
    #: uyu + du = uyudular
    #: eri + diler = eridiler
    #: al + dı = aldılar
    #: böl + dü = böldüler
    #: geç + tiler = geçtiler
    #: çalış + tı = çalıştılar
    #: tut + tu = tuttular
    #: öt + tüler = öttüler
    (r"^(.*[ou][fstkçşhp]) \^ diler$", r"\1tular"),
    (r"^(.*[aı][fstkçşhp]) \^ diler$", r"\1tılar"),
    (r"^(.*[öü][fstkçşhp]) \^ diler$", r"\1tüler"),
    (r"^(.*[ei][fstkçşhp]) \^ diler$", r"\1tiler"),
    (r"^(.*[ou][bcdgğjlmnqrvwxyz]) \^ diler$", r"\1dular"),
    (r"^(.*[aı][bcdgğjlmnqrvwxyz]) \^ diler$", r"\1dılar"),
    (r"^(.*[öü][bcdgğjlmnqrvwxyz]) \^ diler$", r"\1düler"),
    (r"^(.*[ei][bcdgğjlmnqrvwxyz]) \^ diler$", r"\1diler"),
    (r"^(.*[ou]) \^ diler$", r"\1dular"),
    (r"^(.*[aı]) \^ diler$", r"\1dılar"),
    (r"^(.*[öü]) \^ diler$", r"\1düler"),
    (r"^(.*[ei]) \^ diler$", r"\1diler"),
    (r"^(.*[se$][e]) \^ diler$", r"\1ydiler"),
    (r"^(.*[se$][a]) \^ diler$", r"\1ydılar"),
    (r"^(.*[mese$][e]) \^ diler$", r"\1ydiler"),
    (r"^(.*[mese$][a]) \^ diler$", r"\1ydılar"),

    # == +mayacağım, +meyeceğim ==
    #: uyu + mayacağım = uyuymayacağım
    #: eri + meyeceğim = erimeyeceğim
    (r"^(.*[eiöü]) \^ (meyeceğim)$", r"\1meyeceğim"),
    (r"^(.*[aıou]) \^ (meyeceğim)$", r"\1mayacağım"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (meyeceğim)$", r"\1meyeceğim"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (meyeceğim)$", r"\1mayacağım"),

    # == +mayacaksın, +meyeceksin ==
    #: uyu + mayacaksın = uyuymayacaksın
    #: eri + meyeceksin = erimeyeceksin
    (r"^(.*[eiöü]) \^ (meyeceksin)$", r"\1meyeceksin"),
    (r"^(.*[aıou]) \^ (meyeceksin)$", r"\1mayacaksın"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (meyeceksin)$", r"\1meyeceksin"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (meyeceksin)$", r"\1mayacaksın"),

    # == +mayacak, +meyecek ==
    #: uyu + mayacak = uyuymayacak
    #: eri + meyecek = erimeyecek
    (r"^(.*[eiöü]) \^ (meyecek)$", r"\1meyecek"),
    (r"^(.*[aıou]) \^ (meyecek)$", r"\1mayacak"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (meyecek)$", r"\1meyecek"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (meyecek)$", r"\1mayacak"),

    # == +mayacaklar, +meyecekler ==
    #: uyu + mayacaklar = uyuymayacaklar
    #: eri + meyecekler = erimeyecekler
    (r"^(.*[eiöü]) \^ (meyecekler)$", r"\1meyecekler"),
    (r"^(.*[aıou]) \^ (meyecekler)$", r"\1mayacaklar"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (meyecekler)$", r"\1meyecekler"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (meyecekler)$", r"\1mayacaklar"),

    # == +mayacağız, +meyeceğiz ==
    #: uyu + mayacağız = uyuymayacağız
    #: eri + meyeceğiz = erimeyeceğiz
    (r"^(.*[eiöü]) \^ (meyeceğiz)$", r"\1meyeceğiz"),
    (r"^(.*[aıou]) \^ (meyeceğiz)$", r"\1mayacağız"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (meyeceğiz)$", r"\1meyeceğiz"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (meyeceğiz)$", r"\1mayacağız"),

    # == +mayacaksınız, +meyeceksin ==
    #: uyu + mayacaksınız = uyuymayacaksınız
    #: eri + meyeceksiniz = erimeyeceksiniz
    (r"^(.*[eiöü]) \^ (meyeceksiniz)$", r"\1meyeceksin"),
    (r"^(.*[aıou]) \^ (meyeceksiniz)$", r"\1mayacaksınız"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (meyeceksiniz)$", r"\1meyeceksiniz"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (meyeceksiniz)$", r"\1mayacaksınız"),

    # == +medim, +madım ==
    #: uyu + madım = uyumadım
    #: eri + medim = erimedim
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ medim$", r"\1madım"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ medim$", r"\1medim"),
    (r"^(.*[aıou]) \^ medim$", r"\1madım"),
    (r"^(.*[eiöü]) \^ medim$", r"\1medim"),

    # == +medin, +madın ==
    #: uyu + madın = uyumadın
    #: eri + medin = erimedin
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ medin$", r"\1madın"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ medin$", r"\1medin"),
    (r"^(.*[aıou]) \^ medin$", r"\1madın"),
    (r"^(.*[eiöü]) \^ medin$", r"\1medin"),

    # == +medi, +madı ==
    #: uyu + madı = uyumadı
    #: eri + medi = erimedi
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ medi$", r"\1madı"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ medi$", r"\1medi"),
    (r"^(.*[aıou]) \^ medi$", r"\1madı"),
    (r"^(.*[eiöü]) \^ medi$", r"\1medi"),

    # == +medik, +madık ==
    #: uyu + madık = uyumadık
    #: eri + medik = erimedik
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ medik$", r"\1madık"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ medik$", r"\1medik"),
    (r"^(.*[aıou]) \^ medik$", r"\1madık"),
    (r"^(.*[eiöü]) \^ medik$", r"\1medik"),

    # == +mediniz, +madınız ==
    #: uyu + madınız = uyumadınız
    #: eri + mediniz = erimediniz
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ mediniz$", r"\1madınız"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ mediniz$", r"\1mediniz"),
    (r"^(.*[aıou]) \^ mediniz$", r"\1madınız"),
    (r"^(.*[eiöü]) \^ mediniz$", r"\1mediniz"),

    # == +mediler, +madılar ==
    #: uyu + madılar = uyumadılar
    #: eri + mediler = erimediler
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ mediler$", r"\1madılar"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ mediler$", r"\1mediler"),
    (r"^(.*[aıou]) \^ mediler$", r"\1madılar"),
    (r"^(.*[eiöü]) \^ mediler$", r"\1mediler"),

    # == di+se ==
    (r"^(.*[di$medi$][iü]) \^ se$", r"\1yse"),
    (r"^(.*[di$medi$][ıu]) \^ se$", r"\1ysa"),

    # == +mişim, +mışım, +muşum, +müşüm ==
    #: uyu + muşum = uyumuşum
    #: eri + mişim = erimişim
    #: al + mışım = almışım
    #: böl + müşüm = bölmüşüm
    (r"^(.*[ei]) \^ (mişim)$", r"\1mişim"),
    (r"^(.*[öü]) \^ (mişim)$", r"\1müşüm"),
    (r"^(.*[aı]) \^ (mişim)$", r"\1mışım"),
    (r"^(.*[ou]) \^ (mişim)$", r"\1muşum"),
    (r"^(.*[ei][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mişim)$", r"\1mişim"),
    (r"^(.*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mişim)$", r"\1müşüm"),
    (r"^(.*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mişim)$", r"\1mışım"),
    (r"^(.*[ou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mişim)$", r"\1muşum"),

    # == +mişsin, +mışsın, +muşsun, +müşsün ==
    #: uyu + muşsun = uyumuşsun
    #: eri + mişsin = erimişsin
    #: al + mışsın = almışsın
    #: böl + müşsün = bölmüşsün
    (r"^(.*[ei]) \^ (mişsin)$", r"\1mişsin"),
    (r"^(.*[öü]) \^ (mişsin)$", r"\1müşsün"),
    (r"^(.*[aı]) \^ (mişsin)$", r"\1mışsın"),
    (r"^(.*[ou]) \^ (mişsin)$", r"\1muşsun"),
    (r"^(.*[ei][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mişsin)$", r"\1mişsin"),
    (r"^(.*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mişsin)$", r"\1müşsün"),
    (r"^(.*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mişsin)$", r"\1mışsın"),
    (r"^(.*[ou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mişsin)$", r"\1muşsun"),
    
    # == +miş, +mış, +muş, +müş ==
    #: uyu + muş = uyumuş
    #: eri + miş = erimiş
    #: al + mış = almış
    #: böl + müş = bölmüş
    (r"^(.*[ei]) \^ (miş)$", r"\1miş"),
    (r"^(.*[öü]) \^ (miş)$", r"\1müş"),
    (r"^(.*[aı]) \^ (miş)$", r"\1mış"),
    (r"^(.*[ou]) \^ (miş)$", r"\1muş"),
    (r"^(.*[ei][bcçdfgğhjklmnpqrsştvwxyz]) \^ (miş)$", r"\1miş"),
    (r"^(.*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (miş)$", r"\1müş"),
    (r"^(.*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ (miş)$", r"\1mış"),
    (r"^(.*[ou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (miş)$", r"\1muş"),

    # == +mişiz, +mışız, +muşuz, +müşüz ==
    #: uyu + muşuz = uyumuşuz
    #: eri + mişiz = erimişiz
    #: al + mışız = almışız
    #: böl + müşüz = bölmüşüz
    (r"^(.*[ei]) \^ (mişiz)$", r"\1mişiz"),
    (r"^(.*[öü]) \^ (mişiz)$", r"\1müşüz"),
    (r"^(.*[aı]) \^ (mişiz)$", r"\1mışız"),
    (r"^(.*[ou]) \^ (mişiz)$", r"\1muşuz"),
    (r"^(.*[ei][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mişiz)$", r"\1mişiz"),
    (r"^(.*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mişiz)$", r"\1müşüz"),
    (r"^(.*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mişiz)$", r"\1mışız"),
    (r"^(.*[ou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mişiz)$", r"\1muşuz"),

    # == +mişsiniz, +mışsınız, +muşsunuz, +müşsünüz ==
    #: uyu + muşsunuz = uyumuşsunuz
    #: eri + mişsiniz = erimişsiniz
    #: al + mışsınız = almışsınız
    #: böl + müşsünüz = bölmüşsünüz
    (r"^(.*[ei]) \^ (mişsiniz)$", r"\1mişsiniz"),
    (r"^(.*[öü]) \^ (mişsiniz)$", r"\1müşsünüz"),
    (r"^(.*[aı]) \^ (mişsiniz)$", r"\1mışsınız"),
    (r"^(.*[ou]) \^ (mişsiniz)$", r"\1muşsunuz"),
    (r"^(.*[ei][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mişsiniz)$", r"\1mişsiniz"),
    (r"^(.*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mişsiniz)$", r"\1müşsünüz"),
    (r"^(.*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mişsiniz)$", r"\1mışsınız"),
    (r"^(.*[ou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mişsiniz)$", r"\1muşsunuz"),

    # == +mişler, +mışlar, +muşlar, +müşler ==
    #: uyu + muşlar = uyumuşlar
    #: eri + mişler = erimişler
    #: al + mışlar = almışlar
    #: böl + müşler = bölmüşler
    (r"^(.*[ei]) \^ (mişler)$", r"\1mişler"),
    (r"^(.*[öü]) \^ (mişler)$", r"\1müşler"),
    (r"^(.*[aı]) \^ (mişler)$", r"\1mışlar"),
    (r"^(.*[ou]) \^ (mişler)$", r"\1muşlar"),
    (r"^(.*[ei][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mişler)$", r"\1mişler"),
    (r"^(.*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mişler)$", r"\1müşler"),
    (r"^(.*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mişler)$", r"\1mışlar"),
    (r"^(.*[ou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mişler)$", r"\1muşlar"),

    # == +memişim, +mamışım ==
    #: uyu + mamışım = uyumamışım
    #: eri + memişim = erimemişim
    (r"^(.*[eiöü]) \^ (memişim)$", r"\1memişim"),
    (r"^(.*[aıou]) \^ (memişim)$", r"\1mamışım"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (memişim)$", r"\1memişim"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (memişim)$", r"\1mamışım"),

    # == +memişsin, +mamışsın ==
    #: uyu + mamışsın = uyumamışsın
    #: eri + memişsin = erimemişsin
    (r"^(.*[eiöü]) \^ (memişsin)$", r"\1memişsin"),
    (r"^(.*[aıou]) \^ (memişsin)$", r"\1mamışsın"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (memişsin)$", r"\1memişsin"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (memişsin)$", r"\1mamışsın"),

    # == +memiş, +mamış ==
    #: uyu + mamış = uyumamış
    #: eri + memiş = erimemiş
    (r"^(.*[eiöü]) \^ (memiş)$", r"\1memiş"),
    (r"^(.*[aıou]) \^ (memiş)$", r"\1mamış"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (memiş)$", r"\1memiş"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (memiş)$", r"\1mamış"),

    # == +memişiz, +mamışız ==
    #: uyu + mamışız = uyumamışız
    #: eri + memişiz = erimemişiz
    (r"^(.*[eiöü]) \^ (memişiz)$", r"\1memişiz"),
    (r"^(.*[aıou]) \^ (memişiz)$", r"\1mamışız"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (memişiz)$", r"\1memişiz"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (memişiz)$", r"\1mamışız"),

    # == +memişsiniz, +mamışsınız ==
    #: uyu + mamışsınız = uyumamışsınız
    #: eri + memişsiniz = erimemişsiniz
    (r"^(.*[eiöü]) \^ (memişsiniz)$", r"\1memişsiniz"),
    (r"^(.*[aıou]) \^ (memişsiniz)$", r"\1mamışsınız"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (memişsiniz)$", r"\1memişsiniz"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (memişsiniz)$", r"\1mamışsınız"),

    # == +memişler, +mamışlar ==
    #: uyu + mamışlar = uyumamışlar
    #: eri + memişler = erimemişler
    (r"^(.*[eiöü]) \^ (memişler)$", r"\1memişler"),
    (r"^(.*[aıou]) \^ (memişler)$", r"\1mamışlar"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (memişler)$", r"\1memişler"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (memişler)$", r"\1mamışlar"),
    
    # == +sin, +sın, +sun, +sün ==
    #: uyu + sun = uyusun
    #: eri + sin = erisin
    #: al + sın = alsın
    #: böl + sün = bölsün
    (r"^(.*[ei]) \^ (sin)$", r"\1sin"),
    (r"^(.*[öü]) \^ (sin)$", r"\1sün"),
    (r"^(.*[aı]) \^ (sin)$", r"\1sın"),
    (r"^(.*[ou]) \^ (sin)$", r"\1sun"),
    (r"^(.*[ei][bcçdfgğhjklmnpqrsştvwxyz]) \^ (sin)$", r"\1sin"),
    (r"^(.*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (sin)$", r"\1sün"),
    (r"^(.*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ (sin)$", r"\1sın"),
    (r"^(.*[ou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (sin)$", r"\1sun"),

    # == +in, +ın, +un, +ün, +yin, +yın, +yun, +yün ==
    #: uyu + yun = uyuyun
    #: eri + yin = eriyin
    #: anla + yın = anlayın
    #: yürü + yün = yürüyün
    #: geç + in = geçin
    #: al + ın = alın
    #: kon + un = konun
    #: böl + ün = bölün
    (r"^(.*[ei]) \^ (yin)$", r"\1yin"),
    (r"^(.*[öü]) \^ (yin)$", r"\1yün"),
    (r"^(.*[aı]) \^ (yin)$", r"\1yın"),
    (r"^(.*[ou]) \^ (yin)$", r"\1yun"),
    (r"^(.*[ei][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yin)$", r"\1in"),
    (r"^(.*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yin)$", r"\1ün"),
    (r"^(.*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yin)$", r"\1ın"),
    (r"^(.*[ou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (yin)$", r"\1un"),

    # == +sinler, +sınlar, +sunlar, +sünler ==
    #: uyu + sunlar = uyusun
    #: eri + sinler = erisinler
    #: al + sınlar = alsınlar
    #: böl + sünler = bölsünler
    (r"^(.*[ei]) \^ (sinler)$", r"\1sinler"),
    (r"^(.*[öü]) \^ (sinler)$", r"\1sünler"),
    (r"^(.*[aı]) \^ (sinler)$", r"\1sınlar"),
    (r"^(.*[ou]) \^ (sinler)$", r"\1sunlar"),
    (r"^(.*[ei][bcçdfgğhjklmnpqrsştvwxyz]) \^ (sinler)$", r"\1sinler"),
    (r"^(.*[öü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (sinler)$", r"\1sünler"),
    (r"^(.*[aı][bcçdfgğhjklmnpqrsştvwxyz]) \^ (sinler)$", r"\1sınlar"),
    (r"^(.*[ou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (sinler)$", r"\1sunlar"),

    # == +malıyım, +meliyim ==
    #: uyu + malıyım = uyumalıyım
    #: eri + meliyim = erimeliyim
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ meliyim$", r"\1malıyım"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ meliyim$", r"\1meliyim"),
    (r"^(.*[aıou]) \^ meliyim$", r"\1malıyım"),
    (r"^(.*[eiöü]) \^ meliyim$", r"\1meliyim"),

    # == +malısın, +melisin ==
    #: uyu + malısın = uyumalısın
    #: eri + melisin = erimelisin
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ melisin$", r"\1malısın"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ melisin$", r"\1melisin"),
    (r"^(.*[aıou]) \^ melisin$", r"\1malısın"),
    (r"^(.*[eiöü]) \^ melisin$", r"\1melisin"),

    # == +malı, +meli ==
    #: uyu + malı = uyumalı
    #: eri + meli = erimeli
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ meli$", r"\1malı"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ meli$", r"\1meli"),
    (r"^(.*[aıou]) \^ meli$", r"\1malı"),
    (r"^(.*[eiöü]) \^ meli$", r"\1meli"),

    # == +malıyız, +meliyiz ==
    #: uyu + malıyız = uyumalıyız
    #: eri + meliyiz = erimeliyiz
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ meliyiz$", r"\1malıyız"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ meliyiz$", r"\1meliyiz"),
    (r"^(.*[aıou]) \^ meliyiz$", r"\1malıyız"),
    (r"^(.*[eiöü]) \^ meliyiz$", r"\1meliyiz"),

    # == +malısın, +melisin ==
    #: uyu + malısın = uyumalısın
    #: eri + melisin = erimelisin
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ melisin$", r"\1malısın"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ melisin$", r"\1melisin"),
    (r"^(.*[aıou]) \^ melisin$", r"\1malısın"),
    (r"^(.*[eiöü]) \^ melisin$", r"\1melisin"),

    # == +malılar, +meliler ==
    #: uyu + malılar = uyumalılar
    #: eri + meliler = erimeliler
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ meliler$", r"\1malılar"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ meliler$", r"\1meliler"),
    (r"^(.*[aıou]) \^ meliler$", r"\1malılar"),
    (r"^(.*[eiöü]) \^ meliler$", r"\1meliler"),

    # == +me, +ma ==
    #: uyu + may = uyuma
    #: eri + me = erime
    (r"^(.*[eiöü]) \^ (me)$", r"\1me"),
    (r"^(.*[aıou]) \^ (me)$", r"\1ma"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (me)$", r"\1me"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (me)$", r"\1ma"),

    # == +mesin, +masın ==
    #: uyu + masın = uyumasın
    #: eri + mesin = erimesin
    (r"^(.*[eiöü]) \^ (mesin)$", r"\1mesin"),
    (r"^(.*[aıou]) \^ (mesin)$", r"\1masın"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mesin)$", r"\1mesin"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mesin)$", r"\1masın"),

    # == +meyin, +mayın ==
    #: uyu + mayın = uyumayn
    #: eri + meyin = erimeyin
    (r"^(.*[eiöü]) \^ (meyin)$", r"\1meyin"),
    (r"^(.*[aıou]) \^ (meyin)$", r"\1mayın"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (meyin)$", r"\1meyin"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (meyin)$", r"\1mayın"),

    # == +mesinler, +masınlar ==
    #: uyu + masınlar = uyumasınlar
    #: eri + mesinler = erimesinler
    (r"^(.*[eiöü]) \^ (mesinler)$", r"\1mesinler"),
    (r"^(.*[aıou]) \^ (mesinler)$", r"\1masınlar"),
    (r"^(.*[eiöü][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mesinler)$", r"\1mesinler"),
    (r"^(.*[aıou][bcçdfgğhjklmnpqrsştvwxyz]) \^ (mesinler)$", r"\1masınlar"),

]

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = 'italian_words.txt'

KEYMAPS = {
    'Keyboard': {
        '1-': '1',
        '2-': '2',
        '3-': '3',
        '4-': '4',
        '5-': '5',
        '6-': '6',
        '7-': '7',
        '8-': '8',
        '9-': '9',
        '0-': '0',
        'S-': 'q',
        'S-': 'a',
        'T-': 'w',
        'R-': 's',
        'B-': 'e',
        'L-': 'd',
        'K-': 'r',
        'M-': 'f',
        '~': 't',
        '*': 'g',
        'A-': 'c',
        'İ-': 'v',
        '-E': 'b',
        '-I': 'n',
        '-P': 'y',
        '-L': 'h',
        '-R': 'u',
        '-K': 'j',
        '-T': 'i',
        '-S': 'k',
        '-N': 'o',
        '-M': 'l',
        '-Ş': 'p',
        '-Ç': ';',
        'arpeggiate': 'space'
    },
    },


DICTIONARIES_ROOT = 'asset:plover_trl:assets'

DEFAULT_DICTIONARIES = (
    'allwords.txt',
)
