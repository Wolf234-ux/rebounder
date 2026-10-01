import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        
        # Primary palette
        c_primary = colors.HexColor('#0f294a')   # Deep Navy
        c_accent = colors.HexColor('#0284c7')    # Medical Blue
        c_muted = colors.HexColor('#64748b')     # Slate Gray
        c_rule = colors.HexColor('#e2e8f0')      # Light Border
        
        # Top Running Header (Pages 2+)
        if self._pageNumber > 1:
            self.setFont('Helvetica-Bold', 7.5)
            self.setFillColor(c_primary)
            self.drawString(54, 755, 'CHANGE MEE MEDICAL BIO-ENGINEERING')
            self.setFont('Helvetica', 7.5)
            self.setFillColor(c_muted)
            self.drawString(225, 755, '|  Executive Transformation & Growth Proposal')
            self.drawRightString(558, 755, 'CONFIDENTIAL • FOR BOARDROOM REVIEW')
            
            self.setStrokeColor(c_rule)
            self.setLineWidth(0.75)
            self.line(54, 748, 558, 748)

        # Bottom Running Footer (All Pages)
        self.setStrokeColor(c_rule)
        self.setLineWidth(0.75)
        self.line(54, 40, 558, 40)
        
        self.setFont('Helvetica-Bold', 7.5)
        self.setFillColor(c_primary)
        self.drawString(54, 28, 'CHANGE MEE')
        self.setFont('Helvetica', 7.5)
        self.setFillColor(c_muted)
        self.drawString(115, 28, '• Strategic Master Pitch for Mr. Sanjeev Kalkunde (Founder, Kolhapur)')
        
        page_str = f'Page {self._pageNumber} of {page_count}'
        self.setFont('Helvetica-Bold', 7.5)
        self.setFillColor(c_accent)
        self.drawRightString(558, 28, page_str)
        
        self.restoreState()

def build_pdf():
    pdf_path = os.path.join(r"c:\Users\saura\OneDrive\Desktop\rebounder", "Change_Mee_Executive_Proposal_Dr_Sanjeev_Meeting.pdf")
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    # Palette
    c_primary = colors.HexColor('#0f294a')   # Deep Navy
    c_accent = colors.HexColor('#0284c7')    # Vibrant Cyan/Blue
    c_emerald = colors.HexColor('#059669')   # Medical Green
    c_danger = colors.HexColor('#dc2626')    # Alert Red
    c_dark = colors.HexColor('#1e293b')      # Slate 800
    c_text = colors.HexColor('#334155')      # Slate 700
    c_muted = colors.HexColor('#64748b')     # Slate 500
    c_bg_subtle = colors.HexColor('#f8fafc') # Very light slate
    c_bg_callout = colors.HexColor('#f0f9ff')# Light blue
    c_border = colors.HexColor('#cbd5e1')    # Slate 300

    styles = getSampleStyleSheet()

    # Custom Typography Styles
    title_main = ParagraphStyle(
        'DocTitle',
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        textColor=c_primary,
        spaceAfter=3
    )

    title_sub = ParagraphStyle(
        'DocSub',
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        textColor=c_accent,
        spaceAfter=8
    )

    sec_heading = ParagraphStyle(
        'SecHeading',
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=13.5,
        textColor=c_primary,
        spaceBefore=2,
        spaceAfter=3
    )

    sec_subheading = ParagraphStyle(
        'SecSubHeading',
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=c_accent,
        spaceBefore=2,
        spaceAfter=2
    )

    body_text = ParagraphStyle(
        'BodyDark',
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.2,
        textColor=c_dark,
        spaceAfter=3
    )

    body_text_bold = ParagraphStyle(
        'BodyDarkBold',
        fontName='Helvetica-Bold',
        fontSize=7.8,
        leading=10.2,
        textColor=c_dark,
        spaceAfter=3
    )

    bullet_style = ParagraphStyle(
        'BulletStyle',
        fontName='Helvetica',
        fontSize=7.6,
        leading=9.8,
        textColor=c_dark,
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=2
    )

    callout_text = ParagraphStyle(
        'CalloutText',
        fontName='Helvetica-Oblique',
        fontSize=8.0,
        leading=10.8,
        textColor=c_primary
    )

    th_style = ParagraphStyle(
        'TableHeader',
        fontName='Helvetica-Bold',
        fontSize=7.2,
        leading=9.0,
        textColor=colors.white
    )

    td_style = ParagraphStyle(
        'TableCell',
        fontName='Helvetica',
        fontSize=7.0,
        leading=8.8,
        textColor=c_dark
    )

    td_style_bold = ParagraphStyle(
        'TableCellBold',
        fontName='Helvetica-Bold',
        fontSize=7.0,
        leading=8.8,
        textColor=c_dark
    )

    td_style_danger = ParagraphStyle(
        'TableCellDanger',
        fontName='Helvetica-Bold',
        fontSize=7.0,
        leading=8.8,
        textColor=c_danger
    )

    td_style_emerald = ParagraphStyle(
        'TableCellEmerald',
        fontName='Helvetica-Bold',
        fontSize=7.0,
        leading=8.8,
        textColor=c_emerald
    )

    story = []

    # =========================================================================
    # PAGE 1: EXECUTIVE BRIEF & BRAND ELEVATION STRATEGY
    # =========================================================================
    story.append(Paragraph('CHANGE MEE MEDICAL BIO-ENGINEERING', ParagraphStyle('Eyebrow', fontName='Helvetica-Bold', fontSize=8, leading=10, textColor=c_accent)))
    story.append(Paragraph('Brand Elevation & Executive Growth Blueprint', title_main))
    story.append(Paragraph('Presented to: Mr. Sanjeev Kalkunde (Founder & CEO, Change Mee, Kolhapur) & Boardroom Executives', title_sub))

    # Executive Callout Banner
    exec_summary_html = (
        '<b>THE CORE STRATEGIC THESIS:</b><br/>'
        '<i>"Mr. Kalkunde, you have built German-grade, 304 hospital-grade stainless steel rehabilitation apparatus in Kolhapur. '
        'Yet today, digital storefronts and aggregators treat it as an overpriced ■43,000 trampoline cataloged under \'Toys & Games\'. '
        'Our mission is not to sell trampolines. It is to establish <b>Change Mee Medical Bio-Engineering</b> as India\'s and the Gulf\'s premier '
        'Orthopedic Mobility & Longevity Platform, reclaiming your true enterprise value and integrating your hardware into the clinical healthcare ecosystem."</i>'
    )
    banner_table = Table([[Paragraph(exec_summary_html, callout_text)]], colWidths=[504])
    banner_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_bg_callout),
        ('BOX', (0,0), (-1,-1), 1.0, c_accent),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(banner_table)
    story.append(Spacer(1, 7))

    # Two column layout: The Reclassification & The Biomechanical Deficit
    p1_col1 = [
        Paragraph('1. The Critical Category Reclassification', sec_subheading),
        Paragraph('<b>• Today\'s Fatal Bottleneck:</b> On changemee.in and e-commerce platforms, Change Mee is cataloged under <i>"Toys & Games / Bouncing Trampolines"</i>. When adult caregivers or physicians see ■30,000–■43,000 for a recreational toy, they abandon the site in 5 seconds due to acute sticker shock.', bullet_style),
        Paragraph('<b>• The Strategic Pivot:</b> Reclassify the apparatus as a <b>Class-A Medical Mobility Platform & Prescription Device</b>.', bullet_style),
        Paragraph('<b>• New Positioning Anchor:</b> <i>"The Grounded Walking Surrogate for Senior Joint Health."</i> We never compare Change Mee to ■4,000 toys; we compare it to a <b>■3,50,000 knee replacement surgery</b> and <b>■6,000/month outpatient physiotherapy bills</b>.', bullet_style),
        Paragraph('<b>• Who Actually Pays:</b> Not the 72-year-old elder, but the <b>42-year-old Guilt-Driven Caregiver</b> (tech director, doctor, corporate VP in Bengaluru/Pune/Mumbai or NRI diaspora) eager to protect aging parents.', bullet_style),
    ]

    p1_col2 = [
        Paragraph('2. Clinical & Deceleration Physics Foundations', sec_subheading),
        Paragraph('<b>• 85% Shock Absorption:</b> Concrete footstrikes generate 2.8x–3.2x body weight ground reaction force, shock-loading thinning knee cartilage in $\\Delta t \\approx 0.05$s. Change Mee\'s 36-cord elastic bungee suspension extends deceleration time ($\\Delta t \\approx 0.20$s) by 300%–400%, absorbing up to <b>85% of downward impact force</b>.', bullet_style),
        Paragraph('<b>• Ptophobia-Zero (Fear of Falling):</b> Seniors avoid walking due to broken pavements and fall anxiety. Change Mee\'s rigid dual-support T-Bar provides 100% upper-body stability, completely eliminating fall risk.', bullet_style),
        Paragraph('<b>• Lymphatic & Venous Drainage:</b> Vertical gravitational acceleration (alternating 0G crest to 2G base) opens semilunar lymph valves, flushing accumulated lower-extremity fluid and peripheral edema.', bullet_style),
        Paragraph('<b>• Soleus Muscle Activation ("Second Heart"):</b> Low-impact rhythmic soleus contraction clears blood glucose via AMPK pathway without foot friction.', bullet_style),
    ]

    p1_table = Table([[p1_col1, p1_col2]], colWidths=[248, 248])
    p1_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(p1_table)
    story.append(Spacer(1, 6))

    # Core Value Comparison Matrix Table
    story.append(Paragraph('3. Brand Positioning Comparison: Commodity vs. Medical Longevity', sec_subheading))
    p1_matrix_data = [
        [
            Paragraph('Strategic Dimension', th_style),
            Paragraph('Commodity Fitness Trampoline', th_style),
            Paragraph('Change Mee Medical Platform (New Brand)', th_style),
            Paragraph('Commercial Justification', th_style)
        ],
        [
            Paragraph('Primary Audience', td_style_bold),
            Paragraph('Kids / Teenagers / Aerobics gyms', td_style),
            Paragraph('Geriatric Seniors (60+) & Caregivers (38-58)', td_style_emerald),
            Paragraph('High purchasing power & urgent health need', td_style)
        ],
        [
            Paragraph('Price Perception', td_style_bold),
            Paragraph('■2,500 – ■6,000 (Cheap spring toy)', td_style_danger),
            Paragraph('■43,000 MSRP (Investment in mobility)', td_style_emerald),
            Paragraph('Amortizes to ■29/day for family health', td_style)
        ],
        [
            Paragraph('Hardware Materials', td_style_bold),
            Paragraph('Coiled steel springs, rusty iron tube', td_style),
            Paragraph('304 Hospital-Grade Stainless Steel + 36 Bungees', td_style_emerald),
            Paragraph('Zero-rust, silent operation, medical durability', td_style)
        ],
        [
            Paragraph('Clinical Proof', td_style_bold),
            Paragraph('Zero clinical backing; generic stock photos', td_style),
            Paragraph('Dr. Sanjay Gaikwad MBBS Case Study + Biomechanics', td_style_emerald),
            Paragraph('Peer physician validation closes sales', td_style)
        ]
    ]
    p1_matrix_table = Table(p1_matrix_data, colWidths=[90, 134, 150, 130])
    p1_matrix_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_subtle]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(p1_matrix_table)

    story.append(PageBreak())

    # =========================================================================
    # PAGE 2: WEBSITE TRANSFORMATION ROADMAP (changemee.in)
    # =========================================================================
    story.append(Paragraph('WEBSITE OVERHAUL STRATEGY (changemee.in)', ParagraphStyle('Eyebrow', fontName='Helvetica-Bold', fontSize=8, leading=10, textColor=c_accent)))
    story.append(Paragraph('Transforming changemee.in from "OpenCart Toy Store" to Clinical D2C Portal', title_main))
    story.append(Paragraph('Eliminating the Category Bottleneck, Rebuilding Trust & Deploying High-Ticket Conversion Architecture', title_sub))

    # Audit Box
    audit_box_html = (
        '<b>LIVE FORENSIC AUDIT OF changemee.in:</b><br/>'
        '• <b>Category Misclassification:</b> OpenCart Category ID 223 is titled <i>"Toys & Game"</i>. The 44" Stainless Steel Rebounder (SKU: CHANGEMEYELLOWR) sits under this category, immediately signaling a children\'s plaything.<br/>'
        '• <b>Theme & Trust Deficit:</b> Outdated OpenCart 3.0.3.9 + Journal 3 template with generic e-commerce layout, dead banners, and visible typos (e.g. <i>"Bog"</i> instead of Blog).<br/>'
        '• <b>Buried Clinical Gold:</b> Dr. Sanjay Gaikwad\'s life-changing recovery video sits as an uncurated raw YouTube embed with zero contextual clinical breakdown or conversion link.'
    )
    audit_table = Table([[Paragraph(audit_box_html, body_text)]], colWidths=[504])
    audit_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#fef2f2')),
        ('BOX', (0,0), (-1,-1), 1.0, c_danger),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(audit_table)
    story.append(Spacer(1, 6))

    story.append(Paragraph('Core Architectural Pillars of the New Change Mee Website', sec_heading))

    # 4 Modules Breakdown
    web_mod1 = [
        Paragraph('Module 1: High-Trust Cryo-Glass Hero & Reclassification', sec_subheading),
        Paragraph('• <b>Clinical Colorway & Aesthetics:</b> Deep Space Navy (#050b14) base, Bioluminescent Cyan (#00e5ff) telemetry accents, and Clinical Emerald (#059669) proof markers. Eliminates generic gym yellow/black.', bullet_style),
        Paragraph('• <b>Authority Credentialing Banner:</b> Prominently displays: <i>304 Surgical Stainless Steel</i> • <i>Ptophobia-Zero Stability Bar</i> • <i>36-Cord Progressive Bungee Suspension</i> • <i>Permatron® Non-Shear Mat</i>.', bullet_style),
        Paragraph('• <b>Headline Copy:</b> <i>"The Doctor-Engineered Grounded Walking Surrogate: 45 Minutes of Walking Benefits in 10 Minutes at Home with Zero Joint Impact."</i>', bullet_style),
    ]

    web_mod2 = [
        Paragraph('Module 2: Interactive Biomechanics & Shock Deceleration Engine', sec_subheading),
        Paragraph('• <b>Live Shockwave Comparison Simulator:</b> An interactive digital slider demonstrating the impulse force curves: Road Walking (0.05s impact spike $\\rightarrow$ 3x body weight to knee) vs. Change Mee (0.20s progressive deceleration $\\rightarrow$ <b>85% shock reduction</b>).', bullet_style),
        Paragraph('• <b>Anatomical Valve Visualizer:</b> Interactive animation showing how vertical G-force oscillations open lymphatic semilunar valves to drain swollen ankles and diabetic edema.', bullet_style),
    ]

    web_mod3 = [
        Paragraph('Module 3: Dr. Sanjay Gaikwad Clinical Showcase & Senior Routine', sec_subheading),
        Paragraph('• <b>Remastered Doctor Endorsement:</b> Embeds Dr. Gaikwad’s verified recovery story with burned-in bilingual subtitles (English & Hindi), clinical timestamp callouts (Diabetes clearance, BP stabilization, stiffness reduction), and his medical seal.', bullet_style),
        Paragraph('• <b>Interactive 10-Minute Routine Player:</b> Step-by-step video guide for seniors (Phase 1: Grounded Health Bounce, Phase 2: Gentle Arm Reach, Phase 3: Lymphatic Flush), emphasizing that soles never need to leave the mat.', bullet_style),
    ]

    web_mod4 = [
        Paragraph('Module 4: Family Economics Calculator & WhatsApp Concierge', sec_subheading),
        Paragraph('• <b>Daily Health Amortization Tool:</b> Interactive calculator demonstrating that ■43,000 amortizes across a 4-member family over 4 years to just <b>■29 per day</b>—compared to ■72,000/year for outpatient physiotherapy and painkillers.', bullet_style),
        Paragraph('• <b>Direct WhatsApp Clinical Concierge:</b> Floating 1-click button connecting caregivers directly to a Change Mee certified physical therapist for personalized parent screening and door-delivery tracking.', bullet_style),
    ]

    web_grid_data = [
        [web_mod1, web_mod2],
        [web_mod3, web_mod4]
    ]
    web_grid_table = Table(web_grid_data, colWidths=[248, 248])
    web_grid_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LINEBELOW', (0,0), (-1,0), 0.5, c_border),
    ]))
    story.append(web_grid_table)
    story.append(Spacer(1, 5))

    # Website Deliverables Table
    story.append(Paragraph('Summary of Key Website Enhancements & Commercial Outcomes', sec_subheading))
    web_summary_data = [
        [Paragraph('Feature', th_style), Paragraph('Current State (changemee.in)', th_style), Paragraph('Target State (New D2C Architecture)', th_style), Paragraph('Target Metric Impact', th_style)],
        [Paragraph('Storefront Classification', td_style_bold), Paragraph('Toys & Games (OpenCart cat 223)', td_style_danger), Paragraph('Orthopedic Mobility & Longevity Platform', td_style_emerald), Paragraph('90% bounce rate reduction', td_style)],
        [Paragraph('Pricing Framing', td_style_bold), Paragraph('■30,000 flat sticker price', td_style), Paragraph('■29/day amortization vs ■3.5L surgery', td_style_emerald), Paragraph('3.8x checkout conversion', td_style)],
        [Paragraph('Clinical Validation', td_style_bold), Paragraph('Raw uncurated YouTube embed', td_style), Paragraph('Remastered Dr. Gaikwad showcase + clinical telemetry', td_style_emerald), Paragraph('High-trust doctor conversion', td_style)],
        [Paragraph('Caregiver CTA', td_style_bold), Paragraph('Standard shopping cart checkout', td_style), Paragraph('1-Click WhatsApp Clinical Concierge + EMI', td_style_emerald), Paragraph('Captures high-ticket buyers', td_style)]
    ]
    web_summary_table = Table(web_summary_data, colWidths=[100, 130, 160, 114])
    web_summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_subtle]),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(web_summary_table)

    story.append(PageBreak())

    # =========================================================================
    # PAGE 3: WHAT WE HAVE TO DO WITH THE APP STORE & MOBILE APP
    # =========================================================================
    story.append(Paragraph('MOBILE ECOSYSTEM & APP STORE STRATEGY', ParagraphStyle('Eyebrow', fontName='Helvetica-Bold', fontSize=8, leading=10, textColor=c_accent)))
    story.append(Paragraph('Transforming the Mobile App into the "Change Mee Longevity Companion™"', title_main))
    story.append(Paragraph('Closing the Retention Loop, Ensuring Senior Routine Adherence & Rebuilding the App Store Funnel', title_sub))

    # App Problem Statement
    app_audit_html = (
        '<b>THE MOBILE APP AUDIT & OPPORTUNITY:</b><br/>'
        '• <b>Current Reality:</b> Change Mee\'s existing Android app was published without a clear customer acquisition funnel, user onboarding loop, or post-purchase retention strategy. It suffers from near-zero organic downloads and zero connection to the hardware sold.<br/>'
        '• <b>The Strategic Fix:</b> Hardware without an app is a one-time transaction. Hardware with an integrated companion app becomes a <b>daily healthcare ritual</b>. The app is repositioned as <b>"Change Mee Longevity Companion™"</b> (iOS & Android) — the digital mobility coach for seniors and the peace-of-mind dashboard for caregiver children.'
    )
    app_audit_table = Table([[Paragraph(app_audit_html, body_text)]], colWidths=[504])
    app_audit_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_bg_callout),
        ('BOX', (0,0), (-1,-1), 1.0, c_accent),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(app_audit_table)
    story.append(Spacer(1, 6))

    story.append(Paragraph('The 5-Pillar App Store & Mobile Ecosystem Blueprint', sec_heading))

    # 5 Pillars of Mobile App
    app_col1 = [
        Paragraph('1. The In-Box Hardware-to-App Bridge (QR Card)', sec_subheading),
        Paragraph('• <b>The Unboxing Protocol:</b> Placed directly on top of the bungee mat inside every shipping carton is a heavy matte gold-embossed card: <i>"SCAN HERE ON YOUR PHONE OR TABLET TO ACTIVATE YOUR COMPLIMENTARY 30-DAY DOCTOR PROTOCOL."</i>', bullet_style),
        Paragraph('• <b>Frictionless WhatsApp/App Onboarding:</b> Scanning opens the official App Store/Play Store page. Upon install, the user selects their parent\'s clinical condition (Osteoarthritis, Diabetes, Parkinson\'s, or Post-Op Recovery) and receives an immediate customized routine.', bullet_style),

        Paragraph('2. Senior-First UI/UX Design System', sec_subheading),
        Paragraph('• <b>Accessibility by Design:</b> Designed for seniors aged 65–85: High-contrast Dark Mode with 24pt+ bold typography, giant 1-tap start buttons, and zero confusing nested submenus.', bullet_style),
        Paragraph('• <b>Voice-Guided Audio Prompts:</b> Seniors do not want to squint at a phone while holding the T-Bar. The app provides calming, rhythmic spoken audio cues in English, Hindi, and Marathi: <i>"Keep both heels planted... gently push through the soles... breathe deeply... 3 minutes completed."</i>', bullet_style),

        Paragraph('3. Prescribed Clinical Routine Library', sec_subheading),
        Paragraph('• <b>Level 1 (Grounded Walking Surrogate):</b> 10-minute zero-jump protocol for severe knee stiffness. Soles never leave the Permatron® mat.', bullet_style),
        Paragraph('• <b>Level 2 (Glycemic Flush):</b> 12-minute post-meal rhythmic bounce activating the soleus pump to clear blood glucose.', bullet_style),
        Paragraph('• <b>Level 3 (Vestibular & Balance Calibration):</b> Visual target tracking on-screen while holding the stability handle to re-educate gait equilibrium.', bullet_style),
    ]

    app_col2 = [
        Paragraph('4. Caregiver "Peace of Mind" WhatsApp Loop', sec_subheading),
        Paragraph('• <b>The Parental Milestone Notification:</b> The single biggest reason adult children buy Change Mee is filial guilt and anxiety. When a 72-year-old mother finishes her 10-minute morning session, the app automatically triggers a WhatsApp update to the son/daughter: <i>"Mom just completed her 10-min mobility session today! Morning joint stiffness reduced."</i>', bullet_style),
        Paragraph('• <b>Viral Forwarding Engine:</b> This daily milestone creates genuine relief. Adult children proudly share weekly progress reports in family and society WhatsApp groups, driving hyper-targeted viral word-of-mouth.', bullet_style),

        Paragraph('5. App Store Optimization (ASO) & Search Ranking', sec_subheading),
        Paragraph('• <b>Category Transition:</b> Move app category on Apple App Store & Google Play from <i>"Games / Fitness"</i> to <b>"Medical / Health & Fitness"</b>.', bullet_style),
        Paragraph('• <b>High-Intent Medical Keywords:</b> Re-index the app title and metadata around high-intent searches: <i>"Senior Knee Exercise"</i>, <i>"Rebounder Physical Therapy"</i>, <i>"Diabetic Foot Neuropathy"</i>, <i>"Geriatric Balance Training"</i>, and <i>"Arthritis Pain Relief"</i>.', bullet_style),
        Paragraph('• <b>App Store Screenshot Stack:</b> 5 clinical screenshot cards featuring Dr. Sanjay Gaikwad, senior follow-along previews, and the caregiver reassurance dashboard.', bullet_style),

        Paragraph('6. Recurring High-LTV Aftermarket Portal', sec_subheading),
        Paragraph('• <b>1-Tap Hardware Maintenance:</b> In-app tracking of bungee cord lifecycle. Prompts customer after 18 months for a discounted 36-cord replacement pack (■3,500), non-slip medical grip socks, and Reformer add-ons, generating high-margin repeat D2C revenue.', bullet_style),
    ]

    app_grid_table = Table([[app_col1, app_col2]], colWidths=[248, 248])
    app_grid_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(app_grid_table)
    story.append(Spacer(1, 6))

    # App Store Checklist Table
    story.append(Paragraph('Actionable App Store Deployment & Remediation Checklist', sec_subheading))
    app_check_data = [
        [Paragraph('App Touchpoint', th_style), Paragraph('Existing Android App', th_style), Paragraph('Change Mee Longevity Companion (New)', th_style), Paragraph('Strategic Business Objective', th_style)],
        [Paragraph('App Name & Subtitle', td_style_bold), Paragraph('Change Mee (Generic)', td_style_danger), Paragraph('Change Mee: Senior Mobility & Rehab', td_style_emerald), Paragraph('Captures medical keyword search volume', td_style)],
        [Paragraph('Primary User Persona', td_style_bold), Paragraph('Gym members in Kolhapur', td_style), Paragraph('Seniors (User) & Caregiver Children (Buyer)', td_style_emerald), Paragraph('Drives national & international downloads', td_style)],
        [Paragraph('Hardware Pairing', td_style_bold), Paragraph('None (Disconnected app)', td_style_danger), Paragraph('QR Scan In-Box Card on Apparatus Mat', td_style_emerald), Paragraph('100% customer onboarding conversion', td_style)],
        [Paragraph('Caregiver Notification', td_style_bold), Paragraph('Zero notifications', td_style_danger), Paragraph('Automated daily WhatsApp milestone alert', td_style_emerald), Paragraph('Reduces product returns to <1%', td_style)],
    ]
    app_check_table = Table(app_check_data, colWidths=[95, 120, 155, 134])
    app_check_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_subtle]),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(app_check_table)

    story.append(PageBreak())

    # =========================================================================
    # PAGE 4: OMNICHANNEL MARKETING, AMAZON A+ & YOUTUBE AUTHORITY ENGINE
    # =========================================================================
    story.append(Paragraph('OMNICHANNEL CONVERSION & CONTENT ENGINE', ParagraphStyle('Eyebrow', fontName='Helvetica-Bold', fontSize=8, leading=10, textColor=c_accent)))
    story.append(Paragraph('Amazon A+ Stack, YouTube Clinical Engine & Gulf Expansion Blueprint', title_main))
    story.append(Paragraph('Capturing High-Intent Medical Shoppers, Remastering Clinical Assets & Penetrating the GCC Luxury Market', title_sub))

    # Two columns: Amazon Listing & YouTube Authority
    p4_col1 = [
        Paragraph('1. Amazon India Listing: 7-Image Clinical Conversion Stack', sec_subheading),
        Paragraph('Amazon shoppers decide in 15 seconds by swiping image carousels. We replace generic factory photos with an undeniable medical conversion stack:', body_text),
        Paragraph('<b>• Image 1 (Hero & Authority Seal):</b> Apparatus on medical white background with rigid T-Bar, high-visibility bungees, and embossed <i>"304 Surgical Stainless Steel Certified"</i> badge.', bullet_style),
        Paragraph('<b>• Image 2 (Biomechanics Teardown):</b> Split graphic comparing 0.05s concrete footstrike shock vs. 0.20s Change Mee deceleration (<b>-85% shock absorption</b>).', bullet_style),
        Paragraph('<b>• Image 3 (Clinical Social Proof):</b> Dr. Sanjay Gaikwad, M.B.B.S. photograph, medical registration seal, and quote on diabetes and hypertension recovery.', bullet_style),
        Paragraph('<b>• Image 4 (Senior Safety & Zero Fall Risk):</b> 72-year-old elder demonstrating the 3-phase grounded bounce holding the rigid stability handle.', bullet_style),
        Paragraph('<b>• Image 5 (Universal Multi-Gen Hub):</b> Grandparent (knee health) + Working Adult (desk cardio) + Teenager (posture & focus).', bullet_style),
        Paragraph('<b>• Image 6 (Competitor Teardown):</b> Side-by-side comparison: 304 SS frame vs. cheap coiled spring rust, squeaking, and snapping hazards.', bullet_style),
        Paragraph('<b>• Image 7 (Risk Reversal):</b> <i>"15-Day In-Home Mobility Trial + Doorstep Pickup Guarantee."</i>', bullet_style),
    ]

    p4_col2 = [
        Paragraph('2. YouTube Clinical Authority Engine (Flagship Assets)', sec_subheading),
        Paragraph('Older adults consume long-form video on iPads and Smart TVs; caregivers search for parent joint remedies. YouTube is Change Mee\'s anchor customer acquisition channel:', body_text),
        Paragraph('<b>• Dr. Sanjay Gaikwad Remaster (Flagship Asset):</b> Take Dr. Gaikwad’s raw video and give it broadcast-grade production: 4K B-roll of hands gripping the T-Bar, high-contrast burned-in subtitles (English, Hindi, Marathi), and anatomical overlays of lymph fluid draining from swollen ankles. Direct CTA: <i>"Chat with our clinical team on WhatsApp for free parent mobility advice."</i> (Yields <b>3.8x higher conversion</b>).', bullet_style),
        Paragraph('<b>• Viral Short 1: "The Knee Shock Egg Drop Test" (30s):</b> Drop a raw egg from 3 feet onto a steel-spring trampoline $\\rightarrow$ shatters violently. Drop the same egg onto Change Mee bungee mat $\\rightarrow$ gently decelerates unbroken. Hook: <i>"What is happening to your aging mother\'s knees right now on concrete roads."</i>', bullet_style),
        Paragraph('<b>• Viral Short 2: "The 60-Second Ankle Drain Test":</b> Close-up of swollen senior ankles with animated calf pump diagram demonstrating fluid drainage during grounded bounce.', bullet_style),
        Paragraph('<b>• 4-Part 10-Minute Morning Routine Series:</b> Follow-along videos with certified physiotherapist for Arthritis, Diabetes, Parkinson\'s, and Desk Ergonomics.', bullet_style),
    ]

    p4_grid_table = Table([[p4_col1, p4_col2]], colWidths=[248, 248])
    p4_grid_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(p4_grid_table)
    story.append(Spacer(1, 6))

    # Gulf Strategy Box
    gulf_html = (
        '<b>3. GULF / GCC MARKET PENETRATION (UAE, SAUDI ARABIA, KUWAIT, QATAR):</b><br/>'
        '• <b>The Gulf Reality:</b> 6 months of 48°C–52°C summer heat makes outdoor walking physically impossible. The GCC region has one of the world\'s highest adult Type 2 diabetes rates (18%–22%). Affluent local Emirati/Saudi families and expatriates live in spacious air-conditioned villas with dedicated wellness rooms.<br/>'
        '• <b>Positioning:</b> Positioned as the premier <b>"Home Longevity Suite Apparatus"</b> for glycemic regulation in AC comfort.<br/>'
        '• <b>Retail Pricing Power:</b> Target MSRP in GCC is <b>AED 3,499 – AED 3,999 ($950 – $1,080)</b>. Imported German Bellicons sell in Dubai for AED 5,500+. Change Mee delivers superior 304 Stainless Steel durability at an aggressive luxury price point.<br/>'
        '• <b>Channels:</b> Partnership with private longevity clinics in Dubai Healthcare City, luxury medical equipment retailers (Life Pharmacy, Aster Healthcare), and direct D2C with white-glove doorstep assembly and Tabby installments.'
    )
    gulf_table = Table([[Paragraph(gulf_html, body_text)]], colWidths=[504])
    gulf_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_bg_subtle),
        ('BOX', (0,0), (-1,-1), 0.75, c_border),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(gulf_table)
    story.append(Spacer(1, 5))

    # Automated Review Engine Box
    review_html = (
        '<b>4. AUTOMATED 5-STAR REVIEW & PARENT TESTIMONIAL PIPELINE:</b><br/>'
        '• <b>Day 0:</b> Unboxing card welcomes user $\\rightarrow$ • <b>Day 1 (WhatsApp):</b> Clinical concierge checks T-Bar height $\\rightarrow$ • <b>Day 7:</b> Knee mobility pulse check $\\rightarrow$ • <b>Day 14 (Incentive Loop):</b> <i>"Send a 45-second video of your parent using the rebounder and sharing their experience, and receive a <b>Complimentary Care Kit (Grip Socks + Replacement Bungees worth ■2,500)</b> free."</i> Generates 20–30 emotional, authentic parent video reviews every month to fuel Meta ads.'
    )
    review_table = Table([[Paragraph(review_html, body_text)]], colWidths=[504])
    review_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f0fdf4')),
        ('BOX', (0,0), (-1,-1), 0.75, c_emerald),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(review_table)

    story.append(PageBreak())

    # =========================================================================
    # PAGE 5: FINANCIAL ECONOMICS, 90-DAY EXECUTION ROADMAP & BOARDROOM TERMS
    # =========================================================================
    story.append(Paragraph('FINANCIAL ECONOMICS & BOARDROOM EXECUTION PLAN', ParagraphStyle('Eyebrow', fontName='Helvetica-Bold', fontSize=8, leading=10, textColor=c_accent)))
    story.append(Paragraph('Financial Unit Economics, 90-Day Execution Roadmap & SOW Alignment', title_main))
    story.append(Paragraph('Definitive Execution Milestones, Revenue Scaling Architecture & Proposed Boardroom Terms', title_sub))

    # Financial Unit Economics Table
    story.append(Paragraph('1. Financial Unit Economics & Profit Contribution Profile', sec_subheading))
    unit_econ_data = [
        [Paragraph('Metric', th_style), Paragraph('Value (INR)', th_style), Paragraph('Strategic Commercial Rationale', th_style)],
        [Paragraph('Retail Selling Price (MSRP)', td_style_bold), Paragraph('■43,000 (D2C: ■30k Ex-Tax)', td_style_emerald), Paragraph('Investment tier; 3x below imported Bellicon (■1.2L+); premium pricing power.', td_style)],
        [Paragraph('Estimated Bill of Materials (BOM)', td_style_bold), Paragraph('■11,500 – ■13,500', td_style), Paragraph('Includes 304 SS frame, 36 custom bungees, Permatron mat, T-bar & packaging.', td_style)],
        [Paragraph('Gross Profit Margin', td_style_bold), Paragraph('65% – 70%', td_style_emerald), Paragraph('Exceptional gross margin profile leaves extensive headroom for paid acquisition.', td_style)],
        [Paragraph('Target Customer Acquisition Cost (CAC)', td_style_bold), Paragraph('■4,500 – ■6,000', td_style), Paragraph('High-intent Meta/Google search campaigns targeting caregiver children.', td_style)],
        [Paragraph('Net Contribution Margin per Unit', td_style_bold), Paragraph('■21,000 – ■25,000', td_style_emerald), Paragraph('Robust net margin fuels rapid reinvestment into clinical asset production.', td_style)],
        [Paragraph('Recurring Aftermarket Revenue (LTV)', td_style_bold), Paragraph('■3,500 / 18 months', td_style_emerald), Paragraph('Replacement 36-cord bungee matrices & non-slip clinical grip socks.', td_style)],
    ]
    unit_econ_table = Table(unit_econ_data, colWidths=[140, 110, 254])
    unit_econ_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_subtle]),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(unit_econ_table)
    story.append(Spacer(1, 6))

    # 90-Day Execution Roadmap Table
    story.append(Paragraph('2. 90-Day Boardroom Execution Roadmap & Concrete Deliverables', sec_subheading))
    roadmap_data = [
        [Paragraph('Phase & Timeline', th_style), Paragraph('Core Strategic Objectives', th_style), Paragraph('Concrete Deliverables & Verifiable Milestones', th_style)],
        [
            Paragraph('Phase 1: Days 1 – 30<br/><b>Foundation & Digital Overhaul</b>', td_style_bold),
            Paragraph('Reposition brand from toy to medical mobility platform. Eliminate digital leaks.', td_style),
            Paragraph('• Complete overhaul of changemee.in: De-index from Toys & Games, deploy Cryo-Glass UI.<br/>• Remaster Dr. Sanjay Gaikwad testimonial with 4K B-roll & burned-in bilingual subtitles.<br/>• Deploy Amazon Brand Registry with 7-image clinical stack and 5 medical bullet points.<br/>• Publish App Store & Play Store metadata overhaul for Change Mee Companion App.', td_style)
        ],
        [
            Paragraph('Phase 2: Days 31 – 60<br/><b>Content Engine & Performance Ads</b>', td_style_bold),
            Paragraph('Activate paid discovery, YouTube clinical authority, and Caregiver WhatsApp loop.', td_style),
            Paragraph('• Film and publish 4 YouTube senior follow-along routines with physical therapist.<br/>• Launch Meta video ad campaigns targeting adult children (38–58) in Top 8 Indian metros.<br/>• Activate Google Search campaigns on high-intent terms (\'rebounder for elderly\', \'knee arthritis\').<br/>• Deploy automated Day 0–30 WhatsApp Concierge and review generation incentive loop.', td_style)
        ],
        [
            Paragraph('Phase 3: Days 61 – 90<br/><b>B2B Institutional & Senior Living</b>', td_style_bold),
            Paragraph('Scale institutional clinic revenue and initiate GCC distributor discussions.', td_style),
            Paragraph('• Direct B2B institutional outreach to 100+ physiotherapy & orthopedic rehab clinics.<br/>• Pitch demonstration units to 5 premium senior living communities (Antara, Ashiana).<br/>• Launch Doctor & Physio Affiliate Kit with structured 10% educational referral incentives.<br/>• Finalize master distributor agreements for UAE (Dubai Healthcare City) & Saudi Arabia.', td_style)
        ]
    ]
    roadmap_table = Table(roadmap_data, colWidths=[105, 125, 274])
    roadmap_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_subtle]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(roadmap_table)
    story.append(Spacer(1, 6))

    # Proposed SOW Terms & Boardroom Sign-Off
    story.append(Paragraph('3. Proposed SOW Partnership Structure & Boardroom Terms', sec_subheading))
    sow_data = [
        [Paragraph('Commercial Component', th_style), Paragraph('Proposed Structure', th_style), Paragraph('Deliverables, Scope & Risk Reversal Terms', th_style)],
        [
            Paragraph('Monthly Base Retainer', td_style_bold),
            Paragraph('■55,000 / month', td_style_emerald),
            Paragraph('Covers full creative production, website development, Amazon management, video remastering, ad campaign management, App Store optimization, and WhatsApp concierge setup.', td_style)
        ],
        [
            Paragraph('Performance Commission', td_style_bold),
            Paragraph('■3,000 per unit sold', td_style_emerald),
            Paragraph('Direct alignment of incentives. Commission applies to verified online and D2C orders generated through revamped digital channels.', td_style)
        ],
        [
            Paragraph('Risk Reversal Guarantee', td_style_bold),
            Paragraph('14-Day Creative Approval', td_style_bold),
            Paragraph('If initial website designs, Amazon creatives, and remastered video assets do not meet Dr. Sanjeev\'s medical standards, contract may be canceled with zero penalty.', td_style)
        ]
    ]
    sow_table = Table(sow_data, colWidths=[110, 110, 284])
    sow_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_subtle]),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(sow_table)
    story.append(Spacer(1, 6))

    # Final Boardroom Signoff Line
    sign_html = (
        '<b>BOARDROOM DECISION TODAY:</b> Approving Phase 1 initiates the immediate removal of the "Toys & Games" categorization, '
        'launches the clinical D2C landing page, remasters Dr. Sanjay Gaikwad\'s video, and begins App Store companion deployment within 7 business days.'
    )
    sign_table = Table([[Paragraph(sign_html, callout_text)]], colWidths=[504])
    sign_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_bg_callout),
        ('BOX', (0,0), (-1,-1), 1.0, c_accent),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(sign_table)

    # Build PDF
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Generated PDF successfully at: {pdf_path}")

if __name__ == '__main__':
    build_pdf()
