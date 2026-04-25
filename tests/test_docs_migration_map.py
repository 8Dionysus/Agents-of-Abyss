from __future__ import annotations
import sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/'scripts'))
from docs_thematic_common import load_classifier
class DocsMigrationMapTests(unittest.TestCase):
    def setUp(self): self.c=load_classifier(ROOT)
    def test_all_exact_migrations_target_known_districts(self):
        for item in self.c['exact_migrations']:
            d=self.c['districts'][item['district']]; self.assertTrue(item['target'].startswith(d['path']+'/'))
    def test_no_current_root_allowlist_item_is_exact_moved(self):
        allow=set(self.c['current_root_allowlist']); moved={Path(i['source']).name for i in self.c['exact_migrations']}; self.assertFalse(allow & moved)
if __name__=='__main__': unittest.main()
