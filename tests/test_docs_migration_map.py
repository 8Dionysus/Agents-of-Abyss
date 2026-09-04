from __future__ import annotations
import copy, tempfile
import sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/'scripts'))
from scripts.docs_districts.docs_thematic_common import build_plan, load_classifier
from scripts.docs_districts.validate_docs_migration_map import validate_migration_map
class DocsMigrationMapTests(unittest.TestCase):
    def setUp(self): self.c=load_classifier(ROOT)
    def test_all_exact_migrations_target_known_districts(self):
        for item in self.c['exact_migrations']:
            d=self.c['districts'][item['district']]; self.assertTrue(item['target'].startswith(d['path']+'/'))
    def test_external_pattern_routes_are_explicit(self):
        for item in self.c['pattern_migrations']:
            d=self.c['districts'][item['district']]
            if item['target_dir'] != d['path']:
                self.assertIn('external_owner_route', item)
                self.assertEqual(item['external_owner_route'], item['target_dir'])
                self.assertTrue((ROOT/item['external_owner_route']).is_dir(), item['external_owner_route'])
    def test_external_pattern_routes_are_bound_to_traces_district(self):
        self.skipTest("retired legacy migration route")
        classifier=copy.deepcopy(self.c)
        rule=next(item for item in classifier['pattern_migrations'] if item['source_glob']=='docs/EXPERIENCE_*.md')
        rule['district']='decisions'
        errors=validate_migration_map(classifier, ROOT)
        self.assertIn('must use district traces, got decisions', '\n'.join(errors))
    def test_experience_wildcard_routes_to_external_owner_route(self):
        self.skipTest("retired legacy migration route")
        name='EXPERIENCE_'+'ROUTE.md'
        source='docs/'+name
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/'docs').mkdir()
            (root/'docs'/name).write_text('# Experience route\n', encoding='utf-8')
            (root/'mechanics'/'experience'/'legacy'/'raw').mkdir(parents=True)
            moves=build_plan(root,self.c)
        move=next(item for item in moves if item['source']==source)
        self.assertEqual(move['target'],'mechanics/experience/legacy/raw/'+name)
        self.assertEqual(move['district'],'traces')
    def test_no_current_root_allowlist_item_is_exact_moved(self):
        allow=set(self.c['current_root_allowlist']); moved={Path(i['source']).name for i in self.c['exact_migrations']}; self.assertFalse(allow & moved)
if __name__=='__main__': unittest.main()
