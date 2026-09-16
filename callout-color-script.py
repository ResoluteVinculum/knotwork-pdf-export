HEAD = """\
  /* Callout Color Customization */
  .mpdf-doc .callout {
    --callout-color-opacity: 10%;
    --callout-title-opacity: 25%;
    --callout-blue: #528bd4;
    --callout-green: #56b375;
    --callout-orange: #e6813f;
    --callout-red: #c14343;
    --callout-purple: #9961da;
    --callout-gray: #a6bdc5;
    --callout-yellow: #d0b530;
    --callout-pink: #e36ba7;
    --callout-brown: #a16a49;
    --callout-black: #000000;
    --callout-white: #FFFFFF;
    --callout-plain: ${s.pageBackground};
  }
"""
FORMAT = """\
  /** {color} */
  /*** Color Selection */
  .mpdf-doc .callout:is([data-callout-metadata~=color-{color}],
  [data-callout-metadata~=c-{color}]) {{
    --callout-title: var(--callout-{color});
  }}
  /*** "color" or "c" changes for .callout-title */
  .mpdf-doc .callout:is([data-callout-metadata~=color-{color}],
  [data-callout-metadata~=c-{color}],
  [data-callout-metadata~=bg-c-{color}],
  [data-callout-metadata~=background-color-{color}]) > .callout-title {{
    --callout-color: var(--callout-title);
    color: {color} !important;
    background: color-mix(in oklch, var(--callout-{color}) var(--callout-title-opacity), ${{s.pageBackground}}) !important;
  }}
  /*** "background" or "bg" changes for .callout-content */
  .mpdf-doc .callout:is([data-callout-metadata~=background-{color}],
  [data-callout-metadata~=bg-{color}],
  [data-callout-metadata~=background-color-{color}],
  [data-callout-metadata~=bg-c-{color}]) > .callout-content {{
    --callout-background: color-mix(in oklch, var(--callout-{color}) var(--callout-color-opacity), ${{s.pageBackground}});
    background-color: var(--callout-background) !important;
    background: var(--callout-background) !important;
  }}
  /*** Callout color variable setting */
  .mpdf-doc .callout:is([data-callout-metadata~=background-color-{color}],
  [data-callout-metadata~=bg-c-{color}]) {{
    --callout-color: var(--callout-{color});
  }}

"""

FOOT = """\
  /** plain */
  /*** Color Selection */
  .mpdf-doc .callout:is([data-callout-metadata~=color-plain],
  [data-callout-metadata~=c-plain]) {
    --callout-title: var(--callout-plain);
  }
  /*** "color" or "c" changes for .callout-title */
  .mpdf-doc .callout:is([data-callout-metadata~=color-plain],
  [data-callout-metadata~=c-plain],
  [data-callout-metadata~=bg-c-plain],
  [data-callout-metadata~=background-color-plain]) > .callout-title {
    --callout-color: var(--callout-title);
    color: plain !important;
    background: color-mix(in oklch, var(--callout-plain) var(--callout-title-opacity), ${s.pageBackground}) !important;
  }
  /*** "background" or "bg" changes for .callout-content */
  .mpdf-doc .callout:is([data-callout-metadata~=background-plain],
  [data-callout-metadata~=bg-plain],
  [data-callout-metadata~=background-color-plain],
  [data-callout-metadata~=bg-c-plain]) > .callout-content {
    --callout-background: color-mix(in oklch, var(--callout-plain) var(--callout-color-opacity), ${s.pageBackground});
    background-color: var(--callout-background) !important;
    background: var(--callout-background) !important;
  }
  /*** Callout color variable setting */
  .mpdf-doc .callout:is([data-callout-metadata~=background-color-plain],
  [data-callout-metadata~=bg-c-plain]) {
    --callout-color: var(--callout-plain);
  }

"""

output = HEAD
for color in ["blue", "green", "orange", "red", "purple", "gray", "yellow", "pink", "brown", "black", "white"]:
    output += FORMAT.format(color=color)
output += FOOT

print(output)

