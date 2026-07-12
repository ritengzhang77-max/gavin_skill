#!/usr/bin/env python3
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "docs/demos/artifacts"
OUT = ART / "value-mechanism-evidence-deck.pptx"

W, H = 13.333, 7.5
PAPER = "F7F4EE"
WHITE = "FFFDFC"
INK = "172333"
MUTED = "63717C"
RULE = "C9C4BA"
NAVY = "274F73"
BLUE = "5D86AA"
GREEN = "3F806A"
RED = "B85E52"
GOLD = "AC7A39"
PALE_BLUE = "E9F0F5"
PALE_GREEN = "E8F1ED"
PALE_RED = "F5EAE7"
PALE_GOLD = "F3EEE2"


def rgb(h):
    return RGBColor(int(h[0:2],16), int(h[2:4],16), int(h[4:6],16))


def background(slide, color=PAPER):
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = rgb(color)


def line(slide, x1, y1, x2, y2, color=RULE, width: float = 1):
    s = slide.shapes.add_connector(1, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    s.line.color.rgb = rgb(color); s.line.width = Pt(width)
    return s


def rect(slide, x, y, w, h, fill=WHITE, stroke=RULE, width=1, radius=False):
    kind = MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE
    s = slide.shapes.add_shape(kind, Inches(x), Inches(y), Inches(w), Inches(h))
    s.fill.solid(); s.fill.fore_color.rgb = rgb(fill)
    s.line.color.rgb = rgb(stroke); s.line.width = Pt(width)
    return s


def text(slide, x, y, w, h, value, size: float=16, color=INK, bold=False,
         font="DejaVu Sans", align=PP_ALIGN.LEFT, valign=MSO_ANCHOR.TOP,
         margin=.02, italic=False):
    s = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf=s.text_frame; tf.clear(); tf.word_wrap=True
    tf.margin_left=tf.margin_right=tf.margin_top=tf.margin_bottom=Inches(margin)
    tf.vertical_anchor=valign
    p=tf.paragraphs[0]; p.alignment=align
    r=p.add_run(); r.text=value
    r.font.name=font; r.font.size=Pt(size); r.font.bold=bold; r.font.italic=italic; r.font.color.rgb=rgb(color)
    return s


def mixed(slide, x, y, w, h, runs, size: float=15, align=PP_ALIGN.LEFT):
    s=slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf=s.text_frame; tf.clear(); tf.word_wrap=True
    tf.margin_left=tf.margin_right=tf.margin_top=tf.margin_bottom=Inches(.02)
    p=tf.paragraphs[0]; p.alignment=align
    for value,color,bold,italic in runs:
        r=p.add_run(); r.text=value; r.font.name="DejaVu Sans"; r.font.size=Pt(size); r.font.bold=bold; r.font.italic=italic; r.font.color.rgb=rgb(color)
    return s


def header(slide, kicker, title, subtitle=None):
    text(slide,.64,.34,5.8,.22,kicker.upper(),8.5,NAVY,True)
    text(slide,.64,.72,12.0,.62,title,27,INK,True,font="DejaVu Serif")
    if subtitle: text(slide,.66,1.39,11.6,.4,subtitle,12,MUTED)
    line(slide,.64,1.88,12.68,1.88,RULE,1)


def footer(slide,n):
    line(slide,.64,7.08,12.68,7.08,RULE,.8)
    text(slide,.64,7.17,5.8,.16,"VALUE–ACTION MECHANISTIC ANALYSIS",7.5,MUTED,True)
    text(slide,12.2,7.16,.45,.16,str(n),8,MUTED,True,align=PP_ALIGN.RIGHT)


def arrow_text(slide,x,y,w,value,color=NAVY):
    rect(slide,x,y,w,.44,PAPER,color,1)
    text(slide,x+.08,y+.1,w-.16,.2,value,10.5,color,True,align=PP_ALIGN.CENTER)


prs=Presentation(); prs.slide_width=Inches(W); prs.slide_height=Inches(H); blank=prs.slide_layouts[6]

# 1 — quiet academic cover
s=prs.slides.add_slide(blank); background(s)
text(s,.72,.48,5.8,.22,"MECHANISTIC INTERPRETABILITY",9,NAVY,True)
text(s,.72,1.22,11.1,1.25,"From association\nto mechanism",37,INK,True,font="DejaVu Serif")
text(s,.76,2.92,8.1,.6,"An evidence standard for sparse features implicated in value-guided choice.",16,MUTED)
# sparse causal chain
text(s,.78,4.35,2.15,.4,"value state",15,GREEN,True,align=PP_ALIGN.CENTER)
text(s,3.2,4.35,2.15,.4,"feature activity",15,NAVY,True,align=PP_ALIGN.CENTER)
text(s,5.62,4.35,2.15,.4,"model choice",15,RED,True,align=PP_ALIGN.CENTER)
text(s,2.74,4.34,.34,.34,"→",18,GREEN,True,align=PP_ALIGN.CENTER)
text(s,5.16,4.34,.34,.34,"→",18,NAVY,True,align=PP_ALIGN.CENTER)
line(s,.78,5.08,7.75,5.08,RULE,1)
mixed(s,.78,5.36,8.4,.5,[("Question: ",NAVY,True,False),("what evidence distinguishes this chain from scaffolding, content tracking, or post-choice activation?",INK,False,False)],14)
text(s,9.2,5.75,3.4,.3,"Research methods brief",12,NAVY,True,align=PP_ALIGN.RIGHT)
footer(s,1)

# 2 — hero: causal stories
s=prs.slides.add_slide(blank); background(s)
header(s,"Causal ambiguity","Association is compatible with four causal stories","The same signed activation gap can support very different interpretations.")
# left label and equation
text(s,.66,2.18,7.65,.25,"FOUR HYPOTHESES",9,NAVY,True)
rect(s,.66,2.58,7.62,3.77,WHITE,RULE,1)
stories=[
("01","Scaffold","option order  →  feature activity","The feature follows formatting or response position.",BLUE),
("02","Content","option wording  →  feature activity","The feature recognizes what one option says.",GOLD),
("03","Consequence","model choice  →  feature activity","The feature appears after the decision is fixed.",RED),
("04","Mechanism","value state  →  feature  →  choice","The feature participates before or during choice.",GREEN),
]
for i,(n,name,dag,desc,c) in enumerate(stories):
    y=2.78+i*.82
    text(s,.9,y,.42,.27,n,10,c,True)
    text(s,1.38,y,1.25,.28,name,12,INK,True)
    text(s,2.78,y,2.65,.28,dag,11,c,True,font="DejaVu Serif")
    text(s,5.55,y,2.35,.46,desc,10.5,MUTED)
    if i<3: line(s,.9,y+.6,8.0,y+.6,"DED9D1",.7)
# right evidence column
text(s,8.76,2.18,3.86,.25,"WHAT SEPARATES THEM",9,NAVY,True)
for i,(t,d,c) in enumerate([
("Order","Does the sign survive option reversal?",BLUE),
("Timing","Is evidence present before the answer?",GOLD),
("Intervention","Does ablation change choice predictably?",GREEN),
]):
    y=2.58+i*1.13
    text(s,8.78,y,.38,.3,f"{i+1}",11,c,True)
    text(s,9.28,y,3.1,.3,t,13,INK,True)
    text(s,9.28,y+.36,3.0,.42,d,10.5,MUTED)
    line(s,8.78,y+.86,12.55,y+.86,"DED9D1",.8)
rect(s,8.76,5.95,3.82,.62,PALE_GREEN,GREEN,1)
text(s,8.98,6.1,3.38,.28,"Until then: candidate, not mechanism.",11,GREEN,True,align=PP_ALIGN.CENTER)
footer(s,2)

# 3 — controls table
s=prs.slides.add_slide(blank); background(s)
header(s,"Identification strategy","Each alternative explanation needs its own control","A single aggregate score cannot reveal which causal story survived.")
cols=[.68,3.25,7.35,10.2]
widths=[2.55,4.08,2.83,2.45]
heads=["Alternative","Matched comparison","Failure pattern","Interpretation"]
for x,w,h in zip(cols,widths,heads):
    text(s,x,2.16,w,.26,h.upper(),8.5,NAVY,True)
line(s,.66,2.52,12.66,2.52,NAVY,1.4)
rows=[
("Scaffold","Reverse option order; preserve semantic side","Effect follows position","Formatting-sensitive"),
("Content","Compare relevant and unrelated option spans","Effect stays local to wording","Content tracker"),
("Consequence","Move measurement before the answer site","Evidence appears only afterward","Decision readout"),
("Mechanism","Ablate or patch with negative controls","Choice changes in predicted direction","Causal contributor"),
]
for i,row in enumerate(rows):
    y=2.78+i*.92
    shade=WHITE if i%2==0 else "F2EFE8"
    rect(s,.66,y-.12,12.0,.78,shade,shade,0)
    colors=[INK,INK,RED if i<3 else GREEN,NAVY]
    for x,w,val,c in zip(cols,widths,row,colors):
        text(s,x,y,w-.16,.48,val,10.8,c,i==3 and x==cols[2])
line(s,.66,6.57,12.66,6.57,RULE,1)
mixed(s,.7,6.72,11.8,.28,[("Reporting rule  ",NAVY,True,False),("preserve disagreements across controls instead of collapsing them into one confidence score.",INK,False,False)],11.5)
footer(s,3)

# 4 — claims
s=prs.slides.add_slide(blank); background(s)
header(s,"Claim discipline","Use the strongest label the evidence earns","The vocabulary should become more specific only as the design becomes more demanding.")
levels=[
("DESCRIPTIVE","Associated feature","Signed activation differs across choices.",BLUE),
("LOCALIZED","Decision-relevant candidate","Direction survives controls at a relevant site or time.",GOLD),
("CAUSAL","Mechanistic contributor","Matched intervention changes choice as predicted.",GREEN),
]
for i,(level,name,desc,c) in enumerate(levels):
    x=.7+i*4.04
    text(s,x,2.32,3.55,.23,level,9,c,True)
    line(s,x,2.67,x+3.52,2.67,c,2)
    text(s,x,2.95,3.48,.65,name,19,INK,True,font="DejaVu Serif")
    text(s,x,3.88,3.35,.76,desc,11.5,MUTED)
    text(s,x,5.15,3.3,.24,"CLAIM CEILING",8.5,c,True)
    text(s,x,5.52,3.35,.55,["association","candidate involvement","causal contribution"][i],12.5,INK,True)
    if i<2:
        text(s,x+3.58,3.95,.35,.3,"→",17,RULE,True,align=PP_ALIGN.CENTER)
rect(s,.7,6.35,11.98,.5,PALE_BLUE,NAVY,1)
text(s,.92,6.48,11.53,.2,"Mixed evidence is still a result; state exactly where the claim stops.",11.5,NAVY,True,align=PP_ALIGN.CENTER)
footer(s,4)

ART.mkdir(parents=True,exist_ok=True)
prs.save(str(OUT))
print(OUT)
