# -*- coding: utf-8 -*-
"""Copy for the Onira site, one entry per language.

Adding a language means adding one key here and rerunning `python3 build.py`;
the templates, hreflang alternates and sitemap follow automatically. Keep the
`THEMES` keys identical across languages — the alternate links are matched on
them, not on the slugs.
"""

SITE = {
    "origin": "https://onirahypno.com",
    "play": "https://play.google.com/store/apps/details?id=com.oytaub.mindease",
    "email": "support@onirahypno.com",
    "updated": "2026-08-29",
    # Google Search Console verification token for a "URL prefix" property — the
    # content= value of the google-site-verification meta tag it hands you. Leave
    # empty if the property is verified by DNS TXT record instead (preferred: a
    # domain property covers every subdomain and both schemes, and cannot be lost
    # by a template change).
    "search_console": "",
    # Directory and launch-site badges, rendered in every page footer by
    # build.py. They are reciprocal links: those sites link here, these link
    # back. Intrinsic width/height are the DISPLAYED size, so the footer never
    # reflows as they load (the PeerPush artwork is 680x130 and is shown at
    # half). Remote images by necessity -- PeerPush's badge shows a live
    # rating, and a self-hosted copy would freeze it.
    "badges": [
        {"href": "https://www.producthunt.com/products/onira-self-hypnosis"
                 "?embed=true&utm_source=badge-featured&utm_medium=badge"
                 "&utm_campaign=badge-onira-self-hypnosis",
         "src": "https://api.producthunt.com/widgets/embed-image/v1/featured.svg"
                "?post_id=1244605&theme=light&t=1789720917170",
         "alt": "Onira - Self-Hypnosis on Product Hunt",
         "width": 250, "height": 54},
        {"href": "https://peerpush.com/p/onira",
         "src": "https://peerpush.com/p/onira/rating-badge.png",
         "alt": "Onira rating on PeerPush",
         "width": 340, "height": 65},
        {"href": "https://smolhunt.com/projects/onira-self-hypnosis?utm_source=badge",
         "src": "https://smolhunt.com/smolhunt/images/badges/featured-on-light.svg",
         "alt": "Featured on Smol Hunt",
         "width": 150, "height": 44},
    ],
}

# Order used for nav cards and the sitemap. A theme does not have to exist in
# every language: search demand differs by market, and a page is only worth
# having where people actually look for it. `build.py` derives each theme's
# hreflang set from the languages that publish it.
THEMES = ["anxiety", "sleep", "confidence", "stress", "smoking", "focus", "weight",
          "fear", "letting_go", "learning", "motivation", "habits",
          "pain", "ibs", "emotional_recovery", "mental_reset"]

# ---------------------------------------------------------------- English ----

EN = {
    "code": "en",
    "label": "EN",
    "name": "English",
    "base": "",                 # site root
    "theme_dir": "hypnosis",
    "privacy_slug": "privacy",
    "ui": {
        "home_name": "Onira",
        "home_crumb": "Home",
        "badge_alt": "Get it on Google Play",
        "cta_note": "Free, no account, no subscription. One-time purchase to remove ads.",
        "how_title": "How Onira builds your session",
        "how_steps": [
            "You pick a theme and, if you want, type a sentence or two about what is actually going on.",
            "An AI model running on your phone writes the script — induction, deepening, imagery, suggestions, anchoring, then a clear return to full alertness.",
            "Narration starts as soon as the opening is ready and the rest keeps writing while you listen, so a full 15 to 30 minute session begins in seconds.",
            "Keep a session you liked and replay the exact same narration whenever you want.",
        ],
        "works_title": "What a session works on",
        "expect_title": "What to expect",
        "faq_title": "Common questions",
        "privacy_title": "Private by design",
        "privacy_body": "Onira runs its model on your device. The theme you pick, the words you type "
                        "and the session you receive are never uploaded — there is no account, no "
                        "cloud generation and no server that could read them.",
        "privacy_link": "Read the full privacy policy",
        "safety_title": "Not a medical treatment",
        "safety_body": "Onira is a relaxation and self-hypnosis tool. It is not therapy, not medical "
                       "or psychiatric advice, and not a substitute for professional care or emergency "
                       "services. If you are in distress or in danger, contact a local crisis line or "
                       "emergency number.",
        "related_title": "Other themes",
        "foot_tag": "Onira — hypnotherapy sessions written on your phone, by your phone.",
        "foot_privacy": "Privacy policy",
        "foot_play": "Google Play",
        "head_cta": "Get the app",
        "langs_label": "Language",
        "screens_title": "Inside the app",
        # (asset key, alt text, caption). "privacy" resolves to the localised file.
        "screens": [
            ("home", "Onira's home screen: theme picker and free-text field",
             "Pick a theme, add a detail if you want."),
            ("session", "A session playing, with its phase indicator and breathing background",
             "The session narrates itself while a slow-breathing background plays."),
            ("favorites", "The favourites list of saved sessions",
             "Save a session and replay the same narration."),
            ("privacy", "Nothing you type or receive leaves the phone",
             "No account, nothing transmitted, works offline."),
        ],
    },
    "home": {
        "title": "Onira — Self-Hypnosis Sessions Written for You",
        "desc": "Onira writes a personal hypnosis session on your phone and narrates it aloud — "
                "sleep, anxiety, stress, confidence, focus. Nothing leaves your device.",
        "h1": "Self-hypnosis sessions written for you, on your phone",
        "lede": "Most hypnosis apps hand you the same recording as everyone else. Onira writes a "
                "session for your situation, in the moment, with an AI model that runs entirely on "
                "your device — then narrates it aloud while you close your eyes.",
        "intro": [
            "Guided hypnosis works best when the words match what you are actually carrying. A "
            "recording made for a general audience has to stay vague; a session written around the "
            "sentence you just typed can name the thing keeping you awake, and build the imagery "
            "around it.",
            "That is the whole idea behind Onira. You choose a theme, add as much or as little "
            "detail as you like, and a small open-weight language model on your phone writes a "
            "complete script following the classical arc of a hypnotherapy session.",
        ],
        "themes_title": "Choose a theme",
    },
    "themes": {
        "anxiety": {
            "slug": "anxiety",
            "nav": "Anxiety",
            "card": "Loosen the grip of anxious thinking and settle the body.",
            "title": "Self-Hypnosis for Anxiety — Written for You | Onira",
            "desc": "Guided self-hypnosis for anxiety, written on your phone around what you are "
                    "actually anxious about, and narrated aloud. Private, free, no subscription.",
            "h1": "Self-hypnosis for anxiety",
            "lede": "A guided session that slows the body first, then works on the anxious thought "
                    "itself — written around what you are actually worried about.",
            "why_title": "Why hypnosis helps with anxiety",
            "why": [
                "Anxiety keeps two systems busy at once: a body braced for something, and a mind "
                "rehearsing it. Guided hypnosis addresses the first directly — slow, paced language "
                "and steady breathing shift you out of the alert state — which is what makes the "
                "second easier to loosen.",
                "In that settled state, suggestion lands differently. Instead of arguing with an "
                "anxious thought, a session offers a calmer version of the same scene and lets you "
                "rehearse it, so the next time it comes up it carries less charge.",
            ],
            "works_on": [
                "Physical tension — jaw, shoulders, chest, stomach — released stage by stage.",
                "The loop of anticipating what might go wrong, replaced with a rehearsed calm response.",
                "An anchor you can use later: a breath, a word, or a gesture that recalls the session's state.",
                "A specific worry, if you type one in — an interview, a flight, a conversation you are dreading.",
            ],
            "expect": "Sessions run roughly 15 to 30 minutes. You stay aware throughout — hypnosis is "
                      "focused attention, not sleep or unconsciousness — and the session always closes "
                      "with a deliberate return to full alertness. Most people use headphones, sitting "
                      "or lying somewhere they will not be interrupted.",
            "faq": [
                ("Does self-hypnosis actually work for anxiety?",
                 "Guided relaxation and suggestion are widely used as a self-help tool for everyday "
                 "anxiety and stress, and many people find them calming. Onira is a relaxation tool, "
                 "not a treatment for an anxiety disorder — that is something to discuss with a "
                 "clinician."),
                ("Can I do this at bedtime?",
                 "Yes, though the session ends by bringing you back to alertness. If your goal is to "
                 "fall asleep, the sleep theme is written for that instead."),
                ("Do I have to type anything personal?",
                 "No. The theme alone is enough. If you do type something, it stays on your phone — "
                 "the model runs locally and nothing is uploaded."),
            ],
        },
        "sleep": {
            "slug": "sleep",
            "nav": "Sleep",
            "card": "Wind down a busy mind and let sleep arrive on its own.",
            "title": "Self-Hypnosis for Sleep — A Session Written for You | Onira",
            "desc": "Guided sleep hypnosis written on your phone around what is keeping you awake, "
                    "and narrated aloud. Runs offline, nothing leaves your device.",
            "h1": "Self-hypnosis for sleep",
            "lede": "A slow, low-stimulation session for the moment you are in bed and your mind will "
                    "not stop working.",
            "why_title": "Why hypnosis helps with sleep",
            "why": [
                "Trouble falling asleep is rarely about tiredness. It is usually a mind that is still "
                "running — replaying the day, planning tomorrow, checking whether sleep is coming yet. "
                "A guided session gives that attention somewhere gentle to go, which is exactly the "
                "condition sleep needs.",
                "The pacing does most of the work: sentences get slower and softer, imagery gets less "
                "detailed, and there is nothing to decide or follow closely. Many people stop listening "
                "consciously well before the session ends, which is the intended outcome.",
            ],
            "works_on": [
                "Progressive physical release, from the feet upward, so the body stops holding the day.",
                "The habit of monitoring whether you are asleep yet — replaced with something undemanding to follow.",
                "Repetitive, slowing imagery: descending stairs, drifting water, a long quiet corridor.",
                "A specific reason you are awake, if you type it in — a deadline, a conversation, a 3 a.m. habit.",
            ],
            "expect": "Set the volume low and let the session play. It runs 15 to 30 minutes; there is "
                      "no need to stay awake to the end, and nothing to do if you drift off. If a session "
                      "works well for you, save it and replay the same narration each night.",
            "faq": [
                ("Will it wake me up at the end?",
                 "Sleep sessions are written to fade rather than rouse you. If you want a clear return "
                 "to alertness, use one of the daytime themes instead."),
                ("Can I use it every night?",
                 "Yes. Saved sessions replay identically, and familiarity tends to help — the same "
                 "narration becomes a cue that it is time to sleep."),
                ("Does it need an internet connection?",
                 "Only once, to download the AI model on first run. After that, sessions are generated "
                 "and narrated entirely offline."),
            ],
        },
        "confidence": {
            "slug": "confidence",
            "nav": "Confidence",
            "card": "Rehearse being the version of yourself you already know how to be.",
            "title": "Self-Hypnosis for Confidence and Self-Esteem | Onira",
            "desc": "Guided self-hypnosis for confidence, written on your phone around the situation "
                    "you actually face, and narrated aloud. Private and free.",
            "h1": "Self-hypnosis for confidence",
            "lede": "A session built on rehearsal: seeing yourself handle the thing well, in enough "
                    "detail that it stops feeling hypothetical.",
            "why_title": "Why hypnosis helps with confidence",
            "why": [
                "Confidence is rarely missing in general — it goes missing in specific situations. "
                "Speaking up in a meeting, walking into a room, making a call. Those moments are already "
                "heavily rehearsed, just in the wrong direction: you have imagined them going badly many "
                "times.",
                "A hypnosis session is structured rehearsal in the other direction. In a relaxed, "
                "focused state, you walk through the situation going well — posture, voice, what you say "
                "first — and that version gets some of the vividness the anxious version has been "
                "getting for free.",
            ],
            "works_on": [
                "A specific upcoming situation, if you name it — a presentation, a date, an interview, a difficult conversation.",
                "The physical signature of confidence: breathing, posture, unhurried speech.",
                "Recalling times you already handled something well, so the evidence is yours rather than borrowed.",
                "An anchor to use in the moment itself, when there is no time for a full session.",
            ],
            "expect": "Sessions run 15 to 30 minutes and end with a clear return to full alertness, so "
                      "they work well the morning of, or the evening before. Save the session and replay "
                      "it as the date gets closer.",
            "faq": [
                ("Is this just positive affirmations?",
                 "No. Affirmations assert something; a hypnosis session builds a scene and lets you "
                 "rehearse it in a relaxed state, which most people find lands more easily than "
                 "repeating a claim they do not yet believe."),
                ("How specific should my description be?",
                 "As specific as you like. \"Nervous about Thursday's presentation to twelve people\" "
                 "produces a more useful session than \"more confidence\"."),
                ("Is what I type stored anywhere?",
                 "Only on your phone, and only if you save the session. Nothing is sent to a server."),
            ],
        },
        "stress": {
            "slug": "stress",
            "nav": "Stress",
            "card": "Come down from a demanding day and recover properly.",
            "title": "Self-Hypnosis for Stress Relief — Written for You | Onira",
            "desc": "Guided self-hypnosis for stress, written on your phone around the pressure you "
                    "are actually under, and narrated aloud. Offline and private.",
            "h1": "Self-hypnosis for stress relief",
            "lede": "A session for the end of a demanding day — deliberate physical release first, then "
                    "some distance from what is causing the pressure.",
            "why_title": "Why hypnosis helps with stress",
            "why": [
                "Sustained stress keeps the body ready for action long after the demand has passed. "
                "You notice it as a tight jaw, shallow breathing, a short fuse, difficulty settling — "
                "recovery that never quite happens because nothing signals that the day is over.",
                "A guided session is that signal. Slow narration and staged physical release move you "
                "out of the braced state, and the imagery that follows gives you a vantage point on the "
                "pressure rather than being inside it.",
            ],
            "works_on": [
                "Staged release of held tension — hands, jaw, shoulders, breathing.",
                "Separating what is genuinely urgent from what merely feels urgent right now.",
                "A recovery point in the day, so pressure does not simply accumulate.",
                "A specific source of stress, if you name it — workload, a move, caring for someone, money.",
            ],
            "expect": "Sessions run 15 to 30 minutes and end by bringing you back alert, so they fit "
                      "into a lunch break or the gap between work and the evening as easily as bedtime.",
            "faq": [
                ("How often should I use it?",
                 "As often as it helps. Many people use a short session daily for a stretch, then keep "
                 "one saved for demanding days."),
                ("What is the difference from the anxiety theme?",
                 "Stress sessions focus on recovering from real ongoing pressure; anxiety sessions focus "
                 "on the anticipation loop and the fear itself. Use whichever describes your week."),
                ("Can I listen with headphones on the train?",
                 "You can, but treat it as relaxation rather than a full session — do not use it while "
                 "driving or doing anything that needs your attention."),
            ],
        },
        "smoking": {
            "slug": "quit-smoking",
            "nav": "Quitting smoking",
            "card": "Support a decision you have already made, craving by craving.",
            "title": "Self-Hypnosis to Quit Smoking — Written for You | Onira",
            "desc": "Guided self-hypnosis to support quitting smoking, written on your phone around "
                    "your own triggers and reasons, and narrated aloud. Private and free.",
            "h1": "Self-hypnosis to quit smoking",
            "lede": "A session that works on the moment of the craving — the trigger, the ritual, the "
                    "reason you are quitting — rather than on willpower.",
            "why_title": "Why hypnosis is used for quitting smoking",
            "why": [
                "Smoking is held in place by more than nicotine: the coffee, the walk outside, the "
                "phone call, the moment after a meal. Each of those is a learned cue, and cues respond "
                "to rehearsal — which is what a hypnosis session provides.",
                "Sessions work on two fronts. They rehearse the cue arriving and passing without the "
                "cigarette, and they keep your own reason for quitting vivid, so the decision does not "
                "have to be remade under pressure every time.",
            ],
            "works_on": [
                "Your specific triggers, if you name them — the morning coffee, the drive, stress at work.",
                "Riding out a craving as a wave that peaks and passes, instead of a demand to be met.",
                "Your reason for quitting, in your own terms — health, money, children, breath, control.",
                "The identity shift from \"trying to quit\" to someone who does not smoke.",
            ],
            "expect": "Sessions run 15 to 30 minutes and end fully alert. Many people listen daily "
                      "through the first weeks — the period when cues fire hardest — and keep a saved "
                      "session for difficult days afterwards.",
            "faq": [
                ("Will one session make me stop smoking?",
                 "No. Onira supports a decision you have already made; it is not a cure and makes no "
                 "clinical claim. Nicotine replacement, prescribed medication and cessation services "
                 "are worth discussing with a doctor or pharmacist."),
                ("When should I listen?",
                 "Ideally before the times of day your cravings are strongest, and again whenever a "
                 "difficult day is coming."),
                ("Does it work for vaping too?",
                 "The same structure applies — type in what you actually want to stop and the session "
                 "is written around that."),
            ],
        },
        "focus": {
            "slug": "focus",
            "nav": "Focus",
            "card": "Settle a scattered mind before work that needs your attention.",
            "title": "Self-Hypnosis for Focus and Concentration | Onira",
            "desc": "Guided self-hypnosis for focus, written on your phone around the work you are "
                    "about to do, and narrated aloud. Runs offline, nothing is uploaded.",
            "h1": "Self-hypnosis for focus",
            "lede": "A shorter, brighter session to clear the noise before study, writing, or work that "
                    "needs sustained attention.",
            "why_title": "Why hypnosis helps with focus",
            "why": [
                "Losing focus is usually not a shortage of attention but a surplus of competing claims "
                "on it — notifications, half-finished tasks, the low hum of everything else you should "
                "be doing. Attention is already trained on something; it is just not the thing in front "
                "of you.",
                "Hypnosis is, at its simplest, sustained focused attention. A session narrows the field "
                "deliberately, sets aside what is not for now, and rehearses starting — which is "
                "usually the hardest part of a long stretch of work.",
            ],
            "works_on": [
                "Narrowing attention to one task and setting the rest down for a defined period.",
                "The friction of starting, rehearsed until the first minute is unremarkable.",
                "Returning to the task after an interruption without losing the thread.",
                "A specific piece of work, if you name it — an exam, a chapter, a build, a deadline.",
            ],
            "expect": "Use a focus session immediately before the work itself. It ends clearly alert "
                      "and forward-leaning rather than sleepy, so you can move straight into the task.",
            "faq": [
                ("Should I listen while working?",
                 "No — listen first, then work. The session asks for your attention; the task needs it "
                 "afterwards."),
                ("Is this useful for studying?",
                 "That is one of the most common uses. Naming the subject and the exam date makes the "
                 "session noticeably more specific."),
                ("Can I make it shorter?",
                 "Sessions target roughly 15 to 30 minutes. You can stop at any point — nothing breaks "
                 "if you end early."),
            ],
        },
        "weight": {
            "slug": "weight-loss",
            "nav": "Weight",
            "card": "Work on habits and the relationship with food, not on rules.",
            "title": "Self-Hypnosis for Weight Loss and Eating Habits | Onira",
            "desc": "Guided self-hypnosis for weight and eating habits, written on your phone around "
                    "your own patterns, and narrated aloud. Private, free, no subscription.",
            "h1": "Self-hypnosis for weight and eating habits",
            "lede": "A session about the moments around eating — the evening, the boredom, the reward — "
                    "rather than about what you are allowed to eat.",
            "why_title": "Why hypnosis is used for eating habits",
            "why": [
                "Most eating that people want to change is not driven by hunger. It is a habit attached "
                "to a moment: the hour after dinner, the drive home, the end of a hard day, something to "
                "do with your hands. Rules do not touch that, because the moment arrives before any "
                "decision does.",
                "A hypnosis session rehearses those moments differently — noticing the cue, letting it "
                "pass, and building a calmer relationship with eating in general. The emphasis is on "
                "how you eat and why, not on restriction.",
            ],
            "works_on": [
                "The specific moment your habit fires, if you name it — evenings, stress, boredom, celebration.",
                "Eating slowly and noticing fullness rather than finishing automatically.",
                "Separating appetite from comfort-seeking, without treating either as a failure.",
                "A steadier internal tone, since self-criticism tends to feed the cycle rather than break it.",
            ],
            "expect": "Sessions run 15 to 30 minutes and end fully alert. Listening at a consistent time "
                      "— many people choose late afternoon, before the hardest hours — tends to work "
                      "better than listening only after a difficult day.",
            "faq": [
                ("Is this a diet?",
                 "No. Onira gives no dietary, nutritional or medical advice and sets no rules about "
                 "food. It works on habits and the relationship with eating."),
                ("Will it make me lose weight?",
                 "It makes no such claim. Weight is a medical topic; a doctor or dietitian is the right "
                 "place for a plan."),
                ("What if I have a history of disordered eating?",
                 "Please speak to a clinician rather than using a self-help tool. Onira is not designed "
                 "for eating disorders and will redirect content that heads that way."),
            ],
        },
        "fear": {
            "slug": "fear-and-phobias",
            "nav": "Fear",
            "card": "Face the flight, the drive or the height with a rehearsed calm.",
            "title": "Self-Hypnosis for Fear and Phobias | Onira",
            "desc": "Guided self-hypnosis for fear of flying, driving or heights, written on your "
                    "phone around the situation you actually face. Private, free, offline.",
            "h1": "Self-hypnosis for fear and phobias",
            "lede": "A session built around one specific situation — the flight, the lift, the "
                    "motorway — rehearsed slowly enough that your body stops treating it as an "
                    "emergency.",
            "why_title": "Why hypnosis helps with a specific fear",
            "why": [
                "A fear is rarely argued away. The reaction arrives before the reasoning does: the "
                "chest tightens, the attention narrows, and the situation is over before any "
                "sensible thought gets a turn. Guided hypnosis works on the part that moves first "
                "— slow, paced language settles the body, and a settled body reacts differently to "
                "the same trigger.",
                "From there the session rehearses the scene rather than avoiding it. You walk "
                "through the boarding gate, the roundabout, the glass lift, at a pace you can stay "
                "calm through. Repeated rehearsal is what makes the real thing feel familiar "
                "instead of sudden.",
            ],
            "works_on": [
                "The physical spike — breath, chest, hands — slowed deliberately before the scene begins.",
                "Avoidance itself: the situation gets smaller every time it is faced calmly in rehearsal.",
                "An anchor to use in the moment: a breath, a word, a gesture that recalls the session.",
                "Your own situation, if you type it in — a flight next month, a driving test, a tunnel.",
            ],
            "expect": "Sessions run roughly 15 to 30 minutes. You stay aware throughout, and the "
                      "session always closes by bringing you back to full alertness — so it can be "
                      "used the morning of the flight, not only the night before. Most people "
                      "listen with headphones somewhere they will not be interrupted.",
            "faq": [
                ("Can self-hypnosis cure a phobia?",
                 "No. Guided relaxation and mental rehearsal are a self-help tool, and many people "
                 "find them useful for an everyday fear. A phobia that limits your life is treated "
                 "by a clinician — often very effectively — and that is the conversation to have."),
                ("Should I listen during the flight itself?",
                 "You can, and many people do. The session ends by returning you to full alertness, "
                 "so it is safe before or during — but never while driving, even a session about "
                 "driving."),
                ("Do I have to describe what scares me?",
                 "No, the theme alone works. If you do describe it, the detail makes the rehearsal "
                 "sharper — and it stays on your phone, because the model runs locally."),
            ],
        },
        "learning": {
            "slug": "memory-and-learning",
            "nav": "Memory",
            "card": "Settle into the state where studying actually sticks.",
            "title": "Self-Hypnosis for Memory and Learning | Onira",
            "desc": "Guided self-hypnosis for studying, recall and language learning, written on "
                    "your phone around what you are learning. Free, private, works offline.",
            "h1": "Self-hypnosis for memory and learning",
            "lede": "A session for the state learning needs — unhurried, undistracted attention — "
                    "written around the exam, the language or the material in front of you.",
            "why_title": "Why hypnosis helps with studying",
            "why": [
                "Most study problems are not memory problems. They are state problems: half your "
                "attention is on the deadline, the phone, or how badly it is going. What gets "
                "encoded in that state is thin, which is why an hour of anxious revision can leave "
                "almost nothing behind.",
                "A guided session lowers the noise first, then puts the material into the quiet it "
                "leaves. Recall is rehearsed the way it will actually be needed — the word arriving "
                "in conversation, the answer arriving in the exam room — so the practice matches "
                "the moment.",
            ],
            "works_on": [
                "The restlessness that makes a study session collapse into ten minutes of scrolling.",
                "Exam-day recall: rehearsing retrieval under calm conditions rather than only rereading.",
                "Language learning — hearing yourself speak it without the self-consciousness.",
                "A specific subject, if you type one in: an exam date, a vocabulary set, a viva.",
            ],
            "expect": "Sessions run roughly 15 to 30 minutes and close by bringing you back to "
                      "full alertness — they are meant to be used before studying, not instead of "
                      "it. A session recorded once can be replayed before every revision block.",
            "faq": [
                ("Will this let me learn while I sleep?",
                 "No. Sleep-learning is not something hypnosis delivers, and Onira does not claim "
                 "it. What a session can do is get you into a state where deliberate study works "
                 "better — the studying still has to happen."),
                ("Can it help me remember something I have forgotten?",
                 "It can help with ordinary recall — a name, a list, where something was left. "
                 "Hypnosis is not a reliable way to recover distant or distressing memories, and "
                 "Onira is not written for that."),
                ("Is it useful for language learning specifically?",
                 "Yes — mainly for the confidence half. Sessions rehearse speaking without "
                 "hesitation, which is usually what blocks a language you already partly know."),
            ],
        },
        "motivation": {
            "slug": "motivation-and-energy",
            "nav": "Motivation",
            "card": "Start the thing you have been circling for a week.",
            "title": "Self-Hypnosis for Motivation and Energy | Onira",
            "desc": "Guided self-hypnosis for procrastination, low energy and getting started, "
                    "written on your phone around the task you are avoiding. Free and private.",
            "h1": "Self-hypnosis for motivation and energy",
            "lede": "A session about starting — the ten minutes before the task, where motivation "
                    "is actually won or lost — written around the thing you keep putting off.",
            "why_title": "Why hypnosis helps with procrastination",
            "why": [
                "Procrastination is rarely laziness. It is usually avoidance of a feeling attached "
                "to the task — it will be boring, it will expose that you are behind, it will not "
                "be good enough. The task gets postponed because the feeling does, and the feeling "
                "grows every hour it waits.",
                "A session addresses the feeling rather than lecturing you about the task. In a "
                "settled state, starting is rehearsed in detail: sitting down, opening the file, "
                "the first small action. Having rehearsed the start, the start is what stops "
                "being the hard part.",
            ],
            "works_on": [
                "The stall before beginning — rehearsed as a sequence you have already been through.",
                "Flat, heavy energy in the afternoon, addressed as tension rather than as a lack of will.",
                "The all-or-nothing story that a task must be done perfectly or not begun at all.",
                "One specific task, if you type it in: the tax return, the gym, the message you owe.",
            ],
            "expect": "Sessions run roughly 15 to 30 minutes and end by bringing you back to full "
                      "alertness, deliberately — this is a theme to use before the task, not at "
                      "bedtime. Many people record one and replay it as a start-of-day ritual.",
            "faq": [
                ("Will one session make me productive?",
                 "No, and any tool promising that is overselling. What a session reliably does is "
                 "lower the resistance to starting once; doing that repeatedly is what changes a "
                 "habit."),
                ("Is low energy something hypnosis can fix?",
                 "Relaxation can help with energy that is really tension or poor sleep. Persistent "
                 "exhaustion is a medical question first — worth raising with a doctor rather than "
                 "an app."),
                ("Can I use it for exercise motivation?",
                 "Yes. Rehearsing the start — putting the shoes on, leaving the flat — works better "
                 "than rehearsing the workout itself, and that is how the session is written."),
            ],
        },
        "habits": {
            "slug": "nervous-habits",
            "nav": "Nervous habits",
            "card": "Interrupt nail biting or jaw clenching before it runs.",
            "title": "Self-Hypnosis for Nervous Habits | Onira",
            "desc": "Guided self-hypnosis for nail biting, teeth grinding and jaw clenching, "
                    "written on your phone around your own trigger. Private, free, offline.",
            "h1": "Self-hypnosis for nervous habits",
            "lede": "A session for the habits that run without you — biting, clenching, picking — "
                    "aimed at the moment just before they start.",
            "why_title": "Why hypnosis helps with a nervous habit",
            "why": [
                "These habits are not decisions. By the time you notice, the hand is already at "
                "your mouth and the jaw has already been tight for an hour. Willpower arrives too "
                "late to be the tool, which is why deciding to stop so rarely works on its own.",
                "What a session works on is the gap before the habit — the tension that precedes "
                "it and the cue that sets it off. Rehearsing a different response to the same cue, "
                "in a relaxed state, is how the automatic part gets something else to do.",
            ],
            "works_on": [
                "The build-up: shoulders, jaw and hands released before the habit has a reason to start.",
                "Cue awareness — noticing the moment of reaching, which is the only moment you can act in.",
                "A replacement action rehearsed until it is as automatic as the one it replaces.",
                "Your own trigger, if you type it in: meetings, driving, screens, a particular time of day.",
            ],
            "expect": "Sessions run roughly 15 to 30 minutes and close by returning you to full "
                      "alertness. Habits respond to repetition rather than intensity, so a "
                      "recorded session replayed daily does more than an occasional long one.",
            "faq": [
                ("Does this work for teeth grinding at night?",
                 "It can help with the daytime clenching that feeds it. Night grinding is a dental "
                 "matter — worn enamel and jaw pain need a dentist, and a guard often does more "
                 "than any relaxation session."),
                ("How long before a habit changes?",
                 "Longer than one session. These are automatic patterns built over years, and the "
                 "realistic expectation is gradual reduction with daily use, not a switch."),
                ("Is skin picking or hair pulling the same thing?",
                 "They can be more than a nervous habit, and when they cause real distress or "
                 "damage they are worth taking to a clinician. Onira is a relaxation tool, not a "
                 "treatment for them."),
            ],
        },
        "pain": {
            "slug": "pain",
            "nav": "Pain",
            "card": "Ease the bracing and the dread that make pain louder.",
            "title": "Self-Hypnosis for Pain — Written for You | Onira",
            "desc": "Guided self-hypnosis alongside your treatment: less bracing, less dread of the "
                    "next flare, easier nights. A comfort tool, not a cure. Offline and private.",
            "h1": "Self-hypnosis for living with pain",
            "lede": "A session for the parts of pain that are not the injury itself — the bracing, the "
                    "dread of the next flare, and the nights it takes from you.",
            "why_title": "What hypnosis can and cannot do about pain",
            "why": [
                "Pain is never only a signal from the body. How much of your attention it holds, how "
                "tightly you brace around it, how much you dread the next episode — all of that changes "
                "how loud it gets. Those are the parts a guided session can reach, and they are often "
                "the difference between a difficult day and an impossible one.",
                "What it does not do is remove the cause. This theme is written as a companion to your "
                "treatment, never a replacement for it, and it is not a reason to skip an appointment "
                "or change what you have been prescribed. Pain that is new, worsening or unexplained "
                "belongs with a doctor first.",
            ],
            "works_on": [
                "The guarding and muscle tension that build up around a painful area.",
                "Falling asleep when pain keeps pulling your attention back.",
                "The anticipation of the next flare, which tightens everything before it arrives.",
                "Where pain sits in the day — at the edge of your attention rather than the centre of it.",
            ],
            "expect": "Sessions run 15 to 30 minutes and end by bringing you back alert. What people "
                      "describe is usually partial and temporary — turning the volume down rather than "
                      "off — and it tends to come with repetition rather than from one session.",
            "faq": [
                ("Can hypnosis cure my pain?",
                 "No, and anything that tells you otherwise is selling something. Relaxation and "
                 "suggestion are widely used alongside medical care to make pain easier to live with. "
                 "Onira is a relaxation tool in that sense — a complement, not a treatment."),
                ("Will I still feel the pain?",
                 "Most likely yes. The realistic aim is that it takes up less of you: less tension "
                 "around it, less dread before it, more room for the rest of the day."),
                ("Is it safe with my medication?",
                 "A session does not interact with anything you take. What matters is that you never "
                 "reduce or stop a prescribed treatment because a session helped — that decision "
                 "belongs to whoever prescribed it."),
                ("What about migraine?",
                 "The tension and anticipation around an attack are reachable; the attack itself is a "
                 "neurological event and a medical matter. Do not use a session as a substitute for "
                 "treatment that works for you."),
            ],
        },
        "ibs": {
            "slug": "ibs",
            "nav": "IBS",
            "card": "Calm the gut-brain loop that keeps flare-ups going.",
            "title": "Self-Hypnosis for IBS — Written for You | Onira",
            "desc": "Guided self-hypnosis for the stress side of IBS: calmer gut, less anticipation, "
                    "easier days. A relaxation tool alongside your care, not a treatment.",
            "h1": "Self-hypnosis for IBS",
            "lede": "A session for the loop where stress worsens symptoms and symptoms feed stress — the "
                    "part of IBS that responds to calm.",
            "why_title": "Why relaxation reaches the gut",
            "why": [
                "The gut and the nervous system are in constant conversation, which is why a stressful "
                "week shows up in your digestion and why the fear of a flare-up in the wrong place can "
                "bring one on. Guided relaxation works on that axis directly: it lowers the alert state "
                "that keeps the loop running.",
                "Worth being precise, because the distinction matters: gut-directed hypnotherapy is an "
                "established option in IBS care, recommended in clinical guidance when other approaches "
                "have not worked — but it is a structured course delivered by a trained therapist. "
                "Onira is not that course. It is a relaxation tool that works on the same stress axis, "
                "and it sits alongside your care rather than replacing it.",
            ],
            "works_on": [
                "The anticipation — planning a day around where the toilets are, and what that costs you.",
                "Abdominal tension and shallow, held breathing during a flare.",
                "Sleep, which suffers in both directions when symptoms are active.",
                "A specific situation, if you name it: a long journey, a restaurant, a day at the office.",
            ],
            "expect": "Sessions run 15 to 30 minutes. Digestive symptoms respond slowly, so judge this "
                      "over weeks of regular use rather than by how one session went.",
            "faq": [
                ("Is this the same as gut-directed hypnotherapy?",
                 "No. That is a structured programme with a trained therapist, usually several sessions "
                 "over a couple of months. Onira writes relaxation sessions around what you describe. "
                 "If you want the clinical protocol, ask your doctor for a referral."),
                ("Should I get diagnosed first?",
                 "Yes. Digestive symptoms have many causes and some need investigating — bleeding, "
                 "unexplained weight loss and a change in your normal pattern all need a doctor, not "
                 "an app."),
                ("Can I use it during a flare-up?",
                 "You can, and many people do. Sit or lie somewhere you will not be interrupted, and "
                 "treat it as easing the tension around the episode rather than stopping it."),
            ],
        },
        "emotional_recovery": {
            "slug": "emotional-recovery",
            "nav": "Emotional recovery",
            "card": "Settle after something hard, without reliving it.",
            "title": "Self-Hypnosis for Emotional Recovery | Onira",
            "desc": "Guided self-hypnosis for the aftermath of a hard time: calmer nights, less "
                    "rumination, steadier days. A relaxation tool, not trauma therapy.",
            "h1": "Self-hypnosis for emotional recovery",
            "lede": "A session for the aftermath — when the hard thing has passed but your sleep, your "
                    "nerves and your attention have not caught up yet.",
            "why_title": "Calming the aftermath, not reopening it",
            "why": [
                "After something difficult, the body often stays braced long after the event is over. "
                "It shows up as broken sleep, a short fuse, thoughts that circle back at night, a "
                "startle response that has not settled. Those are ordinary aftershocks, and they "
                "respond well to deliberate calm.",
                "These sessions are written to settle that state, not to go back into what caused it. "
                "They will not ask you to revisit a memory or describe what happened. That kind of "
                "work is real, it helps, and it is done with a trained professional who can stay with "
                "you through it — not alone with a phone.",
            ],
            "works_on": [
                "Sleep that broke after a difficult period and has not come back.",
                "Rumination at night — the same scene replaying without resolution.",
                "A body that stays on alert: tight chest, clenched jaw, jumping at small things.",
                "Getting through ordinary days while something heavy is still settling.",
            ],
            "expect": "Sessions run 15 to 30 minutes and always end by bringing you fully alert. If a "
                      "session ever leaves you more distressed rather than calmer, stop using it and "
                      "talk to someone qualified.",
            "faq": [
                ("Can this treat trauma or PTSD?",
                 "No, and it is not written to try. Flashbacks, nightmares, dissociation or avoidance "
                 "that shapes your life are treatable — by a clinician trained in trauma. Onira is a "
                 "relaxation tool for the aftermath, used alongside that kind of help if you have it."),
                ("Will a session make me remember things?",
                 "It is not designed to, and it will not ask you to go looking. Hypnosis is also not a "
                 "reliable way to recover memories — a well-known finding, and one reason this theme "
                 "stays on calming the present rather than digging into the past."),
                ("What if I start feeling worse during a session?",
                 "End it, open your eyes, and come back to the room. That reaction is a signal to work "
                 "with a person rather than an app, and it is worth taking seriously rather than "
                 "pushing through."),
                ("Is grief the same thing?",
                 "Close enough that the theme suits it. Sessions can steady the days and the nights; "
                 "they will not shorten grief, and they are not meant to."),
            ],
        },
    },
}

# ----------------------------------------------------------------- French ----

FR = {
    "code": "fr",
    "label": "FR",
    "name": "Français",
    "base": "fr",
    "theme_dir": "hypnose",
    "privacy_slug": "confidentialite",
    "ui": {
        "home_name": "Onira",
        "home_crumb": "Accueil",
        "badge_alt": "Disponible sur Google Play",
        "cta_note": "Gratuit, sans compte, sans abonnement. Achat unique pour retirer les publicités.",
        "how_title": "Comment Onira compose votre séance",
        "how_steps": [
            "Vous choisissez un thème et, si vous le souhaitez, vous écrivez une phrase ou deux sur ce qui se passe vraiment.",
            "Un modèle d'IA embarqué dans votre téléphone rédige le script — induction, approfondissement, images, suggestions, ancrage, puis un retour net à l'état de veille.",
            "La narration démarre dès que l'ouverture est prête et la suite continue de s'écrire pendant que vous écoutez : une séance complète de 15 à 30 minutes commence en quelques secondes.",
            "Gardez une séance que vous avez aimée et rejouez la même narration quand vous voulez.",
        ],
        "works_title": "Ce que la séance travaille",
        "expect_title": "À quoi s'attendre",
        "faq_title": "Questions fréquentes",
        "privacy_title": "Confidentiel par conception",
        "privacy_body": "Onira exécute son modèle sur votre appareil. Le thème choisi, les mots que vous "
                        "écrivez et la séance obtenue ne sont jamais envoyés — aucun compte, aucune "
                        "génération dans le cloud, aucun serveur susceptible de les lire.",
        "privacy_link": "Lire la politique de confidentialité",
        "safety_title": "Ce n'est pas un traitement médical",
        "safety_body": "Onira est un outil de relaxation et d'auto-hypnose. Ce n'est ni une thérapie, ni "
                       "un avis médical ou psychiatrique, ni un substitut à un suivi professionnel ou aux "
                       "services d'urgence. En cas de détresse ou de danger, contactez une ligne d'écoute "
                       "ou le numéro d'urgence local (en France, le 3114 pour la prévention du suicide).",
        "related_title": "Autres thèmes",
        "foot_tag": "Onira — des séances d'hypnose écrites sur votre téléphone, par votre téléphone.",
        "foot_privacy": "Confidentialité",
        "foot_play": "Google Play",
        "head_cta": "Obtenir l'app",
        "langs_label": "Langue",
        "screens_title": "Dans l'application",
        "screens": [
            ("home", "L'accueil d'Onira : choix du thème et champ de texte libre",
             "Choisissez un thème, ajoutez un détail si vous voulez."),
            ("session", "Une séance en cours, avec l'indicateur de phase et le fond respirant",
             "La séance se narre pendant qu'un fond respire lentement."),
            ("favorites", "La liste des séances enregistrées",
             "Enregistrez une séance et rejouez la même narration."),
            ("privacy", "Rien de ce que vous écrivez ou recevez ne quitte le téléphone",
             "Aucun compte, aucune donnée transmise, fonctionne hors ligne."),
        ],
    },
    "home": {
        "title": "Onira — Séances d'auto-hypnose écrites pour vous",
        "desc": "Onira écrit une séance d'hypnose personnelle sur votre téléphone et la narre à voix "
                "haute : sommeil, anxiété, stress, confiance. Rien ne sort de l'appareil.",
        "h1": "Des séances d'auto-hypnose écrites pour vous, sur votre téléphone",
        "lede": "La plupart des applications d'hypnose vous donnent le même enregistrement qu'à tout le "
                "monde. Onira écrit une séance pour votre situation, sur le moment, avec un modèle d'IA "
                "qui tourne entièrement sur votre appareil — puis vous la narre pendant que vous fermez "
                "les yeux.",
        "intro": [
            "L'hypnose guidée fonctionne mieux quand les mots correspondent à ce que vous portez "
            "réellement. Un enregistrement destiné à tout le monde doit rester vague ; une séance écrite "
            "à partir de la phrase que vous venez de taper peut nommer ce qui vous empêche de dormir et "
            "construire les images autour.",
            "C'est toute l'idée d'Onira. Vous choisissez un thème, ajoutez autant de détails que vous "
            "voulez, et un petit modèle de langage à poids ouverts, sur votre téléphone, rédige un "
            "script complet suivant l'arc classique d'une séance d'hypnothérapie.",
        ],
        "themes_title": "Choisissez un thème",
    },
    "themes": {
        "anxiety": {
            "slug": "anxiete",
            "nav": "Anxiété",
            "card": "Desserrer l'étau des pensées anxieuses et apaiser le corps.",
            "title": "Auto-hypnose pour l'anxiété — écrite pour vous | Onira",
            "desc": "Auto-hypnose guidée contre l'anxiété, écrite sur votre téléphone à partir de ce qui "
                    "vous inquiète vraiment, et narrée à voix haute. Privée et gratuite.",
            "h1": "Auto-hypnose pour l'anxiété",
            "lede": "Une séance guidée qui ralentit d'abord le corps, puis travaille la pensée anxieuse "
                    "elle-même — écrite autour de ce qui vous inquiète réellement.",
            "why_title": "Pourquoi l'hypnose aide face à l'anxiété",
            "why": [
                "L'anxiété occupe deux systèmes à la fois : un corps en alerte et un esprit qui répète "
                "le scénario. L'hypnose guidée s'adresse directement au premier — un rythme lent, une "
                "voix posée, une respiration régulière font redescendre l'état d'alerte — et c'est "
                "précisément ce qui rend le second plus facile à relâcher.",
                "Dans cet état apaisé, la suggestion agit autrement. Plutôt que de discuter avec une "
                "pensée anxieuse, la séance propose une version plus calme de la même scène et vous la "
                "fait répéter, pour qu'elle revienne avec moins de charge.",
            ],
            "works_on": [
                "Les tensions physiques — mâchoire, épaules, poitrine, ventre — relâchées étape par étape.",
                "La boucle d'anticipation du pire, remplacée par une réaction calme déjà répétée.",
                "Un ancrage réutilisable ensuite : une respiration, un mot, un geste qui rappelle l'état de la séance.",
                "Une inquiétude précise, si vous l'écrivez : un entretien, un vol, une conversation redoutée.",
            ],
            "expect": "Les séances durent environ 15 à 30 minutes. Vous restez conscient du début à la "
                      "fin — l'hypnose est une attention focalisée, pas un sommeil ni une perte de "
                      "contrôle — et la séance se termine toujours par un retour net à l'état de veille. "
                      "Un casque, assis ou allongé, dans un endroit sans interruption.",
            "faq": [
                ("L'auto-hypnose fonctionne-t-elle vraiment contre l'anxiété ?",
                 "La relaxation guidée et la suggestion sont couramment utilisées comme outil d'aide "
                 "personnelle face à l'anxiété et au stress du quotidien, et beaucoup de personnes les "
                 "trouvent apaisantes. Onira est un outil de relaxation, pas un traitement d'un trouble "
                 "anxieux : cela se discute avec un professionnel de santé."),
                ("Puis-je l'écouter au coucher ?",
                 "Oui, mais la séance se termine par un retour à la vigilance. Si votre objectif est de "
                 "vous endormir, le thème sommeil est écrit pour cela."),
                ("Dois-je écrire quelque chose de personnel ?",
                 "Non, le thème suffit. Et si vous écrivez quelque chose, cela reste sur votre "
                 "téléphone : le modèle tourne en local, rien n'est envoyé."),
            ],
        },
        "sleep": {
            "slug": "sommeil",
            "nav": "Sommeil",
            "card": "Calmer un esprit trop actif et laisser le sommeil venir.",
            "title": "Auto-hypnose pour le sommeil — écrite pour vous | Onira",
            "desc": "Hypnose guidée pour dormir, écrite sur votre téléphone à partir de ce qui vous tient "
                    "éveillé, et narrée à voix haute. Fonctionne entièrement hors ligne.",
            "h1": "Auto-hypnose pour le sommeil",
            "lede": "Une séance lente et peu stimulante, pour le moment où vous êtes au lit et où votre "
                    "esprit refuse de s'arrêter.",
            "why_title": "Pourquoi l'hypnose aide à s'endormir",
            "why": [
                "La difficulté à s'endormir tient rarement à un manque de fatigue. C'est le plus souvent "
                "un esprit encore en marche : la journée qui repasse, le lendemain qui se prépare, la "
                "vérification permanente de savoir si le sommeil arrive. Une séance guidée donne à cette "
                "attention un endroit doux où se poser — exactement ce dont le sommeil a besoin.",
                "Le rythme fait l'essentiel du travail : les phrases ralentissent, les images se "
                "simplifient, il n'y a rien à décider ni à suivre de près. Beaucoup de personnes cessent "
                "d'écouter consciemment bien avant la fin — c'est le résultat recherché.",
            ],
            "works_on": [
                "Un relâchement progressif du corps, des pieds vers le haut, pour déposer la journée.",
                "L'habitude de surveiller si l'on dort enfin, remplacée par quelque chose de facile à suivre.",
                "Des images répétitives et ralentissantes : un escalier qui descend, l'eau, un long couloir calme.",
                "Une raison précise de ne pas dormir, si vous l'écrivez : une échéance, une discussion, un réveil à 3 h.",
            ],
            "expect": "Réglez le volume bas et laissez la séance se dérouler. Elle dure 15 à 30 minutes ; "
                      "inutile de tenir jusqu'au bout, et rien à faire si vous vous endormez. Si une "
                      "séance vous convient, enregistrez-la et rejouez la même chaque soir.",
            "faq": [
                ("Est-ce que la fin va me réveiller ?",
                 "Les séances de sommeil sont écrites pour s'estomper, pas pour vous ramener à la "
                 "vigilance. Pour un réveil net, utilisez plutôt un thème de journée."),
                ("Puis-je l'utiliser tous les soirs ?",
                 "Oui. Les séances enregistrées se rejouent à l'identique, et l'habitude aide : la même "
                 "narration devient un signal d'endormissement."),
                ("Faut-il une connexion internet ?",
                 "Une seule fois, pour télécharger le modèle au premier lancement. Ensuite, tout est "
                 "généré et narré hors ligne."),
            ],
        },
        "confidence": {
            "slug": "confiance-en-soi",
            "nav": "Confiance en soi",
            "card": "Répéter la version de vous-même que vous savez déjà être.",
            "title": "Auto-hypnose pour la confiance en soi | Onira",
            "desc": "Auto-hypnose guidée pour la confiance en soi, écrite sur votre téléphone à partir de "
                    "la situation que vous affrontez, et narrée à voix haute. Gratuite.",
            "h1": "Auto-hypnose pour la confiance en soi",
            "lede": "Une séance fondée sur la répétition mentale : vous voir gérer la situation, avec "
                    "assez de détails pour que cela cesse d'être hypothétique.",
            "why_title": "Pourquoi l'hypnose aide la confiance en soi",
            "why": [
                "La confiance manque rarement en général : elle manque dans des situations précises. "
                "Prendre la parole en réunion, entrer dans une pièce, passer un appel. Ces moments sont "
                "déjà énormément répétés, mais dans le mauvais sens — vous les avez imaginés mal se "
                "passer un grand nombre de fois.",
                "Une séance d'hypnose est une répétition structurée dans l'autre sens. Dans un état "
                "détendu et focalisé, vous traversez la situation qui se passe bien — la posture, la "
                "voix, la première phrase — et cette version gagne un peu de la netteté que la version "
                "anxieuse obtenait gratuitement.",
            ],
            "works_on": [
                "Une situation précise à venir, si vous la nommez : une présentation, un rendez-vous, un entretien, une conversation difficile.",
                "La signature physique de l'assurance : la respiration, la posture, un débit sans précipitation.",
                "Le rappel de fois où vous avez déjà bien géré, pour que la preuve vienne de vous.",
                "Un ancrage utilisable dans l'instant, quand il n'y a pas le temps d'une séance entière.",
            ],
            "expect": "Les séances durent 15 à 30 minutes et se terminent par un retour net à la "
                      "vigilance : elles s'écoutent aussi bien le matin même que la veille au soir. "
                      "Enregistrez la séance et rejouez-la à l'approche de l'échéance.",
            "faq": [
                ("Est-ce que ce sont juste des affirmations positives ?",
                 "Non. Une affirmation énonce ; une séance d'hypnose construit une scène et vous la fait "
                 "répéter dans un état détendu, ce que la plupart des gens trouvent plus efficace que de "
                 "répéter une phrase à laquelle ils ne croient pas encore."),
                ("Jusqu'où détailler ma description ?",
                 "Autant que vous voulez. « Stressé par la présentation de jeudi devant douze "
                 "personnes » donne une séance bien plus utile que « plus de confiance »."),
                ("Ce que j'écris est-il stocké quelque part ?",
                 "Uniquement sur votre téléphone, et seulement si vous enregistrez la séance. Rien n'est "
                 "envoyé à un serveur."),
            ],
        },
        "stress": {
            "slug": "stress",
            "nav": "Stress",
            "card": "Redescendre après une journée exigeante et récupérer vraiment.",
            "title": "Auto-hypnose contre le stress — écrite pour vous | Onira",
            "desc": "Auto-hypnose guidée contre le stress, écrite sur votre téléphone à partir de la "
                    "pression que vous vivez, et narrée à voix haute. Hors ligne et confidentielle.",
            "h1": "Auto-hypnose contre le stress",
            "lede": "Une séance pour la fin d'une journée exigeante : d'abord un relâchement physique "
                    "délibéré, puis de la distance avec ce qui met la pression.",
            "why_title": "Pourquoi l'hypnose aide face au stress",
            "why": [
                "Un stress prolongé laisse le corps prêt à agir longtemps après que la demande soit "
                "passée. Cela se traduit par une mâchoire serrée, une respiration courte, de "
                "l'irritabilité, du mal à se poser — une récupération qui n'arrive jamais vraiment, "
                "faute de signal indiquant que la journée est finie.",
                "La séance guidée est ce signal. Une narration lente et un relâchement physique par "
                "étapes font sortir de l'état d'alerte, et les images qui suivent donnent un point de "
                "vue sur la pression au lieu de la subir de l'intérieur.",
            ],
            "works_on": [
                "Le relâchement par étapes des tensions retenues : mains, mâchoire, épaules, respiration.",
                "La séparation entre ce qui est réellement urgent et ce qui en a seulement l'air.",
                "Un point de récupération dans la journée, pour que la pression ne s'accumule pas.",
                "Une source de stress précise, si vous la nommez : charge de travail, déménagement, proche à accompagner, argent.",
            ],
            "expect": "Les séances durent 15 à 30 minutes et se terminent en état de veille : elles "
                      "s'insèrent aussi bien dans une pause déjeuner ou entre le travail et la soirée "
                      "qu'au coucher.",
            "faq": [
                ("À quelle fréquence l'utiliser ?",
                 "Aussi souvent que cela aide. Beaucoup écoutent une séance par jour pendant une "
                 "période, puis en gardent une enregistrée pour les journées chargées."),
                ("Quelle différence avec le thème anxiété ?",
                 "Les séances stress visent la récupération après une pression réelle et continue ; les "
                 "séances anxiété visent la boucle d'anticipation et la peur elle-même. Choisissez "
                 "celle qui décrit votre semaine."),
                ("Puis-je écouter au casque dans le train ?",
                 "Oui, mais considérez-le comme de la relaxation plutôt qu'une vraie séance — jamais en "
                 "conduisant ni pendant une activité qui demande votre attention."),
            ],
        },
        "smoking": {
            "slug": "arret-du-tabac",
            "nav": "Arrêt du tabac",
            "card": "Soutenir une décision déjà prise, envie après envie.",
            "title": "Auto-hypnose pour arrêter de fumer | Onira",
            "desc": "Auto-hypnose guidée pour accompagner l'arrêt du tabac, écrite sur votre téléphone à "
                    "partir de vos déclencheurs et de vos raisons, et narrée à voix haute.",
            "h1": "Auto-hypnose pour arrêter de fumer",
            "lede": "Une séance qui travaille le moment de l'envie — le déclencheur, le rituel, votre "
                    "raison d'arrêter — plutôt que la volonté.",
            "why_title": "Pourquoi l'hypnose est utilisée pour arrêter de fumer",
            "why": [
                "Le tabac ne tient pas seulement à la nicotine : il tient au café, à la pause dehors, au "
                "coup de téléphone, au moment après le repas. Chacun de ces instants est un signal "
                "appris, et les signaux appris réagissent à la répétition — c'est exactement ce "
                "qu'offre une séance d'hypnose.",
                "La séance travaille sur deux fronts : elle répète le déclencheur qui arrive et repart "
                "sans cigarette, et elle maintient vivante votre propre raison d'arrêter, pour que la "
                "décision n'ait pas à être reprise sous pression à chaque fois.",
            ],
            "works_on": [
                "Vos déclencheurs précis, si vous les nommez : le café du matin, la voiture, le stress au travail.",
                "Traverser l'envie comme une vague qui monte et redescend, au lieu d'une exigence à satisfaire.",
                "Votre raison d'arrêter, dans vos mots : la santé, l'argent, vos enfants, le souffle, la maîtrise.",
                "Le passage de « j'essaie d'arrêter » à quelqu'un qui ne fume pas.",
            ],
            "expect": "Les séances durent 15 à 30 minutes et se terminent en pleine vigilance. Beaucoup "
                      "écoutent quotidiennement pendant les premières semaines — quand les signaux sont "
                      "les plus forts — puis gardent une séance enregistrée pour les jours difficiles.",
            "faq": [
                ("Une séance suffira-t-elle à me faire arrêter ?",
                 "Non. Onira accompagne une décision déjà prise ; ce n'est pas un traitement et aucune "
                 "revendication clinique n'est faite. Substituts nicotiniques, médicaments prescrits et "
                 "services d'aide à l'arrêt se discutent avec un médecin ou un pharmacien (en France, "
                 "Tabac info service, 39 89)."),
                ("Quand écouter ?",
                 "Idéalement avant les moments de la journée où les envies sont les plus fortes, et à "
                 "nouveau quand une journée difficile s'annonce."),
                ("Est-ce que ça marche aussi pour la vape ?",
                 "La structure est la même : écrivez ce que vous voulez réellement arrêter et la séance "
                 "est écrite autour de cela."),
            ],
        },
        "focus": {
            "slug": "concentration",
            "nav": "Concentration",
            "card": "Apaiser un esprit dispersé avant un travail qui demande de l'attention.",
            "title": "Auto-hypnose pour la concentration | Onira",
            "desc": "Auto-hypnose guidée pour la concentration, écrite sur votre téléphone à partir du "
                    "travail qui vous attend, et narrée à voix haute. Fonctionne hors ligne.",
            "h1": "Auto-hypnose pour la concentration",
            "lede": "Une séance plus courte et plus tonique pour dégager le bruit avant de réviser, "
                    "d'écrire ou de travailler longtemps.",
            "why_title": "Pourquoi l'hypnose aide à se concentrer",
            "why": [
                "Perdre le fil tient rarement à un manque d'attention, mais à un excès de choses qui la "
                "réclament : notifications, tâches à moitié faites, bruit de fond de tout ce que vous "
                "devriez faire par ailleurs. L'attention est déjà occupée — simplement pas par ce qui "
                "est devant vous.",
                "L'hypnose, dans sa définition la plus simple, est une attention focalisée et soutenue. "
                "La séance rétrécit volontairement le champ, met de côté ce qui n'est pas pour "
                "maintenant, et répète le fait de commencer — en général la partie la plus difficile "
                "d'une longue plage de travail.",
            ],
            "works_on": [
                "Le rétrécissement de l'attention à une seule tâche, le reste déposé pour une durée définie.",
                "La friction du démarrage, répétée jusqu'à ce que la première minute soit banale.",
                "Le retour à la tâche après une interruption, sans perdre le fil.",
                "Un travail précis, si vous le nommez : un examen, un chapitre, une livraison, une échéance.",
            ],
            "expect": "Écoutez une séance de concentration juste avant le travail lui-même. Elle se "
                      "termine en état d'éveil net, tourné vers l'action plutôt que somnolent, pour "
                      "enchaîner directement.",
            "faq": [
                ("Faut-il l'écouter en travaillant ?",
                 "Non : écoutez d'abord, travaillez ensuite. La séance demande votre attention ; la "
                 "tâche en a besoin après."),
                ("Est-ce utile pour réviser ?",
                 "C'est l'un des usages les plus fréquents. Nommer la matière et la date de l'examen "
                 "rend la séance nettement plus précise."),
                ("Puis-je la raccourcir ?",
                 "Les séances visent 15 à 30 minutes. Vous pouvez arrêter à tout moment, rien ne "
                 "casse si vous terminez plus tôt."),
            ],
        },
        "weight": {
            "slug": "perte-de-poids",
            "nav": "Poids",
            "card": "Travailler les habitudes et le rapport à la nourriture, pas les règles.",
            "title": "Auto-hypnose pour le poids et l'alimentation | Onira",
            "desc": "Auto-hypnose guidée pour le poids et les habitudes alimentaires, écrite sur votre "
                    "téléphone à partir de vos propres schémas, et narrée à voix haute.",
            "h1": "Auto-hypnose pour le poids et les habitudes alimentaires",
            "lede": "Une séance sur les moments qui entourent le fait de manger — la soirée, l'ennui, la "
                    "récompense — plutôt que sur ce qui serait autorisé.",
            "why_title": "Pourquoi l'hypnose est utilisée pour les habitudes alimentaires",
            "why": [
                "La plupart des prises alimentaires que l'on souhaite changer ne viennent pas de la "
                "faim. Ce sont des habitudes attachées à un moment : l'heure après le dîner, le trajet "
                "du retour, la fin d'une journée dure, le besoin d'occuper ses mains. Les règles n'y "
                "touchent pas, parce que le moment arrive avant toute décision.",
                "Une séance d'hypnose fait répéter ces moments autrement : remarquer le signal, le "
                "laisser passer, et construire un rapport plus calme à l'alimentation en général. "
                "L'accent est mis sur le comment et le pourquoi, pas sur la restriction.",
            ],
            "works_on": [
                "Le moment précis où l'habitude se déclenche, si vous le nommez : la soirée, le stress, l'ennui, la fête.",
                "Manger lentement et remarquer la satiété, plutôt que finir automatiquement.",
                "Distinguer l'appétit de la recherche de réconfort, sans faire de l'un ou l'autre un échec.",
                "Un discours intérieur plus stable, car l'autocritique alimente le cycle au lieu de le rompre.",
            ],
            "expect": "Les séances durent 15 à 30 minutes et se terminent en pleine vigilance. Écouter à "
                      "heure régulière — souvent en fin d'après-midi, avant les heures les plus "
                      "difficiles — fonctionne mieux qu'écouter seulement après une mauvaise journée.",
            "faq": [
                ("Est-ce un régime ?",
                 "Non. Onira ne donne aucun conseil diététique, nutritionnel ou médical et ne fixe "
                 "aucune règle alimentaire. La séance travaille les habitudes et le rapport à "
                 "l'alimentation."),
                ("Est-ce que cela va me faire maigrir ?",
                 "Aucune promesse de ce type n'est faite. Le poids est un sujet médical : un médecin ou "
                 "un diététicien est le bon interlocuteur pour un plan."),
                ("Et en cas de trouble du comportement alimentaire ?",
                 "Adressez-vous à un professionnel plutôt qu'à un outil d'auto-assistance. Onira n'est "
                 "pas conçu pour les TCA et redirige les contenus qui vont dans cette direction."),
            ],
        },
        "fear": {
            "slug": "peurs-et-phobies",
            "nav": "Peurs et phobies",
            "card": "Répéter au calme l'avion, la route ou le vide, avant d'y être.",
            "title": "Auto-hypnose pour les peurs et les phobies | Onira",
            "desc": "Hypnose guidée contre la peur de l'avion, de conduire ou du vide, écrite sur "
                    "votre téléphone à partir de la situation que vous affrontez. Hors ligne.",
            "h1": "Auto-hypnose pour les peurs et les phobies",
            "lede": "Une séance construite autour d'une situation précise — le vol, l'ascenseur, "
                    "l'autoroute — répétée assez lentement pour que le corps cesse d'y voir une "
                    "urgence.",
            "why_title": "Pourquoi l'hypnose aide face à une peur précise",
            "why": [
                "Une peur ne se raisonne pas. La réaction arrive avant le raisonnement : la poitrine "
                "se serre, l'attention se rétrécit, et tout est terminé avant qu'une pensée sensée "
                "ait eu son tour. L'hypnose guidée travaille sur ce qui bouge en premier — un rythme "
                "lent et une respiration posée font sortir de l'état d'alerte, et un corps sorti de "
                "l'alerte ne réagit plus pareil au même déclencheur.",
                "Ensuite, la séance répète la scène au lieu de l'éviter. Vous passez la porte "
                "d'embarquement, le rond-point, l'ascenseur vitré, à une vitesse où vous restez "
                "calme. C'est cette répétition qui rend la situation réelle familière plutôt que "
                "soudaine.",
            ],
            "works_on": [
                "La montée physique — souffle, poitrine, mains — ralentie délibérément avant la scène.",
                "L'évitement lui-même : la situation rétrécit à chaque fois qu'elle est traversée au calme.",
                "Un point d'ancrage utilisable sur le moment : une respiration, un mot, un geste.",
                "Votre situation, si vous l'écrivez : un vol le mois prochain, un examen de conduite, un tunnel.",
            ],
            "expect": "Les séances durent 15 à 30 minutes. Vous restez conscient du début à la fin, "
                      "et la séance se termine toujours par un retour net à la vigilance — elle "
                      "s'utilise donc le matin même du vol, pas seulement la veille. Au casque, "
                      "dans un endroit où vous ne serez pas dérangé.",
            "faq": [
                ("L'auto-hypnose peut-elle guérir une phobie ?",
                 "Non. La relaxation guidée et la répétition mentale sont un outil d'auto-assistance, "
                 "utile pour une peur du quotidien. Une phobie qui limite votre vie se traite avec "
                 "un professionnel, souvent très efficacement : c'est là qu'il faut aller."),
                ("Puis-je écouter pendant le vol ?",
                 "Oui, et beaucoup le font. La séance se termine par un retour à la vigilance, elle "
                 "convient donc avant comme pendant — mais jamais en conduisant, même une séance "
                 "sur la conduite."),
                ("Dois-je décrire ce qui me fait peur ?",
                 "Non, le thème suffit. Si vous le décrivez, la répétition devient plus précise — et "
                 "cela reste sur votre téléphone, puisque le modèle tourne en local."),
            ],
        },
        "letting_go": {
            "slug": "oublier-une-personne",
            "nav": "Tourner la page",
            "card": "Cesser de rejouer la même conversation en boucle.",
            "title": "Auto-hypnose pour oublier une personne | Onira",
            "desc": "Hypnose guidée pour tourner la page après une rupture, écrite sur votre "
                    "téléphone à partir de ce qui vous revient en tête. Gratuite et hors ligne.",
            "h1": "Auto-hypnose pour tourner la page",
            "lede": "Une séance pour le moment où la personne est partie mais où votre tête, elle, "
                    "continue la conversation.",
            "why_title": "Pourquoi l'hypnose aide à passer à autre chose",
            "why": [
                "Ce qui use, après une rupture, ce n'est pas le souvenir : c'est la répétition. La "
                "même scène revient, la même phrase, la réponse que vous auriez dû donner. Chaque "
                "passage rouvre la chose au lieu de la refermer, et décider d'arrêter d'y penser "
                "revient à y penser encore.",
                "Une séance guidée ne cherche pas à effacer quelqu'un — ce n'est pas possible, et "
                "ce n'est pas le but. Elle réduit la charge attachée au souvenir : dans un état "
                "calme, la scène est revisitée à distance, plus lentement, jusqu'à ce qu'elle "
                "cesse de déclencher la même réaction. Le souvenir reste, l'aiguillon s'émousse.",
            ],
            "works_on": [
                "La rumination du soir, quand la même conversation recommence dès que le silence tombe.",
                "L'envie de vérifier son profil, traitée comme une habitude et pas comme une faiblesse.",
                "Le retour de l'attention vers vous : ce que vous voulez, indépendamment de cette personne.",
                "Une scène précise, si vous l'écrivez : le dernier échange, un lieu, une date qui revient.",
            ],
            "expect": "Les séances durent 15 à 30 minutes et se terminent par un retour à la "
                      "vigilance. Les premières remuent parfois un peu — c'est normal quand le "
                      "sujet est récent. Si une séance vous fait du bien, enregistrez-la et "
                      "réécoutez la même : la répétition fait ici l'essentiel du travail.",
            "faq": [
                ("Est-ce que je vais oublier la personne ?",
                 "Non, et ce serait une mauvaise promesse. Ce qui change, c'est l'intensité : le "
                 "souvenir revient moins souvent et pèse moins lourd. C'est ce que fait le temps, "
                 "en un peu plus dirigé."),
                ("Et si c'est un deuil et pas une rupture ?",
                 "Les séances peuvent apaiser les nuits difficiles, mais un deuil n'est pas une "
                 "chose à traiter avec une application. Un accompagnement humain compte davantage, "
                 "et Onira n'est pas écrit pour cela."),
                ("Faut-il écrire son nom ?",
                 "Ce n'est pas nécessaire, le thème suffit. Ce que vous écrivez ne quitte jamais "
                 "le téléphone : la génération se fait en local, rien n'est envoyé."),
            ],
        },
        "motivation": {
            "slug": "motivation-et-energie",
            "nav": "Motivation",
            "card": "Commencer enfin ce que vous repoussez depuis une semaine.",
            "title": "Auto-hypnose pour la motivation et l'énergie | Onira",
            "desc": "Hypnose guidée contre la procrastination et les coups de fatigue, écrite sur "
                    "votre téléphone à partir de la tâche que vous évitez. Gratuite, hors ligne.",
            "h1": "Auto-hypnose pour la motivation et l'énergie",
            "lede": "Une séance sur le fait de commencer — les dix minutes qui précèdent la tâche, "
                    "là où la motivation se gagne ou se perd.",
            "why_title": "Pourquoi l'hypnose aide contre la procrastination",
            "why": [
                "Repousser n'est presque jamais de la paresse. C'est l'évitement d'une sensation "
                "attachée à la tâche : ce sera ennuyeux, cela va montrer le retard accumulé, ce ne "
                "sera pas assez bien. La tâche est repoussée parce que la sensation l'est — et la "
                "sensation grossit à chaque heure d'attente.",
                "Une séance s'occupe de la sensation plutôt que de vous sermonner sur la tâche. "
                "Dans un état calme, le démarrage est répété en détail : s'asseoir, ouvrir le "
                "dossier, faire le premier petit geste. Une fois le démarrage répété, c'est lui "
                "qui cesse d'être le passage difficile.",
            ],
            "works_on": [
                "Le blocage d'avant le début, répété comme une séquence que vous avez déjà traversée.",
                "L'énergie plate de l'après-midi, traitée comme une tension et non comme un manque de volonté.",
                "Le tout ou rien : l'idée qu'une tâche doit être parfaite ou ne pas être commencée.",
                "Une tâche précise, si vous l'écrivez : la déclaration, la salle de sport, le message en retard.",
            ],
            "expect": "Les séances durent 15 à 30 minutes et se terminent volontairement par un "
                      "retour net à la vigilance : c'est un thème à utiliser avant la tâche, pas au "
                      "coucher. Beaucoup en enregistrent une et la rejouent en début de journée.",
            "faq": [
                ("Une séance suffit-elle à me rendre productif ?",
                 "Non, et un outil qui le promet exagère. Ce qu'une séance fait de façon fiable, "
                 "c'est abaisser une fois la résistance à commencer ; c'est en le refaisant que "
                 "l'habitude change."),
                ("L'hypnose peut-elle régler un manque d'énergie ?",
                 "La relaxation aide quand la fatigue est surtout de la tension ou du mauvais "
                 "sommeil. Un épuisement qui dure est d'abord une question médicale, à poser à un "
                 "médecin plutôt qu'à une application."),
                ("Est-ce utile pour se motiver à faire du sport ?",
                 "Oui. Répéter le démarrage — mettre les chaussures, sortir — fonctionne mieux que "
                 "répéter la séance elle-même, et c'est ainsi que le thème est écrit."),
            ],
        },
        "pain": {
            "slug": "douleur",
            "nav": "Douleur",
            "card": "Desserrer la crispation et l'appréhension qui amplifient la douleur.",
            "title": "Auto-hypnose et douleur — écrite pour vous | Onira",
            "desc": "Auto-hypnose guidée en complément de votre traitement : moins de crispation, "
                    "moins d'appréhension, des nuits plus simples. Un confort, pas une cure.",
            "h1": "Auto-hypnose pour vivre avec la douleur",
            "lede": "Une séance pour ce qui, dans la douleur, n'est pas la lésion elle-même : la "
                    "crispation, l'appréhension de la prochaine crise, et les nuits qu'elle prend.",
            "why_title": "Ce que l'hypnose peut et ne peut pas faire sur la douleur",
            "why": [
                "Une douleur n'est jamais seulement un signal du corps. La place qu'elle prend dans "
                "l'attention, la tension avec laquelle on se protège autour d'elle, la crainte de la "
                "prochaine crise : tout cela change son intensité vécue. Ce sont ces parties-là qu'une "
                "séance guidée peut atteindre, et c'est souvent ce qui sépare une journée difficile "
                "d'une journée impossible.",
                "Ce qu'elle ne fait pas, c'est supprimer la cause. Ce thème est écrit comme un "
                "accompagnement de votre traitement, jamais comme un remplacement, et il n'est pas une "
                "raison de sauter un rendez-vous ou de modifier une prescription. Une douleur nouvelle, "
                "qui s'aggrave ou qui reste inexpliquée relève d'abord d'un médecin.",
            ],
            "works_on": [
                "La protection réflexe et les tensions musculaires qui s'installent autour d'une zone douloureuse.",
                "L'endormissement quand la douleur ramène sans cesse l'attention vers elle.",
                "L'anticipation de la prochaine crise, qui crispe tout avant même qu'elle arrive.",
                "La place de la douleur dans la journée : en bordure de l'attention plutôt qu'au centre.",
            ],
            "expect": "Les séances durent 15 à 30 minutes et se terminent en état de veille. Ce que les "
                      "gens décrivent est le plus souvent partiel et temporaire — baisser le volume "
                      "plutôt que l'éteindre — et cela vient avec la répétition, pas en une fois.",
            "faq": [
                ("L'hypnose peut-elle guérir ma douleur ?",
                 "Non, et tout ce qui prétend le contraire vous vend quelque chose. La relaxation et la "
                 "suggestion sont couramment utilisées en accompagnement d'un suivi médical pour rendre "
                 "la douleur plus vivable. Onira est un outil de relaxation en ce sens : un complément, "
                 "pas un traitement."),
                ("Vais-je quand même la sentir ?",
                 "Très probablement oui. L'objectif réaliste est qu'elle prenne moins de place : moins "
                 "de tension autour, moins d'appréhension avant, plus de place pour le reste."),
                ("Est-ce compatible avec mes médicaments ?",
                 "Une séance n'interagit avec rien de ce que vous prenez. Ce qui compte, c'est de ne "
                 "jamais diminuer ni arrêter un traitement prescrit parce qu'une séance a soulagé : "
                 "cette décision appartient à celui qui l'a prescrit."),
                ("Et pour la migraine ?",
                 "La tension et l'anticipation autour de la crise sont accessibles ; la crise elle-même "
                 "est un phénomène neurologique et une affaire médicale. N'utilisez pas une séance à la "
                 "place d'un traitement qui fonctionne pour vous."),
            ],
        },
        "ibs": {
            "slug": "syndrome-intestin-irritable",
            "nav": "Intestin irritable",
            "card": "Apaiser la boucle intestin-cerveau qui entretient les crises.",
            "title": "Auto-hypnose et syndrome de l'intestin irritable | Onira",
            "desc": "Auto-hypnose guidée sur le versant stress du SII : ventre plus calme, moins "
                    "d'anticipation, journées plus simples. Un complément, pas un traitement.",
            "h1": "Auto-hypnose et syndrome de l'intestin irritable",
            "lede": "Une séance pour la boucle où le stress aggrave les symptômes et où les symptômes "
                    "nourrissent le stress — la part du SII qui répond au calme.",
            "why_title": "Pourquoi la relaxation atteint l'intestin",
            "why": [
                "L'intestin et le système nerveux dialoguent en permanence. C'est pour cela qu'une "
                "semaine tendue se lit dans la digestion, et que la peur d'une crise au mauvais moment "
                "suffit parfois à la déclencher. La relaxation guidée agit directement sur cet axe : "
                "elle fait baisser l'état d'alerte qui entretient la boucle.",
                "Soyons précis, car la distinction compte : l'hypnothérapie dirigée vers l'intestin est "
                "une option reconnue dans la prise en charge du SII, recommandée par les "
                "recommandations cliniques lorsque d'autres approches n'ont pas suffi — mais c'est un "
                "protocole structuré, mené par un thérapeute formé. Onira n'est pas ce protocole. C'est "
                "un outil de relaxation qui travaille sur le même axe du stress, en accompagnement de "
                "votre suivi et non à sa place.",
            ],
            "works_on": [
                "L'anticipation : organiser sa journée autour des toilettes, et ce que cela coûte.",
                "Les tensions abdominales et la respiration bloquée pendant une crise.",
                "Le sommeil, qui souffre dans les deux sens quand les symptômes sont actifs.",
                "Une situation précise, si vous la nommez : un long trajet, un restaurant, une journée au bureau.",
            ],
            "expect": "Les séances durent 15 à 30 minutes. Les symptômes digestifs évoluent lentement : "
                      "jugez sur plusieurs semaines d'usage régulier, pas sur une séance.",
            "faq": [
                ("Est-ce la même chose que l'hypnothérapie dirigée vers l'intestin ?",
                 "Non. Celle-ci est un programme structuré avec un thérapeute formé, en général "
                 "plusieurs séances sur deux ou trois mois. Onira écrit des séances de relaxation à "
                 "partir de ce que vous décrivez. Si vous voulez le protocole clinique, demandez une "
                 "orientation à votre médecin."),
                ("Faut-il un diagnostic d'abord ?",
                 "Oui. Des symptômes digestifs ont de nombreuses causes et certaines doivent être "
                 "explorées : saignements, perte de poids inexpliquée, changement durable du transit "
                 "habituel relèvent d'un médecin, pas d'une application."),
                ("Puis-je l'utiliser pendant une crise ?",
                 "Oui, et beaucoup le font. Installez-vous là où personne ne vous dérangera, et voyez-le "
                 "comme un moyen de desserrer la tension autour de l'épisode plutôt que de l'arrêter."),
            ],
        },
        "emotional_recovery": {
            "slug": "apaisement-emotionnel",
            "nav": "Apaisement",
            "card": "Se reposer après un moment dur, sans le revivre.",
            "title": "Auto-hypnose et apaisement émotionnel | Onira",
            "desc": "Auto-hypnose guidée pour l'après-coup : nuits plus calmes, moins de ruminations, "
                    "journées plus stables. Un outil de relaxation, pas une thérapie du trauma.",
            "h1": "Auto-hypnose pour l'apaisement émotionnel",
            "lede": "Une séance pour l'après-coup : quand l'épreuve est passée mais que le sommeil, les "
                    "nerfs et l'attention n'ont pas encore suivi.",
            "why_title": "Apaiser l'après-coup, sans le rouvrir",
            "why": [
                "Après quelque chose de difficile, le corps reste souvent en tension longtemps après "
                "l'événement. Cela se traduit par un sommeil haché, de l'irritabilité, des pensées qui "
                "reviennent en boucle le soir, des sursauts qui ne se calment pas. Ce sont des "
                "répliques ordinaires, et elles répondent bien à un calme délibéré.",
                "Ces séances sont écrites pour apaiser cet état, pas pour retourner dans ce qui l'a "
                "causé. Elles ne vous demanderont pas de revisiter un souvenir ni de raconter ce qui "
                "s'est passé. Ce travail-là existe, il aide, et il se fait avec un professionnel formé "
                "qui peut vous accompagner pendant — pas seul avec un téléphone.",
            ],
            "works_on": [
                "Un sommeil qui s'est cassé après une période difficile et n'est pas revenu.",
                "Les ruminations du soir : la même scène qui repasse sans se résoudre.",
                "Un corps qui reste en alerte : poitrine serrée, mâchoire crispée, sursauts au moindre bruit.",
                "Traverser des journées ordinaires pendant que quelque chose de lourd se dépose encore.",
            ],
            "expect": "Les séances durent 15 à 30 minutes et se terminent toujours par un retour complet "
                      "à l'état de veille. Si une séance vous laisse plus en détresse qu'apaisé, "
                      "arrêtez de l'utiliser et parlez-en à quelqu'un de qualifié.",
            "faq": [
                ("Cela peut-il traiter un trauma ou un état de stress post-traumatique ?",
                 "Non, et ce n'est pas écrit pour essayer. Les reviviscences, les cauchemars, la "
                 "dissociation ou un évitement qui organise votre vie se soignent — auprès d'un "
                 "clinicien formé au psychotraumatisme. Onira est un outil de relaxation pour "
                 "l'après-coup, à utiliser à côté de cette aide si vous l'avez."),
                ("Une séance va-t-elle me faire remonter des souvenirs ?",
                 "Ce n'est pas sa conception, et elle ne vous invitera pas à aller en chercher. "
                 "L'hypnose n'est d'ailleurs pas un moyen fiable de retrouver des souvenirs — un "
                 "résultat bien établi, et l'une des raisons pour lesquelles ce thème reste sur "
                 "l'apaisement du présent plutôt que sur l'exploration du passé."),
                ("Et si je me sens moins bien pendant une séance ?",
                 "Arrêtez, ouvrez les yeux, revenez dans la pièce. Cette réaction est un signal qu'il "
                 "vaut mieux travailler avec une personne qu'avec une application, et elle mérite "
                 "d'être prise au sérieux plutôt que forcée."),
                ("Le deuil, est-ce la même chose ?",
                 "Assez proche pour que le thème convienne. Les séances peuvent stabiliser les journées "
                 "et les nuits ; elles ne raccourciront pas un deuil, et ce n'est pas leur rôle."),
            ],
        },
    },
}

# ---------------------------------------------------------------- Spanish ----

ES = {
    "code": "es",
    "label": "ES",
    "name": "Español",
    "base": "es",
    "theme_dir": "hipnosis",
    "privacy_slug": "privacidad",
    "ui": {
        "home_name": "Onira",
        "home_crumb": "Inicio",
        "badge_alt": "Disponible en Google Play",
        "cta_note": "Gratis, sin cuenta, sin suscripción. Compra única para quitar los anuncios.",
        "how_title": "Cómo compone Onira tu sesión",
        "how_steps": [
            "Eliges un tema y, si quieres, escribes una o dos frases sobre lo que te pasa realmente.",
            "Un modelo de IA que se ejecuta en tu teléfono escribe el guion: inducción, profundización, imágenes, sugestiones, anclaje y una vuelta clara al estado de alerta.",
            "La narración empieza en cuanto está lista la apertura y el resto se sigue escribiendo mientras escuchas: una sesión completa de 15 a 30 minutos arranca en segundos.",
            "Guarda una sesión que te haya gustado y repite la misma narración cuando quieras.",
        ],
        "works_title": "En qué trabaja la sesión",
        "expect_title": "Qué esperar",
        "faq_title": "Preguntas frecuentes",
        "privacy_title": "Privado por diseño",
        "privacy_body": "Onira ejecuta su modelo en tu dispositivo. El tema que eliges, lo que escribes y "
                        "la sesión que recibes nunca se envían: no hay cuenta, ni generación en la nube, "
                        "ni servidor que pueda leerlos.",
        "privacy_link": "Leer la política de privacidad",
        "safety_title": "No es un tratamiento médico",
        "safety_body": "Onira es una herramienta de relajación y autohipnosis. No es terapia, ni consejo "
                       "médico o psiquiátrico, ni un sustituto de la atención profesional o de los "
                       "servicios de emergencia. Si estás en peligro o en crisis, contacta con una línea "
                       "de atención o el número de emergencias local (en España, el 024).",
        "related_title": "Otros temas",
        "foot_tag": "Onira — sesiones de hipnosis escritas en tu teléfono, por tu teléfono.",
        "foot_privacy": "Privacidad",
        "foot_play": "Google Play",
        "head_cta": "Obtener la app",
        "langs_label": "Idioma",
        "screens_title": "Dentro de la app",
        "screens": [
            ("home", "La pantalla de inicio de Onira: temas y campo de texto libre",
             "Elige un tema y añade un detalle si quieres."),
            ("session", "Una sesión en marcha, con el indicador de fase y el fondo que respira",
             "La sesión se narra sola sobre un fondo que respira despacio."),
            ("favorites", "La lista de sesiones guardadas",
             "Guarda una sesión y repite la misma narración."),
            ("privacy", "Ni lo que escribes ni lo que recibes sale del teléfono",
             "Sin cuenta, nada se transmite, funciona sin conexión."),
        ],
    },
    "home": {
        "title": "Onira — Sesiones de autohipnosis escritas para ti",
        "desc": "Onira escribe una sesión de hipnosis personal en tu teléfono y la narra en voz alta: "
                "sueño, ansiedad, estrés, confianza. Nada sale de tu dispositivo.",
        "h1": "Sesiones de autohipnosis escritas para ti, en tu teléfono",
        "lede": "Casi todas las apps de hipnosis te dan la misma grabación que a los demás. Onira escribe "
                "una sesión para tu situación, en el momento, con un modelo de IA que funciona "
                "íntegramente en tu dispositivo, y luego te la narra mientras cierras los ojos.",
        "intro": [
            "La hipnosis guiada funciona mejor cuando las palabras encajan con lo que realmente llevas "
            "encima. Una grabación pensada para todo el mundo tiene que ser vaga; una sesión escrita a "
            "partir de la frase que acabas de escribir puede nombrar aquello que no te deja dormir y "
            "construir las imágenes alrededor.",
            "Esa es la idea de Onira. Eliges un tema, añades los detalles que quieras y un modelo de "
            "lenguaje de pesos abiertos, dentro de tu teléfono, escribe un guion completo siguiendo el "
            "arco clásico de una sesión de hipnoterapia.",
        ],
        "themes_title": "Elige un tema",
    },
    "themes": {
        "anxiety": {
            "slug": "ansiedad",
            "nav": "Ansiedad",
            "card": "Aflojar el pensamiento ansioso y calmar el cuerpo.",
            "title": "Autohipnosis para la ansiedad — escrita para ti | Onira",
            "desc": "Autohipnosis guiada para la ansiedad, escrita en tu teléfono a partir de lo que "
                    "realmente te preocupa y narrada en voz alta. Privada, gratis, sin suscripción.",
            "h1": "Autohipnosis para la ansiedad",
            "lede": "Una sesión guiada que primero frena el cuerpo y luego trabaja el propio pensamiento "
                    "ansioso, escrita alrededor de lo que de verdad te preocupa.",
            "why_title": "Por qué la hipnosis ayuda con la ansiedad",
            "why": [
                "La ansiedad mantiene ocupados dos sistemas a la vez: un cuerpo en alerta y una mente "
                "que ensaya lo que podría pasar. La hipnosis guiada se dirige al primero de forma "
                "directa — ritmo lento, voz pausada, respiración regular bajan el estado de alerta — y "
                "eso es justamente lo que permite aflojar el segundo.",
                "En ese estado de calma la sugestión funciona de otro modo. En lugar de discutir con un "
                "pensamiento ansioso, la sesión ofrece una versión más serena de la misma escena y te "
                "la hace ensayar, para que vuelva con menos carga.",
            ],
            "works_on": [
                "La tensión física — mandíbula, hombros, pecho, estómago — liberada por etapas.",
                "El bucle de anticipar lo peor, sustituido por una respuesta tranquila ya ensayada.",
                "Un anclaje para después: una respiración, una palabra o un gesto que recupera el estado de la sesión.",
                "Una preocupación concreta, si la escribes: una entrevista, un vuelo, una conversación que temes.",
            ],
            "expect": "Las sesiones duran entre 15 y 30 minutos. Estás consciente todo el tiempo — la "
                      "hipnosis es atención enfocada, no sueño ni pérdida de control — y la sesión "
                      "termina siempre con una vuelta clara al estado de alerta. Mejor con auriculares, "
                      "sentado o tumbado donde nadie te interrumpa.",
            "faq": [
                ("¿La autohipnosis funciona de verdad para la ansiedad?",
                 "La relajación guiada y la sugestión se usan habitualmente como herramienta de "
                 "autoayuda para la ansiedad y el estrés cotidianos, y a mucha gente le resultan "
                 "calmantes. Onira es una herramienta de relajación, no un tratamiento para un trastorno "
                 "de ansiedad: eso se consulta con un profesional."),
                ("¿Puedo usarla al acostarme?",
                 "Sí, aunque la sesión termina devolviéndote al estado de alerta. Si lo que quieres es "
                 "dormirte, el tema de sueño está escrito para eso."),
                ("¿Tengo que escribir algo personal?",
                 "No, basta con el tema. Y si escribes algo, se queda en tu teléfono: el modelo funciona "
                 "en local y no se envía nada."),
            ],
        },
        "sleep": {
            "slug": "sueno",
            "nav": "Sueño",
            "card": "Bajar revoluciones y dejar que el sueño llegue solo.",
            "title": "Autohipnosis para dormir — escrita para ti | Onira",
            "desc": "Hipnosis guiada para dormir, escrita en tu teléfono a partir de lo que te mantiene "
                    "despierto y narrada en voz alta. Funciona sin conexión.",
            "h1": "Autohipnosis para dormir",
            "lede": "Una sesión lenta y poco estimulante para ese momento en el que ya estás en la cama y "
                    "tu cabeza no para.",
            "why_title": "Por qué la hipnosis ayuda a dormir",
            "why": [
                "Costar dormirse casi nunca es falta de cansancio. Suele ser una mente todavía en "
                "marcha: el día que se repite, el mañana que se planifica, la comprobación constante de "
                "si el sueño está llegando. Una sesión guiada le da a esa atención un sitio suave donde "
                "posarse, que es justo lo que el sueño necesita.",
                "El ritmo hace casi todo el trabajo: las frases se vuelven más lentas y suaves, las "
                "imágenes menos detalladas, y no hay nada que decidir ni que seguir de cerca. Mucha "
                "gente deja de escuchar conscientemente bastante antes del final, que es precisamente "
                "lo que se busca.",
            ],
            "works_on": [
                "Una relajación progresiva del cuerpo, de los pies hacia arriba, para soltar el día.",
                "El hábito de vigilar si ya te has dormido, sustituido por algo fácil de seguir.",
                "Imágenes repetitivas que frenan: una escalera que baja, agua que fluye, un pasillo largo y silencioso.",
                "Un motivo concreto por el que estás despierto, si lo escribes: una entrega, una conversación, despertarte a las 3.",
            ],
            "expect": "Baja el volumen y deja que la sesión suene. Dura entre 15 y 30 minutos; no hace "
                      "falta aguantar hasta el final y no hay nada que hacer si te duermes. Si una "
                      "sesión te va bien, guárdala y repite la misma cada noche.",
            "faq": [
                ("¿Me despertará al terminar?",
                 "Las sesiones de sueño están escritas para desvanecerse, no para devolverte al estado "
                 "de alerta. Si quieres un despertar claro, usa un tema de día."),
                ("¿Puedo usarla cada noche?",
                 "Sí. Las sesiones guardadas se repiten idénticas, y la familiaridad ayuda: la misma "
                 "narración acaba siendo una señal de que toca dormir."),
                ("¿Necesita conexión a internet?",
                 "Solo una vez, para descargar el modelo la primera vez. Después todo se genera y se "
                 "narra sin conexión."),
            ],
        },
        "confidence": {
            "slug": "confianza-en-uno-mismo",
            "nav": "Confianza",
            "card": "Ensayar la versión de ti que ya sabes ser.",
            "title": "Autohipnosis para la confianza y la autoestima | Onira",
            "desc": "Autohipnosis guiada para la confianza, escrita en tu teléfono a partir de la "
                    "situación que tienes delante y narrada en voz alta. Privada y gratuita.",
            "h1": "Autohipnosis para la confianza en uno mismo",
            "lede": "Una sesión basada en el ensayo: verte resolviendo la situación con suficiente "
                    "detalle como para que deje de parecer hipotética.",
            "why_title": "Por qué la hipnosis ayuda con la confianza",
            "why": [
                "La confianza rara vez falta en general: falta en situaciones concretas. Hablar en una "
                "reunión, entrar en una sala, hacer una llamada. Esos momentos ya están muy ensayados, "
                "solo que en la dirección equivocada: los has imaginado saliendo mal muchas veces.",
                "Una sesión de hipnosis es ensayo estructurado en la otra dirección. En un estado "
                "relajado y enfocado recorres la situación saliendo bien — la postura, la voz, la "
                "primera frase — y esa versión gana algo de la nitidez que la versión ansiosa tenía "
                "gratis.",
            ],
            "works_on": [
                "Una situación concreta que se acerca, si la nombras: una presentación, una cita, una entrevista, una conversación difícil.",
                "La huella física de la seguridad: respiración, postura, hablar sin prisa.",
                "Recordar veces en las que ya lo resolviste bien, para que la prueba sea tuya.",
                "Un anclaje para el momento mismo, cuando no hay tiempo de una sesión entera.",
            ],
            "expect": "Las sesiones duran de 15 a 30 minutos y terminan con una vuelta clara al estado de "
                      "alerta, así que funcionan tanto la mañana misma como la noche anterior. Guarda la "
                      "sesión y repítela a medida que se acerque la fecha.",
            "faq": [
                ("¿Esto son solo afirmaciones positivas?",
                 "No. Una afirmación declara algo; una sesión de hipnosis construye una escena y te la "
                 "hace ensayar en estado relajado, algo que a la mayoría le cala mejor que repetir una "
                 "frase que todavía no se cree."),
                ("¿Cuánto detalle debo dar?",
                 "El que quieras. «Nervioso por la presentación del jueves ante doce personas» da una "
                 "sesión mucho más útil que «más confianza»."),
                ("¿Se guarda en algún sitio lo que escribo?",
                 "Solo en tu teléfono, y únicamente si guardas la sesión. No se envía nada a ningún "
                 "servidor."),
            ],
        },
        "stress": {
            "slug": "estres",
            "nav": "Estrés",
            "card": "Bajar de un día exigente y recuperarte de verdad.",
            "title": "Autohipnosis para el estrés — escrita para ti | Onira",
            "desc": "Autohipnosis guiada para el estrés, escrita en tu teléfono a partir de la presión "
                    "que estás viviendo y narrada en voz alta. Sin conexión y privada.",
            "h1": "Autohipnosis para el estrés",
            "lede": "Una sesión para el final de un día exigente: primero una liberación física "
                    "deliberada, y luego algo de distancia con lo que aprieta.",
            "why_title": "Por qué la hipnosis ayuda con el estrés",
            "why": [
                "El estrés sostenido deja el cuerpo preparado para actuar mucho después de que la "
                "exigencia haya pasado. Se nota en la mandíbula apretada, la respiración corta, la mecha "
                "corta, la dificultad para parar: una recuperación que nunca llega del todo porque nada "
                "señala que el día ha terminado.",
                "La sesión guiada es esa señal. Una narración lenta y una liberación física por etapas "
                "te sacan del estado de alerta, y las imágenes que vienen después te dan un punto de "
                "vista sobre la presión en lugar de vivirla desde dentro.",
            ],
            "works_on": [
                "Soltar por etapas la tensión acumulada: manos, mandíbula, hombros, respiración.",
                "Separar lo que es realmente urgente de lo que solo lo parece ahora mismo.",
                "Un punto de recuperación en el día, para que la presión no se acumule.",
                "Una fuente concreta de estrés, si la nombras: carga de trabajo, una mudanza, cuidar de alguien, dinero.",
            ],
            "expect": "Las sesiones duran de 15 a 30 minutos y terminan devolviéndote al estado de "
                      "alerta, así que encajan igual de bien en una pausa de mediodía, entre el trabajo "
                      "y la tarde, o antes de dormir.",
            "faq": [
                ("¿Con qué frecuencia debo usarla?",
                 "Tanto como te ayude. Mucha gente escucha una sesión diaria durante una temporada y "
                 "luego guarda una para los días exigentes."),
                ("¿En qué se diferencia del tema de ansiedad?",
                 "Las sesiones de estrés se centran en recuperarte de una presión real y continua; las "
                 "de ansiedad, en el bucle de anticipación y el miedo. Elige la que describa tu semana."),
                ("¿Puedo escucharla con auriculares en el tren?",
                 "Puedes, pero tómalo como relajación más que como sesión completa; nunca conduciendo ni "
                 "haciendo algo que requiera tu atención."),
            ],
        },
        "smoking": {
            "slug": "dejar-de-fumar",
            "nav": "Dejar de fumar",
            "card": "Apoyar una decisión ya tomada, ganas a ganas.",
            "title": "Autohipnosis para dejar de fumar — escrita para ti | Onira",
            "desc": "Autohipnosis guiada para acompañar el proceso de dejar de fumar, escrita en tu "
                    "teléfono a partir de tus propios detonantes y motivos, y narrada en voz alta.",
            "h1": "Autohipnosis para dejar de fumar",
            "lede": "Una sesión que trabaja el momento del deseo — el detonante, el ritual, tu motivo "
                    "para dejarlo — en lugar de la fuerza de voluntad.",
            "why_title": "Por qué se usa la hipnosis para dejar de fumar",
            "why": [
                "Fumar no se sostiene solo por la nicotina: se sostiene por el café, la salida a la "
                "calle, la llamada, el momento después de comer. Cada uno de esos instantes es una señal "
                "aprendida, y las señales aprendidas responden al ensayo, que es justo lo que ofrece una "
                "sesión de hipnosis.",
                "La sesión trabaja en dos frentes: ensaya la señal que llega y se va sin cigarrillo, y "
                "mantiene vivo tu propio motivo para dejarlo, de modo que la decisión no tenga que "
                "tomarse de nuevo bajo presión cada vez.",
            ],
            "works_on": [
                "Tus detonantes concretos, si los nombras: el café de la mañana, el coche, el estrés en el trabajo.",
                "Atravesar el deseo como una ola que sube y baja, en vez de una exigencia que hay que satisfacer.",
                "Tu motivo para dejarlo, con tus palabras: salud, dinero, tus hijos, el aire, el control.",
                "El cambio de «estoy intentando dejarlo» a alguien que no fuma.",
            ],
            "expect": "Las sesiones duran de 15 a 30 minutos y terminan plenamente despierto. Mucha gente "
                      "escucha a diario durante las primeras semanas — cuando las señales aprietan más — "
                      "y después guarda una sesión para los días difíciles.",
            "faq": [
                ("¿Una sesión me hará dejar de fumar?",
                 "No. Onira acompaña una decisión que ya has tomado; no es un tratamiento ni hace "
                 "ninguna afirmación clínica. Los sustitutos de nicotina, la medicación prescrita y los "
                 "servicios de deshabituación conviene consultarlos con un médico o farmacéutico."),
                ("¿Cuándo debo escucharla?",
                 "Idealmente antes de los momentos del día en que las ganas son más fuertes, y de nuevo "
                 "cuando se acerque un día difícil."),
                ("¿Sirve también para el vapeo?",
                 "La estructura es la misma: escribe lo que realmente quieres dejar y la sesión se "
                 "escribe alrededor de eso."),
            ],
        },
        "focus": {
            "slug": "concentracion",
            "nav": "Concentración",
            "card": "Ordenar una mente dispersa antes de un trabajo exigente.",
            "title": "Autohipnosis para la concentración | Onira",
            "desc": "Autohipnosis guiada para la concentración, escrita en tu teléfono a partir del "
                    "trabajo que tienes por delante y narrada en voz alta. Funciona sin conexión.",
            "h1": "Autohipnosis para la concentración",
            "lede": "Una sesión más corta y más despierta para despejar el ruido antes de estudiar, "
                    "escribir o trabajar durante un buen rato.",
            "why_title": "Por qué la hipnosis ayuda a concentrarse",
            "why": [
                "Perder la concentración no suele ser falta de atención, sino exceso de cosas que la "
                "reclaman: notificaciones, tareas a medias, el zumbido de todo lo demás que deberías "
                "estar haciendo. La atención ya está puesta en algo; simplemente no en lo que tienes "
                "delante.",
                "La hipnosis es, en su definición más simple, atención enfocada y sostenida. La sesión "
                "estrecha el campo a propósito, aparta lo que no toca ahora y ensaya el empezar, que "
                "suele ser la parte más difícil de un tramo largo de trabajo.",
            ],
            "works_on": [
                "Estrechar la atención a una sola tarea y dejar el resto durante un tiempo definido.",
                "La fricción de arrancar, ensayada hasta que el primer minuto no tenga nada de especial.",
                "Volver a la tarea tras una interrupción sin perder el hilo.",
                "Un trabajo concreto, si lo nombras: un examen, un capítulo, una entrega, una fecha límite.",
            ],
            "expect": "Escucha una sesión de concentración justo antes del trabajo. Termina despierto y "
                      "con impulso, no adormilado, para que puedas pasar directamente a la tarea.",
            "faq": [
                ("¿Debo escucharla mientras trabajo?",
                 "No: escucha primero y trabaja después. La sesión pide tu atención; la tarea la "
                 "necesita a continuación."),
                ("¿Sirve para estudiar?",
                 "Es uno de los usos más frecuentes. Nombrar la asignatura y la fecha del examen hace "
                 "la sesión mucho más concreta."),
                ("¿Puedo hacerla más corta?",
                 "Las sesiones apuntan a 15-30 minutos. Puedes parar cuando quieras; no se rompe nada "
                 "si terminas antes."),
            ],
        },
        "weight": {
            "slug": "perdida-de-peso",
            "nav": "Peso",
            "card": "Trabajar los hábitos y la relación con la comida, no las reglas.",
            "title": "Autohipnosis para el peso y los hábitos alimentarios | Onira",
            "desc": "Autohipnosis guiada para el peso y los hábitos alimentarios, escrita en tu teléfono "
                    "a partir de tus propios patrones y narrada en voz alta.",
            "h1": "Autohipnosis para el peso y los hábitos alimentarios",
            "lede": "Una sesión sobre los momentos que rodean el comer — la noche, el aburrimiento, la "
                    "recompensa — más que sobre lo que estaría permitido.",
            "why_title": "Por qué se usa la hipnosis para los hábitos alimentarios",
            "why": [
                "Casi todo lo que la gente quiere cambiar de su forma de comer no nace del hambre. Es un "
                "hábito pegado a un momento: la hora después de cenar, la vuelta a casa, el final de un "
                "día duro, tener algo que hacer con las manos. Las reglas no llegan ahí, porque el "
                "momento aparece antes que cualquier decisión.",
                "Una sesión de hipnosis ensaya esos momentos de otra manera: notar la señal, dejarla "
                "pasar y construir una relación más tranquila con la comida en general. El énfasis está "
                "en el cómo y el porqué, no en la restricción.",
            ],
            "works_on": [
                "El momento exacto en que se dispara el hábito, si lo nombras: la noche, el estrés, el aburrimiento, una celebración.",
                "Comer despacio y notar la saciedad en lugar de terminar en automático.",
                "Separar el apetito de la búsqueda de consuelo, sin convertir ninguno en un fracaso.",
                "Un tono interno más estable, porque la autocrítica alimenta el ciclo en vez de romperlo.",
            ],
            "expect": "Las sesiones duran de 15 a 30 minutos y terminan plenamente despierto. Escuchar a "
                      "una hora constante — mucha gente elige el final de la tarde, antes de las horas "
                      "más difíciles — funciona mejor que escuchar solo después de un mal día.",
            "faq": [
                ("¿Esto es una dieta?",
                 "No. Onira no da ningún consejo dietético, nutricional ni médico, y no fija reglas "
                 "sobre la comida. Trabaja los hábitos y la relación con el comer."),
                ("¿Voy a adelgazar con esto?",
                 "No se promete nada de eso. El peso es un asunto médico: un médico o un dietista es el "
                 "lugar adecuado para un plan."),
                ("¿Y si tengo antecedentes de trastorno alimentario?",
                 "Habla con un profesional en lugar de usar una herramienta de autoayuda. Onira no está "
                 "diseñada para los TCA y redirige el contenido que va en esa dirección."),
            ],
        },
        "fear": {
            "slug": "miedos-y-fobias",
            "nav": "Miedos y fobias",
            "card": "Ensayar en calma el vuelo, la carretera o la altura.",
            "title": "Autohipnosis para los miedos y las fobias | Onira",
            "desc": "Hipnosis guiada para el miedo a volar, a conducir o a las alturas, escrita en "
                    "tu móvil a partir de la situación que afrontas. Gratis y sin conexión.",
            "h1": "Autohipnosis para los miedos y las fobias",
            "lede": "Una sesión construida alrededor de una situación concreta — el vuelo, el "
                    "ascensor, la autopista — ensayada lo bastante despacio como para que el "
                    "cuerpo deje de tratarla como una emergencia.",
            "why_title": "Por qué la hipnosis ayuda con un miedo concreto",
            "why": [
                "Un miedo no se razona. La reacción llega antes que el razonamiento: el pecho se "
                "cierra, la atención se estrecha y todo ha terminado antes de que un pensamiento "
                "sensato tenga su turno. La hipnosis guiada trabaja sobre lo que se mueve primero "
                "— un ritmo lento y una respiración pausada sacan del estado de alerta, y un "
                "cuerpo fuera de alerta no responde igual al mismo detonante.",
                "Después, la sesión ensaya la escena en lugar de evitarla. Pasas la puerta de "
                "embarque, la rotonda, el ascensor de cristal, a una velocidad en la que sigues "
                "en calma. Ese ensayo repetido es lo que vuelve familiar la situación real, en "
                "lugar de repentina.",
            ],
            "works_on": [
                "La subida física — respiración, pecho, manos — frenada a propósito antes de la escena.",
                "La evitación misma: la situación encoge cada vez que se atraviesa con calma en el ensayo.",
                "Un ancla para el momento: una respiración, una palabra, un gesto que devuelve el estado.",
                "Tu propia situación, si la escribes: un vuelo el mes que viene, un examen, un túnel.",
            ],
            "expect": "Las sesiones duran entre 15 y 30 minutos. Estás consciente en todo momento "
                      "y la sesión termina siempre devolviéndote a la vigilia, así que sirve la "
                      "misma mañana del vuelo, no solo la víspera. Con auriculares y en un sitio "
                      "donde nadie te interrumpa.",
            "faq": [
                ("¿La autohipnosis cura una fobia?",
                 "No. La relajación guiada y el ensayo mental son una herramienta de autoayuda, "
                 "útil para un miedo cotidiano. Una fobia que limita tu vida la trata un "
                 "profesional, a menudo con muy buenos resultados: ahí es donde hay que ir."),
                ("¿Puedo escucharla durante el vuelo?",
                 "Sí, y mucha gente lo hace. La sesión termina devolviéndote a la vigilia, así que "
                 "vale antes y durante — pero nunca conduciendo, ni siquiera una sesión sobre "
                 "conducir."),
                ("¿Tengo que describir lo que me da miedo?",
                 "No, basta con el tema. Si lo describes, el ensayo se vuelve más preciso — y se "
                 "queda en tu móvil, porque el modelo funciona en local."),
            ],
        },
        "letting_go": {
            "slug": "olvidar-a-alguien",
            "nav": "Pasar página",
            "card": "Dejar de repetir la misma conversación en bucle.",
            "title": "Autohipnosis para olvidar a alguien | Onira",
            "desc": "Hipnosis guiada para pasar página tras una ruptura, escrita en tu móvil a "
                    "partir de lo que se te repite en la cabeza. Gratis y sin conexión.",
            "h1": "Autohipnosis para pasar página",
            "lede": "Una sesión para cuando la persona ya se ha ido pero tu cabeza sigue "
                    "manteniendo la conversación.",
            "why_title": "Por qué la hipnosis ayuda a pasar página",
            "why": [
                "Lo que desgasta después de una ruptura no es el recuerdo: es la repetición. Vuelve "
                "la misma escena, la misma frase, la respuesta que deberías haber dado. Cada "
                "pasada reabre el asunto en lugar de cerrarlo, y decidir dejar de pensar en ello "
                "es pensar en ello otra vez.",
                "Una sesión guiada no intenta borrar a nadie — no se puede, y no es el objetivo. "
                "Reduce la carga que lleva pegada el recuerdo: en un estado de calma, la escena se "
                "revisita a distancia y más despacio, hasta que deja de disparar la misma "
                "reacción. El recuerdo se queda; el aguijón se gasta.",
            ],
            "works_on": [
                "La rumiación nocturna, cuando la conversación se reanuda en cuanto llega el silencio.",
                "Las ganas de mirar su perfil, tratadas como un hábito y no como una debilidad.",
                "Devolver la atención a ti: lo que quieres, al margen de esa persona.",
                "Una escena concreta, si la escribes: el último mensaje, un lugar, una fecha que vuelve.",
            ],
            "expect": "Las sesiones duran entre 15 y 30 minutos y terminan devolviéndote a la "
                      "vigilia. Las primeras a veces remueven un poco: es normal cuando el tema es "
                      "reciente. Si una sesión te sienta bien, guárdala y repite la misma — aquí "
                      "la repetición hace la mayor parte del trabajo.",
            "faq": [
                ("¿Voy a olvidar a esa persona?",
                 "No, y sería una mala promesa. Lo que cambia es la intensidad: el recuerdo vuelve "
                 "menos veces y pesa menos. Es lo que hace el tiempo, algo más dirigido."),
                ("¿Y si es un duelo y no una ruptura?",
                 "Las sesiones pueden calmar las noches difíciles, pero un duelo no es algo que "
                 "resuelva una aplicación. El acompañamiento humano importa más, y Onira no está "
                 "escrita para eso."),
                ("¿Hace falta escribir su nombre?",
                 "No hace falta, basta con el tema. Lo que escribas no sale nunca del móvil: la "
                 "generación ocurre en local y no se envía nada."),
            ],
        },
        "learning": {
            "slug": "memoria-y-aprendizaje",
            "nav": "Memoria",
            "card": "Entrar en el estado en el que estudiar de verdad cuaja.",
            "title": "Autohipnosis para la memoria y el estudio | Onira",
            "desc": "Hipnosis guiada para estudiar, memorizar y aprender idiomas, escrita en tu "
                    "móvil a partir de lo que estás aprendiendo. Gratis y sin conexión.",
            "h1": "Autohipnosis para la memoria y el aprendizaje",
            "lede": "Una sesión para el estado que el aprendizaje necesita — atención sin prisa y "
                    "sin ruido — escrita alrededor del examen, el idioma o el material que tienes "
                    "delante.",
            "why_title": "Por qué la hipnosis ayuda a estudiar",
            "why": [
                "La mayoría de los problemas de estudio no son problemas de memoria, sino de "
                "estado: media atención está en la fecha de entrega, en el móvil o en lo mal que "
                "va la cosa. Lo que se graba en ese estado es fino, y por eso una hora de repaso "
                "angustiado deja casi nada.",
                "Una sesión guiada baja primero el ruido y coloca el material en el silencio que "
                "queda. El recuerdo se ensaya tal como hará falta — la palabra que llega en una "
                "conversación, la respuesta que llega en el examen — de modo que la práctica se "
                "parezca al momento real.",
            ],
            "works_on": [
                "La inquietud que convierte una sesión de estudio en diez minutos de pantalla.",
                "La recuperación el día del examen: ensayar el recordar, no solo releer.",
                "Aprender idiomas — oírte hablarlo sin la vergüenza que suele frenar.",
                "Una materia concreta, si la escribes: una fecha de examen, una lista de vocabulario.",
            ],
            "expect": "Las sesiones duran entre 15 y 30 minutos y terminan devolviéndote a la "
                      "vigilia: están pensadas para usarse antes de estudiar, no en lugar de "
                      "estudiar. Una sesión guardada se puede repetir antes de cada bloque de repaso.",
            "faq": [
                ("¿Sirve para aprender mientras duermo?",
                 "No. Aprender dormido no es algo que la hipnosis consiga, y Onira no lo promete. "
                 "Lo que una sesión sí hace es dejarte en un estado donde el estudio deliberado "
                 "cunde más — estudiar hay que estudiar igual."),
                ("¿Puede ayudarme a recordar algo olvidado?",
                 "Con el recuerdo cotidiano sí — un nombre, una lista, dónde quedó algo. La "
                 "hipnosis no es una forma fiable de recuperar recuerdos lejanos o dolorosos, y "
                 "Onira no está escrita para eso."),
                ("¿Sirve para aprender inglés?",
                 "Sobre todo para la parte de confianza. Las sesiones ensayan hablar sin frenarse, "
                 "que es lo que suele bloquear un idioma que ya conoces a medias."),
            ],
        },
        "pain": {
            "slug": "dolor",
            "nav": "Dolor",
            "card": "Aflojar la tensión y el temor que hacen el dolor más ruidoso.",
            "title": "Autohipnosis y dolor — escrita para ti | Onira",
            "desc": "Autohipnosis guiada junto a tu tratamiento: menos tensión, menos temor a la "
                    "próxima crisis, noches más llevaderas. Una herramienta de alivio, no una cura.",
            "h1": "Autohipnosis para convivir con el dolor",
            "lede": "Una sesión para lo que en el dolor no es la lesión: la tensión con que te "
                    "proteges, el temor a la próxima crisis y las noches que te quita.",
            "why_title": "Qué puede y qué no puede hacer la hipnosis con el dolor",
            "why": [
                "El dolor nunca es solo una señal del cuerpo. Cuánta atención ocupa, con cuánta tensión "
                "te proteges a su alrededor, cuánto temes el próximo episodio: todo eso cambia su "
                "intensidad vivida. Son esas partes las que una sesión guiada puede alcanzar, y suelen "
                "marcar la diferencia entre un día difícil y un día imposible.",
                "Lo que no hace es eliminar la causa. Este tema está escrito como acompañamiento de tu "
                "tratamiento, nunca como sustituto, y no es motivo para saltarte una cita ni cambiar lo "
                "que te han recetado. Un dolor nuevo, que empeora o sin explicación es primero cosa de "
                "un médico.",
            ],
            "works_on": [
                "La protección refleja y la tensión muscular que se acumulan alrededor de una zona dolorida.",
                "Conciliar el sueño cuando el dolor devuelve la atención una y otra vez.",
                "La anticipación de la próxima crisis, que lo tensa todo antes de que llegue.",
                "El lugar del dolor en el día: en el borde de la atención en vez de en el centro.",
            ],
            "expect": "Las sesiones duran entre 15 y 30 minutos y terminan devolviéndote al estado de "
                      "alerta. Lo que la gente describe suele ser parcial y temporal — bajar el volumen, "
                      "no apagarlo — y llega con la repetición, no de una vez.",
            "faq": [
                ("¿La hipnosis puede curar mi dolor?",
                 "No, y lo que afirme lo contrario te está vendiendo algo. La relajación y la sugestión "
                 "se usan habitualmente junto a la atención médica para hacer el dolor más llevadero. "
                 "Onira es una herramienta de relajación en ese sentido: un complemento, no un "
                 "tratamiento."),
                ("¿Lo seguiré sintiendo?",
                 "Lo más probable es que sí. El objetivo realista es que ocupe menos: menos tensión "
                 "alrededor, menos temor antes, más sitio para el resto del día."),
                ("¿Es compatible con mi medicación?",
                 "Una sesión no interactúa con nada de lo que tomas. Lo importante es que nunca "
                 "reduzcas ni dejes un tratamiento recetado porque una sesión te alivió: esa decisión "
                 "es de quien te lo recetó."),
                ("¿Y para la migraña?",
                 "La tensión y la anticipación alrededor de la crisis sí son alcanzables; la crisis en "
                 "sí es un fenómeno neurológico y un asunto médico. No uses una sesión en lugar de un "
                 "tratamiento que te funciona."),
            ],
        },
        "ibs": {
            "slug": "intestino-irritable",
            "nav": "Intestino irritable",
            "card": "Calmar el bucle intestino-cerebro que mantiene los brotes.",
            "title": "Autohipnosis y síndrome de intestino irritable | Onira",
            "desc": "Autohipnosis guiada para la parte de estrés del SII: vientre más calmado, menos "
                    "anticipación, días más llevaderos. Un complemento, no un tratamiento.",
            "h1": "Autohipnosis y síndrome de intestino irritable",
            "lede": "Una sesión para el bucle en el que el estrés agrava los síntomas y los síntomas "
                    "alimentan el estrés — la parte del SII que responde a la calma.",
            "why_title": "Por qué la relajación llega al intestino",
            "why": [
                "El intestino y el sistema nervioso hablan sin parar. Por eso una semana tensa se nota "
                "en la digestión, y por eso el miedo a un brote en el peor momento basta a veces para "
                "provocarlo. La relajación guiada actúa justo sobre ese eje: baja el estado de alerta "
                "que mantiene el bucle en marcha.",
                "Conviene ser preciso, porque la distinción importa: la hipnoterapia dirigida al "
                "intestino es una opción reconocida en el manejo del SII, recomendada por las guías "
                "clínicas cuando otros enfoques no han bastado — pero es un programa estructurado "
                "impartido por un terapeuta formado. Onira no es ese programa. Es una herramienta de "
                "relajación que trabaja sobre el mismo eje del estrés, al lado de tu seguimiento y no "
                "en su lugar.",
            ],
            "works_on": [
                "La anticipación: organizar el día según dónde están los baños, y lo que eso cuesta.",
                "La tensión abdominal y la respiración contenida durante un brote.",
                "El sueño, que sufre en ambos sentidos cuando los síntomas están activos.",
                "Una situación concreta, si la escribes: un viaje largo, un restaurante, un día en la oficina.",
            ],
            "expect": "Las sesiones duran entre 15 y 30 minutos. Los síntomas digestivos cambian "
                      "despacio: júzgalo por varias semanas de uso regular, no por una sesión.",
            "faq": [
                ("¿Es lo mismo que la hipnoterapia dirigida al intestino?",
                 "No. Esa es un programa estructurado con un terapeuta formado, normalmente varias "
                 "sesiones a lo largo de dos o tres meses. Onira escribe sesiones de relajación a "
                 "partir de lo que le cuentas. Si quieres el protocolo clínico, pide a tu médico que "
                 "te derive."),
                ("¿Hace falta un diagnóstico primero?",
                 "Sí. Los síntomas digestivos tienen muchas causas y algunas hay que estudiarlas: "
                 "sangrado, pérdida de peso sin explicación o un cambio duradero en tu ritmo habitual "
                 "son cosa de un médico, no de una aplicación."),
                ("¿Puedo usarla durante un brote?",
                 "Sí, y mucha gente lo hace. Ponte donde nadie te interrumpa y tómalo como aflojar la "
                 "tensión alrededor del episodio, no como detenerlo."),
            ],
        },
        "emotional_recovery": {
            "slug": "calma-emocional",
            "nav": "Calma emocional",
            "card": "Reposar después de algo duro, sin volver a vivirlo.",
            "title": "Autohipnosis y calma emocional | Onira",
            "desc": "Autohipnosis guiada para después del golpe: noches más tranquilas, menos rumiación, "
                    "días más estables. Una herramienta de relajación, no terapia de trauma.",
            "h1": "Autohipnosis para la calma emocional",
            "lede": "Una sesión para el después: cuando lo duro ya pasó pero el sueño, los nervios y la "
                    "atención todavía no lo han alcanzado.",
            "why_title": "Calmar el después, sin reabrirlo",
            "why": [
                "Después de algo difícil, el cuerpo suele quedarse en tensión mucho después del "
                "acontecimiento. Se nota en un sueño roto, en la irritabilidad, en pensamientos que "
                "vuelven en bucle por la noche, en sobresaltos que no se apagan. Son réplicas "
                "corrientes, y responden bien a una calma deliberada.",
                "Estas sesiones están escritas para calmar ese estado, no para volver a lo que lo "
                "causó. No te pedirán revisitar un recuerdo ni contar lo que pasó. Ese trabajo existe, "
                "ayuda, y se hace con un profesional formado que puede acompañarte mientras dura — no "
                "a solas con un teléfono.",
            ],
            "works_on": [
                "Un sueño que se rompió tras una época difícil y no ha vuelto.",
                "La rumiación nocturna: la misma escena repitiéndose sin resolverse.",
                "Un cuerpo en alerta: pecho apretado, mandíbula tensa, sobresaltos por nada.",
                "Atravesar días normales mientras algo pesado todavía se asienta.",
            ],
            "expect": "Las sesiones duran entre 15 y 30 minutos y terminan siempre con una vuelta "
                      "completa al estado de alerta. Si una sesión te deja con más angustia en vez de "
                      "más calma, deja de usarla y háblalo con alguien cualificado.",
            "faq": [
                ("¿Esto trata el trauma o el estrés postraumático?",
                 "No, y no está escrito para intentarlo. Las reviviscencias, las pesadillas, la "
                 "disociación o una evitación que organiza tu vida tienen tratamiento — con un "
                 "clínico formado en trauma. Onira es una herramienta de relajación para el después, "
                 "para usar junto a esa ayuda si la tienes."),
                ("¿Una sesión me hará recordar cosas?",
                 "No es su diseño, y no te invitará a ir a buscarlas. La hipnosis tampoco es una forma "
                 "fiable de recuperar recuerdos — un resultado bien establecido, y una de las razones "
                 "por las que este tema se queda en calmar el presente en vez de hurgar en el pasado."),
                ("¿Y si me siento peor durante una sesión?",
                 "Párala, abre los ojos, vuelve a la habitación. Esa reacción es una señal de que "
                 "conviene trabajar con una persona y no con una aplicación, y merece tomarse en "
                 "serio en vez de forzarla."),
                ("¿El duelo es lo mismo?",
                 "Lo bastante parecido como para que el tema sirva. Las sesiones pueden estabilizar los "
                 "días y las noches; no acortarán un duelo, y no es su función."),
            ],
        },
        "mental_reset": {
            "slug": "reprogramar-la-mente",
            "nav": "Reprogramar la mente",
            "card": "Calmar la mente y ensayar otra forma de reaccionar.",
            "title": "Autohipnosis para reprogramar tu mente | Onira",
            "desc": "Autohipnosis guiada para calmar la mente y ensayar respuestas nuevas ante lo que "
                    "siempre te dispara. Escrita en tu teléfono, privada y sin conexión.",
            "h1": "Autohipnosis para reprogramar tu mente",
            "lede": "Una sesión para lo que se repite solo: la reacción automática, el pensamiento de "
                    "siempre, el bucle que ya conoces de memoria.",
            "why_title": "Qué significa de verdad \"reprogramar\"",
            "why": [
                "La palabra sugiere abrir la cabeza y cambiar una línea de código. No funciona así, y "
                "vale la pena decirlo: lo que cambia con la repetición no es un programa sino una "
                "costumbre mental — la respuesta que aparece primero, antes de que decidas nada.",
                "Ahí es donde una sesión guiada tiene sentido. Primero baja el ruido, porque una mente "
                "acelerada no ensaya nada; después te hace recorrer la escena de siempre con otra "
                "reacción, con calma y en detalle. Ensayada varias veces, esa versión empieza a llegar "
                "antes que la automática. Es lento y es repetición, no un interruptor.",
            ],
            "works_on": [
                "Calmar una mente que no para — el paso previo, sin el cual lo demás no sirve.",
                "La reacción automática ante algo concreto: una crítica, un atasco, un mensaje que no llega.",
                "El diálogo interno que ya sabes de memoria, ensayado en una versión más justa.",
                "Una escena que puedes nombrar: una reunión, una conversación pendiente, una rutina que quieres cambiar.",
            ],
            "expect": "Las sesiones duran entre 15 y 30 minutos y terminan devolviéndote al estado de "
                      "alerta. Lo que se nota primero es la calma; el cambio de reacción llega con "
                      "semanas de repetición, no con una sesión.",
            "faq": [
                ("¿De verdad se puede reprogramar la mente?",
                 "No como un ordenador, y desconfía de quien lo prometa. Lo que sí se puede es ensayar "
                 "una respuesta distinta hasta que aparezca sola, que es como cambia cualquier "
                 "costumbre. Onira está escrita para ese ensayo, no para un borrado y reinstalación."),
                ("¿En cuánto tiempo se nota?",
                 "La parte de calma, casi enseguida. La parte de reacción, con repetición regular — "
                 "piensa en semanas de uso frecuente y en una escena concreta cada vez, no en un "
                 "propósito general."),
                ("¿Es lo mismo que las afirmaciones?",
                 "Se parecen en la superficie y se diferencian en el estado. Repetir una frase con la "
                 "cabeza acelerada rebota; la sesión primero baja ese ruido y luego trabaja la escena "
                 "entera, no una frase suelta."),
                ("¿Sirve para calmar la mente antes de dormir?",
                 "Sí, aunque la sesión termina devolviéndote al estado de alerta. Si lo que buscas es "
                 "dormirte, el tema de sueño está escrito justo para eso."),
            ],
        },
    },
}

# ----------------------------------------------------------------- guides ----

# Question pages, as opposed to the theme pages above. A theme page answers
# "I want a session about X"; a guide answers a question someone types before
# they know an app is the answer — which is where the traffic that has never
# heard of Onira comes from. Each one ends on the app as the concrete answer
# rather than opening with it.
#
# Same contract as THEMES: the keys are matched across languages to build the
# hreflang set, the slugs are not, and a guide only has to exist where the
# question is actually asked. The order here is the order of the nav cards and
# the sitemap.
GUIDES = ["fall_asleep", "vs_meditation", "does_it_work", "street_hypnosis",
          "is_it_safe", "learn_self_hypnosis"]

EN["guide_dir"] = "guides"
EN["ui"]["guides_title"] = "Questions people ask"
EN["ui"]["guides_crumb"] = "Guides"
EN["ui"]["guide_answer_title"] = "The short answer"
EN["ui"]["guide_cta_title"] = "Try it tonight"
EN["guides"] = {
    "fall_asleep": {
        "slug": "how-to-fall-asleep-with-self-hypnosis",
        "nav": "Falling asleep",
        "card": "The method, step by step, for the nights your mind will not stop.",
        "title": "How to Fall Asleep With Self-Hypnosis | Onira",
        "desc": "A step-by-step self-hypnosis method for falling asleep when your mind "
                "will not stop, and what to do when it does not work the first time.",
        "h1": "How to fall asleep with self-hypnosis",
        "lede": "A practical method for the nights when the body is tired and the mind "
                "is still running — and an honest account of what it can and cannot do.",
        "answer": "Lie down, let your eyes close, and count slowly down from twenty, "
                  "letting each number land on an out-breath. At every number, release one "
                  "specific place — jaw, shoulders, hands. When you reach one, picture a "
                  "single quiet scene in as much sensory detail as you can hold, and stay "
                  "in it. The point is not to force sleep; it is to give the mind one slow "
                  "thing to do instead of the fast ones it had planned.",
        "sections": [
            ("Why counting yourself down works",
             ["Insomnia at the start of the night is rarely a lack of tiredness. It is a "
              "mind that has been given nothing to do and has filled the gap with tomorrow. "
              "Self-hypnosis works on that gap directly: a slow, repetitive, mildly "
              "demanding task occupies exactly the attention that would otherwise rehearse "
              "an argument or a deadline.",
              "The descending count matters more than the number. Counting down implies "
              "arrival, and pairing each number with an out-breath slows the breath without "
              "you having to think about breathing — which is the reliable way to shift the "
              "nervous system out of its alert setting."],
             []),
            ("The method, step by step",
             ["None of this needs training, and none of it needs you to believe in anything. "
              "It needs about fifteen minutes and a willingness to start over when you drift "
              "into thinking, which you will."],
             ["Set the room up first: dark, cool, phone face down. Deciding to check "
              "something halfway through is what ends most attempts.",
              "Lie on your back, arms at your sides, and take three breaths that are longer "
              "on the way out than on the way in.",
              "Count down from twenty. Say each number silently as you breathe out.",
              "With each number, release one place: jaw, tongue, shoulders, hands, stomach, "
              "thighs, feet. Naming the place is what makes it let go.",
              "At one, choose a scene — a beach at dusk, a path through trees, a room you "
              "remember — and fill it in: the temperature, the sound, what is underfoot.",
              "When you notice you have wandered off into thinking, do not start again from "
              "twenty. Pick the count back up wherever you left it and carry on."]),
            ("What to do when it does not work",
             ["The first few attempts often end in a wandering mind, and that is not failure "
              "— it is the ordinary way attention behaves before it settles into a habit. "
              "What changes the outcome is repetition at the same time of night, so the "
              "sequence itself becomes a cue.",
              "If you are still awake after twenty minutes or so, get up, keep the lights "
              "low, and do something dull until you feel sleepy. Lying in bed fighting for "
              "sleep teaches the body that bed is a place where you fight for sleep, which "
              "is the one association worth protecting against."],
             []),
            ("Where a written session helps",
             ["Doing this from memory means part of you is running the instructions, which "
              "is part of you staying awake. Being narrated to removes that job: you follow "
              "a voice instead of remembering a list, which is why guided sessions work "
              "better than self-directed ones for most people at bedtime.",
              "Onira writes the session on your phone around what is actually keeping you "
              "up — if you type that you cannot stop replaying a conversation, the imagery "
              "and suggestions are built on that rather than on a generic beach. It runs "
              "the model on the device, so nothing you type is uploaded, and it works with "
              "the phone offline and face down."],
             []),
        ],
        "faq": [
            ("How long does it take to fall asleep this way?",
             "Most people who get on with it fall asleep somewhere in the scene rather than "
             "at the end of the count — often fifteen to twenty-five minutes in. If you are "
             "regularly still awake at the end, treat it as a signal to look at the hours "
             "before bed rather than to try harder in bed."),
            ("Is self-hypnosis safe to do at night?",
             "For ordinary sleeplessness, yes — it is guided relaxation, and the worst "
             "common outcome is that you stay awake. It is not a treatment for a sleep "
             "disorder, and persistent insomnia, sleep apnoea or insomnia alongside low "
             "mood are matters for a doctor."),
            ("Can I use a recording instead of doing it myself?",
             "Yes, and for falling asleep a recording is usually better: it removes the job "
             "of remembering the steps. What a recording cannot do is mention the thing you "
             "are actually turning over, which is the gap a session written in the moment "
             "fills."),
        ],
    },
    "vs_meditation": {
        "slug": "hypnosis-vs-meditation",
        "nav": "Hypnosis vs meditation",
        "card": "Two states, two aims — and which one fits what you want tonight.",
        "title": "Hypnosis vs Meditation: Which to Use | Onira",
        "desc": "What actually separates guided hypnosis from meditation, what each one is "
                "good at, and how to pick between them for sleep, anxiety or a habit.",
        "h1": "Hypnosis vs meditation",
        "lede": "They look similar from the outside — eyes closed, slow breathing, a calm "
                "voice — and they are aimed at two different things.",
        "answer": "Meditation trains attention: you practise noticing where the mind went "
                  "and bringing it back, without trying to change what you find. Hypnosis "
                  "uses a relaxed, focused state to rehearse something specific — sleeping, "
                  "staying steady in a meeting, not reaching for the cigarette. If you want "
                  "a general skill, meditate. If you want to work on one named thing, a "
                  "hypnosis session is the more direct tool.",
        "sections": [
            ("What is actually different",
             ["Both practices produce a similar physiological state: slower breath, lower "
              "arousal, narrowed attention. The difference is what you do once you are "
              "there. A meditation keeps returning you to a neutral anchor and asks nothing "
              "of the content of your mind. A hypnosis session takes that same settled "
              "state and puts suggestion into it — images, phrases and rehearsals aimed at "
              "one outcome.",
              "That is also why hypnosis is structured and meditation often is not. A "
              "session has an arc: an induction that settles you, a deepening, imagery, the "
              "suggestions themselves, an anchor to carry out, and a deliberate return to "
              "full alertness. Each part exists to make the next one land."],
             []),
            ("What each one is good at",
             ["Neither is a better practice in the abstract. They answer different "
              "questions, and the honest way to choose is by what you want in the next "
              "month rather than by which sounds more serious."],
             ["Meditation, for a general relationship with your own attention: less "
              "reactivity, more room between a feeling and what you do about it. It pays "
              "off slowly and broadly.",
              "Hypnosis, for a specific target: falling asleep, a fear of flying next "
              "Tuesday, the first ten minutes of a task you keep avoiding, a habit you want "
              "interrupted.",
              "Meditation asks you to stop chasing an outcome, which is exactly what makes "
              "it frustrating when you have one.",
              "Hypnosis is outcome-shaped, which makes it easier to start with and easier "
              "to over-claim for — no session rewrites a life in one sitting."]),
            ("Is one of them better evidenced?",
             ["Both have a real literature and both have more enthusiasm than evidence "
              "around the edges. Mindfulness-based programmes have the larger body of "
              "clinical work, mostly around stress, relapse in depression and chronic pain. "
              "Clinical hypnotherapy has a narrower but genuine record — pain and procedural "
              "distress are its strongest showing, with useful results for sleep onset and "
              "irritable bowel symptoms.",
              "What neither has is a claim to replace treatment. Both are adjuncts: things "
              "that help alongside care, not instead of it."],
             []),
            ("You do not have to pick one",
             ["A common and sensible pattern is meditation as the daily practice and a "
              "hypnosis session for the specific thing that is in the way this week. They "
              "do not compete; if anything, regular meditation makes the settling stage of a "
              "session faster.",
              "Onira sits on the hypnosis side of this. You pick the target, add a sentence "
              "about what is actually going on, and a model running on the phone writes a "
              "session around it, then narrates it — no account, nothing uploaded, and "
              "nothing generic about the imagery."],
             []),
        ],
        "faq": [
            ("Can hypnosis make me do something I do not want to do?",
             "No. In a self-hypnosis session you stay aware and in control throughout, and "
             "suggestions that cut against what you actually want simply do not take. "
             "Stage hypnosis is entertainment built on volunteers who are willing to play "
             "along, and it is not what a therapeutic session is."),
            ("Which is better for anxiety?",
             "For anxiety as a general pattern, meditation has the better long-run "
             "evidence. For a specific anxious situation you can name — a flight, a "
             "presentation, a scan — rehearsing it in a hypnosis session tends to be more "
             "useful than sitting with the breath."),
            ("Is guided meditation the same as hypnosis?",
             "It is the nearest thing. A guided meditation that visualises an outcome and "
             "repeats suggestions is doing most of what a hypnosis session does; the label "
             "differs more than the practice."),
        ],
    },
    "does_it_work": {
        "slug": "does-self-hypnosis-work",
        "nav": "Does it work?",
        "card": "What the evidence supports, what it does not, and who it fails.",
        "title": "Does Self-Hypnosis Actually Work? | Onira",
        "desc": "An honest look at what self-hypnosis is good for, what the evidence "
                "supports, who it does not work for, and how to tell it is doing something.",
        "h1": "Does self-hypnosis actually work?",
        "lede": "Yes, for some things, moderately, and not for everyone — which is a duller "
                "answer than either side of the argument usually gives.",
        "answer": "Self-hypnosis has decent evidence for sleep onset, for pain and "
                  "procedural distress, and for lowering the arousal that feeds anxiety in a "
                  "specific situation. It has weak evidence as a standalone treatment for "
                  "anything clinical, and roughly one person in four responds poorly to "
                  "suggestion regardless of technique. It is a real tool with a narrow "
                  "remit, not a cure and not a placebo.",
        "sections": [
            ("What it is good at",
             ["The clearest results are the least dramatic ones. Getting to sleep faster, "
              "sitting through a dental or medical procedure with less distress, taking the "
              "edge off pain, and going into one identifiable stressful event calmer than "
              "you otherwise would. All of these share a shape: a short horizon and a "
              "physical component that relaxation genuinely moves.",
              "Habit work — smoking, nail biting, the first ten minutes of an avoided task "
              "— sits a step below that. Sessions help, most reliably as one part of a plan "
              "rather than as the plan, and the effect comes from repetition rather than "
              "from any single session being powerful."],
             []),
            ("What it is not",
             ["It is not therapy, and it does not treat depression, an anxiety disorder, "
              "PTSD or an eating disorder. It is not a way to recover forgotten memories — "
              "suggestion makes memory less reliable, not more. It is not a substitute for "
              "medication anyone has prescribed you, and no honest session will suggest "
              "otherwise.",
              "It is also not fast. The marketing around hypnosis leans on single dramatic "
              "sessions, and the actual pattern is a modest effect that accumulates with "
              "daily use over weeks."],
             []),
            ("Why it does not work for everyone",
             ["Suggestibility varies between people and is fairly stable over a lifetime. "
              "Somewhere around one in four people respond weakly to hypnotic suggestion no "
              "matter how it is delivered, and about the same proportion respond strongly. "
              "That is not a matter of intelligence or willpower, and there is no technique "
              "that reliably moves someone from one group to the other.",
              "The practical consequence is worth knowing before you start: if three or "
              "four honest attempts do nothing at all, the reasonable conclusion is that "
              "this is not your tool, rather than that you did it wrong."],
             []),
            ("How to tell whether it is doing anything",
             ["Judge it on the target, not on the experience. People expect to feel "
              "hypnotised and mostly do not — the state is unremarkable from the inside, "
              "closer to being absorbed in a book than to anything theatrical. Feeling "
              "nothing special during a session says very little about whether it worked.",
              "Pick one measurable thing and watch it for two weeks: minutes to fall "
              "asleep, cigarettes in a day, whether you started the task. If the number "
              "moves, keep going; if it does not, stop and try something else. That is a "
              "better test than any account of how deep you went."],
             []),
            ("Where Onira fits",
             ["Onira is a relaxation and self-hypnosis tool, and deliberately not sold as "
              "more than that. What it changes about the usual offering is specificity: "
              "instead of a recording made for everyone, a model on your phone writes the "
              "session around the theme you pick and the sentence you type, then narrates "
              "it aloud.",
              "It runs entirely on the device, so what you type about your own life never "
              "leaves the phone — there is no account and no server that could read it. If "
              "you are in real distress, that is a conversation to have with a person, and "
              "no app is the right answer to it."],
             []),
        ],
        "faq": [
            ("Is self-hypnosis just the placebo effect?",
             "Expectation is a real part of it, as it is in most of medicine. But hypnotic "
             "responding shows up in ways placebo alone does not predict — it varies by "
             "trait suggestibility, and imaging studies find state changes that track it. "
             "The fair summary is a modest genuine effect with an expectation component on "
             "top."),
            ("How often should I do a session?",
             "Daily, for two or three weeks, if you are working on a habit or on sleep. The "
             "effect is cumulative, and the single biggest predictor of getting anything "
             "out of it is having actually done it repeatedly."),
            ("Can I get stuck in hypnosis?",
             "No. Without a voice guiding you, the state simply fades or turns into sleep. "
             "A session that ends properly includes a deliberate return to full alertness "
             "for comfort, not for safety."),
        ],
    },
    "street_hypnosis": {
        "slug": "how-street-hypnosis-works",
        "nav": "Street hypnosis",
        "card": "Real, not mind control — and the same mechanism works on yourself.",
        "title": "How Street Hypnosis Works (And Is It Real?) | Onira",
        "desc": "What is really happening in street hypnosis: the stiff arm, the "
                "handshake, why it works on some people and not others, and "
                "whether it is legal.",
        "h1": "How street hypnosis works",
        "lede": "The stiff arm, the frozen handshake, the volunteer who forgets their own "
                "name — what is going on there, and how much of it is real.",
        "answer": "Street hypnosis is real, and it is not mind control. What the hypnotist "
                  "uses is suggestion, expectation and the volunteer's own willingness to "
                  "go along with the frame — plus a quick screening step that finds the "
                  "people who respond strongly, because roughly one person in four does. "
                  "Nobody is controlled, nobody loses their memory of it, and nobody does "
                  "anything they would genuinely refuse. The same mechanism, minus the "
                  "theatre, is what self-hypnosis uses when you direct it at yourself.",
        "sections": [
            ["What is actually happening",
             ["Hypnosis is focused attention plus suggestion. Narrow someone's attention "
              "hard enough, give them a clear expectation of what is about to happen, and "
              "suggestions start being acted on before the usual critical checking gets "
              "involved. That is the whole mechanism, on a street corner or in a session.",
              "The street version adds two things a recorded session cannot. First, a "
              "person who is socially committed: they stopped, they agreed, people are "
              "watching, and backing out now would be its own small embarrassment. Second, "
              "selection — the hypnotist tries several people and keeps the ones who "
              "respond, which is why the clips you see are all successes."],
             []],
            ["The stiff arm and the frozen handshake",
             ["The set pieces are less mysterious than they look, and each one has a job:"],
             ["**Suggestibility tests** — the stiff arm that will not bend, hands stuck "
              "together, eyelids that will not open. These come first because they tell "
              "the hypnotist how responsive someone is before anything bigger is tried.",
              "**Convincers** — the same tests, doing a second job. Feeling your own arm "
              "refuse to bend is far more persuasive than being told it will, and that "
              "belief makes the next suggestion land harder.",
              "**Pattern interrupt** — the handshake induction. An automatic social action "
              "is started and then broken mid-way, leaving a half-second of blankness, and "
              "a clear instruction is dropped into it. It is surprise used as a doorway, "
              "not a magic word.",
              "**Compliance and rapport** — the unglamorous ingredient. The volunteer wants "
              "this to work. That is not cheating; wanting it is part of how suggestion "
              "works at all."]],
            ["Is it real, or are they actors?",
             ["Mostly real, with the caveat that you are watching an edit. Responsiveness "
              "to hypnotic suggestion varies between people and is fairly stable across a "
              "lifetime: around one in four people respond strongly, about the same "
              "proportion barely respond at all, and the rest sit in between. A street "
              "hypnotist finds the first group and films them.",
              "What is not real is the loss of self. Volunteers stay aware throughout, "
              "remember it afterwards, and can stop whenever they decide to. The dramatic "
              "part — someone unable to recall their name for ten seconds — is a temporary "
              "suggestion someone is going along with, not an off switch."],
             []],
            ["Is hypnosis illegal?",
             ["Doing it is generally legal, and performing it in public is what gets "
              "regulated rather than the thing itself. The United Kingdom is the clearest "
              "example: the Hypnotism Act 1952 requires a licence from the local authority "
              "before hypnotism is performed as public entertainment. Elsewhere the rules "
              "vary by country and sometimes by city, and some places restrict who may use "
              "hypnosis in a clinical context.",
              "The part that matters more than licensing is consent. Hypnotising a stranger "
              "who has not clearly agreed is not a prank, and \"they said yes after I "
              "started\" is not agreement. If you try any of this, ask first, take no for "
              "an answer, and leave anyone who seems distressed alone."],
             []],
            ["What it means if you want to try it on yourself",
             ["Here is the part the videos bury: the mechanism does not need an audience, a "
              "stranger, or a handshake. Attention, expectation and suggestion are the "
              "working parts, and all three are available when you are the one giving the "
              "instructions. What you lose is the spectacle. What you gain is that you can "
              "point it at something you actually want — sleep, a fear, a habit, the hour "
              "before a difficult conversation.",
              "It is also slower and duller than a street clip, and honest about it: the "
              "effect comes from repetition over weeks, not from one dramatic moment. If "
              "you are in the quarter of people who respond strongly, you will notice "
              "quickly. If three or four honest attempts do nothing, this is probably not "
              "your tool."],
             []],
            ["Where Onira fits",
             ["Onira writes self-hypnosis sessions on your phone and narrates them aloud — "
              "you pick a theme, optionally say what is actually going on, and a model "
              "running on the device writes the script and speaks it. It is the self-"
              "directed side of what you have been watching, aimed at sleep, anxiety, "
              "confidence, habits and the rest.",
              "It does not teach street hypnosis and will not make you a hypnotist. It is "
              "free, works offline, and nothing you type leaves the phone."],
             []],
        ],
        "faq": [
            ("Can someone hypnotise me against my will?",
             "No. Suggestion needs your cooperation, and that is why street hypnotists ask "
             "for volunteers rather than picking targets. Someone who does not want to "
             "participate simply does not respond."),
            ("Will I do something embarrassing?",
             "Not something you genuinely object to. People under suggestion decline things "
             "that cross their own lines, which is well documented and also why stage shows "
             "stick to harmless material. The risk at a show is social, not psychological."),
            ("Is the stiff arm proof that someone is hypnotised?",
             "No — it is a suggestibility test. It shows how readily someone accepts a "
             "suggestion, which is useful information, but it is a step before anything "
             "resembling a hypnotic state, not evidence of one."),
            ("Can I learn street hypnosis from Onira?",
             "No, and it is worth being straight about it. Onira writes self-hypnosis "
             "sessions for you to listen to; it does not teach you to hypnotise other "
             "people. If that is what you are after, you want a course, not this app."),
            ("Do people remember what happened?",
             "Yes, in almost every case. Suggested amnesia is a temporary effect in "
             "suggestible people, and it wears off. Waking up with a blank stretch of "
             "missing life is a film convention."),
        ],
    },
    "is_it_safe": {
        "slug": "is-self-hypnosis-safe",
        "nav": "Is it safe?",
        "card": "Safe for most people, with a short list of real exceptions.",
        "title": "Is Self-Hypnosis Safe? | Onira",
        "desc": "The honest risks of self-hypnosis, who should skip it, and the situations "
                "where it needs a doctor first — pregnancy, epilepsy, children and more.",
        "h1": "Is self-hypnosis safe?",
        "lede": "For most people, yes — and the real risks are duller and more specific "
                "than the ones people worry about.",
        "answer": "Self-hypnosis is safe for most healthy adults. You cannot get stuck in "
                  "it, lose control, or be made to do something against your will — those "
                  "are film conventions. The genuine cautions are narrower: never listen "
                  "while driving or operating anything, treat it as a complement rather "
                  "than a replacement for prescribed care, and talk to a doctor first if "
                  "you live with psychosis, a dissociative disorder, bipolar disorder or "
                  "PTSD. For children, epilepsy and pregnancy the answer is usually yes "
                  "with supervision, which is worth asking about rather than assuming.",
        "sections": [
            ["The risks people worry about, and what is actually true",
             ["Almost every fear about hypnosis comes from fiction, so it is worth "
              "clearing them out before the real ones:"],
             ["**Getting stuck.** Not possible. Without a voice guiding you the state "
              "simply fades, or turns into ordinary sleep. The deliberate return to "
              "alertness at the end of a session is for comfort, not rescue.",
              "**Losing control.** Suggestion needs your cooperation. You stay aware, you "
              "remember it, and you decline anything that crosses your own lines — which "
              "is exactly why stage shows ask for volunteers.",
              "**Being reprogrammed without noticing.** Nothing is installed. What "
              "repetition changes is a habit of response, slowly, and only in a direction "
              "you were already pointed.",
              "**Weakening your mind.** There is no evidence that ordinary relaxation and "
              "suggestion harm anyone's judgement, attention or willpower."]],
            ["The risks that are real",
             ["They are less dramatic, and mostly about context rather than the state "
              "itself."],
             ["**Doing it while doing something else.** Never with headphones on while "
              "driving, cycling, cooking or minding a child. This is the most likely way "
              "to come to harm, and it is entirely avoidable.",
              "**Using it instead of treatment.** A session that eases pain or anxiety can "
              "make it tempting to skip an appointment or reduce a prescription. That is "
              "the decision to be most careful about, and it belongs to your doctor.",
              "**Unexpected distress.** Relaxing deeply can let a feeling surface that you "
              "were holding down — grief, anger, a memory. For most people this passes; if "
              "a session reliably leaves you worse, stop and talk to someone qualified.",
              "**Memory.** Suggestion makes recall less reliable, not more. Anything that "
              "offers to recover forgotten events is doing something the evidence does not "
              "support."]],
            ["When to ask a doctor first",
             ["None of these are absolute bans, and most people in these situations use "
              "relaxation tools without trouble. They are the cases where a professional "
              "who knows your history should weigh in before an app does."],
             ["**Psychosis or schizophrenia** — relaxation and suggestion are not "
              "recommended without clinical supervision.",
              "**Dissociative disorders or PTSD** — deep relaxation can trigger "
              "dissociation or intrusive memories. Trauma work belongs with a trained "
              "clinician.",
              "**Bipolar disorder** — generally fine when stable; worth discussing before "
              "using it during an episode.",
              "**Epilepsy** — audio relaxation is not a known seizure trigger, but "
              "conditions differ enough that it is a fair question for your neurologist.",
              "**Pregnancy** — usually fine, and hypnosis for birth preparation is well "
              "established. Mention it at an appointment rather than guessing.",
              "**Children** — self-hypnosis can suit older children with adult guidance. "
              "Onira is written for adults and is not designed for young children."]],
            ["Is it safe for anxiety specifically?",
             ["For everyday anxiety, yes, and it is one of the things guided relaxation is "
              "best at — lowering the physical arousal that feeds the thinking. The "
              "distinction that matters is between everyday anxiety and an anxiety "
              "disorder: the first is a reasonable target for a relaxation tool, the "
              "second is a reasonable target for treatment, and using the tool alongside "
              "that treatment is fine.",
              "One practical note: if listening at bedtime makes you more alert rather "
              "than less, that is common and not a warning sign. A session written for "
              "sleep ends differently from one written for calm."],
             []],
            ["Where Onira fits",
             ["Onira writes self-hypnosis sessions on your phone and narrates them aloud, "
              "for sleep, anxiety, confidence, habits and the rest. Every session ends by "
              "bringing you back fully alert, and every theme page carries the same line "
              "this guide does: it is a relaxation tool, not therapy and not medical "
              "advice.",
              "It is free, runs offline, and nothing you type leaves the device — which "
              "also means nobody is profiling what you were anxious about."],
             []],
        ],
        "faq": [
            ("Can self-hypnosis make my mental health worse?",
             "It is unlikely for most people, and possible in specific conditions — "
             "psychosis, dissociative disorders, and trauma when approached directly. If "
             "you live with any of those, make it a question for your clinician rather "
             "than an experiment."),
            ("Is it safe to listen every night?",
             "Yes. Daily use is how the effect accumulates, and there is no known "
             "downside to it. The usual limit is practical: a session that keeps you up "
             "reading the screen is worse than the sleep you were after."),
            ("Can I get addicted to it?",
             "No, in the dependence sense. People do get attached to a routine that works, "
             "which is ordinary rather than a problem — unless it is replacing care you "
             "actually need."),
            ("Is it safe for kids?",
             "With adult guidance and age-appropriate material, often yes; relaxation is "
             "used with children in clinical settings. Onira is written for adults, so it "
             "is not the right tool for a young child."),
            ("What should I do if a session upsets me?",
             "End it, open your eyes and come back to the room — that is always available "
             "and nothing keeps you under. If it happens more than once, treat it as a "
             "signal to work with a person rather than an app."),
        ],
    },
    "learn_self_hypnosis": {
        "slug": "how-to-learn-self-hypnosis",
        "nav": "Learning it",
        "card": "What to practise, in what order, and how long it really takes.",
        "title": "How to Learn Self-Hypnosis | Onira",
        "desc": "A realistic way to learn self-hypnosis on your own: what to practise "
                "first, how long it takes, what going under feels like, and when to stop.",
        "h1": "How to learn self-hypnosis",
        "lede": "It is a skill with a short syllabus and a slow first fortnight — here is "
                "the order that works and the part everyone gets wrong.",
        "answer": "You can learn self-hypnosis on your own, and most people who get "
                  "anywhere do it in the same order: relax the body deliberately, narrow "
                  "attention onto one thing, then give yourself a specific suggestion and "
                  "repeat it nightly for two or three weeks. Expect the state to feel "
                  "unremarkable — absorbed, like a good book, not unconscious — and judge "
                  "it by whether the target moves, not by how deep it felt. A guided "
                  "recording is the easiest way to start, because reading instructions to "
                  "yourself competes with the relaxing.",
        "sections": [
            ["The order that works",
             ["The pieces are simple. Doing them in this order is what stops the first "
              "week feeling like nothing is happening."],
             ["**Set the situation up.** Somewhere you will not be interrupted, phone "
              "silenced, lying down or sitting back. Deciding to check something halfway "
              "through is what ends most early attempts.",
              "**Relax on purpose, in stages.** Hands, jaw, shoulders, breathing — "
              "longer out than in. This is the part people skip, and it is the part that "
              "makes the rest possible.",
              "**Narrow your attention.** A slow count down from twenty, a single image, "
              "the feeling of your own breathing. One thing, held loosely.",
              "**Give one suggestion, in the present and in the positive.** Not \"I will "
              "not panic\" but \"my breathing stays slow and I stay steady\". Rehearse it "
              "as a scene, in detail, rather than repeating it as a phrase.",
              "**Come back deliberately.** Count up, open your eyes, be fully alert. This "
              "matters for the habit, not for safety."]],
            ["What it actually feels like",
             ["This is where most people conclude they cannot do it. The expectation is "
              "something dramatic — a threshold, a click, a sense of going under. The real "
              "thing is closer to being absorbed in a film: the room recedes a bit, time "
              "gets unreliable, and you could stop at any moment but do not particularly "
              "want to.",
              "Which means feeling nothing special says very little. Judge the fortnight "
              "on the target instead: minutes to fall asleep, whether you started the "
              "avoided task, how a stressful hour went. If the number moves, it is "
              "working, whatever it felt like."],
             []],
            ["How long it takes",
             ["The first sessions are for learning the shape, not for results. A fair "
              "expectation is that relaxing gets noticeably easier within a week, and that "
              "anything you are actually aiming at takes two to three weeks of near-daily "
              "practice to shift.",
              "Responsiveness also varies between people and is fairly stable over a "
              "lifetime — roughly one in four respond strongly, about as many barely "
              "respond at all. If three or four honest attempts do nothing whatsoever, the "
              "reasonable conclusion is that this is not your tool, not that you need to "
              "try harder."],
             []],
            ["Can you learn it from a book, or on your own?",
             ["On your own, yes — it is one of the few things in this field that genuinely "
              "does not need a practitioner. From a book, partly: books are good for "
              "understanding what you are doing and poor as a live guide, because reading "
              "instructions to yourself is the opposite of narrowing your attention.",
              "That is the practical argument for a recording. Something else holds the "
              "structure and the pacing while you do the only part that cannot be "
              "delegated, which is letting it work. Once the shape is familiar, doing it "
              "unaided gets much easier."],
             []],
            ["Learning self-hypnosis is not learning to hypnotise people",
             ["Worth separating, because the searches run together. Hypnotising someone "
              "else is a performance and an interpersonal skill, with consent and "
              "calibration to learn, and it is taught in courses. Self-hypnosis is a "
              "private routine aimed at one of your own problems.",
              "Being good at the second tells you almost nothing about the first, and the "
              "reverse is also true."],
             []],
            ["Where Onira fits",
             ["Onira writes the session for you and narrates it aloud: you pick a theme "
              "and, if you want, type a sentence about what is actually going on. That "
              "removes the two things beginners struggle with — holding the structure, and "
              "finding the words for a suggestion that fits your situation.",
              "It is free, works offline, and nothing you type leaves your phone. If you "
              "later want to run sessions in your head without it, that is a fine outcome "
              "and the app will have done its job."],
             []],
        ],
        "faq": [
            ("How long should a session be?",
             "Fifteen to thirty minutes suits most purposes. Shorter works once the skill "
             "is familiar; much longer mostly adds drifting off, which is fine if sleep "
             "was the point and wasted otherwise."),
            ("What time of day is best?",
             "Whenever you can be uninterrupted, with one caveat: sessions aimed at "
             "anything other than sleep end by returning you to full alertness, so "
             "bedtime is not automatically the right slot."),
            ("Do I need to write my own script?",
             "No, and writing one while trying to relax is the classic beginner trap. "
             "Start with something that narrates for you, and write your own later if you "
             "find you want to."),
            ("Can I learn it if my mind never stops?",
             "That is the normal starting condition, not a disqualification. The "
             "staged physical relaxation exists precisely because a racing mind will not "
             "narrow on command — the body goes first and the mind follows."),
            ("Is self-hypnosis the same as meditation?",
             "Related but aimed differently. Meditation trains a general relationship with "
             "your attention; self-hypnosis points that attention at one specific target. "
             "The practice overlaps, the intent does not."),
        ],
    },
}

FR["guide_dir"] = "guides"
FR["ui"]["guides_title"] = "Les questions qu'on se pose"
FR["ui"]["guides_crumb"] = "Guides"
FR["ui"]["guide_answer_title"] = "En bref"
FR["ui"]["guide_cta_title"] = "À essayer ce soir"
FR["guides"] = {
    "fall_asleep": {
        "slug": "s-endormir-avec-l-auto-hypnose",
        "nav": "S'endormir",
        "card": "La méthode, étape par étape, pour les nuits où la tête ne s'arrête pas.",
        "title": "S'endormir avec l'auto-hypnose : la méthode | Onira",
        "desc": "Une méthode d'auto-hypnose étape par étape pour s'endormir quand la tête "
                "tourne, et quoi faire quand ça ne marche pas du premier coup.",
        "h1": "S'endormir avec l'auto-hypnose",
        "lede": "Une méthode concrète pour les nuits où le corps est fatigué et l'esprit "
                "continue de tourner — et ce qu'elle peut, ou non, y changer.",
        "answer": "Allongez-vous, laissez les yeux se fermer et comptez lentement de vingt "
                  "à un, chaque chiffre posé sur une expiration. À chaque chiffre, relâchez "
                  "un endroit précis : la mâchoire, les épaules, les mains. Arrivé à un, "
                  "installez une scène calme et remplissez-la de détails sensoriels. Il ne "
                  "s'agit pas de forcer le sommeil, mais de donner à l'esprit une chose "
                  "lente à faire à la place de celles, rapides, qu'il avait prévues.",
        "sections": [
            ("Pourquoi le compte à rebours fonctionne",
             ["L'insomnie de début de nuit vient rarement d'un manque de fatigue. C'est un "
              "esprit à qui l'on ne donne rien à faire et qui remplit le vide avec demain. "
              "L'auto-hypnose s'adresse directement à ce vide : une tâche lente, répétitive "
              "et juste assez exigeante occupe exactement l'attention qui, sinon, rejouerait "
              "une conversation ou une échéance.",
              "C'est la descente qui compte, plus que le nombre choisi. Compter à rebours "
              "suppose une arrivée, et associer chaque chiffre à une expiration ralentit le "
              "souffle sans avoir à y penser — c'est le levier le plus fiable pour faire "
              "sortir le système nerveux de son réglage de vigilance."],
             []),
            ("La méthode, étape par étape",
             ["Rien là-dedans ne demande d'apprentissage, et rien ne demande d'y croire. Il "
              "faut environ un quart d'heure et l'acceptation de recommencer quand l'esprit "
              "part ailleurs, ce qui arrivera."],
             ["Préparez la pièce d'abord : sombre, fraîche, téléphone retourné. Décider de "
              "vérifier quelque chose en cours de route est ce qui interrompt la plupart des "
              "tentatives.",
              "Allongez-vous sur le dos, bras le long du corps, et prenez trois respirations "
              "plus longues à l'expiration qu'à l'inspiration.",
              "Comptez de vingt à un, chaque chiffre prononcé intérieurement sur l'expiration.",
              "À chaque chiffre, relâchez un endroit : mâchoire, langue, épaules, mains, "
              "ventre, cuisses, pieds. C'est le fait de nommer l'endroit qui le fait lâcher.",
              "À un, choisissez une scène — une plage au crépuscule, un chemin sous les "
              "arbres, une pièce dont vous vous souvenez — et remplissez-la : la "
              "température, le son, ce qu'il y a sous les pieds.",
              "Quand vous vous apercevez que vous êtes reparti dans vos pensées, ne "
              "recommencez pas à vingt. Reprenez le compte là où vous l'aviez laissé."]),
            ("Quand ça ne marche pas",
             ["Les premières tentatives finissent souvent en esprit qui vagabonde, et ce "
              "n'est pas un échec : c'est la façon ordinaire dont l'attention se comporte "
              "avant que la séquence devienne une habitude. Ce qui change le résultat, c'est "
              "la répétition à la même heure, jusqu'à ce que la séquence elle-même serve de "
              "signal.",
              "Si vous êtes encore éveillé au bout d'une vingtaine de minutes, levez-vous, "
              "gardez une lumière basse et faites quelque chose d'ennuyeux jusqu'à ce que le "
              "sommeil revienne. Rester au lit à lutter apprend au corps que le lit est un "
              "endroit où l'on lutte — c'est la seule association qu'il vaille vraiment la "
              "peine de protéger."],
             []),
            ("Ce qu'apporte une séance écrite",
             ["Le faire de mémoire, c'est laisser une partie de soi dérouler les consignes — "
              "donc une partie de soi éveillée. Être guidé par une voix supprime ce travail : "
              "on suit au lieu de se souvenir, et c'est pourquoi les séances guidées "
              "fonctionnent mieux, au coucher, que l'auto-hypnose menée de tête.",
              "Onira écrit la séance sur votre téléphone à partir de ce qui vous empêche "
              "réellement de dormir : si vous tapez que vous rejouez une conversation en "
              "boucle, les images et les suggestions se construisent là-dessus plutôt que "
              "sur une plage générique. Le modèle tourne sur l'appareil, donc rien de ce que "
              "vous écrivez n'est envoyé, et tout fonctionne hors ligne, téléphone retourné."],
             []),
        ],
        "faq": [
            ("En combien de temps s'endort-on avec cette méthode ?",
             "La plupart de ceux à qui elle convient s'endorment dans la scène plutôt qu'à "
             "la fin du compte, souvent entre quinze et vingt-cinq minutes. Si vous êtes "
             "régulièrement encore éveillé à la fin, c'est un signal à regarder du côté des "
             "heures qui précèdent le coucher, pas une raison d'insister au lit."),
            ("L'auto-hypnose est-elle sans risque le soir ?",
             "Pour un mauvais sommeil ordinaire, oui : c'est de la relaxation guidée, et "
             "l'issue la plus désagréable est de rester éveillé. Ce n'est pas un traitement "
             "d'un trouble du sommeil : une insomnie persistante, une apnée ou une insomnie "
             "avec humeur basse relèvent d'un médecin."),
            ("Puis-je utiliser un enregistrement plutôt que le faire moi-même ?",
             "Oui, et pour s'endormir un enregistrement vaut généralement mieux : il "
             "supprime le travail de mémorisation. Ce qu'un enregistrement ne peut pas "
             "faire, c'est nommer ce qui vous préoccupe ce soir-là — c'est exactement le "
             "vide que comble une séance écrite sur le moment."),
        ],
    },
    "vs_meditation": {
        "slug": "hypnose-ou-meditation",
        "nav": "Hypnose ou méditation",
        "card": "Deux états, deux objectifs — et lequel correspond à ce que vous cherchez.",
        "title": "Hypnose ou méditation : laquelle choisir ? | Onira",
        "desc": "Ce qui sépare vraiment l'hypnose guidée de la méditation, ce que chacune "
                "sait faire, et comment choisir pour le sommeil, l'anxiété ou une habitude.",
        "h1": "Hypnose ou méditation",
        "lede": "De l'extérieur, elles se ressemblent — yeux fermés, souffle lent, une voix "
                "calme — et elles ne visent pas la même chose.",
        "answer": "La méditation entraîne l'attention : on s'exerce à remarquer où l'esprit "
                  "est parti et à revenir, sans chercher à changer ce qu'on trouve. "
                  "L'hypnose utilise un état détendu et focalisé pour répéter quelque chose "
                  "de précis : dormir, rester posé en réunion, ne pas tendre la main vers la "
                  "cigarette. Pour une compétence générale, méditez. Pour travailler une "
                  "chose nommée, une séance d'hypnose est l'outil le plus direct.",
        "sections": [
            ("Ce qui change vraiment",
             ["Les deux pratiques produisent un état physiologique voisin : souffle ralenti, "
              "vigilance abaissée, attention resserrée. La différence est ce qu'on y fait "
              "une fois arrivé. Une méditation vous ramène sans cesse à un point neutre et "
              "ne demande rien au contenu de l'esprit. Une séance d'hypnose prend ce même "
              "état posé et y introduit de la suggestion : des images, des formulations et "
              "des répétitions orientées vers un résultat.",
              "C'est aussi pourquoi l'hypnose est structurée là où la méditation ne l'est "
              "souvent pas. Une séance a un arc : une induction qui installe, un "
              "approfondissement, des images, les suggestions elles-mêmes, un ancrage à "
              "emporter, puis un retour net à l'état de veille. Chaque partie existe pour "
              "que la suivante fonctionne."],
             []),
            ("Ce que chacune sait faire",
             ["Aucune n'est meilleure dans l'absolu. Elles répondent à des questions "
              "différentes, et la façon honnête de choisir, c'est de partir de ce que vous "
              "voulez dans le mois qui vient, pas de celle qui paraît la plus sérieuse."],
             ["La méditation, pour un rapport général à votre attention : moins de "
              "réactivité, plus d'espace entre une émotion et ce qu'on en fait. Le bénéfice "
              "est lent et large.",
              "L'hypnose, pour une cible précise : s'endormir, la peur de l'avion mardi "
              "prochain, les dix premières minutes d'une tâche évitée, une habitude à "
              "interrompre.",
              "La méditation demande d'arrêter de courir après un résultat, ce qui la rend "
              "frustrante précisément quand on en a un.",
              "L'hypnose est faite pour un résultat, ce qui la rend plus facile à commencer "
              "et plus facile à survendre : aucune séance ne réécrit une vie en une fois."]),
            ("Laquelle est la mieux étayée ?",
             ["Les deux ont une vraie littérature, et les deux traînent plus d'enthousiasme "
              "que de preuves à leurs marges. Les programmes fondés sur la pleine conscience "
              "ont le corpus clinique le plus large, surtout autour du stress, de la rechute "
              "dépressive et de la douleur chronique. L'hypnothérapie clinique a un dossier "
              "plus étroit mais réel : la douleur et la détresse pendant un acte médical "
              "sont ses meilleurs résultats, avec des effets utiles sur l'endormissement et "
              "le côlon irritable.",
              "Ce qu'aucune des deux ne peut revendiquer, c'est de remplacer un traitement. "
              "Ce sont des compléments : des choses qui aident à côté d'un suivi, pas à sa "
              "place."],
             []),
            ("Vous n'avez pas à choisir",
             ["Un schéma courant et raisonnable : la méditation comme pratique quotidienne, "
              "et une séance d'hypnose pour la chose précise qui gêne cette semaine. Elles "
              "ne se concurrencent pas ; méditer régulièrement rend même la phase "
              "d'installation d'une séance plus rapide.",
              "Onira se situe du côté de l'hypnose. Vous choisissez la cible, ajoutez une "
              "phrase sur ce qui se passe vraiment, et un modèle qui tourne sur le téléphone "
              "écrit une séance autour de ça, puis la narre — sans compte, sans rien "
              "envoyer, et sans images génériques."],
             []),
        ],
        "faq": [
            ("L'hypnose peut-elle me faire faire quelque chose contre ma volonté ?",
             "Non. En auto-hypnose, vous restez conscient et aux commandes du début à la "
             "fin, et une suggestion qui va contre ce que vous voulez ne prend tout "
             "simplement pas. L'hypnose de spectacle est un divertissement reposant sur des "
             "volontaires prêts à jouer le jeu ; ce n'est pas une séance thérapeutique."),
            ("Laquelle est la meilleure pour l'anxiété ?",
             "Pour l'anxiété comme tendance générale, la méditation a les meilleures données "
             "sur la durée. Pour une situation anxiogène identifiable — un vol, une "
             "présentation, un examen — répéter la scène en hypnose est en général plus "
             "utile que de rester avec le souffle."),
            ("La méditation guidée, est-ce la même chose que l'hypnose ?",
             "C'est ce qui s'en rapproche le plus. Une méditation guidée qui visualise un "
             "résultat et répète des suggestions fait l'essentiel de ce que fait une séance "
             "d'hypnose ; l'étiquette diffère plus que la pratique."),
        ],
    },
    "does_it_work": {
        "slug": "l-auto-hypnose-marche-t-elle",
        "nav": "Est-ce que ça marche ?",
        "card": "Ce que les données soutiennent, ce qu'elles ne soutiennent pas, et pour qui "
                "ça ne marche pas.",
        "title": "L'auto-hypnose marche-t-elle vraiment ? | Onira",
        "desc": "Un point honnête sur ce que l'auto-hypnose sait faire, ce que les données "
                "soutiennent, pour qui elle ne marche pas, et comment le vérifier.",
        "h1": "L'auto-hypnose marche-t-elle vraiment ?",
        "lede": "Oui, pour certaines choses, modérément, et pas pour tout le monde — une "
                "réponse plus terne que celles que donnent d'habitude les deux camps.",
        "answer": "L'auto-hypnose est correctement étayée sur l'endormissement, sur la "
                  "douleur et la détresse pendant un acte médical, et sur la baisse de "
                  "vigilance qui alimente l'anxiété dans une situation donnée. Elle est mal "
                  "étayée comme traitement autonome de quoi que ce soit de clinique, et "
                  "environ une personne sur quatre répond mal à la suggestion, quelle que "
                  "soit la technique. C'est un outil réel au périmètre étroit, ni remède ni "
                  "placebo.",
        "sections": [
            ("Ce qu'elle sait faire",
             ["Les résultats les plus nets sont les moins spectaculaires. S'endormir plus "
              "vite, traverser un soin dentaire ou médical avec moins de détresse, atténuer "
              "une douleur, aborder un événement stressant identifié plus calmement qu'on ne "
              "l'aurait fait. Tout cela a la même forme : un horizon court et une composante "
              "physique que la relaxation déplace réellement.",
              "Le travail sur les habitudes — tabac, ongles rongés, les dix premières "
              "minutes d'une tâche évitée — vient un cran en dessous. Les séances aident, "
              "surtout comme un élément d'un plan plutôt que comme le plan, et l'effet vient "
              "de la répétition, pas de la puissance d'une séance isolée."],
             []),
            ("Ce qu'elle n'est pas",
             ["Ce n'est pas une psychothérapie, et elle ne traite ni la dépression, ni un "
              "trouble anxieux, ni un état de stress post-traumatique, ni un trouble du "
              "comportement alimentaire. Ce n'est pas un moyen de retrouver des souvenirs "
              "oubliés : la suggestion rend la mémoire moins fiable, pas plus. Ce n'est pas "
              "un substitut à un médicament prescrit, et aucune séance honnête ne laissera "
              "entendre le contraire.",
              "Ce n'est pas rapide non plus. Le marketing de l'hypnose s'appuie sur des "
              "séances uniques et spectaculaires ; la réalité est un effet modeste qui "
              "s'accumule avec un usage quotidien sur plusieurs semaines."],
             []),
            ("Pourquoi elle ne marche pas pour tout le monde",
             ["La suggestibilité varie d'une personne à l'autre et reste assez stable au "
              "cours d'une vie. Environ une personne sur quatre répond faiblement à la "
              "suggestion hypnotique quelle que soit la manière dont elle est amenée, et à "
              "peu près autant y répondent fortement. Ce n'est une question ni "
              "d'intelligence ni de volonté, et aucune technique ne fait passer de façon "
              "fiable d'un groupe à l'autre.",
              "La conséquence pratique mérite d'être connue avant de commencer : si trois ou "
              "quatre tentatives honnêtes ne produisent rien du tout, la conclusion "
              "raisonnable est que ce n'est pas votre outil, pas que vous vous y prenez mal."],
             []),
            ("Comment savoir si ça fait quelque chose",
             ["Jugez sur la cible, pas sur la sensation. On s'attend à se sentir hypnotisé "
              "et, la plupart du temps, ça n'arrive pas : de l'intérieur, l'état n'a rien de "
              "remarquable, plus proche d'être absorbé par un livre que de quoi que ce soit "
              "de théâtral. Ne rien ressentir de spécial pendant une séance ne dit presque "
              "rien de son effet.",
              "Choisissez une seule chose mesurable et suivez-la deux semaines : minutes "
              "pour s'endormir, cigarettes dans la journée, tâche commencée ou non. Si le "
              "chiffre bouge, continuez ; sinon, arrêtez et essayez autre chose. C'est un "
              "meilleur test que n'importe quel récit de profondeur atteinte."],
             []),
            ("Où se situe Onira",
             ["Onira est un outil de relaxation et d'auto-hypnose, et n'est délibérément pas "
              "vendue comme davantage. Ce qu'elle change à l'offre habituelle, c'est la "
              "précision : au lieu d'un enregistrement fait pour tout le monde, un modèle "
              "embarqué dans votre téléphone écrit la séance autour du thème choisi et de la "
              "phrase que vous tapez, puis la narre à voix haute.",
              "Tout tourne sur l'appareil : ce que vous écrivez de votre vie ne quitte jamais "
              "le téléphone — il n'y a ni compte ni serveur qui pourrait le lire. Si vous "
              "allez réellement mal, c'est une conversation à avoir avec une personne, et "
              "aucune application n'est la bonne réponse à ça."],
             []),
        ],
        "faq": [
            ("L'auto-hypnose, n'est-ce pas juste un effet placebo ?",
             "L'attente en fait partie, comme dans une grande partie de la médecine. Mais la "
             "réponse hypnotique se manifeste d'une façon que le placebo seul ne prédit "
             "pas : elle varie selon la suggestibilité de la personne, et l'imagerie "
             "retrouve des changements d'état qui la suivent. Le résumé juste : un effet "
             "réel et modeste, avec une part d'attente par-dessus."),
            ("À quelle fréquence faire une séance ?",
             "Tous les jours, deux à trois semaines, s'il s'agit d'une habitude ou du "
             "sommeil. L'effet est cumulatif, et le meilleur prédicteur d'un résultat reste "
             "de l'avoir réellement fait de façon répétée."),
            ("Peut-on rester bloqué en hypnose ?",
             "Non. Sans voix pour guider, l'état se dissipe simplement ou se transforme en "
             "sommeil. Une séance qui se termine correctement comprend un retour net à "
             "l'état de veille, par confort et non par sécurité."),
        ],
    },
}

ES["guide_dir"] = "guias"
ES["ui"]["guides_title"] = "Preguntas frecuentes"
ES["ui"]["guides_crumb"] = "Guías"
ES["ui"]["guide_answer_title"] = "En corto"
ES["ui"]["guide_cta_title"] = "Pruébalo esta noche"
ES["guides"] = {
    "fall_asleep": {
        "slug": "dormirse-con-autohipnosis",
        "nav": "Dormirse",
        "card": "El método, paso a paso, para las noches en que la cabeza no para.",
        "title": "Dormirse con autohipnosis: el método | Onira",
        "desc": "Un método de autohipnosis paso a paso para dormirse cuando la cabeza no "
                "para, y qué hacer cuando no funciona a la primera.",
        "h1": "Dormirse con autohipnosis",
        "lede": "Un método concreto para las noches en que el cuerpo está cansado y la "
                "cabeza sigue funcionando — y qué puede y qué no puede cambiar.",
        "answer": "Túmbate, deja que se cierren los ojos y cuenta despacio de veinte a uno, "
                  "con cada número apoyado en una espiración. En cada número suelta un sitio "
                  "concreto: la mandíbula, los hombros, las manos. Al llegar a uno, instala "
                  "una escena tranquila y llénala de detalles sensoriales. No se trata de "
                  "forzar el sueño, sino de darle a la mente algo lento que hacer en lugar "
                  "de lo rápido que tenía previsto.",
        "sections": [
            ("Por qué funciona la cuenta atrás",
             ["El insomnio del principio de la noche rara vez es falta de cansancio. Es una "
              "mente a la que no se le ha dado nada que hacer y que ha llenado el hueco con "
              "el día siguiente. La autohipnosis va directa a ese hueco: una tarea lenta, "
              "repetitiva y algo exigente ocupa exactamente la atención que si no estaría "
              "repasando una conversación o una fecha de entrega.",
              "Importa más la bajada que el número. Contar hacia atrás implica una llegada, "
              "y unir cada número a una espiración frena la respiración sin tener que pensar "
              "en respirar, que es la palanca más fiable para sacar al sistema nervioso de "
              "su ajuste de alerta."],
             []),
            ("El método, paso a paso",
             ["Nada de esto requiere entrenamiento ni creer en nada. Requiere un cuarto de "
              "hora y aceptar volver a empezar cuando la mente se vaya, que se irá."],
             ["Prepara antes la habitación: oscura, fresca, el móvil boca abajo. Decidir "
              "mirar algo a mitad de camino es lo que corta la mayoría de los intentos.",
              "Túmbate boca arriba, los brazos a los lados, y haz tres respiraciones más "
              "largas al soltar que al tomar aire.",
              "Cuenta de veinte a uno, cada número dicho por dentro al espirar.",
              "Con cada número suelta un sitio: mandíbula, lengua, hombros, manos, vientre, "
              "muslos, pies. Nombrar el sitio es lo que hace que se suelte.",
              "En el uno, elige una escena — una playa al atardecer, un camino entre "
              "árboles, una habitación que recuerdes — y complétala: la temperatura, el "
              "sonido, lo que hay bajo los pies.",
              "Cuando te des cuenta de que te has ido a pensar, no vuelvas al veinte. Retoma "
              "la cuenta donde la dejaste y sigue."]),
            ("Cuando no funciona",
             ["Los primeros intentos suelen acabar con la mente dispersa, y eso no es un "
              "fracaso: es cómo se comporta la atención antes de que la secuencia se "
              "convierta en costumbre. Lo que cambia el resultado es repetirla a la misma "
              "hora, hasta que la propia secuencia funcione como señal.",
              "Si al cabo de unos veinte minutos sigues despierto, levántate, mantén la luz "
              "baja y haz algo aburrido hasta que vuelva el sueño. Quedarte en la cama "
              "peleando le enseña al cuerpo que la cama es un sitio donde se pelea, y esa es "
              "la única asociación que de verdad conviene proteger."],
             []),
            ("Qué aporta una sesión escrita",
             ["Hacerlo de memoria significa que una parte de ti va ejecutando las "
              "instrucciones, o sea, una parte de ti despierta. Que te guíe una voz elimina "
              "ese trabajo: sigues en lugar de recordar, y por eso las sesiones guiadas "
              "funcionan mejor a la hora de dormir que la autohipnosis de memoria.",
              "Onira escribe la sesión en tu móvil a partir de lo que de verdad te mantiene "
              "despierto: si escribes que no dejas de darle vueltas a una conversación, las "
              "imágenes y las sugestiones se construyen sobre eso y no sobre una playa "
              "genérica. El modelo se ejecuta en el dispositivo, así que nada de lo que "
              "escribes se envía, y todo funciona sin conexión y con el móvil boca abajo."],
             []),
        ],
        "faq": [
            ("¿Cuánto se tarda en dormirse así?",
             "La mayoría de quienes se llevan bien con el método se duermen dentro de la "
             "escena y no al final de la cuenta, a menudo entre los quince y los "
             "veinticinco minutos. Si sigues despierto al final de forma habitual, es una "
             "señal para mirar las horas previas a acostarte, no para insistir en la cama."),
            ("¿Es seguro hacer autohipnosis por la noche?",
             "Para el mal dormir corriente, sí: es relajación guiada y lo peor que suele "
             "pasar es seguir despierto. No es un tratamiento de un trastorno del sueño: un "
             "insomnio persistente, una apnea o un insomnio con ánimo bajo son cosa de un "
             "médico."),
            ("¿Puedo usar una grabación en vez de hacerlo yo?",
             "Sí, y para dormirse una grabación suele ser mejor: quita el trabajo de "
             "recordar los pasos. Lo que una grabación no puede hacer es nombrar lo que te "
             "preocupa esa noche, que es justo el hueco que llena una sesión escrita en el "
             "momento."),
        ],
    },
    "vs_meditation": {
        "slug": "hipnosis-o-meditacion",
        "nav": "Hipnosis o meditación",
        "card": "Dos estados, dos objetivos — y cuál encaja con lo que buscas.",
        "title": "Hipnosis o meditación: cuál elegir | Onira",
        "desc": "Qué separa de verdad a la hipnosis guiada de la meditación, para qué sirve "
                "cada una y cómo elegir para el sueño, la ansiedad o un hábito.",
        "h1": "Hipnosis o meditación",
        "lede": "Desde fuera se parecen — ojos cerrados, respiración lenta, una voz "
                "tranquila — y no apuntan a lo mismo.",
        "answer": "La meditación entrena la atención: practicas darte cuenta de adónde se ha "
                  "ido la mente y volver, sin intentar cambiar lo que encuentras. La "
                  "hipnosis usa un estado relajado y enfocado para ensayar algo concreto: "
                  "dormir, mantenerte entero en una reunión, no alargar la mano hacia el "
                  "cigarrillo. Si quieres una habilidad general, medita. Si quieres trabajar "
                  "una cosa con nombre, una sesión de hipnosis es la herramienta directa.",
        "sections": [
            ("Qué cambia realmente",
             ["Las dos prácticas producen un estado fisiológico parecido: respiración más "
              "lenta, menos activación, atención estrechada. La diferencia es qué haces una "
              "vez allí. Una meditación te devuelve una y otra vez a un ancla neutra y no le "
              "pide nada al contenido de la mente. Una sesión de hipnosis toma ese mismo "
              "estado y le mete sugestión: imágenes, frases y ensayos dirigidos a un "
              "resultado.",
              "Por eso también la hipnosis está estructurada y la meditación a menudo no. "
              "Una sesión tiene un arco: una inducción que te instala, una profundización, "
              "imágenes, las sugestiones, un anclaje para llevarte y una vuelta clara al "
              "estado de vigilia. Cada parte existe para que funcione la siguiente."],
             []),
            ("Para qué sirve cada una",
             ["Ninguna es mejor en abstracto. Responden a preguntas distintas, y la forma "
              "honesta de elegir es partir de lo que quieres en el próximo mes, no de cuál "
              "suena más seria."],
             ["La meditación, para la relación general con tu atención: menos reactividad, "
              "más espacio entre una emoción y lo que haces con ella. Rinde despacio y "
              "ancho.",
              "La hipnosis, para una diana concreta: dormirte, el miedo a volar del martes "
              "que viene, los diez primeros minutos de una tarea que evitas, un hábito que "
              "quieres interrumpir.",
              "La meditación pide dejar de perseguir un resultado, que es justo lo que la "
              "hace frustrante cuando tienes uno.",
              "La hipnosis está hecha para un resultado, lo que la hace más fácil de empezar "
              "y más fácil de sobrevender: ninguna sesión reescribe una vida de una vez."]),
            ("¿Cuál está mejor respaldada?",
             ["Las dos tienen literatura real y las dos arrastran más entusiasmo que pruebas "
              "en los bordes. Los programas basados en mindfulness tienen el cuerpo clínico "
              "más amplio, sobre todo en estrés, recaída depresiva y dolor crónico. La "
              "hipnoterapia clínica tiene un expediente más estrecho pero genuino: el dolor "
              "y el malestar durante un procedimiento médico son sus mejores resultados, con "
              "efectos útiles en la conciliación del sueño y en el colon irritable.",
              "Lo que ninguna puede reclamar es sustituir a un tratamiento. Son "
              "complementos: cosas que ayudan junto a un seguimiento, no en su lugar."],
             []),
            ("No hace falta elegir",
             ["Un patrón común y razonable: la meditación como práctica diaria y una sesión "
              "de hipnosis para lo concreto que estorba esta semana. No compiten; meditar a "
              "menudo incluso acelera la fase de instalación de una sesión.",
              "Onira está del lado de la hipnosis. Eliges la diana, añades una frase sobre "
              "lo que pasa de verdad, y un modelo que se ejecuta en el móvil escribe una "
              "sesión alrededor de eso y la narra — sin cuenta, sin enviar nada y sin "
              "imágenes genéricas."],
             []),
        ],
        "faq": [
            ("¿La hipnosis puede hacerme hacer algo que no quiero?",
             "No. En autohipnosis sigues consciente y al mando de principio a fin, y una "
             "sugestión que va contra lo que quieres sencillamente no prende. La hipnosis de "
             "espectáculo es entretenimiento con voluntarios dispuestos a seguir el juego, y "
             "no es lo que es una sesión terapéutica."),
            ("¿Cuál es mejor para la ansiedad?",
             "Para la ansiedad como patrón general, la meditación tiene mejores datos a "
             "largo plazo. Para una situación ansiosa que puedas nombrar — un vuelo, una "
             "presentación, una prueba — ensayarla en una sesión de hipnosis suele ser más "
             "útil que quedarse con la respiración."),
            ("¿La meditación guiada es lo mismo que la hipnosis?",
             "Es lo que más se le acerca. Una meditación guiada que visualiza un resultado y "
             "repite sugestiones hace casi todo lo que hace una sesión de hipnosis; la "
             "etiqueta se diferencia más que la práctica."),
        ],
    },
    "does_it_work": {
        "slug": "funciona-la-autohipnosis",
        "nav": "¿Funciona?",
        "card": "Qué respaldan los datos, qué no, y a quién no le funciona.",
        "title": "¿Funciona de verdad la autohipnosis? | Onira",
        "desc": "Una mirada honesta a para qué sirve la autohipnosis, qué respaldan los "
                "datos, a quién no le funciona y cómo comprobar si hace algo.",
        "h1": "¿Funciona de verdad la autohipnosis?",
        "lede": "Sí, para algunas cosas, de forma moderada, y no para todo el mundo — una "
                "respuesta más sosa que la que suele dar cada bando.",
        "answer": "La autohipnosis tiene datos decentes en la conciliación del sueño, en el "
                  "dolor y el malestar durante un procedimiento médico, y en bajar la "
                  "activación que alimenta la ansiedad en una situación concreta. Tiene "
                  "datos flojos como tratamiento por sí sola de nada clínico, y alrededor de "
                  "una persona de cada cuatro responde mal a la sugestión, use la técnica "
                  "que use. Es una herramienta real de alcance estrecho, ni cura ni placebo.",
        "sections": [
            ("Para qué sirve",
             ["Los resultados más claros son los menos espectaculares. Dormirse antes, pasar "
              "un tratamiento dental o médico con menos malestar, rebajar un dolor, llegar a "
              "un acontecimiento estresante identificado más tranquilo de lo que habrías "
              "llegado. Todo eso comparte una forma: horizonte corto y un componente físico "
              "que la relajación mueve de verdad.",
              "El trabajo sobre hábitos — tabaco, uñas, los diez primeros minutos de una "
              "tarea evitada — va un escalón por debajo. Las sesiones ayudan, sobre todo "
              "como una parte de un plan y no como el plan, y el efecto viene de la "
              "repetición, no de que una sesión suelta sea potente."],
             []),
            ("Qué no es",
             ["No es psicoterapia, y no trata la depresión, ni un trastorno de ansiedad, ni "
              "un estrés postraumático, ni un trastorno de la conducta alimentaria. No es "
              "una forma de recuperar recuerdos olvidados: la sugestión vuelve la memoria "
              "menos fiable, no más. No sustituye a un medicamento que te hayan recetado, y "
              "ninguna sesión honesta dará a entender lo contrario.",
              "Tampoco es rápida. El marketing de la hipnosis se apoya en sesiones únicas y "
              "espectaculares; el patrón real es un efecto modesto que se acumula con uso "
              "diario a lo largo de semanas."],
             []),
            ("Por qué no le funciona a todo el mundo",
             ["La sugestionabilidad varía entre personas y es bastante estable a lo largo de "
              "la vida. Alrededor de una de cada cuatro responde débilmente a la sugestión "
              "hipnótica se le presente como se le presente, y más o menos la misma "
              "proporción responde con fuerza. No es cuestión de inteligencia ni de fuerza "
              "de voluntad, y no hay técnica que mueva a alguien de un grupo al otro de "
              "forma fiable.",
              "La consecuencia práctica conviene saberla antes de empezar: si tres o cuatro "
              "intentos honestos no producen absolutamente nada, la conclusión razonable es "
              "que esta no es tu herramienta, no que lo estés haciendo mal."],
             []),
            ("Cómo saber si hace algo",
             ["Júzgalo por la diana, no por la sensación. Uno espera sentirse hipnotizado y "
              "casi nunca ocurre: por dentro el estado no tiene nada de notable, más cerca "
              "de estar absorto en un libro que de nada teatral. No sentir nada especial "
              "durante una sesión dice muy poco sobre si funcionó.",
              "Elige una sola cosa medible y síguela dos semanas: minutos hasta dormirte, "
              "cigarrillos en el día, si empezaste la tarea o no. Si el número se mueve, "
              "sigue; si no, para y prueba otra cosa. Es mejor prueba que cualquier relato "
              "de lo hondo que llegaste."],
             []),
            ("Dónde encaja Onira",
             ["Onira es una herramienta de relajación y autohipnosis, y deliberadamente no "
              "se vende como más. Lo que cambia respecto a la oferta habitual es la "
              "precisión: en lugar de una grabación hecha para todo el mundo, un modelo "
              "dentro de tu móvil escribe la sesión alrededor del tema que eliges y de la "
              "frase que escribes, y luego la narra en voz alta.",
              "Todo se ejecuta en el dispositivo, así que lo que escribes sobre tu vida "
              "nunca sale del móvil: no hay cuenta ni servidor que pudiera leerlo. Si estás "
              "pasándolo mal de verdad, esa es una conversación para tener con una persona, "
              "y ninguna aplicación es la respuesta correcta a eso."],
             []),
        ],
        "faq": [
            ("¿La autohipnosis no es solo efecto placebo?",
             "La expectativa forma parte, como en buena parte de la medicina. Pero la "
             "respuesta hipnótica aparece de formas que el placebo por sí solo no predice: "
             "varía según la sugestionabilidad de la persona, y la neuroimagen encuentra "
             "cambios de estado que la acompañan. El resumen justo: un efecto real y "
             "modesto, con una parte de expectativa encima."),
            ("¿Con qué frecuencia conviene hacer una sesión?",
             "A diario, dos o tres semanas, si trabajas un hábito o el sueño. El efecto es "
             "acumulativo, y el mejor predictor de sacar algo sigue siendo haberlo hecho de "
             "verdad y de forma repetida."),
            ("¿Se puede uno quedar atrapado en hipnosis?",
             "No. Sin una voz que guíe, el estado simplemente se disuelve o se convierte en "
             "sueño. Que una sesión termine con una vuelta clara al estado de vigilia es por "
             "comodidad, no por seguridad."),
        ],
    },
}

LANGS = [EN, FR, ES]
