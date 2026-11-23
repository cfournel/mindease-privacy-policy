"""Turns the reviewed drafts (tools/drafts/<lang>.json, from translate_site.py) into content_ptde.py (mindease#57).

Everything a translation cannot know is set here by hand: slugs (the natural search phrasing of each country), the
narration voice (Onira's own pt/de voices, app 0.18.0), the local helplines and the news block.
Rerun after editing a draft: python3 tools/make_ptde.py
"""
import json
import pathlib
import pprint
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import ptde_comparisons  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]

META = {
    "pt": {"code": "pt", "base": "pt", "label": "PT", "name": "Português", "theme_dir": "hipnose", "guide_dir": "guias",
           "privacy_slug": "privacidade"},
    "de": {"code": "de", "base": "de", "label": "DE", "name": "Deutsch", "theme_dir": "hypnose", "guide_dir": "ratgeber",
           "privacy_slug": "datenschutz"},
}
THEME_SLUGS = {
    "pt": {"anxiety": "ansiedade", "sleep": "dormir", "confidence": "autoconfianca", "stress": "estresse",
           "smoking": "parar-de-fumar", "focus": "foco-e-concentracao", "weight": "emagrecer", "fear": "medos-e-fobias",
           "learning": "memoria-e-aprendizado", "motivation": "motivacao-e-energia", "habits": "habitos-nervosos",
           "pain": "dor", "ibs": "sindrome-do-intestino-irritavel", "emotional_recovery": "recuperacao-emocional",
           "anger": "controlar-a-raiva", "burnout": "burnout", "night_waking": "acordar-de-madrugada"},
    "de": {"anxiety": "angst", "sleep": "schlafen", "confidence": "selbstbewusstsein", "stress": "stress",
           "smoking": "rauchen-aufhoeren", "focus": "konzentration", "weight": "abnehmen", "fear": "aengste-und-phobien",
           "learning": "lernen-und-gedaechtnis", "motivation": "motivation-und-energie",
           "habits": "nervoese-angewohnheiten", "pain": "schmerzen", "ibs": "reizdarm",
           "emotional_recovery": "emotionale-heilung", "anger": "wut-kontrollieren", "burnout": "burnout",
           "night_waking": "naechtliches-aufwachen"},
}
GUIDE_SLUGS = {
    "pt": {"fall_asleep": "como-dormir-com-auto-hipnose", "vs_meditation": "hipnose-ou-meditacao",
           "does_it_work": "auto-hipnose-funciona", "street_hypnosis": "como-funciona-a-hipnose-de-rua",
           "is_it_safe": "auto-hipnose-e-segura", "learn_self_hypnosis": "como-aprender-auto-hipnose"},
    "de": {"fall_asleep": "mit-selbsthypnose-einschlafen", "vs_meditation": "hypnose-oder-meditation",
           "does_it_work": "funktioniert-selbsthypnose", "street_hypnosis": "wie-funktioniert-strassenhypnose",
           "is_it_safe": "ist-selbsthypnose-gefaehrlich", "learn_self_hypnosis": "selbsthypnose-lernen"},
}
NEWS = {
    "pt": ("Novidade: o Onira em português",
           ["O Onira agora fala português do Brasil: a interface, as sessões prontas e as sessões escritas para você.",
            "A narração usa a voz própria do Onira, feita para a hipnose: suave e lenta, ela muda de tom conforme a sessão "
            "se aprofunda."]),
    "de": ("Neu: Onira auf Deutsch",
           ["Onira gibt es jetzt auf Deutsch: die Oberfläche, die fertigen Sitzungen und die Sitzungen, die nur für dich "
            "geschrieben werden.",
            "Vorgelesen wird mit Oniras eigener Stimme für Hypnose: sanft und langsam, sie ändert ihren Ton, je tiefer die "
            "Sitzung wird."]),
}
HELPLINE = {
    "pt": " No Brasil, o CVV atende 24 horas pelo 188, de graça; em caso de emergência, ligue 192 (SAMU).",
    "de": " In Deutschland erreichst du die TelefonSeelsorge rund um die Uhr kostenlos unter 0800 111 0 111, im Notfall "
          "die 112.",
}


# Titles <= 60 and descriptions 70-160 characters (audit.py), and wording a native search would use.
OVERRIDES = {
    "pt": {
        "ui.privacy_body": "Tudo pode ficar no seu celular: o Onira pode rodar o modelo no aparelho, offline, e então o tema "
                           "escolhido, as palavras que você digita e a sessão recebida nunca saem dele. Se preferir, o Onira "
                           "Cloud escreve a sessão no servidor do próprio Onira, só depois que você concorda; o texto não é "
                           "guardado e nada identifica você. Não há conta em nenhum caso.",
        "home.title": "Onira: sessões de auto-hipnose escritas para você",
        "themes.anxiety.title": "Auto-hipnose para ansiedade, feita para você | Onira",
        "themes.confidence.title": "Auto-hipnose para confiança e autoestima | Onira",
        "themes.focus.title": "Auto-hipnose para foco e concentração | Onira",
        "themes.weight.title": "Auto-hipnose para emagrecer e comer melhor | Onira",
        "themes.fear.title": "Auto-hipnose para medos e fobias | Onira",
        "themes.learning.title": "Auto-hipnose para memória e aprendizado | Onira",
        "themes.habits.title": "Auto-hipnose para hábitos nervosos | Onira",
        "themes.pain.title": "Auto-hipnose para a dor, feita para você | Onira",
        "themes.ibs.title": "Auto-hipnose para a síndrome do intestino irritável | Onira",
        "themes.ibs.h1": "Auto-hipnose para a síndrome do intestino irritável",
        "themes.emotional_recovery.title": "Auto-hipnose para a recuperação emocional | Onira",
        "themes.anger.title": "Auto-hipnose para raiva e irritabilidade | Onira",
        "themes.anger.h1": "Auto-hipnose para a raiva e o pavio curto",
        "themes.burnout.title": "Auto-hipnose para burnout e esgotamento | Onira",
        "themes.burnout.h1": "Auto-hipnose para burnout e esgotamento",
        "themes.night_waking.title": "Auto-hipnose para quem acorda de madrugada | Onira",
        "themes.night_waking.h1": "Auto-hipnose para quem acorda de madrugada",
        "guides.fall_asleep.title": "Como dormir com auto-hipnose | Onira",
        "guides.fall_asleep.h1": "Como dormir com auto-hipnose",
        "guides.vs_meditation.title": "Hipnose ou meditação: diferenças e qual usar | Onira",
        "guides.vs_meditation.h1": "Hipnose ou meditação?",
        "guides.does_it_work.title": "A auto-hipnose funciona mesmo? | Onira",
        "guides.does_it_work.h1": "A auto-hipnose funciona mesmo?",
        "guides.is_it_safe.title": "A auto-hipnose é segura? | Onira",
        "guides.is_it_safe.h1": "A auto-hipnose é segura?",
        "home.desc": "O Onira cria no seu celular uma sessão de hipnose só para você e a narra em voz alta: sono, ansiedade, "
                     "estresse, confiança e foco.",
        "themes.stress.title": "Auto-hipnose para aliviar o estresse | Onira",
        "themes.smoking.title": "Auto-hipnose para parar de fumar, feita para você | Onira",
        "themes.smoking.desc": "Auto-hipnose guiada para parar de fumar, escrita no seu celular a partir dos seus gatilhos e "
                               "motivos, e narrada em voz alta. Privada e gratuita.",
        "themes.weight.desc": "Auto-hipnose para emagrecer e mudar hábitos alimentares, escrita no seu celular a partir dos "
                              "seus padrões e narrada em voz alta. Grátis, sem assinatura.",
        "themes.learning.desc": "Auto-hipnose guiada para estudar, memorizar e aprender idiomas, escrita no seu celular a "
                                "partir do que você está estudando. Grátis e offline.",
        "themes.habits.desc": "Auto-hipnose guiada para roer unhas, ranger os dentes ou travar a mandíbula, escrita no seu "
                              "celular em torno do seu gatilho. Grátis e offline.",
        "themes.pain.desc": "Auto-hipnose como complemento ao seu tratamento: menos tensão, menos medo da próxima crise, "
                            "noites mais tranquilas. Um conforto, não uma cura.",
        "themes.ibs.desc": "Auto-hipnose guiada para o lado estressante da SII: intestino mais calmo, menos antecipação, dias "
                           "mais leves. Um apoio ao seu tratamento, não um tratamento.",
        "themes.emotional_recovery.desc": "Auto-hipnose guiada depois de um período difícil: noites mais tranquilas, menos "
                                          "ruminação, dias mais estáveis. Relaxamento, não terapia para trauma.",
        "themes.anger.desc": "Auto-hipnose guiada para a raiva e o pavio curto: acalme o corpo primeiro e treine uma reação "
                             "mais lenta aos seus gatilhos. Grátis e offline.",
        "themes.burnout.desc": "Auto-hipnose guiada para o burnout: descanso de verdade, desligar do trabalho e dormir "
                               "melhor. Um apoio ao relaxamento, não um tratamento.",
        "themes.night_waking.desc": "Uma sessão guiada para quando você acorda de madrugada e não volta a dormir: baixe o "
                                    "alerta, esqueça o relógio e adormeça de novo.",
        "guides.vs_meditation.desc": "O que separa a hipnose guiada da meditação, para que cada uma serve melhor e como "
                                     "escolher para dormir, ansiedade ou mudar um hábito.",
        "guides.does_it_work.desc": "Uma análise honesta: para que a auto-hipnose serve, o que as pesquisas mostram, para "
                                    "quem não funciona e como saber se está fazendo efeito.",
        "guides.learn_self_hypnosis.desc": "Um método realista para aprender auto-hipnose sozinho: o que praticar primeiro, "
                                           "quanto tempo leva, como é o transe e quando parar.",
    },
    "de": {
        "ui.privacy_body": "Alles kann auf deinem Handy bleiben: Onira kann das Modell auf dem Gerät ausführen, offline, und "
                           "dann verlassen das gewählte Thema, deine Worte und die Sitzung es nie. Wenn dir das lieber ist, "
                           "schreibt Onira Cloud die Sitzung auf Oniras eigenem Server, erst nach deiner Zustimmung; der Text "
                           "wird nicht gespeichert, und nichts identifiziert dich. Ein Konto gibt es in keinem Fall.",
        "themes.stress.title": "Selbsthypnose gegen Stress, nur für dich | Onira",
        "themes.pain.title": "Selbsthypnose bei Schmerzen, nur für dich | Onira",
        "themes.ibs.title": "Selbsthypnose bei Reizdarm, nur für dich | Onira",
        "themes.anger.h1": "Selbsthypnose bei Wut und kurzer Zündschnur",
        "themes.sleep.h1": "Selbsthypnose zum Einschlafen",
        "guides.street_hypnosis.title": "Wie funktioniert Straßenhypnose wirklich? | Onira",
        "guides.vs_meditation.h1": "Hypnose oder Meditation?",
        "home.title": "Onira: Selbsthypnose, nur für dich geschrieben",
        "home.desc": "Onira schreibt auf deinem Handy eine persönliche Hypnose-Sitzung und liest sie vor: für Schlaf, Angst, "
                     "Stress, Selbstvertrauen und Fokus.",
        "themes.anxiety.title": "Selbsthypnose gegen Angst, nur für dich | Onira",
        "themes.sleep.title": "Selbsthypnose zum Einschlafen, für dich geschrieben | Onira",
        "themes.confidence.title": "Selbsthypnose für mehr Selbstvertrauen | Onira",
        "themes.smoking.title": "Mit Selbsthypnose rauchfrei werden | Onira",
        "themes.smoking.desc": "Geführte Selbsthypnose zum Rauchstopp, auf deinem Handy aus deinen eigenen Auslösern und "
                               "Gründen geschrieben und vorgelesen. Privat und kostenlos.",
        "themes.focus.desc": "Geführte Selbsthypnose für mehr Fokus, auf deinem Handy rund um die anstehende Arbeit "
                             "geschrieben und vorgelesen. Läuft offline.",
        "themes.weight.title": "Selbsthypnose zum Abnehmen und für Essgewohnheiten | Onira",
        "themes.weight.desc": "Selbsthypnose zum Abnehmen und für bessere Essgewohnheiten, auf deinem Handy aus deinen "
                              "eigenen Mustern geschrieben. Kostenlos, ohne Abo.",
        "themes.fear.desc": "Geführte Selbsthypnose bei Flugangst, Angst vorm Autofahren oder Höhenangst, geschrieben für "
                            "die Situation, die dir bevorsteht. Kostenlos, offline.",
        "themes.learning.desc": "Geführte Selbsthypnose zum Lernen, Erinnern und Sprachenlernen, auf deinem Handy rund um "
                                "deinen Lernstoff geschrieben. Kostenlos und offline.",
        "themes.motivation.desc": "Geführte Selbsthypnose gegen Aufschieben und Antriebslosigkeit, geschrieben für die "
                                  "Aufgabe, die du gerade vor dir herschiebst. Kostenlos.",
        "themes.habits.desc": "Geführte Selbsthypnose bei Nägelkauen, Zähneknirschen und verspanntem Kiefer, auf deinem "
                              "Handy rund um deinen Auslöser geschrieben. Offline.",
        "themes.pain.desc": "Geführte Selbsthypnose als Ergänzung zur Behandlung: weniger Anspannung, weniger Angst vor dem "
                            "nächsten Schub, ruhigere Nächte. Kein Heilmittel.",
        "themes.ibs.desc": "Geführte Selbsthypnose für die Stressseite des Reizdarms: ein ruhigerer Bauch, weniger "
                           "Erwartungsangst, leichtere Tage. Ergänzung, kein Ersatz.",
        "themes.anger.desc": "Geführte Selbsthypnose bei Wut und kurzer Zündschnur: erst den Körper beruhigen, dann eine "
                             "langsamere Reaktion auf deine Auslöser üben. Offline.",
        "themes.burnout.desc": "Geführte Selbsthypnose bei Burnout, wenn du müde und zugleich aufgedreht bist: echte "
                               "Erholung, Abschalten, besserer Schlaf. Keine Behandlung.",
        "themes.night_waking.desc": "Eine geführte Sitzung, wenn du nachts aufwachst und nicht mehr einschläfst: Wachheit "
                                    "senken, die Uhr vergessen, wieder einschlafen.",
        "guides.vs_meditation.title": "Hypnose oder Meditation: der Unterschied | Onira",
        "guides.vs_meditation.desc": "Was Hypnose und Meditation wirklich unterscheidet, wofür beide gut sind und wie du "
                                     "für Schlaf, Angst oder eine Gewohnheit die richtige wählst.",
        "guides.street_hypnosis.desc": "Was bei der Straßenhypnose wirklich passiert: der steife Arm, der eingefrorene "
                                       "Händedruck, warum es nur bei manchen klappt, und ob es legal ist.",
        "guides.is_it_safe.desc": "Die ehrlichen Risiken der Selbsthypnose, wer darauf verzichten sollte und wann du erst "
                                  "ärztlichen Rat brauchst: Schwangerschaft, Epilepsie, Kinder.",
        "guides.learn_self_hypnosis.desc": "Ein realistischer Weg, Selbsthypnose allein zu lernen: was du zuerst übst, wie "
                                           "lange es dauert, wie sich Trance anfühlt, wann du aufhörst.",
    },
}
# Draft wording fixed everywhere it appears: (pattern, replacement).
FIXES = {
    "pt": [(r"Hipnose autog[eê]nica", "Auto-hipnose"), (r"hipnose autog[eê]nica", "auto-hipnose"),
           (r"Hipnose autoinduzida", "Auto-hipnose"), (r"hipnose autoinduzida", "auto-hipnose"),
           (r"\bAutohipno", "Auto-hipno"), (r"\bautohipno", "auto-hipno"), (r"\bAuto-Hipno", "Auto-hipno")],
    "de": [(r"\bSessions\b", "Sitzungen"), (r"\bSessionen\b", "Sitzungen"), (r"\bSession\b", "Sitzung"), (r"Vorfreude auf Beschwerden", "Erwartungsangst"),
           (r"kurzen Zündungen", "kurzer Zündschnur")],
}


# Everything can run on the phone, and Onira Cloud is an option (charles, 2026-11-21): the drafts were translated from
# copy that said nothing ever leaves the device. Literal (old, new) pairs, applied after FIXES; each must match.
CLOUD = {
    "pt": [
        ("Um modelo de IA rodando no seu celular escreve o roteiro — indução, aprofundamento, imagética, sugestões, "
         "ancoragem e, por fim, um retorno claro ao estado de alerta total.",
         "Um modelo de IA escreve o roteiro — indução, aprofundamento, imagética, sugestões, ancoragem e, por fim, um "
         "retorno claro ao estado de alerta total. Ele pode rodar inteiramente no seu celular, offline, ou no Onira "
         "Cloud, se você preferir."),
        ("Onira — sessões de hipnoterapia escritas no seu celular, pelo seu celular.",
         "Onira — sessões de hipnoterapia escritas para você, até totalmente offline."),
        ("Funciona 100% offline, nada sai do seu dispositivo", "Pode funcionar 100% offline, no aparelho"),
        ("Não. O tema por si só já é suficiente. Se você digitar algo, ele permanece no seu celular — o modelo roda "
         "localmente e nada é enviado para a nuvem.",
         "Não. O tema por si só já é suficiente. Se você digitar algo, isso pode ficar no seu celular: com o modelo no "
         "aparelho, nada é enviado. Com o Onira Cloud, só se você aceitar, o texto é enviado para escrever a sessão e "
         "não é guardado."),
        ("Funciona offline, nada sai do seu dispositivo.", "Pode funcionar totalmente offline."),
        ("Apenas uma vez, para baixar o modelo de IA na primeira execução. Depois disso, as sessões são geradas e "
         "narradas totalmente offline.",
         "Não, se as sessões forem escritas no seu celular: o modelo de IA é baixado uma vez e depois as sessões são "
         "geradas e narradas totalmente offline. O Onira Cloud, a outra opção, precisa de conexão."),
        ("Apenas no seu celular, e somente se você salvar a sessão. Nada é enviado para um servidor.",
         "Apenas no seu celular, e somente se você salvar a sessão. Com o Onira Cloud, o texto é enviado para escrever "
         "a sessão e não é guardado; no aparelho, nada é enviado."),
        ("Funciona offline e mantém sua privacidade.", "Privada, até offline."),
        ("Funciona offline, nada é enviado.", "Pode funcionar totalmente offline."),
        ("Privada, gratuita, offline.", "Grátis, até offline."),
        ("e ele permanece no seu telefone, porque o modelo roda localmente.",
         "e ele pode ficar no seu celular, porque o modelo pode rodar localmente."),
        ("Grátis e offline.", "Grátis, até offline."),
        ("O modelo roda no dispositivo, então nada do que você digita é enviado para a nuvem, e funciona com o celular "
         "offline e virado para baixo.",
         "O modelo pode rodar no aparelho: nada do que você digita é enviado, e funciona com o celular offline e virado "
         "para baixo (o Onira Cloud também existe, se você preferir)."),
        ("e um modelo rodando no seu telefone escreve uma sessão em torno disso, depois narra — sem conta, nada enviado "
         "para a nuvem e nada genérico nas imagens.",
         "e um modelo, no celular ou no Onira Cloud, escreve uma sessão em torno disso, depois narra — sem conta e nada "
         "genérico nas imagens."),
        ("Ela roda inteiramente no dispositivo, então o que você digita sobre sua própria vida nunca sai do celular — "
         "não há conta nem servidor que possa ler isso.",
         "Ela pode rodar inteiramente no aparelho, e então o que você digita sobre sua própria vida nunca sai do "
         "celular. O Onira Cloud é uma opção, só com o seu acordo, e não guarda o texto; não há conta em nenhum caso."),
        ("e um modelo rodando no dispositivo escreve o roteiro e o fala.",
         "e um modelo, no aparelho ou no Onira Cloud, escreve o roteiro e o fala."),
        ("É gratuita, funciona offline, e nada do que você digita sai do telefone.",
         "É gratuita, pode funcionar offline, e então nada do que você digita sai do celular."),
        ("É gratuito, funciona offline e nada que você digita sai do dispositivo",
         "É gratuito, pode funcionar offline, e então nada que você digita sai do aparelho"),
        ("É gratuito, funciona offline e nada que você digita sai do seu celular.",
         "É gratuito, pode funcionar offline, e então nada que você digita sai do seu celular."),
    ],
    "de": [
        ("Ein KI-Modell auf deinem Handy schreibt das Skript – Einleitung, Vertiefung, Imagination, Suggestionen, "
         "Verankerung und schließlich eine klare Rückkehr zur vollen Wachheit.",
         "Ein KI-Modell schreibt das Skript – Einleitung, Vertiefung, Imagination, Suggestionen, Verankerung und "
         "schließlich eine klare Rückkehr zur vollen Wachheit. Es kann komplett auf deinem Handy laufen, offline, oder "
         "in der Onira Cloud, wenn dir das lieber ist."),
        ("Onira – Hypnose-Sitzungen, geschrieben auf deinem Handy, von deinem Handy.",
         "Onira – Hypnose-Sitzungen, für dich geschrieben, auch komplett offline."),
        ("Funktioniert komplett offline, nichts verlässt das Gerät", "Kann komplett offline laufen, auf dem Gerät"),
        ("mit einem KI-Modell, das vollständig auf deinem Gerät läuft", "mit einem KI-Modell, das vollständig auf deinem Gerät laufen kann"),
        ("Wenn du etwas eingibst, bleibt es auf deinem Handy – das Modell läuft lokal, und nichts wird hochgeladen.",
         "Wenn du etwas eingibst, kann es auf deinem Handy bleiben: Mit dem Modell auf dem Gerät wird nichts "
         "hochgeladen. Mit Onira Cloud, nur wenn du zustimmst, wird es zum Schreiben der Sitzung gesendet und nicht "
         "gespeichert."),
        ("Läuft offline, nichts verlässt dein Gerät.", "Kann komplett offline laufen."),
        ("Nur einmal, um das KI-Modell beim ersten Start herunterzuladen. Danach werden Sitzungen komplett offline "
         "generiert und vorgelesen.",
         "Nicht, wenn die Sitzungen auf deinem Handy geschrieben werden: Das KI-Modell wird einmal heruntergeladen, "
         "danach werden Sitzungen komplett offline generiert und vorgelesen. Onira Cloud, die andere Option, braucht "
         "eine Verbindung."),
        ("Nur auf deinem Handy und nur, wenn du die Sitzung speicherst. Nichts wird an einen Server gesendet.",
         "Nur auf deinem Handy und nur, wenn du die Sitzung speicherst. Mit Onira Cloud wird es zum Schreiben der "
         "Sitzung gesendet und nicht gespeichert; auf dem Gerät wird nichts gesendet."),
        ("Offline und privat.", "Privat, auch offline."),
        ("Läuft offline.", "Kann offline laufen."),
        ("Kostenlos, offline.", "Kostenlos, auch offline."),
        ("und es bleibt auf deinem Telefon, weil das Modell lokal läuft.",
         "und es kann auf deinem Handy bleiben, weil das Modell lokal laufen kann."),
        ("Kostenlos und offline.", "Kostenlos, auch offline."),
        ("rund um deinen Auslöser geschrieben. Offline.", "rund um deinen Auslöser geschrieben. Auch offline."),
        ("eine langsamere Reaktion auf deine Auslöser üben. Offline.",
         "eine langsamere Reaktion auf deine Auslöser üben. Auch offline."),
        ("Das Modell läuft auf dem Gerät, also wird nichts hochgeladen, und es funktioniert mit dem Handy offline und "
         "Display nach unten.",
         "Das Modell kann auf dem Gerät laufen: Dann wird nichts hochgeladen, und es funktioniert mit dem Handy offline "
         "und Display nach unten (Onira Cloud gibt es auch, wenn dir das lieber ist)."),
        ("und ein Modell auf deinem Telefon schreibt eine Sitzung darum herum und spricht sie vor — kein Konto, nichts "
         "wird hochgeladen, und keine generischen Bilder.",
         "und ein Modell, auf dem Handy oder in der Onira Cloud, schreibt eine Sitzung darum herum und spricht sie vor — "
         "kein Konto und keine generischen Bilder."),
        ("Es läuft vollständig auf dem Gerät, also verlässt, was du über dein eigenes Leben tippst, das Telefon nie – es "
         "gibt kein Konto und keinen Server, der es lesen könnte.",
         "Es kann vollständig auf dem Gerät laufen, dann verlässt, was du über dein eigenes Leben tippst, das Handy nie. "
         "Onira Cloud ist eine Option, nur mit deiner Zustimmung, und speichert den Text nicht; ein Konto gibt es in "
         "keinem Fall."),
        ("und ein Modell, das auf dem Gerät läuft, schreibt das Skript und spricht es.",
         "und ein Modell, auf dem Gerät oder in der Onira Cloud, schreibt das Skript und spricht es."),
        ("Es ist kostenlos, funktioniert offline, und nichts, was du tippst, verlässt das Telefon.",
         "Es ist kostenlos, kann offline laufen, und dann verlässt nichts, was du tippst, das Handy."),
        ("Es ist kostenlos, läuft offline und nichts, was du eingibst, verlässt das Gerät",
         "Es ist kostenlos, kann offline laufen, und dann verlässt nichts, was du eingibst, das Gerät"),
        ("Es ist kostenlos, funktioniert offline, und nichts, was du eingibst, verlässt dein Telefon.",
         "Es ist kostenlos, kann offline laufen, und dann verlässt nichts, was du eingibst, dein Handy."),
        ("lokale Krisen hotline", "lokale Krisenhotline"),
        ("aufgeführt wird.anderswo", "aufgeführt wird. Anderswo"),
    ],
}


def cloud(v, lang, hits):
    if isinstance(v, dict):
        return {k: cloud(x, lang, hits) for k, x in v.items()}
    if isinstance(v, list):
        return [cloud(x, lang, hits) for x in v]
    if isinstance(v, str):
        for i, (old, new) in enumerate(CLOUD[lang]):
            if old in v:
                hits.add(i)
                v = v.replace(old, new)
    return v


PRIVACY_SCREEN = {
    "pt": ["privacy", "Nada sai do celular sem o seu acordo",
           "Sem conta. No aparelho funciona offline; Onira Cloud só se você aceitar."],
    "de": ["privacy", "Nichts verlässt dein Handy ohne dein Okay",
           "Kein Konto. Auf dem Gerät offline; Onira Cloud nur mit deiner Zustimmung."],
}


def fix(v, rules):
    if isinstance(v, dict):
        return {k: fix(x, rules) for k, x in v.items()}
    if isinstance(v, list):
        return [fix(x, rules) for x in v]
    if isinstance(v, str):
        for pat, rep in rules:
            v = re.sub(pat, rep, v)
    return v


def apply_overrides(out, lang):
    for path, value in OVERRIDES[lang].items():
        *parents, leaf = path.split(".")
        node = out
        for p in parents:
            node = node[p]
        assert leaf in node, path
        node[leaf] = value


def shape(v, ref):
    """JSON turned every tuple into a list: give each container the type it has in the English copy."""
    if isinstance(v, dict) and isinstance(ref, dict):
        return {k: shape(x, ref.get(k)) for k, x in v.items()}
    if isinstance(v, list):
        items = [shape(x, ref[i] if isinstance(ref, (list, tuple)) and i < len(ref) else None) for i, x in enumerate(v)]
        return tuple(items) if isinstance(ref, tuple) else items
    return v


def fix_de(v):
    if isinstance(v, dict):
        return {k: fix_de(x) for k, x in v.items()}
    if isinstance(v, list):
        return [fix_de(x) for x in v]
    if isinstance(v, str):
        # The app says "Sitzung"; the draft mixed in the anglicism.
        return re.sub(r"\bSessions\b", "Sitzungen", re.sub(r"\bSession\b", "Sitzung", v))
    return v


def build(lang):
    d = json.loads((ROOT / "tools" / "drafts" / f"{lang}.json").read_text())
    # Pages added after the drafts (home FAQ, phones, comparisons): translated by hand in ptde_comparisons.py.
    d.update(ptde_comparisons.units(lang))
    d["home"]["faq"] = ptde_comparisons.HOME_FAQ[lang]
    d = fix(d, FIXES[lang])
    if lang == "de":
        d = fix_de(d)
    out = dict(META[lang])
    out["ui"] = d["ui"]
    out["home"] = d["home"]
    out["home"]["news_title"], out["home"]["news"] = NEWS[lang]
    if not out["ui"]["safety_body"].rstrip().endswith(HELPLINE[lang].strip()):
        out["ui"]["safety_body"] = out["ui"]["safety_body"].rstrip() + HELPLINE[lang]
    out["themes"] = {}
    for key, slug in THEME_SLUGS[lang].items():
        out["themes"][key] = {**d[f"themes.{key}"], "slug": slug}
    out["guides"] = {}
    for key, slug in {**GUIDE_SLUGS[lang], **ptde_comparisons.SLUGS[lang]}.items():
        out["guides"][key] = {**d[f"guides.{key}"], "slug": slug}
    apply_overrides(out, lang)
    hits = set()
    out = cloud(out, lang, hits)
    missed = [CLOUD[lang][i][0][:60] for i in range(len(CLOUD[lang])) if i not in hits]
    assert not missed, missed
    # No pt/de capture of the morning/midday homes yet ("day" blends three times of day), and the privacy card says what
    # the pt/de card says (Onira Cloud only with the listener's OK).
    out["ui"]["screens"] = [PRIVACY_SCREEN[lang] if sc[0] == "privacy" else sc
                            for sc in out["ui"]["screens"] if sc[0] != "day"]
    import sys
    sys.path.insert(0, str(ROOT))
    import content
    return shape(out, content.EN)


def main():
    parts = ['# -*- coding: utf-8 -*-\n"""Portuguese (Brazil) and German copy (mindease#57). Generated by tools/make_ptde.py from the reviewed\n'
             'drafts in tools/drafts/: edit the drafts or make_ptde.py, not this file."""\n']
    for lang, var in (("pt", "PT"), ("de", "DE")):
        parts.append(f"\n{var} = " + pprint.pformat(build(lang), width=120, sort_dicts=False) + "\n")
    (ROOT / "content_ptde.py").write_text("".join(parts), encoding="utf-8")
    print("wrote content_ptde.py")


if __name__ == "__main__":
    main()
