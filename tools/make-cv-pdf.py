"""
Generates assets/Manoj-Rajan-CV.pdf - the file behind the site's "Download CV" button.

Run from the project root:      python tools/make-cv-pdf.py

Content mirrors the master CV. Edit the CONTENT block below and re-run; the
layout, spacing and page breaks are handled automatically.

Requires: pip install reportlab
"""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, Frame, KeepTogether, PageTemplate,
                                Paragraph, Spacer)

OUT = Path(__file__).resolve().parent.parent / "assets" / "Manoj-Rajan-CV.pdf"

# ── Identity ──────────────────────────────────────────────────────────────
NAME = "Manoj Rajan"
CREDENTIALS = "PMP<super rise=3 size=6>&#174;</super>  ·  CBAP<super rise=3 size=6>&#174;</super>  ·  ITIL<super rise=3 size=6>&#174;</super>"
TITLE = "Digital Transformation &amp; Enterprise Business Systems Lead"
TAGLINE = "Senior Business Analysis  ·  ERP &amp; Fleet Systems  ·  Transformation Delivery"
CONTACT = ("Dubai, UAE  ·  +971 56 285 5932  ·  "
           '<a href="mailto:echoflare06@gmail.com" color="#B45309">echoflare06@gmail.com</a>')
LINKS = ('<a href="https://www.linkedin.com/in/manojrajanuae/" color="#B45309">linkedin.com/in/manojrajanuae</a>'
         "  ·  "
         '<a href="https://mdxdxbhub2026.github.io/Portfolio/" color="#B45309">mdxdxbhub2026.github.io/Portfolio</a>')

INK = colors.HexColor("#0F172A")
ACCENT = colors.HexColor("#B45309")
BODY = colors.HexColor("#27313F")
MUTED = colors.HexColor("#5B6675")
RULE = colors.HexColor("#D8DEE7")

# ── Content ───────────────────────────────────────────────────────────────
SUMMARY = (
    "Digital Transformation and Enterprise Business Systems professional with 20+ years progressing "
    "from business analysis to specialist-level ownership of enterprise systems and fleet-wide "
    "transformation — including being retained through a company acquisition to lead the critical systems "
    "transition, then continuing to scale platform adoption and reporting automation across 70+ vessels. Delivered "
    "<b>USD 2.5M+</b> in cumulative savings and cost avoidance by driving system adoption to 90%, "
    "digitising procurement from manual quotations to 500+ daily transactions and building an "
    "in-house BI capability that replaced vendor-dependent reporting. Led cross-functional teams and "
    "up to 448 users through platform migrations and change management programmes, and provided functional "
    "leadership to a team of 10 Business Analysts while coordinating cross-functional delivery involving "
    "business users, technical teams, vendors, vessels and management."
)

HIGHLIGHTS = [
    "Retained through the UASC – Hapag-Lloyd acquisition to safeguard AMOS operations across "
    "<b>32 vessels</b> with zero operational disruption; later scaled SERTICA digital workflows to "
    "<b>448+ vessel and shore users</b> across 73 vessels.",
    "Revitalised the under-adopted AMOS ERP platform through capability assessment, process redesign "
    "and change management, raising adoption to <b>~90%</b> and avoiding ~USD 1M in replacement costs.",
    "Digitised procurement through the AMOS–ShipServ integration, from 5–6 manual quotations to "
    "<b>500+ daily digital transactions</b> and USD 1M+ in cumulative savings.",
    "Built an in-house reporting capability: <b>150+ SQL-based AMOS reports</b> (USD 500K+ vendor spend "
    "avoided) and 50+ SERTICA KPI dashboards replacing manual Excel reporting.",
]

COMPETENCIES = ("Digital transformation  ·  Enterprise business systems  ·  Business analysis (CBAP)  ·  "
                "Programme &amp; project delivery (PMP)  ·  ERP &amp; fleet management systems  ·  "
                "Systems integration  ·  Requirements &amp; UAT  ·  Release governance  ·  Change management  ·  "
                "Vendor &amp; stakeholder management  ·  SQL reporting &amp; KPI dashboards  ·  "
                "Process automation  ·  AI-assisted workflows")

EXPERIENCE = [
    {
        "role": "Specialist — Fleet Management Software / Central Operations",
        "dates": "Apr 2023 – Oct 2026",
        "org": "Hapag-Lloyd AG  ·  Dubai, UAE",
        "note": "Scope: Fleet-wide enterprise systems ownership, digital transformation delivery, "
                "business process improvement and cross-functional stakeholder coordination",
        "bullets": [
            "Led safety digitalisation across <b>73 vessels</b> and mobile maintenance workflows across "
            "40 vessels by standardising SERTICA processes, lifting adoption to 80–90% and cutting "
            "manual reporting effort by up to 90%.",
            "Transitioned <b>448+ vessel and shore users</b> onto standardised digital workflows through "
            "structured training and a SharePoint knowledge hub, embedding consistent practice fleet-wide.",
            "Delivered <b>50+ KPI dashboards</b> and automated reports via SQL Server and SERTICA's native "
            "reporting tool, replacing manual Excel processes and raising platform adoption to 80–90%.",
        ],
    },
    {
        "role": "Maritime IT Analyst — Fleet Management",
        "dates": "Jun 2017 – Mar 2023",
        "org": "Hapag-Lloyd AG  ·  Dubai, UAE",
        "note": "Retained through the UASC – Hapag-Lloyd acquisition to lead enterprise systems "
                "continuity and integration",
        "bullets": [
            "Safeguarded AMOS operations across <b>32 vessels</b> through the merger by coordinating "
            "enterprise systems integration and cross-functional migration of critical fleet applications, "
            "ensuring zero disruption to operations.",
            "Modernised infrastructure across 32 vessels — migrating legacy servers to VMware and "
            "standing up AMOS, Active Directory and file/email services — resolving 70–80% of "
            "critical production incidents and cutting post-migration downtime by ~90%.",
            "Established Jira-based incident management and a Confluence knowledge base, supporting "
            "SLA-based resolution of 30–40 monthly incidents while reducing reliance on subject-matter experts.",
        ],
    },
    {
        "role": "Senior Business Analyst — Fleet Management",
        "dates": "Feb 2006 – Jun 2017",
        "org": "United Arab Shipping Company (UASC)  ·  Dubai, UAE",
        "note": "Progressed through application support and business analysis responsibilities into a "
                "senior business analysis role within Fleet Management  ·  Scope: Enterprise business "
                "systems leadership",
        "bullets": [
            "Revitalised the under-adopted AMOS ERP platform through enterprise-wide capability assessment, "
            "process redesign and change management, raising adoption to approximately 90% and avoiding <b>~USD 1M</b> "
            "in system replacement costs.",
            "Digitised procurement via the AMOS–ShipServ integration, scaling daily quotation capacity "
            "from 5–6 manual requests to <b>500+ digital transactions</b> and delivering USD 1M+ in "
            "cumulative savings.",
            "Built <b>150+ SQL-based reports</b> and dashboards using AMOS's native reporting tool, reducing "
            "development costs by 75%, avoiding USD 500K+ in vendor expenditure and enabling faster "
            "operational decisions.",
            "Re-engineered workflows across three operational departments, digitising manual activities and "
            "cutting administrative paperwork by 75%.",
            "Directed end-to-end AMOS enhancement delivery — product roadmap, vendor negotiation, "
            "requirements, UAT and release governance — while providing functional leadership to a team "
            "of <b>10 Business Analysts</b>.",
        ],
    },
]

PROJECTS = [
    ("Enterprise Fleet Safety Digitalisation", "Hapag-Lloyd  ·  Jun 2022 – Jul 2026",
     "Digitised safety jobs, drills and event reporting across the fleet — requirements, process "
     "redesign, UAT, phased rollout and training with Fleet Management, HSEQ, IT, vessels and vendors."),
    ("AMOS–ShipServ TradeNet Integration", "UASC  ·  Dec 2014 – Dec 2015",
     "Led functional and integration delivery of the RFQ-to-order-confirmation cycle: interface and "
     "field mapping, validation rules, exception handling, integration testing and UAT across AMOS, "
     "ShipServ and Spectec."),
    ("Haulage Contract Data Automation", "UASC  ·  Dec 2015 – Feb 2016",
     "Converted haulage business rules into a macro-enabled Excel solution generating validated, "
     "upload-ready contract records."),
]

EXPERTISE = [
    ("Platforms &amp; tools", "SERTICA · AMOS ERP · ShipServ TradeNet · SQL Server · Microsoft 365 · "
                              "SharePoint · Jira · Confluence · VMware · Active Directory"),
]

EDUCATION = [
    ("Master of Computer Applications (MCA)", "Utkal University", "2002"),
    ("Bachelor of Science (BSc), Physics", "Sambalpur University", "1998"),
]

CERTIFICATIONS = [
    ("Project Management Professional (PMP<super rise=3 size=6>&#174;</super>)",
     "Project Management Institute (PMI)", "Issued Dec 2020 · valid to Dec 2027 · ID 2906566"),
    ("Certified Business Analysis Professional (CBAP<super rise=3 size=6>&#174;</super>)",
     "International Institute of Business Analysis (IIBA)",
     "Issued Jan 2021 · valid to Jan 2027 · ID 27452398"),
    ("ITIL<super rise=3 size=6>&#174;</super> Foundation", "EXIN",
     "Issued Mar 2009 · ID 5748085.20561483"),
    ("AI Development &amp; Agentic AI (CAIDP · CAAIP)", "LISRC",
     "In progress · expected Oct 2026"),
]

PROTOTYPES = (
    "Completing a three-month programme in AI development and agentic AI (CAIDP and CAAIP, LISRC), "
    "applied through independent, non-production prototypes built on synthetic data with AI-assisted "
    "development, prompt engineering and functional testing."
)

PROTOTYPE_ITEMS = [
    ('<a href="https://mdxdxbhub2026.github.io/maritime-operations-ai/#/dashboard" color="#B45309">'
     "Maritime Operations AI Control Tower</a>",
     "Live web app (React, TypeScript) — fleet overview, anomaly detection, predictive maintenance, "
     "voyage and fuel optimisation, safety monitoring and human-in-the-loop automation with approval gates."),
    ('<a href="https://mdxdxbhub2026.github.io/Maritime-Haulage-Intelligence/" color="#B45309">'
     "Maritime Haulage Intelligence</a>",
     "Live web app — the 2015 UASC haulage contract capability rebuilt with a deterministic rule engine, "
     "weight-slab generator and an AI layer kept clear of the calculation path."),
    ("More concepts",
     'GreenRoute AI, CareerConnectAI, Ledger 24K — '
     '<a href="https://mdxdxbhub2026.github.io/digital-ai-portfolio/" color="#B45309">'
     "mdxdxbhub2026.github.io/digital-ai-portfolio</a>"),
]

# ── Styles ────────────────────────────────────────────────────────────────
S = {
    "name": ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=23, leading=26,
                           textColor=INK, spaceAfter=3),
    "creds": ParagraphStyle("creds", fontName="Helvetica-Bold", fontSize=8, leading=11,
                            textColor=ACCENT, spaceAfter=5),
    "title": ParagraphStyle("title", fontName="Helvetica", fontSize=11, leading=14,
                            textColor=BODY, spaceAfter=2),
    "tagline": ParagraphStyle("tagline", fontName="Helvetica", fontSize=8.2, leading=11,
                              textColor=MUTED, spaceAfter=6),
    "contact": ParagraphStyle("contact", fontName="Helvetica", fontSize=8.5, leading=12,
                              textColor=BODY),
    "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=9, leading=11,
                         textColor=INK, spaceBefore=11, spaceAfter=5),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=8.8, leading=12.4,
                           textColor=BODY, alignment=TA_JUSTIFY),
    "role": ParagraphStyle("role", fontName="Helvetica-Bold", fontSize=10, leading=12.5,
                           textColor=INK, spaceBefore=7),
    "org": ParagraphStyle("org", fontName="Helvetica-Bold", fontSize=8.6, leading=11,
                          textColor=BODY, spaceBefore=1),
    "note": ParagraphStyle("note", fontName="Helvetica-Oblique", fontSize=8, leading=10.5,
                           textColor=MUTED, spaceAfter=3),
    "dates": ParagraphStyle("dates", fontName="Helvetica-Bold", fontSize=8, leading=11,
                            textColor=ACCENT),
    "bullet": ParagraphStyle("bullet", fontName="Helvetica", fontSize=8.8, leading=12.2,
                             textColor=BODY, leftIndent=10, bulletIndent=1, spaceAfter=2.5,
                             alignment=TA_JUSTIFY),
    "kv": ParagraphStyle("kv", fontName="Helvetica", fontSize=8.8, leading=12.2,
                         textColor=BODY, leftIndent=10, bulletIndent=1, spaceAfter=2.5),
}


def rule(width, thickness=0.6, color=RULE, space=3):
    """A horizontal rule as a flowable."""
    from reportlab.platypus import Flowable

    class Rule(Flowable):
        def __init__(self):
            super().__init__()
            self.width, self.height = width, thickness + space

        def draw(self):
            self.canv.setStrokeColor(color)
            self.canv.setLineWidth(thickness)
            self.canv.line(0, space, self.width, space)

    return Rule()


def heading(text, width):
    """Section heading with its underline, kept together with what follows."""
    return [Paragraph(text.upper(), S["h2"]), rule(width, 1.1, ACCENT, 2), Spacer(1, 4)]


def build() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    margin = 15 * mm
    width = A4[0] - 2 * margin

    def decorate(canvas, doc):
        canvas.saveState()
        # Accent spine down the left edge
        canvas.setFillColor(ACCENT)
        canvas.rect(0, 0, 3.2 * mm, A4[1], stroke=0, fill=1)
        # Footer
        canvas.setFont("Helvetica", 7)
        canvas.setFillColor(MUTED)
        canvas.drawString(margin, 9 * mm, f"{NAME}  ·  Curriculum Vitae")
        canvas.drawRightString(A4[0] - margin, 9 * mm, f"Page {doc.page}")
        canvas.restoreState()

    doc = BaseDocTemplate(str(OUT), pagesize=A4,
                          leftMargin=margin, rightMargin=margin,
                          topMargin=14 * mm, bottomMargin=16 * mm,
                          title=f"{NAME} — Curriculum Vitae", author=NAME,
                          subject="Digital Transformation & Enterprise Business Systems Lead",
                          keywords="Digital Transformation, Enterprise Business Systems, Business Analysis, "
                                   "PMP, CBAP, ERP, AMOS, SERTICA, Fleet Management Systems, Dubai")
    frame = Frame(margin, 16 * mm, width, A4[1] - 30 * mm, id="body",
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="cv", frames=[frame], onPage=decorate)])

    st = []

    # Header
    st += [Paragraph(NAME, S["name"]),
           Paragraph(CREDENTIALS, S["creds"]),
           Paragraph(TITLE, S["title"]),
           Paragraph(TAGLINE, S["tagline"]),
           Paragraph(CONTACT, S["contact"]),
           Paragraph(LINKS, S["contact"]),
           Spacer(1, 3), rule(width, 1.4, INK, 2)]

    st += heading("Professional summary", width)
    st += [Paragraph(SUMMARY, S["body"])]

    st += heading("Career highlights", width)
    st += [Paragraph(h, S["bullet"], bulletText="•") for h in HIGHLIGHTS]

    st += heading("Core competencies", width)
    st += [Paragraph(COMPETENCIES, S["body"]), Spacer(1, 3)]
    for label, items in EXPERTISE:
        st += [Paragraph(f"<b>{label}:</b> {items}", S["kv"], bulletText="•")]

    st += heading("Work experience", width)
    for job in EXPERIENCE:
        block = [Paragraph(job["role"], S["role"]),
                 Paragraph(f'{job["dates"]}', S["dates"]),
                 Paragraph(job["org"], S["org"]),
                 Paragraph(job["note"], S["note"])]
        block += [Paragraph(b, S["bullet"], bulletText="•") for b in job["bullets"][:2]]
        st += [KeepTogether(block)]
        st += [Paragraph(b, S["bullet"], bulletText="•") for b in job["bullets"][2:]]

    st += heading("Selected projects", width)
    for name, meta, desc in PROJECTS:
        st += [Paragraph(f"<b>{name}</b>  <font color='#B45309' size=7.6>{meta}</font><br/>{desc}",
                         S["kv"], bulletText="•")]

    st += heading("Education", width)
    for degree, school, year in EDUCATION:
        st += [Paragraph(f"<b>{degree}</b>, {school}  ·  <font color='#B45309'>{year}</font>",
                         S["kv"], bulletText="•")]

    st += heading("Certifications", width)
    for cert, body_name, detail in CERTIFICATIONS:
        st += [Paragraph(f"<b>{cert}</b> — {body_name}"
                         f"<font color='#5B6675' size=7.6>&nbsp; {detail}</font>",
                         S["kv"], bulletText="•")]

    st += heading("AI development &amp; independent prototypes", width)
    st += [Paragraph(PROTOTYPES, S["body"]), Spacer(1, 3)]
    for name, desc in PROTOTYPE_ITEMS:
        st += [Paragraph(f"<b>{name}</b> — {desc}", S["kv"], bulletText="•")]

    doc.build(st)
    print(f"Wrote {OUT}  ({OUT.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    build()
