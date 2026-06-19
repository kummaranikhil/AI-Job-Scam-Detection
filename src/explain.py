def explain_prediction(job_text):

    suspicious_keywords = {

        "urgent": "Urgent hiring",

        "immediately": "Immediate joining",

        "whatsapp": "WhatsApp communication",

        "telegram": "Telegram communication",

        "earn": "High salary promise",

        "weekly": "Weekly payment",

        "daily": "Daily payment",

        "investment": "Investment required",

        "registration fee": "Registration fee",

        "payment": "Advance payment requested",

        "work from home": "Work From Home",

        "no experience": "No experience required",

        "limited seats": "Creates false urgency",

        "click here": "Suspicious external link",

        "apply now": "Pressure to apply quickly",

        "guaranteed": "Unrealistic guarantee"

    }

    job_text = job_text.lower()

    found = []

    for keyword, reason in suspicious_keywords.items():

        if keyword in job_text:

            found.append(reason)

    return found