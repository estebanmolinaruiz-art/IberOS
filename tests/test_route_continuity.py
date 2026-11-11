import unittest
from iberos.route_continuity import ContinuityWitness, Period, audit_continuity

IB=Period("iberian",-429,-349)
ROM=Period("roman",1,200)

def w(id,earliest,latest,kind="material_road",direct=True,geom=True,
      group=None,verification="verified"):
    return ContinuityWitness(id,"picola_alcudia","src-"+id,group or id,kind,
                             earliest,latest,verification,direct,geom)

class HistoricalContinuityTests(unittest.TestCase):
    def test_late_road_not_backdated(self):
        r=audit_continuity([w("roman-road",1,200)],"picola_alcudia",[IB,ROM])
        self.assertEqual(r["periods"]["iberian"]["status"],"no_qualified_evidence")
        self.assertFalse(r["continuity_between_periods_proven"])
    def test_context_not_route(self):
        r=audit_continuity([w("port",-429,-349,"settlement_relation",False,False)],
                           "picola_alcudia",[IB])
        self.assertEqual(r["periods"]["iberian"]["status"],"context_only")
    def test_two_independent_direct_eligible_only_for_review(self):
        r=audit_continuity([w("a",-429,-349),w("b",-429,-349)],
                           "picola_alcudia",[IB])
        self.assertEqual(r["periods"]["iberian"]["status"],"candidate_for_archaeological_review")
        self.assertFalse(r["periods"]["iberian"]["road_proven"])
    def test_duplicate_editions_collapse(self):
        r=audit_continuity([w("a",-429,-349,group="same"),w("b",-429,-349,group="same")],
                           "picola_alcudia",[IB])
        self.assertEqual(r["periods"]["iberian"]["direct_geometric_witness_groups"],1)
    def test_unverified_excluded(self):
        r=audit_continuity([w("a",-429,-349,verification="unverified")],
                           "picola_alcudia",[IB])
        self.assertEqual(r["periods"]["iberian"]["status"],"no_qualified_evidence")
    def test_same_source_later_is_not_earlier(self):
        r=audit_continuity([w("later",100,170)],"picola_alcudia",[IB])
        self.assertFalse(r["backdating_allowed"])
    def test_mismatched_corridor_excluded(self):
        obs=ContinuityWitness("other","different","x","g","material_road",-429,-349,"verified",True,True)
        r=audit_continuity([obs],"picola_alcudia",[IB])
        self.assertEqual(r["periods"]["iberian"]["status"],"no_qualified_evidence")

if __name__=="__main__":
    unittest.main()
