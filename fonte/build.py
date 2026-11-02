#!/usr/bin/env python3
"""Reconstrúe un único index.html co texto e o xogo autocontidos."""
from pathlib import Path
root=Path(__file__).resolve().parent
project=root.parent if root.name=='fonte' else root
tpl=(root/'template.html').read_text(encoding='utf-8')
story=(root/'story.json').read_text(encoding='utf-8')
js=(root/'game.js').read_text(encoding='utf-8')
html=tpl.replace('__STORY_JSON__',story.replace('</script','<\\/script')).replace('__GAME_SCRIPT__',js.replace('</script','<\\/script'))
(project/'index.html').write_text(html,encoding='utf-8')
print(f"Xogo preparado: {project/'index.html'} ({len(html):,} caracteres)")
