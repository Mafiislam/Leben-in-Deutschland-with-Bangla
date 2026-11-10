# Leben in Deutschland Test: Deutsch, English, বাংলা

A free practice site for the German citizenship test (Einbürgerungstest, "Leben in Deutschland"). Every question is shown in German, English and Bangla.

* 300 general questions and 160 state questions (10 for each of the 16 Bundesländer)
* Correct answers and a short explanation for each question, in all three languages
* Switch each language on or off. The interface is available in German, English and Bangla
* Study mode with search and "mark as learned"
* Practice quiz with instant feedback and a list of your mistakes
* Exam simulation: 30 general and 3 state questions, 60 minutes, 17 correct answers to pass
* Works offline once opened (installable as an app), light and dark mode, no tracking, no sign up

## Run it

It is a plain static site, so any web server works.

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000`. To publish it, enable GitHub Pages for this repository (branch root).

## How the data is built

```
data/base.json            German and English text, correct answers, images
translations/bn/*.json    Bangla: question, four options, explanation
scripts/merge_bn.py       merges both into data/questions.json (used by the site)
scripts/check_bn.py       checks that every translation file is complete and valid
scripts/gen_states_bn.py  builds the Bangla for the state questions from reviewed templates
```

After you change a translation, run:

```bash
python3 -I scripts/check_bn.py
python3 -I scripts/merge_bn.py --strict
```

Bump `CACHE` in `sw.js` when you publish an update, so returning visitors get the new files.

## Bangla translation notes

* German terms that matter for the real test (for example Grundgesetz, Bundestag, Rechtsstaat) stay in brackets after the Bangla word.
* Place names are written in Bangla with the German spelling in brackets.
* Questions about office holders and parliament seats change after elections. Check them on the BAMF website before you sit the test.
* A native speaker should proofread the Bangla. Corrections are welcome as pull requests to `translations/bn/`.

## Sources and licences

* The questions come from the official catalogue of the Federal Office for Migration and Refugees (BAMF): <https://www.bamf.de/SharedDocs/Anlagen/DE/Integration/Einbuergerung/gesamtfragenkatalog-lebenindeutschland.html>
* The German and English wording, the English explanations and the question images come from the open source project by Abdullah Butt: <https://github.com/abdullahbutt/leben-in-deutschland-test>. Its content is licensed under CC BY-NC 4.0, so this project is for personal and educational use only. Commercial use needs the author's written permission.
* The Bangla translations and the app code in this repository are new work. The code is under the MIT licence (see `LICENSE`). The data and translations follow CC BY-NC 4.0 (see `LICENSE-CONTENT.md`).
* The font is Noto Sans Bengali (SIL Open Font Licence, `fonts/OFL-NotoSansBengali.txt`).

This site is not an official BAMF product. It is for study only.
