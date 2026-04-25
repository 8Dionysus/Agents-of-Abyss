from __future__ import annotations
import sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/'scripts'))
from docs_thematic_common import build_plan, load_classifier
class DocsThematicCleanupTests(unittest.TestCase):
    def setUp(self): self.c=load_classifier(ROOT)
    def test_required_district_readmes_exist(self):
        for d in self.c['districts'].values(): self.assertTrue((ROOT/d['readme']).exists(), d['readme'])
    def test_no_flat_docs_need_thematic_cleanup(self): self.assertEqual(build_plan(ROOT,self.c), [])
    def test_docs_readme_mentions_protocol_and_index(self):
        text=(ROOT/'docs/README.md').read_text(encoding='utf-8'); self.assertIn('THEMATIC_DISTRICT_PROTOCOL',text); self.assertIn('CURRENT_SURFACE_INDEX',text); self.assertIn('generated/docs_thematic_index.min.json',text)
if __name__=='__main__': unittest.main()
