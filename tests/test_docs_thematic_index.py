from __future__ import annotations
import json, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/'scripts'))
from docs_thematic_common import load_classifier, render_index
class DocsThematicIndexTests(unittest.TestCase):
    def test_generated_index_matches_classifier(self): self.assertEqual((ROOT/'generated/docs_thematic_index.min.json').read_text(encoding='utf-8'), render_index(load_classifier(ROOT)))
    def test_index_is_machine_compact(self):
        text=(ROOT/'generated/docs_thematic_index.min.json').read_text(encoding='utf-8'); self.assertEqual(text.count('\n'),1); self.assertEqual(json.loads(text)['generated_rule'],'Reflects docs/thematic_districts.json; does not author meaning.')
if __name__=='__main__': unittest.main()
