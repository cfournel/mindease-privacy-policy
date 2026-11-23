"""Portuguese (Brazil) and German copy of the pages added after the first pt/de drafts (mindease#57): the home FAQ,
the compatible-phones guide and the AI hypnosis app comparisons. Translated by hand from the English pages of
2026-11-23 (facts checked on the rivals' sites on 2026-11-22). make_ptde.py merges these units into the drafts.
"""

PHONES = {"pt": "/pt/guias/celulares-compativeis-offline/", "de": "/de/ratgeber/kompatible-handys-offline/"}
BEST = {"pt": "/pt/guias/melhores-apps-de-hipnose-com-ia/", "de": "/de/ratgeber/beste-ki-hypnose-apps/"}
VS_SLUG = {
    "pt": {"vs_hypnothera": "onira-ou-hypnothera", "vs_inthemoment": "onira-ou-inthemoment", "vs_hypnova": "onira-ou-hypnova"},
    "de": {"vs_hypnothera": "onira-oder-hypnothera", "vs_inthemoment": "onira-oder-inthemoment",
           "vs_hypnova": "onira-oder-hypnova"},
}
SLUGS = {
    "pt": {"phones": "celulares-compativeis-offline", "best_ai_apps": "melhores-apps-de-hipnose-com-ia", **VS_SLUG["pt"]},
    "de": {"phones": "kompatible-handys-offline", "best_ai_apps": "beste-ki-hypnose-apps", **VS_SLUG["de"]},
}


def _vs_url(lang, key):
    return f"/{lang}/{'guias' if lang == 'pt' else 'ratgeber'}/{VS_SLUG[lang][key]}/"


ROWS = {
    "pt": ["Grátis", "Conta", "Onde a sessão é escrita", "Offline", "Plataformas", "Idiomas", "Pago"],
    "de": ["Kostenlos", "Konto", "Wo die Sitzung geschrieben wird", "Offline", "Plattformen", "Sprachen", "Kostenpflichtig"],
}
ONIRA = {
    "pt": ["Sessões personalizadas sem créditos e sem limite, um anúncio enquanto cada uma é preparada", "Nenhuma",
           f"No celular [se ele roda o modelo]({PHONES['pt']}); senão, Onira Cloud com o seu consentimento",
           "Sim, inclusive a escrita, em um celular compatível", "Android",
           "Português, inglês, francês, espanhol, alemão",
           "Compra única remove os anúncios; Onira Cloud: um anúncio por sessão ou assinatura opcional"],
    "de": ["Persönliche Sitzungen ohne Credits und ohne Limit, eine Werbung, während jede vorbereitet wird", "Keins",
           f"Auf dem Handy, [wenn es das Modell ausführen kann]({PHONES['de']}), sonst Onira Cloud mit deiner Zustimmung",
           "Ja, das Schreiben inklusive, auf einem kompatiblen Handy", "Android",
           "Deutsch, Englisch, Französisch, Spanisch, Portugiesisch",
           "Einmalkauf entfernt die Werbung; Onira Cloud: eine Werbung pro Sitzung oder optionales Abo"],
}
RIVAL = {
    "pt": {
        "Hypnothera": ["25 créditos, depois mais 15 por semana (1 crédito ≈ 1 min de áudio); sessões rápidas ilimitadas "
                       "de 30 s a 5 min", "Sim (um teste de 5 min sem conta)", "Nos servidores deles",
                       "Download das sessões com assinatura", "iOS, Android, web", "14 idiomas, mais de 100 vozes",
                       "US$ 6,99/semana, US$ 19,99/mês ou US$ 99,99/ano (aumento anunciado para novos assinantes em "
                       "1º de dezembro de 2026)"],
        "InTheMoment": ["2 sessões novas por dia, no máximo 20 min, guardadas por 60 dias", "Sim", "Nos servidores deles",
                        "Download das sessões com o Pro", "iOS, Android, web", "18 idiomas com o Pro",
                        "Pro: £ 14,99/mês (5 sessões por dia, até 45 min)"],
        "Hypnova": ["Mais de 300 sessões prontas; 60 créditos no cadastro para sessões personalizadas",
                    "Sim, para os créditos", "Nos servidores deles", "Não informado", "iOS, Android, web",
                    "Não informado", "Pro: US$ 12,99/mês (240 créditos) ou US$ 99,99/ano"],
    },
    "de": {
        "Hypnothera": ["25 Credits, dann jede Woche 15 weitere (1 Credit ≈ 1 Min. Audio); unbegrenzte Kurz-Sitzungen von "
                       "30 s bis 5 Min.", "Ja (5 Min. Test ohne Konto)", "Auf ihren Servern",
                       "Sitzungen herunterladen mit Abo", "iOS, Android, Web", "14 Sprachen, über 100 Stimmen",
                       "6,99 $/Woche, 19,99 $/Monat oder 99,99 $/Jahr (Preiserhöhung für Neukunden zum 1. Dezember 2026 "
                       "angekündigt)"],
        "InTheMoment": ["2 neue Sitzungen pro Tag, höchstens 20 Min., 60 Tage gespeichert", "Ja", "Auf ihren Servern",
                        "Sitzungen herunterladen mit Pro", "iOS, Android, Web", "18 Sprachen mit Pro",
                        "Pro: 14,99 £/Monat (5 Sitzungen pro Tag, bis 45 Min.)"],
        "Hypnova": ["Über 300 fertige Sitzungen; 60 Credits bei der Anmeldung für persönliche Sitzungen",
                    "Ja, für die Credits", "Auf ihren Servern", "Keine Angabe", "iOS, Android, Web", "Keine Angabe",
                    "Pro: 12,99 $/Monat (240 Credits) oder 99,99 $/Jahr"],
    },
}
CHECKED = {"pt": "22 de novembro de 2026", "de": "22. November 2026"}


def _table(lang, apps, caption):
    cols = [ONIRA[lang]] + [RIVAL[lang][a] for a in apps]
    return {"headers": [""] + ["Onira"] + apps,
            "rows": [[crit] + [c[i] for c in cols] for i, crit in enumerate(ROWS[lang])],
            "caption": caption}


HOME_FAQ = {
    "pt": [
        ["O Onira é grátis?",
         "Sim. As sessões personalizadas e as prontas são grátis, sem créditos para contar e sem assinatura obrigatória: "
         "um anúncio passa enquanto a sessão personalizada é preparada, e uma compra única o remove."],
        ["Preciso de uma conta?",
         "Não. Sem cadastro, sem e-mail e sem login: você abre o app e começa uma sessão."],
        ["O Onira funciona offline?",
         f"Sim, [se o seu celular roda o modelo]({PHONES['pt']}) (cerca de 6 GB de RAM ou mais): depois de um download "
         "único, as sessões são escritas e narradas no celular, até em modo avião. Nos outros celulares, o Onira Cloud "
         "escreve a sessão, só com o seu acordo."],
        ["É hipnoterapia ou um tratamento médico?",
         "Não. O Onira é uma ferramenta de relaxamento e auto-hipnose. Ele não substitui um médico, um terapeuta nem os "
         "serviços de emergência."],
        ["Em quais idiomas o Onira fala?",
         "Português do Brasil, inglês, francês, espanhol e alemão, cada um com a sua própria voz de narração, feita para "
         "a hipnose."],
    ],
    "de": [
        ["Ist Onira kostenlos?",
         "Ja. Persönliche und fertige Sitzungen sind kostenlos, ohne Credits zum Zählen und ohne Pflicht-Abo: Während "
         "eine persönliche Sitzung vorbereitet wird, läuft eine Werbung, und ein Einmalkauf entfernt sie."],
        ["Brauche ich ein Konto?",
         "Nein. Keine Registrierung, keine E-Mail, kein Login: Du öffnest die App und startest eine Sitzung."],
        ["Funktioniert Onira offline?",
         f"Ja, [wenn dein Handy das Modell ausführen kann]({PHONES['de']}) (etwa 6 GB RAM oder mehr): Nach einem "
         "einmaligen Download werden die Sitzungen auf dem Handy geschrieben und vorgelesen, auf Wunsch im Flugmodus. "
         "Auf anderen Handys schreibt Onira Cloud die Sitzung, nur mit deiner Zustimmung."],
        ["Ist das Hypnotherapie oder eine medizinische Behandlung?",
         "Nein. Onira ist ein Werkzeug für Entspannung und Selbsthypnose. Es ersetzt weder Ärztin oder Arzt noch "
         "Therapie oder Notdienste."],
        ["Welche Sprachen spricht Onira?",
         "Deutsch, Englisch, Französisch, Spanisch und brasilianisches Portugiesisch, jeweils mit einer eigenen, für "
         "Hypnose gemachten Erzählstimme."],
    ],
}


def _phones(lang):
    if lang == "pt":
        return {
            "nav": "Celulares compatíveis",
            "card": "Quais celulares escrevem as sessões offline, e o que acontece nos outros.",
            "title": "Quais celulares rodam o Onira offline? | Onira",
            "desc": "O Onira escreve as sessões no celular, offline, quando ele tem cerca de 6 GB de RAM. Como "
                    "verificar o seu e o que o Onira Cloud faz nos outros.",
            "h1": "Quais celulares rodam o Onira offline?",
            "lede": "O Onira pode escrever cada sessão no próprio celular, sem conexão e sem enviar nada a lugar "
                    "nenhum. Para isso é preciso um celular razoavelmente potente: veja quais, como saber, e o que "
                    "acontece nos outros.",
            "answer": "Um celular Android com cerca de 6 GB de memória (RAM) ou mais, e uns 2 GB livres de "
                      "armazenamento para um download único do modelo de IA (1,7 GB). Nesses celulares a sessão é "
                      "escrita no aparelho, até em modo avião, e o que você digita nunca sai dele. Nos celulares mais "
                      "leves, o Onira oferece o Onira Cloud: a sessão é escrita no servidor do próprio Onira, só com o "
                      "seu acordo, e o texto não é guardado.",
            "sections": [
                ["Por que a memória importa mais que a velocidade",
                 ["O modelo que escreve a sua sessão precisa ficar na memória do celular enquanto trabalha. Num "
                  "celular de 6 GB ele ocupa cerca de 1,6 GB durante a escrita e é descarregado assim que a última "
                  "parte fica pronta, e a sessão toca com a memória livre de novo. Abaixo disso, o Android começaria "
                  "a fechar apps, o Onira inclusive, no meio da sessão.",
                  "O próprio Onira verifica a memória do celular; não há nada para configurar. Ele foi testado num "
                  "Samsung Galaxy S20 FE de 6 GB, um intermediário mais antigo, que escreve uma sessão completa com "
                  "folga. Os detalhes técnicos estão em [como rodamos um modelo de IA num celular]"
                  "(/guides/running-an-llm-on-a-phone/) (em inglês)."],
                 []],
                ["Como verificar o seu celular",
                 ["Você pode conferir, ou simplesmente deixar o Onira decidir."],
                 ["Abra Configurações e depois Sobre o telefone: a quantidade de RAM aparece ali (em algumas marcas, "
                  "em Especificações ou Hardware).",
                  "6 GB ou mais: o Onira pode escrever as suas sessões no celular, offline.",
                  "4 GB ou menos: as sessões prontas funcionam normalmente, e as personalizadas passam pelo Onira "
                  "Cloud, depois do seu acordo.",
                  "Na dúvida? Comece uma sessão personalizada: se o celular não puder rodar o modelo, o Onira avisa e "
                  "oferece o Onira Cloud."]],
                ["O que acontece na primeira vez",
                 ["Na primeira sessão personalizada, o Onira pergunta uma vez se você quer usar o Onira Cloud. Escolha "
                  "manter no celular e o modelo é baixado (1,7 GB, melhor no Wi-Fi); depois disso, toda sessão é "
                  "escrita no aparelho. Escolha a nuvem e a sessão começa na hora, sem o download. Dá para mudar de "
                  "ideia depois, nas Configurações.",
                  "As sessões prontas nunca enviam nada e funcionam em qualquer celular."],
                 []],
                ["O Onira Cloud, nos outros celulares",
                 ["O que é enviado: o tema, o idioma do app e as palavras que você digitou, por uma conexão "
                  "criptografada até o servidor do próprio Onira, que escreve a sessão e a devolve. O texto não é "
                  "armazenado e não há conta. Um vídeo curto de publicidade paga cada sessão na nuvem. Os detalhes "
                  "estão na [política de privacidade](/privacy/) (em inglês)."],
                 []],
            ],
            "faq": [
                ["O meu celular tem 4 GB de RAM. Posso usar o Onira?",
                 "Sim. As sessões prontas funcionam como em qualquer celular, e as personalizadas são escritas pelo "
                 "Onira Cloud, se você concordar."],
                ["Preciso de internet?",
                 "Uma vez, para baixar o modelo e a voz de narração. Depois disso, num celular compatível, as sessões "
                 "são escritas e narradas offline."],
                ["Quanto espaço ocupa?",
                 "Cerca de 1,7 GB para o modelo e 80 MB para a voz de narração do seu idioma."],
                ["Existe versão para iPhone?",
                 "Ainda não: o Onira é um app Android."],
            ],
        }
    return {
        "nav": "Kompatible Handys",
        "card": "Welche Handys deine Sitzungen offline schreiben, und was auf den anderen passiert.",
        "title": "Welche Handys können Onira offline ausführen? | Onira",
        "desc": "Onira schreibt Sitzungen offline auf dem Handy, wenn es etwa 6 GB RAM hat. So prüfst du deins, und "
                "das macht Onira Cloud auf anderen Handys.",
        "h1": "Welche Handys können Onira offline ausführen?",
        "lede": "Onira kann jede Sitzung direkt auf deinem Handy schreiben, ohne Verbindung und ohne etwas irgendwohin "
                "zu senden. Dafür braucht es ein einigermaßen leistungsfähiges Handy: welche das sind, wie du es "
                "erkennst und was auf den anderen passiert.",
        "answer": "Ein Android-Handy mit etwa 6 GB Arbeitsspeicher (RAM) oder mehr und rund 2 GB freiem Speicher für "
                  "einen einmaligen Download des KI-Modells (1,7 GB). Auf diesen Handys wird die Sitzung auf dem Gerät "
                  "geschrieben, auf Wunsch im Flugmodus, und was du tippst, verlässt es nie. Auf schwächeren Handys "
                  "bietet Onira Onira Cloud an: Die Sitzung wird auf Oniras eigenem Server geschrieben, nur mit deiner "
                  "Zustimmung, und der Text wird nicht gespeichert.",
        "sections": [
            ["Warum der Arbeitsspeicher mehr zählt als die Geschwindigkeit",
             ["Das Modell, das deine Sitzung schreibt, muss während der Arbeit im Arbeitsspeicher des Handys liegen. "
              "Auf einem 6-GB-Handy belegt es beim Schreiben etwa 1,6 GB und wird entladen, sobald der letzte Teil "
              "fertig ist; die Sitzung läuft dann mit wieder freiem Speicher. Darunter würde Android anfangen, Apps zu "
              "schließen, Onira eingeschlossen, mitten in der Sitzung.",
              "Onira prüft den Arbeitsspeicher selbst; du musst nichts einstellen. Getestet wurde auf einem Samsung "
              "Galaxy S20 FE mit 6 GB, einem älteren Mittelklasse-Handy, das eine ganze Sitzung problemlos schreibt. "
              "Die technischen Details stehen in [wie wir ein KI-Modell auf einem Handy ausführen]"
              "(/guides/running-an-llm-on-a-phone/) (auf Englisch)."],
             []],
            ["So prüfst du dein Handy",
             ["Du kannst nachsehen oder Onira einfach entscheiden lassen."],
             ["Öffne Einstellungen, dann Über das Telefon: Dort steht der Arbeitsspeicher (bei manchen Marken unter "
              "Gerätespezifikationen oder Hardware).",
              "6 GB oder mehr: Onira kann deine Sitzungen offline auf dem Handy schreiben.",
              "4 GB oder weniger: Fertige Sitzungen funktionieren wie gewohnt, persönliche laufen über Onira Cloud, "
              "nachdem du zugestimmt hast.",
              "Unsicher? Starte eine persönliche Sitzung: Wenn das Handy das Modell nicht ausführen kann, sagt Onira "
              "es dir und bietet stattdessen Onira Cloud an."]],
            ["Was beim ersten Mal passiert",
             ["Bei deiner ersten persönlichen Sitzung fragt Onira einmal, ob du Onira Cloud nutzen möchtest. Entscheidest "
              "du dich fürs Handy, wird das Modell heruntergeladen (1,7 GB, am besten im WLAN), und danach wird jede "
              "Sitzung auf dem Gerät geschrieben. Entscheidest du dich für die Cloud, startet die Sitzung sofort, ohne "
              "Download. Du kannst es später in den Einstellungen ändern.",
              "Fertige Sitzungen senden nie etwas und funktionieren auf jedem Handy."],
             []],
            ["Onira Cloud auf den anderen Handys",
             ["Was gesendet wird: das Thema, die Sprache der App und die Worte, die du getippt hast, über eine "
              "verschlüsselte Verbindung an Oniras eigenen Server, der die Sitzung schreibt und zurückschickt. Der "
              "Text wird nicht gespeichert, und es gibt kein Konto. Ein kurzes Werbevideo bezahlt jede Cloud-Sitzung. "
              "Details stehen in der [Datenschutzerklärung](/privacy/) (auf Englisch)."],
             []],
        ],
        "faq": [
            ["Mein Handy hat 4 GB RAM. Kann ich Onira nutzen?",
             "Ja. Fertige Sitzungen funktionieren wie auf jedem Handy, und persönliche Sitzungen schreibt Onira Cloud, "
             "wenn du zustimmst."],
            ["Brauche ich eine Internetverbindung?",
             "Einmal, um das Modell und die Erzählstimme herunterzuladen. Danach werden Sitzungen auf einem kompatiblen "
             "Handy offline geschrieben und vorgelesen."],
            ["Wie viel Speicher braucht es?",
             "Etwa 1,7 GB für das Modell und 80 MB für die Erzählstimme deiner Sprache."],
            ["Gibt es eine iPhone-Version?",
             "Noch nicht: Onira ist eine Android-App."],
        ],
    }


def _best(lang):
    p = PHONES[lang]
    vs = {k: _vs_url(lang, k) for k in VS_SLUG[lang]}
    apps = ["Hypnothera", "InTheMoment", "Hypnova"]
    if lang == "pt":
        return {
            "nav": "Apps de hipnose com IA comparados",
            "card": "Onira, Hypnothera, InTheMoment e Hypnova: plano grátis, conta, offline, idiomas.",
            "title": "Melhores apps de hipnose com IA em 2026, comparados | Onira",
            "desc": "Onira, Hypnothera, InTheMoment e Hypnova comparados: plano grátis, conta, uso offline, Android, "
                    "idiomas e preços, conferidos nos próprios sites.",
            "h1": "Apps de hipnose com IA comparados (2026)",
            "lede": "Quatro apps escrevem uma sessão de hipnose a partir do que você conta. Nem por isso são iguais: o "
                    "que é grátis, a conta, onde a sessão é escrita e os idiomas mudam tudo. Esta página é publicada "
                    "pelo Onira; as informações sobre os outros apps vêm dos sites deles.",
            "answer": "Se você quer sem conta, sem créditos e nada saindo do celular, o Onira é o único dos quatro que "
                      f"escreve a sessão no aparelho, [se o seu celular rodar o modelo]({p}). Se você usa iPhone, ou "
                      "quer muitas vozes e idiomas, o Hypnothera e o InTheMoment oferecem mais, com conta e um plano "
                      "grátis limitado. O Hypnova se destaca pela biblioteca grátis de mais de 300 sessões prontas.",
            "table": _table(lang, apps, f"Conferido em {CHECKED[lang]} nos sites do Hypnothera, do InTheMoment e do "
                                        "Hypnova. Os preços nas lojas variam por país."),
            "sections": [
                ["Como comparamos",
                 ["Ficamos com os apps que escrevem uma sessão a partir das suas palavras, não os que só oferecem "
                  "gravações. Para cada um anotamos o que o site informa: o que é grátis e por quanto tempo, se precisa "
                  "de conta, onde o texto é escrito, o que funciona offline, plataformas, idiomas e preços. Nós fazemos "
                  "o Onira: leia esta tabela sabendo disso, e confira os preços ao assinar, eles mudam com frequência."],
                 []],
                ["Se a privacidade vem em primeiro lugar",
                 ["Hypnothera, InTheMoment e Hypnova escrevem a sessão nos servidores deles, o que significa enviar o "
                  "que você descreve e, em geral, criar uma conta. O Onira escreve a sessão no celular quando ele tem "
                  "cerca de 6 GB de RAM: o que você digita nunca sai dele, e funciona em modo avião. Num celular mais "
                  "leve, o Onira Cloud assume, só com o seu acordo, sem conta e sem guardar o texto."],
                 []],
                ["Se você quer muitas sessões grátis",
                 ["Grátis quer dizer coisas diferentes. O Hypnothera conta em créditos, cerca de um minuto de áudio por "
                  "crédito, recarregados toda semana. O InTheMoment permite duas sessões novas por dia. O Hypnova "
                  "oferece uma grande biblioteca pronta e créditos para personalizar. O Onira não conta nada: cada "
                  "sessão personalizada custa um anúncio."],
                 []],
                ["Se você usa iPhone ou quer muitas vozes para escolher",
                 ["O Onira é só para Android e tem uma voz por idioma, feita para a hipnose. O Hypnothera lista mais de "
                  "100 vozes e 14 idiomas, o InTheMoment 18 idiomas com o Pro e a opção de editar o roteiro; os dois "
                  "também estão no iPhone e na web."],
                 []],
                ["Compare dois de cada vez",
                 [f"Cada comparação em detalhe: [Onira ou Hypnothera]({vs['vs_hypnothera']}), "
                  f"[Onira ou InTheMoment]({vs['vs_inthemoment']}), [Onira ou Hypnova]({vs['vs_hypnova']})."],
                 []],
            ],
            "faq": [
                ["Qual app de hipnose com IA é realmente grátis?",
                 "Todos têm uma parte grátis, limitada de formas diferentes: créditos no Hypnothera e no Hypnova, duas "
                 "sessões por dia no InTheMoment. O Onira não tem créditos nem limite: um anúncio por sessão "
                 "personalizada, que uma compra única remove."],
                ["Um app de hipnose com IA funciona sem internet?",
                 "O Onira pode escrever e narrar a sessão offline, num celular com cerca de 6 GB de RAM. Os outros "
                 "escrevem a sessão online; alguns depois deixam baixar o áudio com assinatura."],
                ["Esses apps exigem conta?",
                 "Hypnothera, InTheMoment e Hypnova exigem, pelo menos para usar os créditos ou as sessões grátis do "
                 "dia. O Onira não tem conta."],
                ["A hipnose com IA substitui um terapeuta?",
                 "Não. Esses apps são ferramentas de relaxamento e auto-hipnose. Diante de um transtorno de ansiedade, "
                 "uma depressão, uma dor persistente ou um vício, fale com um médico."],
            ],
        }
    return {
        "nav": "KI-Hypnose-Apps im Vergleich",
        "card": "Onira, Hypnothera, InTheMoment und Hypnova: Gratis-Version, Konto, offline, Sprachen.",
        "title": "Die besten KI-Hypnose-Apps 2026 im Vergleich | Onira",
        "desc": "Onira, Hypnothera, InTheMoment und Hypnova im Vergleich: Gratis-Version, Konto, offline, Android, "
                "Sprachen und Preise, auf ihren Websites geprüft.",
        "h1": "KI-Hypnose-Apps im Vergleich (2026)",
        "lede": "Vier Apps schreiben eine Hypnose-Sitzung aus dem, was du ihnen erzählst. Gleich sind sie deshalb noch "
                "lange nicht: Was kostenlos ist, das Konto, wo die Sitzung geschrieben wird und die Sprachen machen den "
                "Unterschied. Diese Seite wird von Onira veröffentlicht; die Angaben zu den anderen Apps stammen von "
                "deren eigenen Websites.",
        "answer": "Wenn du kein Konto, keine Credits und nichts, was dein Handy verlässt, willst, ist Onira die einzige "
                  f"der vier, die die Sitzung auf dem Gerät schreibt, [wenn dein Handy das Modell ausführen kann]({p}). "
                  "Wenn du ein iPhone nutzt oder viele Stimmen und Sprachen willst, bieten Hypnothera und InTheMoment "
                  "mehr, mit Konto und begrenzter Gratis-Version. Hypnova fällt durch seine kostenlose Bibliothek mit "
                  "über 300 fertigen Sitzungen auf.",
        "table": _table(lang, apps, f"Geprüft am {CHECKED[lang]} auf den Websites von Hypnothera, InTheMoment und "
                                    "Hypnova. Die Preise in den Stores variieren je nach Land."),
        "sections": [
            ["Wie wir verglichen haben",
             ["Wir haben die Apps genommen, die eine Sitzung aus deinen eigenen Worten schreiben, nicht die, die nur "
              "Aufnahmen anbieten. Für jede haben wir notiert, was ihre Website angibt: was kostenlos ist und wie lange, "
              "ob du ein Konto brauchst, wo der Text geschrieben wird, was offline funktioniert, Plattformen, Sprachen "
              "und Preise. Wir machen Onira: Lies diese Tabelle mit diesem Wissen und prüfe die Preise, wenn du ein Abo "
              "abschließt, sie ändern sich oft."],
             []],
            ["Wenn dir Privatsphäre am wichtigsten ist",
             ["Hypnothera, InTheMoment und Hypnova schreiben die Sitzung auf ihren Servern; das heißt, was du "
              "beschreibst, wird gesendet, und meist brauchst du ein Konto. Onira schreibt die Sitzung auf dem Handy, "
              "wenn es etwa 6 GB RAM hat: Was du tippst, verlässt es nie, und es funktioniert im Flugmodus. Auf einem "
              "schwächeren Handy übernimmt Onira Cloud, nur mit deiner Zustimmung, ohne Konto und ohne den Text zu "
              "speichern."],
             []],
            ["Wenn du viele kostenlose Sitzungen willst",
             ["Kostenlos heißt nicht überall dasselbe. Hypnothera rechnet in Credits, etwa eine Minute Audio pro Credit, "
              "jede Woche aufgefüllt. InTheMoment erlaubt zwei neue Sitzungen pro Tag. Hypnova bietet eine große "
              "fertige Bibliothek und Credits zum Personalisieren. Onira zählt nichts: Jede persönliche Sitzung kostet "
              "eine Werbung."],
             []],
            ["Wenn du ein iPhone nutzt oder viele Stimmen zur Auswahl willst",
             ["Onira gibt es nur für Android, mit einer Stimme pro Sprache, für Hypnose gemacht. Hypnothera listet über "
              "100 Stimmen und 14 Sprachen, InTheMoment 18 Sprachen mit Pro und die Möglichkeit, das Skript zu "
              "bearbeiten; beide gibt es auch für iPhone und im Web."],
             []],
            ["Zwei im direkten Vergleich",
             [f"Jeder Vergleich im Detail: [Onira oder Hypnothera]({vs['vs_hypnothera']}), "
              f"[Onira oder InTheMoment]({vs['vs_inthemoment']}), [Onira oder Hypnova]({vs['vs_hypnova']})."],
             []],
        ],
        "faq": [
            ["Welche KI-Hypnose-App ist wirklich kostenlos?",
             "Alle haben einen kostenlosen Teil, unterschiedlich begrenzt: Credits bei Hypnothera und Hypnova, zwei "
             "Sitzungen pro Tag bei InTheMoment. Onira hat keine Credits und kein Limit: eine Werbung pro persönlicher "
             "Sitzung, die ein Einmalkauf entfernt."],
            ["Kann eine KI-Hypnose-App ohne Internet funktionieren?",
             "Onira kann die Sitzung offline schreiben und vorlesen, auf einem Handy mit etwa 6 GB RAM. Die anderen "
             "schreiben die Sitzung online; manche lassen dich das Audio danach mit Abo herunterladen."],
            ["Brauchen diese Apps ein Konto?",
             "Hypnothera, InTheMoment und Hypnova schon, zumindest für Credits oder die täglichen Gratis-Sitzungen. "
             "Onira hat kein Konto."],
            ["Ersetzt KI-Hypnose eine Therapie?",
             "Nein. Diese Apps sind Werkzeuge für Entspannung und Selbsthypnose. Bei einer Angststörung, einer "
             "Depression, anhaltenden Schmerzen oder einer Sucht sprich mit einer Ärztin oder einem Arzt."],
        ],
    }


VS_TEXT = {
    "pt": {
        "nav": "Onira ou %s", "title": "Onira ou %s: qual app de hipnose com IA? | Onira",
        "h1": "Onira ou %s: qual escolher?", "caption": "Conferido em %s no site do %s. Página publicada pelo Onira.",
        "onira_if": "Escolha o Onira se…", "rival_if": "Escolha o %s se…", "others": "Os outros apps",
        "others_text": "Hypnothera, InTheMoment e Hypnova lado a lado: [a comparação completa](%s).",
        "vs_hypnothera": dict(
            card="Com ou sem créditos, com ou sem conta: as diferenças, conferidas.",
            desc="Onira ou Hypnothera: plano grátis, conta, uso offline, vozes, idiomas e preços comparados pelo "
                 "site do Hypnothera, para escolher pelo que importa para você.",
            lede="Os dois escrevem uma sessão de hipnose a partir das suas palavras e a leem em voz alta. O "
                 "Hypnothera aposta na escolha (vozes, idiomas, durações, web e iPhone); o Onira, na simplicidade e "
                 "na privacidade, sem conta e sem créditos.",
            answer="Escolha o Onira se você usa Android e quer sessões sem conta e sem créditos, escritas no celular "
                   "[se ele rodar o modelo](@PHONES@). Escolha o Hypnothera se você usa iPhone, quer escolher entre "
                   "mais de 100 vozes e 14 idiomas, ou sessões muito longas, e não se importa com créditos.",
            onira_if=["Você não quer conta, nem e-mail, nem créditos para acompanhar.",
                      "Você quer que o que digita fique no celular, ou usar o app em modo avião.",
                      "Você ouve em um dos cinco idiomas do Onira, no Android."],
            rival_if=["Você usa iPhone ou quer ouvir no navegador.",
                      "Você quer escolher entre muitas vozes, ou um idioma além dos cinco do Onira.",
                      "Você quer sessões muito longas ou editar o roteiro."],
            faq=[["O Hypnothera é grátis?",
                  "Em parte: uma conta grátis recebe 25 créditos, depois mais 15 por semana (cerca de um minuto de "
                  "áudio por crédito), além de sessões rápidas ilimitadas de 30 segundos a 5 minutos, segundo o site "
                  "em 22 de novembro de 2026."],
                 ["Preciso de conta no Onira?", "Não, nem para as sessões personalizadas nem para as prontas."]]),
        "vs_inthemoment": dict(
            card="Duas sessões por dia ou sem limite, online ou no celular: a comparação.",
            desc="Onira ou InTheMoment: sessões grátis, conta, uso offline, idiomas e preços comparados pelo site do "
                 "InTheMoment, para escolher o app que combina com você.",
            lede="Os dois escrevem uma sessão a partir do que você descreve. O InTheMoment mistura meditação e "
                 "hipnose e lembra das suas avaliações; o Onira é todo dedicado à auto-hipnose, sem conta e com uma "
                 "IA que pode rodar no celular.",
            answer="Escolha o Onira se você quer sessões sem conta e sem limite diário, escritas no celular [se ele "
                   "rodar o modelo](@PHONES@). Escolha o InTheMoment se você também quer meditação, editar o roteiro "
                   "ou idiomas além dos cinco do Onira, com conta.",
            onira_if=["Duas sessões por dia não bastam, ou você não quer contar.",
                      "Você não quer criar uma conta.",
                      "Você quer que o que digita fique no celular."],
            rival_if=["Você quer meditação e hipnose no mesmo app.",
                      "Você quer ler e editar o roteiro antes de ouvir (com o Pro).",
                      "Você usa iPhone ou ouve no navegador."],
            faq=[["O InTheMoment é grátis?",
                  "Em parte: o plano grátis permite criar duas sessões novas por dia, de até 20 minutos, guardadas "
                  "por 60 dias, segundo o site em 22 de novembro de 2026."],
                 ["O Onira limita o número de sessões?",
                  "Não. Cada sessão personalizada vem com um anúncio, que uma compra única remove; não há créditos "
                  "nem limite diário."]]),
        "vs_hypnova": dict(
            card="Uma grande biblioteca com créditos, ou sessões escritas sem contar: a comparação.",
            desc="Onira ou Hypnova: biblioteca, créditos, conta, uso offline e preços comparados pelo site do "
                 "Hypnova, para escolher pelo seu jeito de ouvir.",
            lede="O Hypnova oferece mais de 300 sessões prontas e créditos para pedir novas; o Onira escreve cada "
                 "sessão para você, sem créditos e sem conta, com uma IA que pode rodar no celular.",
            answer="Escolha o Hypnova se você gosta de escolher numa grande biblioteca de sessões prontas, no iPhone "
                   "ou no Android. Escolha o Onira se você quer sobretudo sessões escritas para a sua situação, sem "
                   "créditos e sem conta, escritas no celular [se ele rodar o modelo](@PHONES@).",
            onira_if=["Você quer sobretudo sessões personalizadas, sem acompanhar um saldo de créditos.",
                      "Você não quer criar uma conta.",
                      "Você quer que o que digita fique no celular."],
            rival_if=["Você quer uma grande biblioteca de sessões prontas grátis.",
                      "Você usa iPhone ou ouve no navegador.",
                      "Algumas sessões personalizadas por mês bastam para você."],
            faq=[["O Hypnova é grátis?",
                  "As mais de 300 sessões prontas são grátis. As personalizadas usam créditos, contados por minuto de "
                  "áudio: 60 no cadastro, 240 por mês com o Pro, segundo o site em 22 de novembro de 2026."],
                 ["O Onira tem sessões prontas?",
                  "Sim, para cada tema, tocando sem enviar nada; mas a ideia dele é escrever a sessão a partir do que "
                  "você conta."]]),
    },
    "de": {
        "nav": "Onira oder %s", "title": "Onira oder %s: Welche KI-Hypnose-App? | Onira",
        "h1": "Onira oder %s: Welche App passt zu dir?",
        "caption": "Geprüft am %s auf der Website von %s. Seite von Onira veröffentlicht.",
        "onira_if": "Nimm Onira, wenn…", "rival_if": "Nimm %s, wenn…", "others": "Die anderen Apps",
        "others_text": "Hypnothera, InTheMoment und Hypnova nebeneinander: [der vollständige Vergleich](%s).",
        "vs_hypnothera": dict(
            card="Mit oder ohne Credits, mit oder ohne Konto: die Unterschiede, geprüft.",
            desc="Onira oder Hypnothera: Gratis-Version, Konto, offline, Stimmen, Sprachen und Preise, verglichen "
                 "anhand der Hypnothera-Website.",
            lede="Beide schreiben eine Hypnose-Sitzung aus deinen eigenen Worten und lesen sie vor. Hypnothera setzt "
                 "auf Auswahl (Stimmen, Sprachen, Längen, Web und iPhone); Onira auf Einfachheit und Privatsphäre, "
                 "ohne Konto und ohne Credits.",
            answer="Nimm Onira, wenn du Android nutzt und Sitzungen ohne Konto und ohne Credits willst, auf dem Handy "
                   "geschrieben, [wenn es das Modell ausführen kann](@PHONES@). Nimm Hypnothera, wenn du ein iPhone "
                   "nutzt, aus über 100 Stimmen und 14 Sprachen wählen willst oder sehr lange Sitzungen möchtest und "
                   "dich Credits nicht stören.",
            onira_if=["Du willst kein Konto, keine E-Mail-Adresse und keine Credits im Blick behalten.",
                      "Du willst, dass das, was du tippst, auf dem Handy bleibt, oder die App im Flugmodus nutzen.",
                      "Du hörst in einer der fünf Sprachen von Onira, auf Android."],
            rival_if=["Du nutzt ein iPhone oder willst im Browser hören.",
                      "Du willst aus vielen Stimmen wählen oder eine andere Sprache als Oniras fünf.",
                      "Du willst sehr lange Sitzungen oder das Skript selbst bearbeiten."],
            faq=[["Ist Hypnothera kostenlos?",
                  "Teilweise: Ein kostenloses Konto bekommt 25 Credits, dann jede Woche 15 weitere (etwa eine Minute "
                  "Audio pro Credit), dazu unbegrenzte Kurz-Sitzungen von 30 Sekunden bis 5 Minuten, laut Website am "
                  "22. November 2026."],
                 ["Brauche ich für Onira ein Konto?",
                  "Nein, weder für persönliche noch für fertige Sitzungen."]]),
        "vs_inthemoment": dict(
            card="Zwei Sitzungen pro Tag oder kein Limit, online oder auf dem Handy: der Vergleich.",
            desc="Onira oder InTheMoment: kostenlose Sitzungen, Konto, offline, Sprachen und Preise, verglichen "
                 "anhand der InTheMoment-Website.",
            lede="Beide schreiben eine Sitzung aus dem, was du beschreibst. InTheMoment mischt Meditation und Hypnose "
                 "und merkt sich dein Feedback; Onira dreht sich ganz um Selbsthypnose, ohne Konto und mit einer KI, "
                 "die auf dem Handy laufen kann.",
            answer="Nimm Onira, wenn du Sitzungen ohne Konto und ohne Tageslimit willst, auf dem Handy geschrieben, "
                   "[wenn es das Modell ausführen kann](@PHONES@). Nimm InTheMoment, wenn du auch Meditation willst, "
                   "das Skript bearbeiten möchtest oder andere Sprachen als Oniras fünf brauchst, mit Konto.",
            onira_if=["Zwei Sitzungen pro Tag reichen dir nicht, oder du willst nicht zählen.",
                      "Du willst kein Konto anlegen.",
                      "Du willst, dass das, was du tippst, auf dem Handy bleibt."],
            rival_if=["Du willst Meditation und Hypnose in derselben App.",
                      "Du willst das Skript vor dem Hören lesen und bearbeiten (mit Pro).",
                      "Du nutzt ein iPhone oder hörst im Browser."],
            faq=[["Ist InTheMoment kostenlos?",
                  "Teilweise: Mit dem Gratis-Plan kannst du zwei neue Sitzungen pro Tag erstellen, bis zu 20 Minuten "
                  "lang, 60 Tage gespeichert, laut Website am 22. November 2026."],
                 ["Begrenzt Onira die Zahl der Sitzungen?",
                  "Nein. Jede persönliche Sitzung kommt mit einer Werbung, die ein Einmalkauf entfernt; es gibt keine "
                  "Credits und kein Tageslimit."]]),
        "vs_hypnova": dict(
            card="Eine große Bibliothek mit Credits oder Sitzungen ohne Zählen: der Vergleich.",
            desc="Onira oder Hypnova: Bibliothek, Credits, Konto, Offline-Nutzung und Preise, verglichen anhand der "
                 "Hypnova-Website, damit du nach deiner Art zu hören wählst.",
            lede="Hypnova bietet über 300 fertige Sitzungen und Credits, um neue schreiben zu lassen; Onira schreibt "
                 "jede Sitzung für dich, ohne Credits und ohne Konto, mit einer KI, die auf dem Handy laufen kann.",
            answer="Nimm Hypnova, wenn du gern aus einer großen Bibliothek fertiger Sitzungen wählst, auf iPhone oder "
                   "Android. Nimm Onira, wenn du vor allem Sitzungen für deine Situation willst, ohne Credits und ohne "
                   "Konto, auf dem Handy geschrieben, [wenn es das Modell ausführen kann](@PHONES@).",
            onira_if=["Du willst vor allem persönliche Sitzungen, ohne ein Credit-Guthaben im Blick zu behalten.",
                      "Du willst kein Konto anlegen.",
                      "Du willst, dass das, was du tippst, auf dem Handy bleibt."],
            rival_if=["Du willst eine große Bibliothek kostenloser fertiger Sitzungen.",
                      "Du nutzt ein iPhone oder hörst im Browser.",
                      "Ein paar persönliche Sitzungen im Monat reichen dir."],
            faq=[["Ist Hypnova kostenlos?",
                  "Die über 300 fertigen Sitzungen sind kostenlos. Persönliche Sitzungen kosten Credits, pro Minute "
                  "Audio gezählt: 60 bei der Anmeldung, 240 im Monat mit Pro, laut Website am 22. November 2026."],
                 ["Hat Onira fertige Sitzungen?",
                  "Ja, für jedes Thema, und sie laufen, ohne etwas zu senden; aber die Idee ist, die Sitzung aus dem zu "
                  "schreiben, was du erzählst."]]),
    },
}


def _vs(lang, key, rival):
    t = VS_TEXT[lang]
    f = t[key]
    return {
        "nav": t["nav"] % rival, "card": f["card"], "title": t["title"] % rival, "desc": f["desc"],
        "h1": t["h1"] % rival, "lede": f["lede"], "answer": f["answer"].replace("@PHONES@", PHONES[lang]),
        "table": _table(lang, [rival], t["caption"] % (CHECKED[lang], rival)),
        "sections": [[t["onira_if"], [], f["onira_if"]], [t["rival_if"] % rival, [], f["rival_if"]],
                     [t["others"], [t["others_text"] % BEST[lang]], []]],
        "faq": f["faq"],
    }


def units(lang):
    """The draft units of these pages, keyed like translate_site.py's (slugs are set by make_ptde.py)."""
    return {
        "guides.phones": _phones(lang),
        "guides.best_ai_apps": _best(lang),
        "guides.vs_hypnothera": _vs(lang, "vs_hypnothera", "Hypnothera"),
        "guides.vs_inthemoment": _vs(lang, "vs_inthemoment", "InTheMoment"),
        "guides.vs_hypnova": _vs(lang, "vs_hypnova", "Hypnova"),
    }
