import unittest
from iberos.route_function import RouteObservation, assess_route_function

class RouteFunctionTests(unittest.TestCase):
    def test_context_only_cannot_establish_role(self):
        obs=[RouteObservation("port","study1","port_1",-500,-300,False)]
        result=assess_route_function(obs,-429,-349)
        self.assertEqual(result["candidate_type"],"unknown")
        self.assertFalse(result["function_proven"])

    def test_independent_direct_trade_support(self):
        obs=[RouteObservation("warehouse","s1","excavation_a",-500,-300,True),
             RouteObservation("trade_goods","s2","excavation_b",-500,-300,True)]
        self.assertEqual(assess_route_function(obs,-429,-349)["candidate_type"],"commercial")

    def test_duplicate_study_not_independent(self):
        obs=[RouteObservation("fort","s1","same_object",-500,-300,True),
             RouteObservation("garrison","s2","same_object",-500,-300,True)]
        self.assertEqual(assess_route_function(obs,-429,-349)["candidate_type"],"unknown")

    def test_mixed_support(self):
        obs=[RouteObservation("port","s1","a",-500,-300,True),
             RouteObservation("market","s2","b",-500,-300,True),
             RouteObservation("fort","s3","c",-500,-300,True),
             RouteObservation("garrison","s4","d",-500,-300,True)]
        self.assertEqual(assess_route_function(obs,-429,-349)["candidate_type"],"mixed")

    def test_late_data_excluded(self):
        obs=[RouteObservation("fort","s1","a",-100,100,True),
             RouteObservation("garrison","s2","b",-100,100,True)]
        self.assertEqual(assess_route_function(obs,-429,-349)["candidate_type"],"unknown")

if __name__ == "__main__":
    unittest.main()
