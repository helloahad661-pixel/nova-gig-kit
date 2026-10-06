#!/usr/bin/env python3
"""Fiverr launch kit — every field validated against Fiverr's 2026 character limits."""

LIMITS = {
    "gig_title": 80,            # must start with "I will"
    "gig_description": 1200,    # ~200-240 words; first 110 = search preview
    "package_desc": 100,        # per tier
    "tag": 20,                  # per tag, 5 tags max
    "profile_bio": 600,         # "About" section
    "prof_title": 60,           # professional title (conservative)
    "faq_q": 70,
    "faq_a": 300,
    "req_q": 200,               # buyer requirement question
}

PROFILE = {
    "prof_title": "Hospitality AI Automation Specialist",
    "bio": (
        "I build AI automation for vacation-rental and small-hotel hosts: the guest "
        "questions, review replies, turnover checklists and booking follow-ups that "
        "eat your day.\n\n"
        "I'm a Hotel Administration student, so I speak hospitality, not just code. "
        "I know what a 2am check-in question and a 42-message Tuesday actually cost you.\n\n"
        "Every build is tested, documented and handed over so you can run it without me. "
        "Clear scope, fast replies, no jargon.\n\n"
        "Automation I set up: guest messaging, review response, direct-booking follow-up, "
        "restock and turnover tracking."
    ),
    "skills": [
        "AI Automation", "Chatbot Development", "Workflow Automation", "API Integration",
        "Airbnb", "Vacation Rentals", "Hospitality", "Guest Communication",
        "Google Sheets", "Automation", "Problem Solving", "Communication",
        "Customer Service", "Attention to Detail", "Time Management",
    ],
    "languages": ["English", "Hindi", "Bangla"],
    "education": "Casa College, Nicosia — Hotel Administration",
}

GIG = {
    "title": "I will build AI automation and guest chatbots for vacation rentals",
    "tags": ["airbnb automation", "vacation rental", "ai chatbot", "ai automation", "guest messaging"],
    "description": (
        "Tired of answering the same guest questions at midnight? I build the AI "
        "automation that answers them for you — 24/7, in your voice.\n\n"
        "WHAT YOU GET\n"
        "✓ A working automation built around YOUR listing and house rules\n"
        "✓ AI guest-message responder for check-in, Wi-Fi, parking, check-out\n"
        "✓ Review response drafts so you never fall behind on reviews\n"
        "✓ Turnover / restock tracker so nothing gets missed between guests\n"
        "✓ Full handover doc + a walkthrough video so you can run it yourself\n\n"
        "WHY ME\n"
        "I study Hotel Administration — I understand your operation, not just the tech. "
        "I don't hand you a tool and disappear; I build it, test it, and show you how it works.\n\n"
        "WHY HOSTS ORDER THIS\n"
        "Every unanswered message is a worse review. Every slow reply is a booking lost "
        "to another host. Automation fixes both, starting today.\n\n"
        "Not sure what to automate first? Message me before ordering — I'll tell you "
        "honestly whether it's worth it."
    ),
    "packages": [
        {
            "name": "Starter",
            "price": 35,
            "desc": "1 automation: AI guest-message responder, tested and handed over with a walkthrough.",
            "delivery": "3 days",
            "revisions": 1,
        },
        {
            "name": "Host",
            "price": 95,
            "desc": "3 automations: guest messages + review replies + turnover tracker. Handover doc included.",
            "delivery": "5 days",
            "revisions": 2,
        },
        {
            "name": "Pro",
            "price": 195,
            "desc": "Full guest-journey automation with AI chatbot, review flow, trackers and a training call.",
            "delivery": "7 days",
            "revisions": 3,
        },
    ],
    "faqs": [
        ("Do you need access to my Airbnb account?",
         "No. I build with links, your house rules and your listing details. Where a tool needs a connection, I walk you through granting it safely — you stay in control of your account."),
        ("Will it sound like me?",
         "Yes. I train the replies on your actual house rules, tone and house style, so guests get your voice, not a generic bot. You approve the wording before anything goes live."),
        ("Which tools do you use?",
         "Whatever fits your setup — n8n, OpenAI, Google Sheets or Airtable, and the PMS or booking tools you already use. If you already pay for something, I build on top of it."),
        ("What do you need from me to start?",
         "Your listing link, your house rules, and a short list of the messages you answer most often. That's enough for me to start. Everything else I can ask as I build."),
        ("Do you work with small properties?",
         "Yes — most of my work is for single-listing hosts and small independents. You don't need a big operation to benefit from automation."),
    ],
    "requirements": [
        "What is the ONE message or task you answer most often? Be specific.",
        "Which platforms do you use (Airbnb, Booking.com, your own site, a PMS)?",
        "Paste your listing or website link, plus a sample of how you usually reply to guests.",
    ],
}

# ─────────────────────────── validation ───────────────────────────
def check(label, value, limit, count_chars=None):
    n = count_chars if count_chars is not None else len(value)
    ok = n <= limit
    flag = "PASS" if ok else "FAIL"
    print(f"  [{flag}] {label:<34} {n:>4}/{limit}")
    if not ok:
        print(f"         -> {value[:90]}...")
    return ok

def main():
    ok = True
    print("PROFILE")
    ok &= check("professional title", PROFILE["prof_title"], LIMITS["prof_title"])
    ok &= check("bio (About)", PROFILE["bio"], LIMITS["profile_bio"])
    ok &= check("skills count (max 15)", "x" * len(PROFILE["skills"]), 15)

    print("\nGIG")
    ok &= check("gig title (must start 'I will')", GIG["title"], LIMITS["gig_title"])
    ok &= check("  starts with 'I will'", GIG["title"][:6] if GIG["title"].startswith("I will") else "BAD", 6, count_chars=6 if GIG["title"].startswith("I will") else 99)
    ok &= check("description", GIG["description"], LIMITS["gig_description"])
    preview = GIG["description"].split("\n")[0]
    print(f"  [info] search preview (first 110): {preview[:110]}")
    ok &= check("tags count (max 5)", "x" * len(GIG["tags"]), 5)
    for t in GIG["tags"]:
        ok &= check(f"  tag: {t}", t, LIMITS["tag"])

    print("\nPACKAGES (3 max)")
    ok &= check("package count (max 3)", "x" * len(GIG["packages"]), 3)
    for p in GIG["packages"]:
        ok &= check(f"  {p['name']} desc", p["desc"], LIMITS["package_desc"])

    print("\nFAQs (10 max)")
    ok &= check("faq count (max 10)", "x" * len(GIG["faqs"]), 10)
    for q, a in GIG["faqs"]:
        ok &= check(f"  Q: {q[:30]}...", q, LIMITS["faq_q"])
        ok &= check(f"    A for {q[:18]}...", a, LIMITS["faq_a"])

    print("\nBUYER REQUIREMENTS")
    for r in GIG["requirements"]:
        ok &= check(f"  {r[:30]}...", r, LIMITS["req_q"])

    print("\n" + ("ALL FIELDS VALID ✅" if ok else "SOME FIELDS OVER LIMIT ❌"))
    return 0 if ok else 1

if __name__ == "__main__":
    raise SystemExit(main())
