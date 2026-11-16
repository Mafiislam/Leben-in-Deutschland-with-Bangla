"""Generates translations/bn/states.json (Bangla for the 160 state questions).

The state questions follow fixed templates, so wording is built from reviewed
Bangla templates and glossaries. Anything that is not covered raises an error
instead of being guessed. Place names get the German spelling in brackets.
Run from the repo root: python3 -I scripts/gen_states_bn.py"""
import json, re

base = json.load(open('data/base.json', encoding='utf-8'))
Q = {q['id']: q for q in base['questions']}
SLUGS = [s['slug'] for s in base['states']]

NAME = {  # full name (used in menus)
 'baden-wuerttemberg': 'বাডেন-ভ্যুর্টেমবের্গ', 'bayern': 'বাইয়ার্ন (ব্যাভারিয়া)', 'berlin': 'বার্লিন',
 'brandenburg': 'ব্র্যান্ডেনবুর্গ', 'bremen': 'ব্রেমেন', 'hamburg': 'হামবুর্গ', 'hessen': 'হেসেন',
 'mecklenburg-vorpommern': 'মেকলেনবুর্গ-ফরপোমার্ন', 'niedersachsen': 'নিডারজাকসেন (লোয়ার স্যাক্সনি)',
 'nordrhein-westfalen': 'নর্থ রাইন-ভেস্টফালেন', 'rheinland-pfalz': 'রাইনল্যান্ড-প্ফালৎস', 'saarland': 'ঝারল্যান্ড',
 'sachsen': 'জাকসেন (স্যাক্সনি)', 'sachsen-anhalt': 'জাকসেন-আনহাল্ট', 'schleswig-holstein': 'শ্লেসভিগ-হলস্টাইন',
 'thueringen': 'থুরিঙ্গেন',
}
SHORT = {k: re.sub(r'\s*\(.*\)', '', v) for k, v in NAME.items()}
DIGITS = '০১২৩৪৫৬৭৮৯'
def bd(s): return re.sub(r'\d', lambda m: DIGITS[int(m.group())], str(s))

PLACE = {  # districts, cities and states appearing as options
 'Mecklenburg Lake District': 'মেকলেনবুর্গ হ্রদ এলাকা', 'Neckar-Odenwald-Kreis': 'নেকার-ওডেনভাল্ট-ক্রাইস',
 'North Frisia': 'উত্তর ফ্রিজিয়া', 'Altötting': 'আলটোটিং', 'Prignitz': 'প্রিগনিৎস',
 'Rhein-Sieg-Kreis': 'রাইন-জীগ-ক্রাইস', 'Altona': 'আলটোনা', 'Pankow': 'পানকাউ', 'Vogtlandkreis': 'ফোগটল্যান্ডক্রাইস',
 'Amberg-Sulzbach': 'আমবের্গ-জুলৎসবাখ', 'Hemelingen': 'হেমেলিঙ্গেন', 'Ammerland': 'আমারল্যান্ড',
 'Main-Taunus-Kreis': 'মাইন-টাউনুস-ক্রাইস', 'Westerwaldkreis': 'ভেস্টারভাল্টক্রাইস', 'Emsland': 'এমসল্যান্ড',
 'Neunkirchen': 'নয়নকির্শেন', 'Uckermark': 'উকারমার্ক', 'Börde': 'বোর্দে', 'Wartburgkreis': 'ভার্টবুর্গক্রাইস',
 'Heidelberg': 'হাইডেলবের্গ', 'Stuttgart': 'স্টুটগার্ট', 'Karlsruhe': 'কার্লসরুয়ে', 'Mannheim': 'ম্যানহাইম',
 'Ingolstadt': 'ইনগোলস্টাট', 'Regensburg': 'রেগেনসবুর্গ', 'Nuremberg': 'নুরেমবার্গ', 'Munich': 'মিউনিখ',
 'Potsdam': 'পটসডাম', 'Cottbus': 'কটবুস', 'Brandenburg (city)': 'ব্র্যান্ডেনবুর্গ (শহর)', 'Frankfurt (Oder)': 'ফ্রাঙ্কফুর্ট (ওডার)',
 'Kassel': 'কাসেল', 'Darmstadt': 'ডার্মস্টাট', 'Frankfurt': 'ফ্রাঙ্কফুর্ট', 'Wiesbaden': 'ভিসবাডেন',
 'Greifswald': 'গ্রাইফসভাল্ট', 'Schwerin': 'শভেরিন', 'Rostock': 'রস্টক', 'Wismar': 'ভিসমার',
 'Hanover': 'হানোভার', 'Brunswick': 'ব্রাউনশভাইগ', 'Wolfsburg': 'ভলফসবুর্গ', 'Osnabrück': 'ওসনাব্রুক',
 'Cologne': 'কলোন', 'Bonn': 'বন', 'Düsseldorf': 'ডুসেলডর্ফ', 'Dortmund': 'ডর্টমুন্ড',
 'Mainz': 'মাইনৎস', 'Kaiserslautern': 'কাইজারসলাউটার্ন', 'Ludwigshafen': 'লুডভিগসহাফেন', 'Koblenz': 'কোবলেনৎস',
 'Homburg': 'হমবুর্গ', 'Saarbrücken': 'ঝারব্রুকেন', 'Völklingen': 'ফোলকলিঙ্গেন',
 'Leipzig': 'লাইপজিগ', 'Chemnitz': 'কেমনিৎস', 'Dresden': 'ড্রেসডেন', 'Görlitz': 'গোর্লিৎস',
 'Halle': 'হালে', 'Dessau': 'ডেসাউ', 'Magdeburg': 'মাগদেবুর্গ', 'Wittenberg': 'ভিটেনবের্গ',
 'Husum': 'হুজুম', 'Flensburg': 'ফ্লেন্সবুর্গ', 'Lübeck': 'লুবেক', 'Kiel': 'কিল',
 'Eisenach': 'আইজেনাখ', 'Erfurt': 'এরফুর্ট', 'Gera': 'গেরা', 'Jena': 'ইয়েনা',
 'Berlin': 'বার্লিন', 'Bremen': 'ব্রেমেন', 'Hamburg': 'হামবুর্গ', 'Saarland': 'ঝারল্যান্ড', 'Brandenburg': 'ব্র্যান্ডেনবুর্গ',
 'Hesse': 'হেসেন', 'Bavaria': 'বাইয়ার্ন', 'Saxony': 'জাকসেন', 'Thuringia': 'থুরিঙ্গেন',
}
COLOR = {'blue': 'নীল', 'white': 'সাদা', 'red': 'লাল', 'green': 'সবুজ', 'black': 'কালো', 'gold': 'সোনালি', 'yellow': 'হলুদ'}
def colors(s): return '-'.join(COLOR[c] for c in s.split('-'))

OPT = {
 'at the municipal public order office': 'পৌর জনশৃঙ্খলা দপ্তরে (Ordnungsamt)',
 'at the Consumer Advice Centre': 'ভোক্তা পরামর্শ কেন্দ্রে (Verbraucherzentrale)',
 'at the State Agency for Civic Education': 'রাজ্য রাজনৈতিক শিক্ষা কেন্দ্রে (Landeszentrale für politische Bildung)',
 'at the State Commissioner for Civic Education': 'রাজ্য রাজনৈতিক শিক্ষা কমিশনারের কাছে (Landesbeauftragter für politische Bildung)',
 'at the churches': 'গির্জাগুলোতে',
 'First Minister': 'প্রথম মন্ত্রী (Erster Minister)', 'Prime Minister': 'প্রধানমন্ত্রী (Premierminister)', 'Mayor': 'মেয়র (Bürgermeister)',
 'Minister-President': 'মন্ত্রী-প্রেসিডেন্ট (Ministerpräsident)', 'Lord Mayor': 'লর্ড মেয়র (Oberbürgermeister)',
 'President of the Senate': 'সিনেটের প্রেসিডেন্ট (Präsident des Senats)', 'Governing Mayor': 'শাসক মেয়র (Regierender Bürgermeister)',
 'First Mayor': 'প্রথম মেয়র (Erster Bürgermeister)', 'Governing Senator': 'শাসক সেনেটর (Regierender Senator)',
 'Minister of Finance': 'অর্থমন্ত্রী (Finanzminister)', 'Minister of Justice': 'বিচারমন্ত্রী (Justizminister)',
 'Minister of the Interior': 'স্বরাষ্ট্রমন্ত্রী (Innenminister)', 'Minister of Foreign Affairs': 'পররাষ্ট্রমন্ত্রী (Außenminister)',
 'Finance Senator': 'অর্থ সেনেটর (Finanzsenator)', 'Interior Senator': 'স্বরাষ্ট্র সেনেটর (Innensenator)',
 'Senator for External Affairs': 'পররাষ্ট্র বিষয়ক সেনেটর (Senator für Außenangelegenheiten)', 'Justice Senator': 'বিচার সেনেটর (Justizsenator)',
}

def place_opt(o):
    en = o['en'].rstrip('.')
    if en not in PLACE: raise KeyError('place: ' + en)
    de = o['de'].rstrip('.')
    bn = PLACE[en]
    return f'{bn} ({de})' if de.lower() != bn.lower() else bn

def opt_generic(o):
    en = o['en']
    if re.fullmatch(r'\d+', en): return bd(en)
    if en in OPT: return OPT[en]
    if re.fullmatch(r'[a-z]+(-[a-z]+)+', en): return colors(en)
    raise KeyError('option: ' + en)

COAT = {  # question 301 explanations
 'baden-wuerttemberg': 'বাডেন-ভ্যুর্টেমবের্গের প্রতীকে সোনালি ঢালের ওপর তিনটি কালো সিংহ আছে। এই প্রতীক মধ্যযুগের স্টাউফার রাজবংশ থেকে এসেছে, যারা একসময় এই অঞ্চল শাসন করত।',
 'bayern': 'বাইয়ার্নের প্রতীক সবচেয়ে বেশি পরিচিত সাদা-নীল রম্বস নকশার (Rautenwappen) জন্য, যা ঐতিহাসিক ভিটেলসবাখ রাজবংশের প্রতিনিধিত্ব করে।',
 'berlin': 'বার্লিনের প্রতীকে সাদা/রুপালি ঢালের ওপর একটি কালো ভালুক আছে। এটি দীর্ঘদিন ধরে শহরের সাথে যুক্ত একটি প্রতীক।',
 'brandenburg': 'ব্র্যান্ডেনবুর্গের প্রতীকে সাদা/রুপালি ঢালের ওপর একটি লাল ঈগল আছে, যা ঐতিহাসিক ব্র্যান্ডেনবুর্গ মার্কগ্রাফশাফটের (Markgrafschaft) প্রতীক।',
 'bremen': 'ব্রেমেনের প্রতীকে “ব্রেমেন চাবি” আছে, অর্থাৎ লাল ঢালের ওপর একটি রুপালি চাবি। এটি শহরের ঐতিহাসিক স্বাধীন হানসা বাণিজ্যবন্দর হিসেবে ভূমিকার প্রতীক।',
 'hamburg': 'হামবুর্গের প্রতীকে লাল ঢালের ওপর মিনারসহ একটি সাদা দুর্গদ্বার আছে। এটি শহরের ঐতিহাসিক সুরক্ষিত হানসা বাণিজ্যকেন্দ্র হওয়ার প্রতীক।',
 'hessen': 'সঠিক প্রতীকে হেসেনের ঐতিহ্যবাহী লাল-সাদা ডোরাকাটা সিংহ (“Hessischer Löwe”) আছে, যা মধ্যযুগ থেকে রাজ্যের প্রতীক হিসেবে ব্যবহৃত হচ্ছে। হেসেনেই আছে ফ্রাঙ্কফুর্ট আম মাইন, জার্মানির আর্থিক রাজধানী ও ইউরোপীয় কেন্দ্রীয় ব্যাংকের (EZB) কেন্দ্র। তবে রাজ্যের রাজধানী ভিসবাডেন।',
 'mecklenburg-vorpommern': 'মেকলেনবুর্গ-ফরপোমার্নের প্রতীকে মুকুটধারী একটি ষাঁড়ের মাথা আছে, যা ঐতিহাসিক মেকলেনবুর্গ ডাচির প্রতীক থেকে নেওয়া।',
 'niedersachsen': 'নিডারজাকসেনের প্রতীকে লাল ঢালের ওপর পিছনের পায়ে ওঠা একটি সাদা (রুপালি) ঘোড়া আছে। এটি “জাকসেন ঘোড়া” (Sachsenross), ঐতিহাসিক জাকসেন অঞ্চলের একটি সুপরিচিত প্রতীক।',
 'nordrhein-westfalen': 'নর্থ রাইন-ভেস্টফালেনের প্রতীক এর ঐতিহাসিক অঞ্চলগুলোর, অর্থাৎ রাইনল্যান্ড, ভেস্টফালেন ও লিপ্পের (Lippe) প্রতিনিধিত্বকারী উপাদান মিলিয়ে তৈরি।',
 'rheinland-pfalz': 'রাইনল্যান্ড-প্ফালৎসের প্রতীকে একটি ক্রুশ, একটি চাকা ও একটি সিংহ মিলেছে। এগুলো রাজ্য গঠনে যুক্ত হওয়া ঐতিহাসিক ভূখণ্ড ট্রিয়ার, মাইনৎস ও প্ফালৎসের প্রতিনিধিত্ব করে।',
 'saarland': 'ঝারল্যান্ডের প্রতীকে রাজ্য গঠনে যুক্ত হওয়া ঐতিহাসিক ভূখণ্ডগুলোর প্রতীক মেলানো হয়েছে। এটি ফ্রান্স ও জার্মানির মাঝের জটিল আঞ্চলিক ইতিহাস প্রতিফলিত করে।',
 'sachsen': 'জাকসেনের প্রতীকে কালো-সোনালি ডোরাকাটা ঢাল (Rautenkranz) আছে, যা ঐতিহাসিক ভেটিন রাজবংশ থেকে এসেছে।',
 'sachsen-anhalt': 'জাকসেন-আনহাল্টের প্রতীকে একটি কালো ভালুক ও অন্যান্য ঐতিহাসিক আঞ্চলিক প্রতীক মিলেছে। এগুলো ১৯৪৫ সালের পর রাজ্য গঠনে একত্র হওয়া ভূখণ্ডগুলোকে প্রতিফলিত করে।',
 'schleswig-holstein': 'শ্লেসভিগ-হলস্টাইনের প্রতীকে একটি নেটল পাতা (Nesselblatt) ও দুটি নীল সিংহ আছে। এগুলো শ্লেসভিগ ও হলস্টাইনের ঐতিহাসিক ডাচির প্রতীক।',
 'thueringen': 'থুরিঙ্গেনের প্রতীকে লাল-সাদা ডোরাকাটা সিংহ আছে, যা লুডোভিংগার সিংহ (Ludowinger Löwe) নামে পরিচিত। এটি মধ্যযুগের থুরিঙ্গেনের ল্যান্ডগ্রাফদের (Landgrafen) সময় থেকে এসেছে।',
}
MAP = {  # question 308 explanations
 'baden-wuerttemberg': 'বাডেন-ভ্যুর্টেমবের্গ জার্মানির দক্ষিণ-পশ্চিমে অবস্থিত। এর সীমান্তে আছে ফ্রান্স ও সুইজারল্যান্ড, এবং বাইয়ার্ন, হেসেন ও রাইনল্যান্ড-প্ফালৎস।',
 'bayern': 'বাইয়ার্ন আয়তনে জার্মানির বৃহত্তম রাজ্য, যা দক্ষিণ-পূর্বে অবস্থিত। এর সীমান্তে আছে অস্ট্রিয়া ও চেক প্রজাতন্ত্র এবং জার্মানির আরও কয়েকটি রাজ্য।',
 'berlin': 'বার্লিন একটি নগর-রাজ্য, যা উত্তর-পূর্ব জার্মানিতে ব্র্যান্ডেনবুর্গ রাজ্য দ্বারা সম্পূর্ণ ঘেরা।',
 'brandenburg': 'ব্র্যান্ডেনবুর্গ নগর-রাজ্য বার্লিনকে ঘিরে উত্তর-পূর্ব জার্মানিতে অবস্থিত এবং এর সীমান্তে পোল্যান্ড আছে।',
 'bremen': 'ব্রেমেন একটি ছোট নগর-রাজ্য। এটি উত্তর-পশ্চিম জার্মানিতে নিডারজাকসেন দ্বারা সম্পূর্ণ ঘেরা দুটি আলাদা অংশ নিয়ে গঠিত।',
 'hamburg': 'হামবুর্গ উত্তর জার্মানির একটি নগর-রাজ্য, যা শ্লেসভিগ-হলস্টাইন ও নিডারজাকসেন রাজ্য দ্বারা ঘেরা।',
 'hessen': 'হেসেন জার্মানির মধ্য-পশ্চিমে অবস্থিত। এর সীমান্তে আছে নর্থ রাইন-ভেস্টফালেন, রাইনল্যান্ড-প্ফালৎস, বাইয়ার্ন, থুরিঙ্গেন, নিডারজাকসেন ও বাডেন-ভ্যুর্টেমবের্গ।',
 'mecklenburg-vorpommern': 'মেকলেনবুর্গ-ফরপোমার্ন উত্তর-পূর্ব জার্মানিতে বাল্টিক সাগরের উপকূলে অবস্থিত এবং এর সীমান্তে পোল্যান্ড আছে।',
 'niedersachsen': 'নিডারজাকসেন উত্তর-পশ্চিম জার্মানিতে অবস্থিত। এর সীমান্তে আছে নেদারল্যান্ডস এবং জার্মানির আরও কয়েকটি রাজ্য।',
 'nordrhein-westfalen': 'নর্থ রাইন-ভেস্টফালেন জার্মানির সবচেয়ে জনবহুল রাজ্য, যা পশ্চিমে অবস্থিত। এর সীমান্তে আছে নেদারল্যান্ডস ও বেলজিয়াম।',
 'rheinland-pfalz': 'রাইনল্যান্ড-প্ফালৎস দক্ষিণ-পশ্চিম জার্মানিতে অবস্থিত। এর সীমান্তে আছে ফ্রান্স, লুক্সেমবুর্গ ও বেলজিয়াম।',
 'saarland': 'ঝারল্যান্ড (নগর-রাজ্য বাদে) আয়তনে জার্মানির সবচেয়ে ছোট রাজ্য, যা দক্ষিণ-পশ্চিমে অবস্থিত। এর সীমান্তে আছে ফ্রান্স ও লুক্সেমবুর্গ।',
 'sachsen': 'জাকসেন পূর্ব জার্মানিতে অবস্থিত এবং এর সীমান্তে আছে পোল্যান্ড ও চেক প্রজাতন্ত্র।',
 'sachsen-anhalt': 'জাকসেন-আনহাল্ট মধ্য-পূর্ব জার্মানিতে অবস্থিত। এখানে মার্টিন লুথারের সাথে যুক্ত ভিটেনবের্গ দুর্গ গির্জার (Schlosskirche) মতো ঐতিহাসিক স্থান আছে।',
 'schleswig-holstein': 'শ্লেসভিগ-হলস্টাইন জার্মানির সবচেয়ে উত্তরের রাজ্য এবং এর সীমান্তে ডেনমার্ক আছে।',
 'thueringen': 'থুরিঙ্গেন মধ্য জার্মানিতে অবস্থিত। বিস্তীর্ণ বনভূমির কারণে একে প্রায়ই “জার্মানির সবুজ হৃদয়” বলা হয়।',
}
CITY_STATES = {'berlin': 'বার্লিন', 'hamburg': 'হামবুর্গ', 'bremen': 'ব্রেমেন'}
HEAD_X = {'berlin': 'শাসক মেয়র (Regierender Bürgermeister)', 'bremen': 'সিনেটের প্রেসিডেন্ট (Präsident des Senats)', 'hamburg': 'প্রথম মেয়র (Erster Bürgermeister)'}

out = {'_states': NAME}
for slug in SLUGS:
    S = SHORT[slug]
    g = lambda n: Q[f'{slug}-{n}']
    # 301 coat of arms (image options)
    out[f'{slug}-301'] = {'q': f'{S}ের রাজ্য প্রতীক (Wappen) কোনটি?', 'x': COAT[slug]}
    # 302 district
    q = g(302); city = slug in CITY_STATES
    right = q['opts'][q['correct']]
    rp = place_opt(right).split(' (')[0]
    x = f'{rp} {S}ে অবস্থিত। বাকি বিকল্পগুলো জার্মানির অন্য রাজ্যের জেলা।'
    if slug == 'hessen':
        x = 'মাইন-টাউনুস-ক্রাইস (Main-Taunus-Kreis) হেসেনের একটি জেলা, যা ফ্রাঙ্কফুর্টের কাছে। আমারল্যান্ড (Ammerland) নিডারজাকসেনে, আলটোটিং (Altötting) বাইয়ার্নে এবং প্রিগনিৎস (Prignitz) ব্র্যান্ডেনবুর্গে।'
    kind = 'Bezirk' if city else 'Landkreis'
    out[q['id']] = {'q': f'এগুলোর মধ্যে কোনটি {S}ের একটি জেলা ({kind})?', 'o': [place_opt(o) for o in q['opts']], 'x': x}
    # 303 term of parliament
    q = g(303); yrs = bd(re.search(r'(\d) years', q['exp_en']).group(1))
    out[q['id']] = {'q': f'{S}ের রাজ্য সংসদ কত বছরের জন্য নির্বাচিত হয়?', 'o': [opt_generic(o) for o in q['opts']],
                    'x': f'{S}ের রাজ্য সংসদ{" (Landtag)" if slug == "hessen" else ""} {yrs} বছরের মেয়াদের জন্য নির্বাচিত হয়।'}
    # 304 local voting age
    q = g(304); age = bd(re.search(r'is (\d+)', q['exp_en']).group(1))
    x = f'{S}ে স্থানীয় নির্বাচনে ভোট দেওয়ার ন্যূনতম বয়স {age} বছর।'
    if slug == 'hessen': x += ' কিছু অন্য জার্মান রাজ্যে স্থানীয় পর্যায়ে ১৬ বছর বয়স থেকে ভোট দেওয়া যায়।'
    out[q['id']] = {'q': f'{S}ে কত বছর বয়স থেকে স্থানীয় নির্বাচনে ভোট দেওয়া যায়?', 'o': [opt_generic(o) for o in q['opts']], 'x': x}
    # 305 flag
    q = g(305); col = re.search(r'is ([a-z-]+)[,.]', q['exp_en']).group(1)
    x = f'{S}ের রাজ্য পতাকা {colors(col)}।'
    if slug == 'hessen': x = f'হেসেনের রাজ্য পতাকা {colors(col)}, যা হেসেনের সিংহ (Hessischer Löwe) প্রতীকের রঙের সাথে মেলে।'
    out[q['id']] = {'q': f'{S}ের রাজ্য পতাকার রং কী কী?', 'o': [opt_generic(o) for o in q['opts']], 'x': x}
    # 306 civic education
    q = g(306)
    if slug == 'hessen':
        x = 'রাজ্য রাজনৈতিক শিক্ষা কেন্দ্র (Landeszentrale für politische Bildung) হেসেনের নাগরিকদের জন্য রাজনৈতিক বিষয়ে নিরপেক্ষ ও দলনিরপেক্ষ তথ্য দেয়।'
    elif slug == 'schleswig-holstein':
        x = 'শ্লেসভিগ-হলস্টাইনে রাজনৈতিক শিক্ষা ও তথ্য পাওয়া যায় রাজ্য রাজনৈতিক শিক্ষা কমিশনারের (Landesbeauftragter für politische Bildung) কাছে।'
    else:
        x = f'{S}ে রাজনৈতিক শিক্ষা ও তথ্য পাওয়া যায় রাজ্য রাজনৈতিক শিক্ষা কেন্দ্রে (Landeszentrale für politische Bildung)।'
    out[q['id']] = {'q': f'{S}ে রাজনৈতিক বিষয়ে তথ্য কোথায় পাওয়া যায়?', 'o': [opt_generic(o) for o in q['opts']], 'x': x}
    # 307 capital / city-state
    q = g(307)
    if city:
        rest = [v for k, v in CITY_STATES.items() if k != slug]
        out[q['id']] = {'q': 'কোন ফেডারেল রাজ্য একটি নগর-রাজ্য (Stadtstaat)?', 'o': [place_opt(o) for o in q['opts']],
                        'x': f'{S} জার্মানির তিনটি নগর-রাজ্যের (Stadtstaaten) একটি। অন্য দুটি হলো {rest[0]} ও {rest[1]}।'}
    else:
        cp = place_opt(q['opts'][q['correct']]).split(' (')[0]
        x = f'{cp} {S}ের রাজধানী।'
        if slug == 'hessen': x = 'ভিসবাডেন হেসেনের রাজধানী। ফ্রাঙ্কফুর্ট রাজ্যের সবচেয়ে বড় শহর, কিন্তু রাজধানী নয়।'
        out[q['id']] = {'q': f'{S}ের রাজ্য রাজধানীর নাম …', 'o': [place_opt(o) for o in q['opts']], 'x': x}
    # 308 map (image options)
    out[f'{slug}-308'] = {'q': f'{S} কোন (চিহ্নিত) ফেডারেল রাজ্য?', 'x': MAP[slug]}
    # 309 head of government
    q = g(309)
    if slug in HEAD_X: x = f'{S}ের সরকারপ্রধানের উপাধি {HEAD_X[slug]}।'
    elif slug == 'hessen': x = 'হেসেনের সরকারপ্রধানের উপাধি Ministerpräsident/in (মন্ত্রী-প্রেসিডেন্ট), প্রধানমন্ত্রী বা মেয়র নয়। ২০২৫ সালের হিসাবে: বোরিস রাইন (CDU)।'
    else: x = f'{S}ের সরকারপ্রধানের উপাধি মন্ত্রী-প্রেসিডেন্ট (Ministerpräsident/in)।'
    out[q['id']] = {'q': f'{S}ের সরকারপ্রধানকে কী বলা হয়?', 'o': [opt_generic(o) for o in q['opts']], 'x': x}
    # 310 ministry missing
    q = g(310)
    senator = 'Senator' in q['en']
    x = 'পররাষ্ট্র বিষয় ফেডারেল সরকারের দায়িত্ব, রাজ্যের নয়। তাই জার্মানির কোনো রাজ্যে এই মন্ত্রণালয় নেই।'
    if slug == 'hessen': x = 'পররাষ্ট্র বিষয় ফেডারেল সরকারের দায়িত্ব, রাজ্যের নয়। তাই হেসেনসহ জার্মানির কোনো রাজ্যে পররাষ্ট্রমন্ত্রী নেই।'
    out[q['id']] = {'q': f'{S}ে কোন {"সেনেটর" if senator else "মন্ত্রী"} নেই?', 'o': [opt_generic(o) for o in q['opts']], 'x': x}

json.dump(out, open('translations/bn/states.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote', len(out) - 1, 'state questions')
