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
}

# Order used for nav cards and the sitemap. A theme does not have to exist in
# every language: search demand differs by market, and a page is only worth
# having where people actually look for it. `build.py` derives each theme's
# hreflang set from the languages that publish it.
THEMES = ["anxiety", "sleep", "confidence", "stress", "smoking", "focus", "weight",
          "fear", "letting_go", "learning", "motivation", "habits"]

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
    },
}

LANGS = [EN, FR, ES]
