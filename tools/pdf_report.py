import os
from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(result):

    os.makedirs("reports", exist_ok=True)

    # Unique filename
    filename = datetime.now().strftime(
        "evaluation_%Y%m%d_%H%M%S.pdf"
    )

    filepath = os.path.join("reports", filename)

    doc = SimpleDocTemplate(filepath)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph("<b>Assignment Evaluation Report</b>", styles["Title"])
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(result.replace("\n", "<br/>"), styles["BodyText"])
    )

    doc.build(story)

    return filepath