HEAD = """\

  /* Generics */
  body,
  body.theme-dark,
  body.theme-light {
  --font-default: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Microsoft YaHei Light", sans-serif;
  --font-monospace: "Fira Code", "Fira Code Medium", "Source Code Pro", monospace;
  --font-text: var(--font-text-override), var(--font-default);
  --font-monospace-default: var(--font-monospace-default-override), var(--font-monospace);
  --font-interface: var(--font-interface-override), var(--font-default);
  --rmx: "remixicon";
  --mdi: "Material Icons Sharp";
  --its: "its";
  --fa5: "Font Awesome 5 Free Solid";
  --fa6: "Font Awesome 6 Free Solid";
  --rpg: "rpg-awesome";
  --radius-s: 0;
  --radius-m: calc(var(--radius-s) * 1.1);
  --radius-l: calc(var(--radius-s) * 1.2);
  --radius-xl: calc(var(--radius-s) * 1.5);
  --radius-h: calc(var(--radius-s) / .50);
  --slider-track-radius: var(--radius-h);
  --input-radius: var(--radius-s);
  --search-input-radius: var(--radius-h);
  --icon-btn-radius: var(--radius-s);
  --tag-radius: var(--radius-l);
  --slider-thumb-radius: var(--radius-h);
  --status-bar-radius: var(--radius-m) 0 0 0;
  --checkbox-radius: var(--radius-m);
  --toggle-radius: var(--radius-h);
  --toggle-thumb-radius: var(--radius-h);
  --clickable-icon-radius: var(--radius-s);
  --pill-radius: var(--radius-m);
  --image-radius: var(--radius-s);
  --bold-weight: 900;
  --bold-modifier: 500;
  --font-ui-smaller: 13.5px;
  --font-ui-small: 14px;
  --font-ui-medium: 15px;
  --font-ui-large: 20px;
  --font-smallest: .85em;
  --font-smaller:.90em;
  --font-small: .95em;
  --icon-xs: 14px;
  --icon-s: 16px;
  --icon-m: 17px;
  --icon-l: 18px;
  --line-height-tight: 1.3em;
  --scroll-size: 7px;
  --divider-width: 2px;
  --divider-width-hover: 5px;
  --tag-padding-x: 7px;
  --tag-padding-y: 3px;
  --prompt-border-width: 3px;
  --shadow-s: 2px 2px 0 var(--outline);
  --shadow-m: 3px 3px 0 var(--outline);
  --shadow-ml: 4px 4px 0 var(--outline);
  --shadow-l: 5px 5px 0 var(--outline);
  --input-shadow: var(--shadow-s);
  --input-shadow-hover: var(--shadow-m);
  --embed-block-shadow-hover: var(--input-shadow);
  --message-color: var(--text-dl);
  --message-box-shadow: var(--shadow-s);
  --message-border-width: 0px;
  --message-border-color: var(--outline);
  --toggle-shadow: none;
  --box-border-s: 1px solid var(--outline);
  --box-border: 2px solid var(--outline);
  --box-border-m: 3px solid var(--outline);
}
  /* Callout Sizing */
  .mpdf-doc .callout {
    --callout-micro: 10%;
    --callout-tiny: 20%;
    --callout-small: 30%;
    --callout-small-med: 35%;
    --callout-med-small: 40%;
    --callout-medium: 50%;
    --callout-med-tall: 65%;
    --callout-tall-med: 80%;
    --callout-tall: 95%;
  }
  .mpdf-doc .callout[data-callout-metadata~=wmicro] {
    max-width: unset !important;
    width: var(--callout-micro) !important;
  }
  .mpdf-doc .callout[data-callout-metadata~=wtiny] {
    max-width: unset !important;
    width: var(--callout-tiny) !important;
  }
  .mpdf-doc .callout[data-callout-metadata~=wsmall] {
    max-width: unset !important;
    width: var(--callout-small) !important;
  }
  .mpdf-doc .callout[data-callout-metadata~=ws-med] {
    max-width: unset !important;
    width: var(--callout-small-med) !important;
  }
  .mpdf-doc .callout[data-callout-metadata~=wm-sm] {
    max-width: unset !important;
    width: var(--callout-med-small) !important;
  }
  .mpdf-doc .callout[data-callout-metadata~=wmed] {
    max-width: unset !important;
    width: var(--callout-medium) !important;
  }
  .mpdf-doc .callout[data-callout-metadata~=wm-tl] {
    max-width: unset !important;
    width: var(--callout-med-tall) !important;
  }
  .mpdf-doc .callout[data-callout-metadata~=wtl-med] {
    max-width: unset !important;
    width: var(--callout-tall-med) !important;
  }
  .mpdf-doc .callout[data-callout-metadata~=wtall] {
    max-width: unset !important;
    width: var(--callout-tall) !important;
  }
  .mpdf-doc .callout[data-callout-metadata~=sban], .mpdf-doc .callout[data-callout-metadata~=wfull] {
    width: 100% !important;
    float: unset !important;
    max-width: 100% !important;
  }
  .mpdf-doc .callout[data-callout-metadata~=wtiny-c] {
    width: 19% !important;
  }
  .mpdf-doc .callout[data-callout-metadata~=wsmall-c] {
    width: 32.4% !important;
  }
  .mpdf-doc .callout[data-callout-metadata~=ws-med-c] {
    width: 39% !important;
  }
  .mpdf-doc .callout[data-callout-metadata~=wm-sm-c] {
    width: 49% !important;
  }
  .mpdf-doc .callout[data-callout-metadata~=wmed-c] {
    width: 59% !important;
  }
  .mpdf-doc .callout[data-callout-metadata~=wm-tl-c] {
    width: 79% !important;
  }
  .mpdf-doc .callout[data-callout-metadata~=wfit] {
    width: fit-content !important;
    max-width: min-content !important;
  }
  .mpdf-doc .callout[data-callout-metadata~=static] {
    --callout-micro: 50px;
    --callout-tiny: 100px;
    --callout-small: 200px;
    --callout-small-med: 300px;
    --callout-med-small: 400px;
    --callout-medium: 500px;
    --callout-med-tall: 600px;
    --callout-tall: 700px;
  }

  .mpdf-doc .callout:is([data-callout-metadata~=content-padding-small],
  [data-callout-metadata~=c-p-sm]) {
    --callout-content-padding: 6px !important;
  }

  .mpdf-doc .callout:is([data-callout-metadata~=content-padding-medium],
  [data-callout-metadata~=c-p-med]) {
    --callout-content-padding: 12px !important;
  }
  .mpdf-doc .callout:is([data-callout-metadata~=content-padding-large],
  [data-callout-metadata~=c-p-lg]) {
    --callout-content-padding: 24px !important;
  }

  .mpdf-doc .callout:is([data-callout-metadata~=txt-l],
  [data-callout-metadata~=text-left]) > .callout-content > * {
    text-align: left !important;
  }

  .mpdf-doc .callout:is([data-callout-metadata~=txt-r],
  [data-callout-metadata~=text-right]) > .callout-content {
    text-align: right !important;
  }

  .mpdf-doc .callout:is([data-callout-metadata~=txt-c],
  [data-callout-metadata~=text-center]) > .callout-content {
    text-align: center !important;
  }

  .mpdf-doc .callout:is([data-callout-metadata~=ttl-c],
  [data-callout-metadata~=title-center]) .callout-title {
    justify-content: center !important;
  }
  .mpdf-doc .callout:is([data-callout-metadata~=ttl-c],
  [data-callout-metadata~=title-center]) .callout-title-inner {
    display: block !important;
    flex: unset !important;
  }

  .mpdf-doc .callout:is([data-callout-metadata~=text-small],
  [data-callout-metadata~=txt-s]) > .callout-content > * {
    --font-text-size: var(--font-smallest);
    --tag-size: var(--font-smallest);
    --table-text-size: var(--font-smallest);
    font-size: var(--font-text-size) !important;
  }

  /* Callout Positioning */
  .mpdf-doc .callout:is([data-callout-metadata~="p+r"], [data-callout-metadata~=left]) {
    float: left !important;
    margin: unset !important;
    margin-right: 10px !important;
  }
  .mpdf-doc .callout:is([data-callout-metadata~="p+l"], [data-callout-metadata~=right]) {
    float: right !important;
    margin: unset !important;
    margin-left: 10px !important;
  }
  .mpdf-doc .callout:is([data-callout-metadata~=ctr],
    [data-callout-metadata~=center]) {
      display: block !important;
      margin: auto !important;
      float: unset !important;
    }
  /* Callout Partial Visibility Rules */
  .mpdf-doc .callout:is([data-callout-metadata~=no-t],
  [data-callout-metadata~=no-title]) > .callout-title {
    display: none !important;
  }

  .mpdf-doc .callout:is([data-callout-metadata~=s-t],
  [data-callout-metadata~=show-title]) > .callout-title {
    display: flex !important;
  }
  .mpdf-doc .callout:is([data-callout-metadata~=s-t],
  [data-callout-metadata~=show-title]) > .callout-content > p {
    margin-top: 0 !important;
  }

  .mpdf-doc .callout:is([data-callout-metadata~=subtitle],
  [data-callout-metadata~=subt]) .callout-title {
    align-content: center !important;
    align-items: center !important;
  }
  .mpdf-doc .callout:is([data-callout-metadata~=subtitle],
  [data-callout-metadata~=subt]) .callout-title em {
    display: block !important;
    font-style: normal !important;
    font-size: var(--font-small) !important;
    line-height: 12px !important;
    font-weight: normal !important;
  }
  .mpdf-doc .callout:is([data-callout-metadata~=subtitle],
  [data-callout-metadata~=subt]) .callout-title em em {
    font-style: italic !important;
    display: inline-block !important;
  }
  .mpdf-doc .callout:is([data-callout-metadata~=no-i],
  [data-callout-metadata~=no-icon]) > .callout-title > .callout-icon {
    width: 0 !important;
    height: 0 !important;
    --icon-size: 0;
  }
  
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
  /*** "color" or "c" changes for .callout-icon svg */
  .mpdf-doc .callout:is([data-callout-metadata~=color-{color}],
  [data-callout-metadata~=c-{color}],
  [data-callout-metadata~=bg-c-{color}],
  [data-callout-metadata~=background-color-{color}]) > .callout-icon svg {{
    stroke: {color} !important;
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

  /* Callout for Captions */
  .mpdf-doc .callout:is([data-callout~=caption]) > .callout-title {
    display: none !important;
  }
  .mpdf-doc .callout:is([data-callout~=caption]) {
    border-inline-start: none !important;
  }
  
  .mpdf-doc .callout:is([data-callout~=caption]) {
    background: ${s.pageBackground} !important;
    text-align: center !important;
    border: 2px ${s.pageBackground} solid !important;
    padding: 0 !important;
    margin: 0 !important;
    max-width: 30vh !important;
  }
  .mpdf-doc .callout:is([data-callout~=caption]) > callout-content {
    border-radius: 10px !important;
    overflow: hidden !important;
    border: 2px ${s.accentColor} solid !important;
  }
  .mpdf-doc .callout[data-callout~=caption] > .callout-content > p :is(.image-embed, img) + br {
    display: none !important;
  }
  .mpdf-doc .callout[data-callout~=caption] > .callout-content img {
    display: block !important;
    margin: auto !important;
    border-radius: 10px !important;
  }
  .mpdf-doc .callout[data-callout~=caption] p {
    margin-block-start: 0 !important;
    margin-block-end: 0 !important;
    color: ${s.accentColor} !important;
  }

  .mpdf-doc .callout[data-callout~=caption]:is([data-callout-metadata~=sban], [data-callout-metadata~=banner]) .image-embed img {
    width: 100% !important;
  }

"""

output = HEAD
for color in ["blue", "green", "orange", "red", "purple", "gray", "yellow", "pink", "brown", "black", "white"]:
    output += FORMAT.format(color=color)
output += FOOT

import os
with open(os.path.join(os.path.dirname(__file__), "ignore_its-css-builder.css"), 'w') as fid:
    fid.write(output)

