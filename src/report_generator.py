from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from pathlib import Path
from datetime import datetime


def generate_report(job_text, prediction, confidence, risk, reasons):

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    filename = reports_dir / f"Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

    doc = SimpleDocTemplate(str(filename))
    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AI Job Scam Detection Report</b>", styles["Title"]))
    story.append(Paragraph(f"<b>Date:</b> {datetime.now()}", styles["Normal"]))
    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph(f"<b>Prediction:</b> {prediction}", styles["Normal"]))
    story.append(Paragraph(f"<b>Confidence:</b> {confidence:.2f}%", styles["Normal"]))
    story.append(Paragraph(f"<b>Risk Level:</b> {risk}", styles["Normal"]))
    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>AI Explanation</b>", styles["Heading2"]))

    if reasons:
        for reason in reasons:
            story.append(Paragraph(f"• {reason}", styles["Normal"]))
    else:
        story.append(Paragraph("No suspicious keywords detected.", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))
    story.append(Paragraph("<b>Job Description</b>", styles["Heading2"]))
    story.append(Paragraph(job_text.replace("\n", "<br/>"), styles["Normal"]))

    doc.build(story)

    return filename